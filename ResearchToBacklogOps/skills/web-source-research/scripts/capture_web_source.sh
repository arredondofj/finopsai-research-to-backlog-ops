#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  capture_web_source.sh <url> <output.md> [--question "research focus"]

Purpose:
  Validate a general web URL, fetch the page, capture durable source metadata,
  extract readable text, and write a markdown capture artifact.

Notes:
  - This script fetches the page content over the network.
  - It records original URL, final URL, canonical URL when discoverable,
    title, site name, access date, content type, and extracted text.
  - It is designed for general web pages, not YouTube transcript acquisition
    and not GitHub repository assessment.
EOF
}

if [[ $# -lt 2 ]]; then
  usage >&2
  exit 2
fi

URL="$1"
OUTPUT_PATH="$2"
shift 2

QUESTION=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --question)
      if [[ $# -lt 2 || "$2" == --* ]]; then
        echo "Missing value for --question." >&2
        usage >&2
        exit 2
      fi
      QUESTION="$2"
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
      echo "Unexpected positional argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if ! command -v curl >/dev/null 2>&1; then
  echo "curl is required but was not found on PATH." >&2
  exit 3
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 is required but was not found on PATH." >&2
  exit 3
fi

python3 - "$URL" <<'PY'
import sys
from urllib.parse import urlparse

url = sys.argv[1].strip()
parsed = urlparse(url)

if parsed.scheme not in {"http", "https"}:
    print("Invalid web URL: URL must start with http:// or https://.", file=sys.stderr)
    raise SystemExit(2)

if not parsed.netloc:
    print("Invalid web URL: host is missing.", file=sys.stderr)
    raise SystemExit(2)
PY

mkdir -p "$(dirname "$OUTPUT_PATH")"

html_file="$(mktemp)"
meta_file="$(mktemp)"
trap 'rm -f "$html_file" "$meta_file"' EXIT

curl_output="$(
  curl \
    --location \
    --silent \
    --show-error \
    --fail \
    --compressed \
    --output "$html_file" \
    --write-out '%{url_effective}\n%{content_type}\n' \
    "$URL"
)"

FINAL_URL="$(printf '%s\n' "$curl_output" | sed -n '1p')"
CONTENT_TYPE="$(printf '%s\n' "$curl_output" | sed -n '2p')"
ACCESS_DATE_UTC="$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
ACCESS_DATE_LOCAL="$(date '+%Y-%m-%d')"

python3 - "$URL" "$FINAL_URL" "$CONTENT_TYPE" "$ACCESS_DATE_UTC" "$QUESTION" "$html_file" "$meta_file" <<'PY'
import html
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

original_url, final_url, content_type, access_date_utc, question, html_path, meta_path = sys.argv[1:]
raw_html = Path(html_path).read_text(encoding="utf-8", errors="replace")


def first_match(pattern: str, text: str, flags: int = 0) -> str:
    match = re.search(pattern, text, flags)
    return html.unescape(match.group(1).strip()) if match else ""


title = first_match(r"<title[^>]*>(.*?)</title>", raw_html, re.IGNORECASE | re.DOTALL)
canonical_url = first_match(
    r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)["\']',
    raw_html,
    re.IGNORECASE,
)
if not canonical_url:
    canonical_url = first_match(
        r'<meta[^>]+property=["\']og:url["\'][^>]+content=["\']([^"\']+)["\']',
        raw_html,
        re.IGNORECASE,
    )
site_name = first_match(
    r'<meta[^>]+property=["\']og:site_name["\'][^>]+content=["\']([^"\']+)["\']',
    raw_html,
    re.IGNORECASE,
)
if not site_name:
    site_name = first_match(
        r'<meta[^>]+name=["\']application-name["\'][^>]+content=["\']([^"\']+)["\']',
        raw_html,
        re.IGNORECASE,
    )
description = first_match(
    r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']+)["\']',
    raw_html,
    re.IGNORECASE,
)


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.skip_depth = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style", "noscript"}:
            self.skip_depth += 1
        elif tag in {"p", "div", "section", "article", "li", "br", "h1", "h2", "h3", "h4", "h5", "h6"}:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in {"script", "style", "noscript"} and self.skip_depth > 0:
            self.skip_depth -= 1
        elif tag in {"p", "div", "section", "article", "li", "br", "h1", "h2", "h3", "h4", "h5", "h6"}:
            self.parts.append("\n")

    def handle_data(self, data):
        if self.skip_depth:
            return
        cleaned = " ".join(data.split())
        if cleaned:
            self.parts.append(cleaned)


extractor = TextExtractor()
extractor.feed(raw_html)
text = "\n".join(part for part in extractor.parts if part != "\n")
text = re.sub(r"\n{3,}", "\n\n", text).strip()

payload = {
    "original_url": original_url,
    "final_url": final_url,
    "canonical_url": canonical_url,
    "title": title,
    "site_name": site_name,
    "description": description,
    "content_type": content_type,
    "access_date_utc": access_date_utc,
    "question": question,
    "extracted_text": text,
}

Path(meta_path).write_text(json.dumps(payload, ensure_ascii=True), encoding="utf-8")
PY

python3 - "$meta_file" "$OUTPUT_PATH" "$ACCESS_DATE_LOCAL" <<'PY'
import json
import sys
from pathlib import Path

meta_path, output_path, access_date_local = sys.argv[1:]
payload = json.loads(Path(meta_path).read_text(encoding="utf-8"))

title = payload["title"] or "Untitled source"
site_name = payload["site_name"] or "Unknown"
canonical = payload["canonical_url"] or "Not detected"
description = payload["description"] or "Not detected"
question = payload["question"] or "Not provided"
text = payload["extracted_text"] or "No readable text could be extracted."

markdown = f"""# Web Source Capture

## Access Metadata

- Original URL: `{payload["original_url"]}`
- Final URL: `{payload["final_url"]}`
- Canonical URL: `{canonical}`
- Title: {title}
- Publisher / Site: {site_name}
- Access date (local): `{access_date_local}`
- Access date (UTC): `{payload["access_date_utc"]}`
- Acquisition method: `scripted fetch via capture_web_source.sh`
- Content type: `{payload["content_type"] or "Unknown"}`
- Research question: {question}

## Source Summary

- Meta description: {description}

## Extracted Text

```text
{text}
```
"""

Path(output_path).write_text(markdown, encoding="utf-8")
PY

echo "Validated web URL locally."
echo "Web capture artifact saved:"
echo "$OUTPUT_PATH"
