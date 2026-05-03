#!/usr/bin/env python3
"""Search ACSM sports nutrition course references.

Usage:
    python scripts/search_course.py 碳水 糖原
    python scripts/search_course.py --limit 20 蛋白质 减脂
"""

from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REFERENCES = ROOT / "references"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Search course reference markdown files.")
    parser.add_argument("keywords", nargs="+", help="Keywords to search for.")
    parser.add_argument("--limit", type=int, default=30, help="Maximum matches to print.")
    parser.add_argument(
        "--context",
        type=int,
        default=80,
        help="Characters of context to show before and after the match.",
    )
    return parser.parse_args()


def snippet(line: str, keyword: str, context: int) -> str:
    compact = " ".join(line.strip().split())
    index = compact.lower().find(keyword.lower())
    if index == -1:
        return compact[: context * 2]
    start = max(index - context, 0)
    end = min(index + len(keyword) + context, len(compact))
    prefix = "..." if start > 0 else ""
    suffix = "..." if end < len(compact) else ""
    return f"{prefix}{compact[start:end]}{suffix}"


def iter_markdown_files() -> list[Path]:
    files = sorted(
        path
        for path in REFERENCES.glob("*.md")
        if path.name not in {"safety_boundaries.md", "study_paths.md", "reference_map.md"}
    )
    return sorted(files, key=lambda path: (path.name == "course_index.md", path.name))


def main() -> int:
    args = parse_args()
    keywords = [keyword.strip() for keyword in args.keywords if keyword.strip()]
    if not keywords:
        return 1

    printed = 0
    for path in iter_markdown_files():
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            lines = path.read_text().splitlines()

        for line_number, line in enumerate(lines, start=1):
            matched = next((keyword for keyword in keywords if keyword.lower() in line.lower()), None)
            if not matched:
                continue
            print(f"{path.relative_to(ROOT)}:{line_number}: {snippet(line, matched, args.context)}")
            printed += 1
            if printed >= args.limit:
                return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
