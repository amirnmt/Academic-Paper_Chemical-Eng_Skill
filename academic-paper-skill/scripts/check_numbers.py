#!/usr/bin/env python3
"""Check that every number in a draft is traceable to the results log.

Usage:
    python check_numbers.py draft.tex --log results_log.md
    python check_numbers.py sections/*.tex --log results_log.md --min 0 --show-matched
    python check_numbers.py draft.md --log results_log.md --include-equations

For each number in the draft it looks for a value in the log that rounds to it
(2.37 in the log matches 2.4 and 2.37 in the draft; 0.0123 matches 1.23 %
only if the log also lists 1.23). It also flags patterns that often signal a
result no run produced (references/research-integrity.md §2, F3):
  - the same uncertainty (± value) repeated in three or more places;
  - exactly round improvement or reduction figures ("by 50 %", "2 times faster").

Skipped by default: years 1900-2099, numbers in citations, cross-references
(Fig. 3, Table 2, Section 4.1, Eq. (5)), labels, small integers below --min
(default 10, so counts like "three cases" or "5 layers" are not reported),
and display equations (add --include-equations to check them).

Only the standard library is needed. Exit code 1 means untraced numbers were found.
A match shows that the value exists in the log, not that it is used for the
right quantity: check the context column.
"""
import argparse
import re
import sys
from collections import defaultdict

NUM = re.compile(
    r"(?<![A-Za-z_\\\d.])"
    r"([-−–]?\d{1,3}(?:[,\u2009\u202f]\d{3})+(?:\.\d+)?|[-−–]?\d+(?:\.\d+)?)"
    r"(?:\s*(?:[eE]([-−+]?\d+)|\s*(?:\\times|×|x)\s*10\^?\{?([-−+]?\d+)\}?))?"
    r"(?![\d])"
)
XREF = re.compile(
    r"\b(?:Fig(?:ure)?s?\.?|Tables?|Tab\.|Sections?|Sec\.|Eqs?\.?|Equations?|Appendix|Ref\.|Refs\.|Chapter|Step|Case|Scenario|Run|Algorithm|Line)\s*~?\(?\s*[A-Z]?\d+(?:\.\d+)*(?:\s*[-–,]\s*\d+)*\)?",
    re.I,
)
LATEX_DROP = [
    (re.compile(r"(?<!\\)%.*"), ""),
    (re.compile(r"\\(?:label|ref|eqref|cref|Cref|autoref|cite[pt]?|citep|citet|citeauthor|citeyear|includegraphics|url|href|bibliography|input|include)\s*(?:\[[^\]]*\])?\{[^}]*\}"), " "),
    (re.compile(r"\\(?:begin|end)\{[^}]*\}"), " "),
    (re.compile(r"\\(?:vspace|hspace|setlength|addtolength)\*?\{[^}]*\}"), " "),
    (re.compile(r"\\(?:sub)*section\*?\{"), "{"),
]
DISPLAY_MATH = re.compile(
    r"\\begin\{(equation|align|gather|multline|eqnarray)\*?\}.*?\\end\{\1\*?\}|\\\[.*?\\\]|\$\$.*?\$\$", re.S
)
CITATION_BRACKETS = re.compile(r"\[(?:\d+(?:\s*[-–,]\s*\d+)*)\]")
AUTHOR_YEAR = re.compile(r"\([A-Z][^()]{0,80}?\b(?:19|20)\d{2}[a-z]?\)")
PLUSMINUS = re.compile(r"(?:\\pm|±)\s*\$?\s*(\d+(?:\.\d+)?)")
ROUND_CLAIM = re.compile(
    r"\b(?:improv\w*|reduc\w*|increas\w*|decreas\w*|lower\w*|higher|faster|slower|better|outperform\w*|gain\w*|sav\w*)\b[^.]{0,40}?"
    r"\b((?:[1-9]0|[1-9]5|100)(?:\.0+)?\s*(?:\\?%|percent)|(?:2|3|4|5|10)(?:\.0+)?\s*(?:times|×|\\times|-fold|fold))",
    re.I,
)


def to_float(mant: str, exp1, exp2):
    s = mant.replace("−", "-").replace("–", "-").replace(",", "").replace("\u2009", "").replace("\u202f", "")
    v = float(s)
    e = exp1 or exp2
    if e:
        v *= 10 ** int(e.replace("−", "-").replace("+", ""))
    return v


def decimals(mant: str, exp1, exp2) -> int:
    d = len(mant.split(".")[1]) if "." in mant else 0
    e = exp1 or exp2
    if e:
        d -= int(e.replace("−", "-").replace("+", ""))
    return d


def clean(text: str, is_tex: bool, include_eq: bool) -> str:
    if is_tex:
        if not include_eq:
            text = DISPLAY_MATH.sub(lambda m: "\n" * m.group(0).count("\n"), text)
        for rx, rep in LATEX_DROP:
            text = rx.sub(rep, text)
    else:
        if not include_eq:
            text = DISPLAY_MATH.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    text = CITATION_BRACKETS.sub(" ", text)
    text = AUTHOR_YEAR.sub(" ", text)
    text = XREF.sub(" ", text)
    return text


def numbers(line: str):
    for m in NUM.finditer(line):
        mant, e1, e2 = m.group(1), m.group(2), m.group(3)
        try:
            v = to_float(mant, e1, e2)
        except ValueError:
            continue
        yield m, v, decimals(mant, e1, e2)


def load_log(path: str):
    vals = []
    for line in open(path, encoding="utf-8", errors="replace"):
        if line.lstrip().startswith("#"):
            continue
        for m, v, d in numbers(line):
            vals.append((abs(v), d))
    return vals


def matches(v: float, d: int, log) -> bool:
    v = abs(v)
    tol = 0.5 * 10 ** (-d) + 1e-12 if d > -20 else 0
    for lv, ld in log:
        if abs(lv - v) <= tol or abs(lv - v) <= 1e-9 * max(1.0, lv):
            return True
    return False


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+")
    ap.add_argument("--log", required=True, help="results_log.md (any text file with the traced values)")
    ap.add_argument("--min", type=float, default=10, help="ignore integers with absolute value below this (default 10)")
    ap.add_argument("--include-equations", action="store_true", help="also check numbers in display equations")
    ap.add_argument("--show-matched", action="store_true", help="also list numbers that were found in the log")
    a = ap.parse_args()

    log = load_log(a.log)
    print(f"Log: {a.log} ({len(log)} values)")
    total_untraced = 0
    for path in a.files:
        raw = open(path, encoding="utf-8", errors="replace").read()
        text = clean(raw, path.endswith(".tex"), a.include_equations)
        untraced, matched = [], []
        pm = defaultdict(list)
        rounds = []
        for no, line in enumerate(text.splitlines(), 1):
            if line.lstrip().startswith(("|---", "\\documentclass", "\\usepackage")):
                continue
            for m, v, d in numbers(line):
                is_int = d <= 0 and float(v).is_integer()
                if is_int and 1900 <= abs(v) <= 2099:
                    continue
                if is_int and abs(v) < a.min:
                    continue
                ctx = line[max(0, m.start() - 35): m.end() + 25].strip()
                (matched if matches(v, d, log) else untraced).append((no, m.group(0).strip(), ctx))
            for m in PLUSMINUS.finditer(line):
                pm[m.group(1)].append(no)
            for m in ROUND_CLAIM.finditer(line):
                rounds.append((no, m.group(0).strip()))
        print(f"\n== {path}")
        print(f"  numbers checked: {len(untraced) + len(matched)}; in log: {len(matched)}; NOT in log: {len(untraced)}")
        for no, val, ctx in untraced:
            print(f"  line {no:>5}  untraced  {val:<14} … {ctx} …")
        if a.show_matched:
            for no, val, ctx in matched:
                print(f"  line {no:>5}  ok        {val:<14} … {ctx} …")
        reps = {k: v for k, v in pm.items() if len(v) >= 3}
        for k, lines in reps.items():
            print(f"  CHECK  the same uncertainty ±{k} appears {len(lines)} times (lines {', '.join(map(str, lines[:8]))}): "
                  "are these computed separately?")
        for no, s in rounds:
            print(f"  line {no:>5}  CHECK  round figure in a comparison: '{s}': confirm it is the exact computed value")
        total_untraced += len(untraced)
    print("\nEvery untraced number is either added to the log with its source or removed from the draft "
          "(references/research-integrity.md §1).")
    return 1 if total_untraced else 0


if __name__ == "__main__":
    sys.exit(main())
