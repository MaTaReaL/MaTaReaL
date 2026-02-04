#!/usr/bin/env python3
"""Simple PDF to Word (DOCX) converter."""

from __future__ import annotations

import argparse
import pathlib
import sys

try:
    from pdf2docx import Converter
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "Missing dependency 'pdf2docx'. Install it with: pip install -r requirements.txt"
    ) from exc


def convert_pdf_to_docx(input_path: pathlib.Path, output_path: pathlib.Path) -> None:
    converter = Converter(str(input_path))
    try:
        converter.convert(str(output_path), start=0, end=None)
    finally:
        converter.close()


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert a PDF file to a Word DOCX file."
    )
    parser.add_argument("input", type=pathlib.Path, help="Path to the PDF file")
    parser.add_argument(
        "-o",
        "--output",
        type=pathlib.Path,
        help="Path to the output DOCX file (default: same name with .docx)",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    input_path = args.input
    if not input_path.exists():
        print(f"Input file not found: {input_path}", file=sys.stderr)
        return 1
    if input_path.suffix.lower() != ".pdf":
        print("Input file must be a PDF.", file=sys.stderr)
        return 1

    output_path = args.output or input_path.with_suffix(".docx")
    convert_pdf_to_docx(input_path, output_path)
    print(f"Saved: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
