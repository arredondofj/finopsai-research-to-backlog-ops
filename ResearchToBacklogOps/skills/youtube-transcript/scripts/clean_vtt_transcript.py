#!/usr/bin/env python3
"""Convert YouTube WebVTT captions into timestamped analysis-ready text.

This script performs mechanical cleanup only:
- remove WebVTT headers, cue timing metadata, inline timing tags, and HTML tags
- unescape HTML entities
- collapse rolling-caption overlap common in YouTube subtitles
- preserve approximate timestamps for each output paragraph

It intentionally does not perform transcript-specific wording corrections.
Apply the cleanup prompt after this pass for high-confidence content fixes.
"""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path


TIMING_RE = re.compile(
    r"^(?P<start>(?:\d{2}:)?\d{2}:\d{2}\.\d{3})\s+-->\s+"
)
INLINE_TIME_RE = re.compile(r"<(?:\d{2}:)?\d{2}:\d{2}\.\d{3}>")
TAG_RE = re.compile(r"<[^>]+>")
SPACE_RE = re.compile(r"\s+")
SENTENCE_END_RE = re.compile(r'[.!?][\)"\]]?$')
DURATION_LINE_RE = re.compile(
    r"^\s*(?:(?:\d+\s+hours?,\s*)?(?:\d+\s+minutes?,\s*)?\d+\s+seconds?|"
    r"(?:\d+\s+hours?,\s*)?\d+\s+minutes?|"
    r"\d+\s+hours?)\s*$",
    re.IGNORECASE,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Clean a YouTube .vtt transcript into timestamped plain text. "
            "This removes caption scaffolding and rolling-caption duplication "
            "without summarizing or rewriting content."
        )
    )
    parser.add_argument("input", type=Path, help="Path to the source .vtt file.")
    parser.add_argument(
        "output",
        type=Path,
        help="Path where the cleaned transcript .txt file should be written.",
    )
    parser.add_argument(
        "--min-words",
        type=int,
        default=35,
        help="Minimum words to prefer before ending a paragraph. Default: 35.",
    )
    parser.add_argument(
        "--max-words",
        type=int,
        default=95,
        help="Maximum words per paragraph before forcing a break. Default: 95.",
    )
    return parser.parse_args()


def normalize_timestamp(value: str) -> str:
    if value.count(":") == 1:
        return f"00:{value.rsplit('.', 1)[0]}"
    return value.rsplit(".", 1)[0]


def clean_caption_line(line: str) -> str:
    line = html.unescape(line)
    line = INLINE_TIME_RE.sub("", line)
    line = TAG_RE.sub("", line)
    return SPACE_RE.sub(" ", line).strip()


def extract_cues(raw_text: str) -> list[tuple[str, str]]:
    lines = raw_text.splitlines()
    cues: list[tuple[str, str]] = []
    index = 0

    while index < len(lines):
        match = TIMING_RE.match(lines[index].strip())
        if not match:
            index += 1
            continue

        timestamp = normalize_timestamp(match.group("start"))
        index += 1
        text_lines: list[str] = []

        while index < len(lines) and not TIMING_RE.match(lines[index].strip()):
            cleaned = clean_caption_line(lines[index])
            if cleaned and not DURATION_LINE_RE.match(cleaned):
                text_lines.append(cleaned)
            index += 1

        text = SPACE_RE.sub(" ", " ".join(text_lines)).strip()
        if text:
            cues.append((timestamp, text))

    return cues


def append_without_overlap(
    emitted_words: list[str],
    word_timestamps: list[str],
    timestamp: str,
    cue_text: str,
) -> None:
    cue_words = cue_text.split()
    if not cue_words:
        return

    max_overlap = min(len(emitted_words), len(cue_words), 80)
    overlap = 0
    for size in range(max_overlap, 0, -1):
        if emitted_words[-size:] == cue_words[:size]:
            overlap = size
            break

    if overlap == len(cue_words):
        return

    new_words = cue_words[overlap:]
    emitted_words.extend(new_words)
    word_timestamps.extend([timestamp] * len(new_words))


def paragraphize(
    words: list[str],
    word_timestamps: list[str],
    min_words: int,
    max_words: int,
) -> list[tuple[str, str]]:
    if min_words < 1:
        raise ValueError("--min-words must be at least 1")
    if max_words < min_words:
        raise ValueError("--max-words must be greater than or equal to --min-words")

    paragraphs: list[tuple[str, str]] = []
    start = 0
    while start < len(words):
        forced_end = min(start + max_words, len(words))
        chosen_end = forced_end

        for candidate in range(min(start + min_words, len(words)), forced_end):
            if SENTENCE_END_RE.search(words[candidate]):
                chosen_end = candidate + 1
                break

        if forced_end == len(words) and len(words) - chosen_end < 18:
            chosen_end = len(words)

        timestamp = word_timestamps[min(start, len(word_timestamps) - 1)]
        text = " ".join(words[start:chosen_end]).strip()
        if text:
            paragraphs.append((timestamp, text))
        start = chosen_end

    return paragraphs


def clean_vtt(raw_text: str, min_words: int, max_words: int) -> str:
    cues = extract_cues(raw_text)
    emitted_words: list[str] = []
    word_timestamps: list[str] = []

    for timestamp, cue_text in cues:
        append_without_overlap(emitted_words, word_timestamps, timestamp, cue_text)

    if not emitted_words:
        return ""

    paragraphs = paragraphize(emitted_words, word_timestamps, min_words, max_words)
    return "\n\n".join(f"[{timestamp}] {text}" for timestamp, text in paragraphs) + "\n"


def main() -> int:
    args = parse_args()
    if args.input.suffix.lower() != ".vtt":
        print(f"Input file must be a .vtt file: {args.input}", file=sys.stderr)
        return 2
    if not args.input.exists():
        print(f"Input file not found: {args.input}", file=sys.stderr)
        return 2

    try:
        raw_text = args.input.read_text(encoding="utf-8")
        cleaned = clean_vtt(raw_text, args.min_words, args.max_words)
    except UnicodeDecodeError as exc:
        print(f"Could not read input as UTF-8: {exc}", file=sys.stderr)
        return 2
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    if not cleaned.strip():
        print("No caption text found in the VTT file.", file=sys.stderr)
        return 3

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(cleaned, encoding="utf-8")
    print(f"Cleaned transcript written: {args.output}")
    print(f"Output lines: {len(cleaned.splitlines())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
