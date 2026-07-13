#!/usr/bin/env python3
"""Plain text excerpt -> TEI P5 XML.

Date: 10.11.2024

Reads a plain-text fiction excerpt and encodes it as TEI P5 XML so the corpus can be
queried and annotated in a standard digital humanities format. It splits the file
into logical paragraphs, merges line breaks that continue a sentence, and groups
passages under chapter <div> elements when headings match "Chapter N". Each body
paragraph receives a stable xml:id (p00001, …) for later cultural tagging in CSV
and TEI <note> elements. The script is the first step in the pipeline: structured
TEI is required before exporting passages for annotation and building reports.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from cultural_tei.constants import DEFAULT_AUTHOR, DEFAULT_TITLE
from cultural_tei.text_to_tei import convert_txt_to_tei

PROJECT = Path(__file__).resolve().parent

# Edit these paths for another excerpt, or pass arguments on the command line.
INPUT_PATH = PROJECT / "Possession_1000.txt"
OUTPUT_PATH = PROJECT / "Possession_1000.tei.xml"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input",
        nargs="?",
        default=str(INPUT_PATH),
        help=f"Source plain-text file (default: {INPUT_PATH.name})",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=str(OUTPUT_PATH),
        help=f"TEI XML output (default: {OUTPUT_PATH.name})",
    )
    parser.add_argument("--title", default=DEFAULT_TITLE)
    parser.add_argument("--author", default=DEFAULT_AUTHOR)
    args = parser.parse_args(argv)

    inp = Path(args.input)
    out = Path(args.output)
    n = convert_txt_to_tei(inp, out, title=args.title, author=args.author)
    print(f"Wrote {out} ({n} paragraphs)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
