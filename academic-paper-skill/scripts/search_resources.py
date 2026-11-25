#!/usr/bin/env python3
"""Search the full-text resources (converted writing guides and papers).

Usage:
  python scripts/search_resources.py TERM [TERM ...] [--dir DIR] [--context N] [--max N]
  python scripts/search_resources.py --list
  python scripts/search_resources.py --headings [--dir DIR]

All terms must occur within the context window around a matching line
(default: +/- 3 lines). A term with spaces ("topic sentence") is matched as a
phrase. Matching ignores case and line breaks inside a phrase. Output is
Markdown: file, line number, nearest heading, and the passage.

Standard library only.
"""
import argparse
import os
import re
import sys
import unicodedata
from pathlib import Path

DEFAULT_DIR = Path(__file__).resolve().parent.parent / "resources"
EXTS = {".md", ".txt", ".markdown"}

# Markdown heading, or a numbered chapter/section title such as
# "8. Abstract and Keywords" or "2.3 Reporting results" (short line, no final full stop).
HEADING_RX = re.compile(
    r"^(#{1,6}\s+\S.*|(\d{1,2}(\.\d{1,2}){0,2}\.?)\s+[A-Z][^.]{2,70})$"
)
PAGE_NUM_RX = re.compile(r"\s+\d{1,4}$")  # running heads end with a page number



def read_text(path):
    """Read a text file; on Windows also paths longer than 260 characters."""
    s = str(Path(path).resolve())
    if os.name == "nt" and len(s) >= 240 and not s.startswith("\\\\?\\"):
        s = "\\\\?\\" + s
    with open(s, encoding="utf-8", errors="replace") as fh:
        return fh.read()

def iter_files(root):
    root = Path(root)
    if root.is_file():
        yield root
        return
    for p in sorted(root.rglob("*")):
        if p.is_file() and p.suffix.lower() in EXTS and p.name.lower() != "readme.md" \
                and p.name.upper() != "NOTICE.MD":
            yield p


def read_lines(path):
    # NFKC turns ligatures such as \ufb01 into "fi" so that words match
    return unicodedata.normalize("NFKC", read_text(path)).splitlines()


def headings_of(lines):
    out = []
    for i, line in enumerate(lines):
        s = line.strip()
        if s and len(s) <= 90 and HEADING_RX.match(s):
            out.append((i, PAGE_NUM_RX.sub("", s.lstrip("# ").strip())))
    return out


def nearest_heading(heads, idx):
    best = ""
    for i, h in heads:
        if i <= idx:
            best = h
        else:
            break
    return best


def term_regex(term):
    words = [re.escape(w) for w in term.split()]
    # allow line breaks / hyphenation / multiple spaces between words of a phrase
    return re.compile(r"[\s\-]+".join(words), re.IGNORECASE)


def search_file(path, terms, context, max_hits):
    lines = read_lines(path)
    if not lines:
        return [], False
    heads = headings_of(lines)
    rxs = [term_regex(t) for t in terms]
    first = rxs[0]
    hits, last_end = [], -1
    n = len(lines)
    for i, line in enumerate(lines):
        # first term may be split across this and the next line
        two = line + " " + (lines[i + 1] if i + 1 < n else "")
        if not first.search(two):
            continue
        lo, hi = max(0, i - context), min(n, i + context + 1)
        window = " ".join(lines[lo:hi])
        if not all(rx.search(window) for rx in rxs[1:]):
            continue
        if lo <= last_end:  # overlapping with previous hit: extend it
            prev = hits[-1]
            hits[-1] = (prev[0], hi, prev[2])
        else:
            hits.append((lo, hi, nearest_heading(heads, i)))
        last_end = hi
        if len(hits) > max_hits:  # one extra hit shows that results were cut
            break
    results = []
    for lo, hi, head in hits[:max_hits]:
        passage = "\n".join(lines[lo:hi]).strip()
        for rx in rxs:
            passage = rx.sub(lambda m: f"**{m.group(0)}**", passage)
        results.append((lo + 1, head, passage))
    return results, len(hits) > max_hits


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("terms", nargs="*", help="search terms; all must occur in the window")
    ap.add_argument("--dir", default=str(DEFAULT_DIR), help="folder or file to search (default: resources/)")
    ap.add_argument("--context", type=int, default=3, help="lines before and after a match (default 3)")
    ap.add_argument("--max", type=int, default=8, help="maximum passages per file (default 8)")
    ap.add_argument("--list", action="store_true", help="list searchable files")
    ap.add_argument("--headings", action="store_true", help="list the headings found in each file")
    args = ap.parse_args()

    root = Path(args.dir)
    if not root.exists():
        sys.exit(f"Not found: {root}")
    files = list(iter_files(root))
    if not files:
        sys.exit(f"No .md or .txt files under {root}. See resources/README.md.")

    if args.list:
        print(f"# Searchable files under {root}\n")
        for f in files:
            print(f"- {f.relative_to(root) if root.is_dir() else f.name}  ({len(read_text(f).encode('utf-8')) // 1024} KB)")
        return
    if args.headings:
        for f in files:
            print(f"\n## {f.name}\n")
            seen = set()
            for i, h in headings_of(read_lines(f)):
                if h not in seen:
                    seen.add(h)
                    print(f"- L{i + 1}: {h}")
        return
    if not args.terms:
        ap.error("give at least one search term, or --list / --headings")

    total = 0
    print(f"# Search: {' + '.join(args.terms)}\n")
    for f in files:
        res, cut = search_file(f, args.terms, args.context, args.max)
        if not res:
            continue
        more = "; more exist, raise --max or add a term" if cut else ""
        print(f"## {f.name}  ({len(res)} passage{'s' if len(res) != 1 else ''}{more})\n")
        for line_no, head, passage in res:
            print(f"**L{line_no}**" + (f" ({head})" if head else ""))
            print()
            for pl in passage.splitlines():
                print(f"> {pl}")
            print()
        total += len(res)
    if total == 0:
        print("No passages found. Try fewer terms, a larger --context, or synonyms.")


if __name__ == "__main__":
    main()
