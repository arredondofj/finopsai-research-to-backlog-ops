#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  acquire_transcript.sh <youtube-url> [--date YYYY_MM_DD] [--lang LANG]

Purpose:
  Validate a YouTube URL, download subtitles/transcript only, and preserve the
  downloaded subtitle artifact under the workspace input/ directory.

Examples:
  skills/youtube-transcript-pipeline/scripts/acquire_transcript.sh "https://www.youtube.com/watch?v=VIDEO_ID"
  skills/youtube-transcript-pipeline/scripts/acquire_transcript.sh "https://youtu.be/VIDEO_ID" --date 2026_04_19

Notes:
  - This script does not download video or audio.
  - Local URL validation runs before any network request.
  - YouTube subtitle acquisition requires network access. In sandboxed runs,
    approve network access before retrying DNS, connection, TLS, timeout, or
    network-unreachable failures.
  - yt-dlp performs the remote usability/subtitle availability check.
EOF
}

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
INPUT_DIR="$WORKSPACE_ROOT/input"
RUN_DATE="$(date '+%Y_%m_%d')"
LANG="en.*"
URL=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --date)
      if [[ $# -lt 2 || "$2" == --* ]]; then
        echo "Missing value for --date." >&2
        usage >&2
        exit 2
      fi
      RUN_DATE="$2"
      shift 2
      ;;
    --lang)
      if [[ $# -lt 2 || "$2" == --* ]]; then
        echo "Missing value for --lang." >&2
        usage >&2
        exit 2
      fi
      LANG="$2"
      shift 2
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    --*)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
    *)
      if [[ -n "$URL" ]]; then
        echo "Only one YouTube URL may be provided." >&2
        usage >&2
        exit 2
      fi
      URL="$1"
      shift
      ;;
  esac
done

if [[ -z "$URL" ]]; then
  echo "No YouTube URL provided. Stop: transcript acquisition requires a usable YouTube URL." >&2
  usage >&2
  exit 2
fi

if [[ ! "$RUN_DATE" =~ ^[0-9]{4}_[0-9]{2}_[0-9]{2}$ ]]; then
  echo "Invalid --date value '$RUN_DATE'. Expected YYYY_MM_DD." >&2
  exit 2
fi

if ! command -v yt-dlp >/dev/null 2>&1; then
  echo "yt-dlp is required but was not found on PATH. Stop: cannot acquire transcript." >&2
  exit 3
fi

python3 - "$URL" <<'PY'
import re
import sys
from urllib.parse import parse_qs, urlparse

url = sys.argv[1].strip()
parsed = urlparse(url)
host = parsed.netloc.lower()
path = parsed.path.strip("/")

if parsed.scheme not in {"http", "https"}:
    print("Invalid YouTube URL: URL must start with http:// or https://.", file=sys.stderr)
    raise SystemExit(2)

allowed_hosts = {
    "youtube.com",
    "www.youtube.com",
    "m.youtube.com",
    "music.youtube.com",
    "youtu.be",
}

if host not in allowed_hosts:
    print("Invalid YouTube URL: host must be youtube.com or youtu.be.", file=sys.stderr)
    raise SystemExit(2)

video_id = ""
if host == "youtu.be":
    video_id = path.split("/")[0] if path else ""
elif path == "watch":
    video_id = parse_qs(parsed.query).get("v", [""])[0]
elif path.startswith("shorts/") or path.startswith("embed/"):
    parts = path.split("/")
    video_id = parts[1] if len(parts) > 1 else ""

if not re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id or ""):
    print("Invalid YouTube URL: could not find a valid 11-character video id.", file=sys.stderr)
    raise SystemExit(2)
PY

mkdir -p "$INPUT_DIR"

before_file="$(mktemp)"
after_file="$(mktemp)"
trap 'rm -f "$before_file" "$after_file"' EXIT

find "$INPUT_DIR" -maxdepth 1 -type f | sort > "$before_file"

echo "Validated YouTube URL locally."
echo "Downloading subtitles only with yt-dlp..."

yt_dlp_log="$(mktemp)"
trap 'rm -f "$before_file" "$after_file" "$yt_dlp_log"' EXIT

if ! yt-dlp \
  --no-playlist \
  --skip-download \
  --write-sub \
  --write-auto-sub \
  --sub-langs "$LANG" \
  --sub-format "vtt" \
  --output "$INPUT_DIR/%(title).200B [%(id)s]_${RUN_DATE}.%(ext)s" \
  "$URL" 2>&1 | tee "$yt_dlp_log"; then
  if grep -Eiq 'failed to resolve|name or service not known|nodename nor servname provided|temporary failure in name resolution|network is unreachable|connection refused|connection reset|timed out|timeout|TLS|SSL|certificate|proxy|Unable to download webpage' "$yt_dlp_log"; then
    echo "yt-dlp could not reach YouTube after local URL validation. Stop: this appears to be a DNS/network-access failure; retry with approved network access before treating the URL or subtitles as unavailable." >&2
    exit 6
  fi
  echo "yt-dlp could not download a transcript for this URL. Stop: verify the URL is reachable and subtitles are available." >&2
  exit 4
fi

find "$INPUT_DIR" -maxdepth 1 -type f | sort > "$after_file"

new_files="$(comm -13 "$before_file" "$after_file" | grep -E '\.vtt$' || true)"
if [[ -z "$new_files" ]]; then
  echo "No new .vtt transcript file was created. Stop: subtitles may be unavailable for this video/language." >&2
  exit 5
fi

echo "Transcript artifact(s) saved:"
printf "%s\n" "$new_files"
