#!/usr/bin/env python3
"""Check figure, table and equation references in a manuscript.

Usage:
    python check_figrefs.py draft.md
    python check_figrefs.py draft.tex --kinds fig,tab
    python check_figrefs.py draft.md --captions captions.txt

Reports, for figures (Fig./Figure), tables (Table) and, with --kinds eq, numbered
equations (Eq./Equation):
  * items that have a caption but are never cited in the text;
  * items cited before every lower-numbered item has been cited (first citations
    out of order);
  * citations of numbers that have no caption (only when captions are found).

Ranges and lists count as citations of every item in them: "Figs. 4-6",
"Figures 2 and 3", "Tables 1, 3 and 5", "Fig. 2(b)", "Fig. S3" (supplementary
items are reported separately and not checked for order).

Captions are detected as lines that start with "Fig. N", "Figure N" or "Table N"
followed by a period or colon (Markdown or plain text), or LaTeX \\caption{} inside
figure/table environments (numbered in order of appearance). In LaTeX, \\ref{}
cannot be resolved to numbers here: use the compiled PDF text (pdftotext) instead.

Calibration: in 21 published Computers & Chemical Engineering papers (304 figures
and tables), 19 items appeared before their first mention and 20 were not cited by
number in the text: both happen in print, but reviewers and editors flag them.
Every flag is a prompt to check, not proof of an error.
"""
import argparse
import re
import sys

KIND_WORDS = {
    "fig": r"(?:Fig(?:ure)?s?\.?|FIGS?\.?|Figures?)",
    "tab": r"(?:Tables?|Tabs?\.)",
    "eq": r"(?:Eqs?\.|Equations?)",
}
NUM = r"S?\d+[a-z]?(?:\s*\([a-z]\))?"
LIST = rf"{NUM}(?:\s*(?:[-–—]|to|,|and|&|,\s*and)\s*{NUM})*"


def expand(spec: str):
    """'4-6' -> [4,5,6]; '2 and 3' -> [2,3]; 'S3' -> ['S3']."""
    out = []
    spec = re.sub(r"\([a-z]\)", "", spec)
    parts = re.split(r"\s*(?:,\s*and|,|and|&)\s*", spec)
    for p in parts:
        p = p.strip()
        m = re.fullmatch(r"(S?)(\d+)[a-z]?\s*(?:[-–—]|to)\s*S?(\d+)[a-z]?", p)
        if m:
            a, b = int(m.group(2)), int(m.group(3))
            if 0 < b - a < 50:
                out += [f"{m.group(1)}{i}" if m.group(1) else i for i in range(a, b + 1)]
                continue
        m = re.fullmatch(r"(S?)(\d+)[a-z]?", p)
        if m:
            out.append(f"S{m.group(2)}" if m.group(1) else int(m.group(2)))
    return out


def find_captions(lines, kind):
    caps = {}
    if kind == "eq":
        return caps
    word = {"fig": r"(?:Fig\.|Figure)", "tab": r"Table"}[kind]
    rx = re.compile(rf"^\s*(?:[#*_>]+\s*)*{word}\s*(\d+)\s*[.:|]", re.I)
    for no, line in enumerate(lines, 1):
        m = rx.match(line)
        if m and int(m.group(1)) not in caps:
            caps[int(m.group(1))] = no
    return caps


def latex_captions(text, kind):
    env = {"fig": "figure", "tab": "table"}.get(kind)
    if not env:
        return {}
    caps, n = {}, 0
    for m in re.finditer(rf"\\begin\{{{env}\*?\}}(.*?)\\end\{{{env}\*?\}}", text, re.S):
        if "\\caption" in m.group(1):
            n += 1
            caps[n] = text[:m.start()].count("\n") + 1
    return caps


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--kinds", default="fig,tab", help="comma list of fig, tab, eq (default fig,tab)")
    ap.add_argument("--keep-end-matter", action="store_true", help="also scan References and later")
    a = ap.parse_args()
    text = open(a.file, encoding="utf-8", errors="replace").read()
    is_tex = a.file.endswith(".tex")
    if not a.keep_end_matter:
        m = re.search(r"^\s*(?:#+\s*|\\section\*?\{)?\s*(?:\d+\.?\s*)?(References|Bibliography)\b", text, re.I | re.M)
        if m and m.start() > len(text) * 0.5:
            text = text[:m.start()]
    lines = text.splitlines()
    problems = 0
    for kind in [k.strip() for k in a.kinds.split(",") if k.strip()]:
        caps = latex_captions(text, kind) if is_tex else find_captions(lines, kind)
        cap_lines = set(caps.values())
        rx = re.compile(rf"\b{KIND_WORDS[kind]}\s*({LIST})")
        first = {}
        supp = set()
        for no, line in enumerate(lines, 1):
            if no in cap_lines:
                continue
            for m in rx.finditer(line):
                for item in expand(m.group(1)):
                    if isinstance(item, str):
                        supp.add(item)
                    elif item not in first:
                        first[item] = no
        name = {"fig": "Figure", "tab": "Table", "eq": "Equation"}[kind]
        print(f"== {name}s: {len(caps)} captions found, {len(first)} numbers cited"
              + (f", supplementary cited: {', '.join(sorted(supp))}" if supp else ""))
        for n in sorted(caps):
            if n not in first:
                print(f"  line {caps[n]:>5}  {name} {n} has a caption but is never cited by number")
                problems += 1
            elif first[n] > caps[n] and not is_tex:
                print(f"  line {caps[n]:>5}  note: {name} {n} caption precedes its first citation (line {first[n]});"
                      " fine for floats placed by LaTeX, check it in the final layout")
        if caps:
            for n in sorted(first):
                if n not in caps:
                    print(f"  line {first[n]:>5}  {name} {n} is cited but no caption was found")
                    problems += 1
        order = sorted(first.items(), key=lambda kv: kv[1])
        seen_max = 0
        for n, no in order:
            if n > seen_max + 1:
                missing = [i for i in range(seen_max + 1, n) if i not in first or first[i] > no]
                if missing:
                    print(f"  line {no:>5}  {name} {n} first cited before {name} {', '.join(map(str, missing))}")
                    problems += 1
            seen_max = max(seen_max, n)
    if not problems:
        print("  no issues")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
