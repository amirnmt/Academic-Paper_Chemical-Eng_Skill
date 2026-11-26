#!/usr/bin/env python3
"""Convert PDFs (and other documents) to Markdown text for searching.

Usage:
  python scripts/convert_to_markdown.py INPUT_DIR_OR_FILE OUTPUT_DIR [--engine auto|markitdown|pymupdf|pypdf]
                                        [--overwrite]

Engines, tried in this order with --engine auto:
  markitdown  pip install 'markitdown[pdf]'  (also converts .docx, .pptx, .html)
  pymupdf     pip install pymupdf            (fast; good reading order for two-column papers)
  pypdf       pip install pypdf

Each input file becomes OUTPUT_DIR/<same name>.md. Existing outputs are skipped
unless --overwrite is given. Conversion keeps the text but damages equations,
tables and some layouts: check numbers and equations against the original.
"""
import argparse
import os
import re
import sys
from pathlib import Path

PDF_ONLY = {".pdf"}
MARKITDOWN_EXTS = {".pdf", ".docx", ".pptx", ".xlsx", ".html", ".htm", ".epub"}


def engine_markitdown():
    from markitdown import MarkItDown  # noqa: WPS433
    md = MarkItDown()
    return (lambda p: md.convert(long_path(p)).text_content), MARKITDOWN_EXTS


def engine_pymupdf():
    try:
        import pymupdf as fitz  # noqa: WPS433
    except ImportError:
        import fitz  # noqa: WPS433
        if not hasattr(fitz, "Document"):  # an unrelated package called "fitz"
            raise ImportError("fitz is not PyMuPDF")

    def convert(p):
        with fitz.open(long_path(p)) as doc:
            return "\n\n".join(page.get_text("text") for page in doc)
    return convert, PDF_ONLY


def engine_pypdf():
    from pypdf import PdfReader  # noqa: WPS433

    def convert(p):
        return "\n\n".join((page.extract_text() or "") for page in PdfReader(long_path(p)).pages)
    return convert, PDF_ONLY


def long_path(p):
    """Windows refuses paths over 260 characters unless they carry the \\\\?\\ prefix."""
    s = str(Path(p).resolve())
    if os.name == "nt" and len(s) >= 240 and not s.startswith("\\\\?\\"):
        return "\\\\?\\" + s
    return s


LIGATURES = {"\ufb00": "ff", "\ufb01": "fi", "\ufb02": "fl", "\ufb03": "ffi", "\ufb04": "ffl",
             "\ufb05": "st", "\ufb06": "st", "\u00ad": ""}


def tidy(text):
    """Replace typographic ligatures (\ufb01 -> fi) and soft hyphens so words can be searched."""
    # a soft hyphen at a line end splits a word ("in\u00ad\ncreases"): join the parts
    text = re.sub(r"\u00ad[ \t]*\r?\n[ \t]*", "", text)
    for a, b in LIGATURES.items():
        text = text.replace(a, b)
    return text


ENGINES = {"markitdown": engine_markitdown, "pymupdf": engine_pymupdf, "pypdf": engine_pypdf}


def pick_engine(name):
    names = list(ENGINES) if name == "auto" else [name]
    errors = []
    for n in names:
        try:
            conv, exts = ENGINES[n]()
            return n, conv, exts
        except ImportError as e:
            errors.append(f"{n}: {e}")
    sys.exit("No conversion engine available. Install one of: markitdown[pdf], pymupdf, pypdf.\n"
             + "\n".join(errors))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", help="folder (searched recursively) or single file")
    ap.add_argument("output", help="folder for the .md files")
    ap.add_argument("--engine", default="auto", choices=["auto", *ENGINES])
    ap.add_argument("--overwrite", action="store_true", help="convert again even if the .md exists")
    args = ap.parse_args()

    name, convert, exts = pick_engine(args.engine)
    src = Path(args.input)
    files = [src] if src.is_file() else sorted(p for p in src.rglob("*") if p.suffix.lower() in exts)
    if not files:
        sys.exit(f"No convertible files found in {src} (engine {name}: {', '.join(sorted(exts))}).")
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)
    done = skipped = failed = 0
    for f in files:
        target = out / (f.stem + ".md")
        if os.path.exists(long_path(target)) and not args.overwrite:
            skipped += 1
            continue
        try:
            text = tidy(convert(f))
        except Exception as e:  # keep going: one damaged PDF should not stop the batch
            print(f"FAILED  {f.name}: {e}")
            failed += 1
            continue
        if len(text.strip()) < 200:
            print(f"WARNING {f.name}: almost no text extracted (scanned PDF? needs OCR)")
        with open(long_path(target), "w", encoding="utf-8") as fh:
            fh.write(text)
        done += 1
    print(f"Engine: {name}. Converted {done}, skipped {skipped} existing, failed {failed}. Output: {out}")


if __name__ == "__main__":
    main()
