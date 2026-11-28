#!/usr/bin/env python3
"""Check acronyms and abbreviations in a manuscript.

Usage:
    python check_acronyms.py draft.tex
    python check_acronyms.py draft.md --abstract abstract.md --allow CFD,ODE
    python check_acronyms.py main.tex --allow-file my_acronyms.txt

Rules checked (common journal copy-editing practice; the journal's own rules win):
  1. Defined at first use: the term written out, followed by its acronym in brackets,
     "ethylene oxide (EO)". Later uses take the acronym alone.
  2. The abstract is a separate scope: an acronym used there is defined there,
     and again in the body (pass the abstract with --abstract, or let the script
     find a LaTeX abstract environment or a Markdown "Abstract" heading).
  3. Defined only once per scope.
  4. Defined but used fewer than --min-uses times after the definition
     (default 2): consider writing the term out instead.
  5. Not used in the title or headings without need (reported as a note).

Common abbreviations (SI units, chemical formulas, DNA, CPU, ...) are allowed by
default; add your own with --allow or --allow-file (one per line). Only the
standard library is needed. The script never changes the file.
"""
import argparse
import re
import sys
from collections import Counter, defaultdict

DEFAULT_ALLOW = set("""
SI UK USA US EU UN DNA RNA PDF URL DOI ISBN ISSN CPU GPU RAM PC ID OK PhD MSc BSc
AM PM CO CO2 H2O O2 N2 H2 CH4 NOx SOx NH3 HCl NaCl
K Pa kPa MPa GPa MW kW GW kJ MJ J W V A Hz mol kmol min ms ns
LaTeX BibTeX TeX MATLAB IEEE ISO ASME AIChE ACS RSC
I II III IV V VI VII VIII IX X
kWh MWh GWh TWh Wh GJ TJ PJ MMBtu USD EUR GBP CNY MHz GHz kHz KB MB GB TB
GAMS CPLEX GUROBI BARON IPOPT CONOPT DICOPT SCIP YALMIP CasADi COMSOL ANSYS
""".split())

ELEMENTS = set("""H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge
As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pt Au Hg Pb Bi U""".split())


def is_formula(tok: str) -> bool:
    """True for chemical formulas such as ZnO, SiO2, SO2, CaCl2 (all parts are element symbols)."""
    parts = re.findall(r"[A-Z][a-z]?\d*", tok)
    return "".join(parts) == tok and len(parts) >= 2 and all(re.sub(r"\d", "", x) in ELEMENTS for x in parts)


def is_name(tok: str) -> bool:
    """True for camel-case product or proper names (SimaPro, PyTorch, ScienceDirect, McGraw):
    a run of three or more lower-case letters after an inner capital."""
    return bool(re.search(r"[a-z]{3,}", tok)) and not tok.isupper()


END_MATTER = re.compile(r"^\s*(#+\s*|\\section\*?\{)?\s*(\d+\.?\s*)?(References|Bibliography|CRediT authorship|Declaration of competing|Declaration of generative AI|Acknowledg(e)?ments?|Data availability|Funding)\b", re.I | re.M)

ACRO = re.compile(r"\b([A-Z][A-Za-z]*[A-Z][A-Za-z0-9]*s?|[A-Z]{2,}[0-9]*s?)\b")
DEF = re.compile(r"([A-Za-z][A-Za-z\- ]{3,120}?)\s*\(\s*([A-Z][A-Za-z0-9]*[A-Z][A-Za-z0-9]*|[A-Z]{2,}[0-9]*)s?\s*[,;)]")


def strip_latex(t: str) -> str:
    t = re.sub(r"(?<!\\)%.*", "", t)
    t = re.sub(r"\\(?:label|ref|eqref|cref|Cref|cite[pt]?|citep|citet|includegraphics|url|href|usepackage|documentclass|bibliographystyle|bibliography)\s*(?:\[[^\]]*\])?\{[^}]*\}", " ", t)
    t = re.sub(r"\\begin\{(equation|align|gather|multline)\*?\}.*?\\end\{\1\*?\}", lambda m: "\n" * m.group(0).count("\n"), t, flags=re.S)
    t = re.sub(r"\$[^$]*\$", " ", t)
    return t


def split_scopes(text: str, is_tex: bool):
    """Return (abstract_text, abstract_offset_lines, body_text, body_offset_lines)."""
    if is_tex:
        m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", text, re.S)
        if m:
            abs_t = m.group(1)
            body = text[:m.start()] + "\n" * m.group(0).count("\n") + text[m.end():]
            return abs_t, text[:m.start(1)].count("\n"), body, 0
    else:
        m = re.search(r"^#+\s*Abstract\s*$(.*?)(?=^#+\s)", text, re.S | re.M | re.I)
        if m:
            body = text[:m.start()] + "\n" * m.group(0).count("\n") + text[m.end():]
            return m.group(1), text[:m.start(1)].count("\n"), body, 0
    return "", 0, text, 0


def initials_match(full: str, acro: str) -> bool:
    words_all = [w for w in re.split(r"[\s\-]+", full) if w]
    letters = acro.rstrip("s").upper()
    stop = {"of", "and", "the", "for", "in", "on", "with", "a", "an", "to", "by"}
    # allow one trailing word that is not part of the acronym ("... programming problem (MINLP)")
    for drop in (0, 1):
        words = words_all[:len(words_all) - drop] if drop else words_all
        if not words:
            continue
        # shortest tail of words whose initials (or leading letters) spell the acronym
        for k in range(1, min(len(words), len(letters) + 3) + 1):
            tail = words[-k:]
            s = "".join(w[0].upper() for w in tail if w.lower() not in stop)
            if s == letters or "".join(w[0].upper() for w in tail) == letters:
                return True
        for k in range(1, min(len(words), len(letters) + 2) + 1):
            joined = "".join(words[-k:]).upper()
            it = iter(joined)
            if joined[:1] == letters[:1] and all(c in it for c in letters):
                return True
    return False


def scan(scope_name: str, text: str, offset: int, allow: set, min_uses: int):
    issues = []
    defined = {}
    defs_count = Counter()
    uses = defaultdict(list)
    prev = ""   # tail of the previous two lines, for definitions broken across lines
    for no, line in enumerate(text.splitlines(), offset + 1):
        heading = bool(re.match(r"\s*(#+\s|\\(?:sub)*section\*?\{|\\title\{)", line))
        joined_line = (prev[-160:] + " " + line) if prev.strip() else line
        prev = (prev[-160:] + " " + line) if line.strip() else ""
        for m in DEF.finditer(joined_line):
            if m.end() <= len(joined_line) - len(line):
                continue  # definition lies wholly on the previous line (already handled)
            full, acro = m.group(1).strip(), m.group(2)
            if acro in allow:
                continue
            if initials_match(full, acro):
                defs_count[acro] += 1
                if acro in defined:
                    issues.append((no, scope_name, f"{acro} defined again (first defined on line {defined[acro]})"))
                else:
                    if uses[acro]:
                        issues.append((uses[acro][0], scope_name, f"{acro} used before its definition on line {no}"))
                    defined[acro] = no
        for m in ACRO.finditer(line):
            a = m.group(1)
            base = a[:-1] if a.endswith("s") and a[:-1] in defined else a
            if base in allow or a in allow or len(base.rstrip("s")) < 2:
                continue
            if re.fullmatch(r"[A-Z][a-z]+", base) or is_formula(base) or is_name(base):
                continue
            # skip the occurrence inside its own definition parentheses
            if re.search(r"\(\s*" + re.escape(a) + r"\s*[,;)]", line[max(0, m.start() - 2): m.end() + 2]) and defined.get(base) == no:
                continue
            if heading:
                issues.append((no, scope_name, f"note: {base} in a title or heading; write it out if the term is not well known"))
                continue
            uses[base].append(no)
    for a, lines in uses.items():
        if a not in defined:
            issues.append((lines[0], scope_name, f"{a} used ({len(lines)}×) but never defined in this scope"))
        else:
            after = [l for l in lines if l >= defined[a]]
            if len(after) < min_uses:
                issues.append((defined[a], scope_name,
                               f"{a} defined but used only {len(after)}× afterwards: consider writing it out"))
    return sorted(set(issues)), defined


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--abstract", help="separate abstract file (otherwise detected in the main file)")
    ap.add_argument("--allow", default="", help="comma-separated acronyms that need no definition")
    ap.add_argument("--allow-file", help="file with one allowed acronym per line")
    ap.add_argument("--min-uses", type=int, default=2)
    ap.add_argument("--keep-end-matter", action="store_true",
                    help="also check References, CRediT, declarations and acknowledgements (skipped by default)")
    a = ap.parse_args()

    allow = set(DEFAULT_ALLOW) | {x.strip() for x in a.allow.split(",") if x.strip()}
    if a.allow_file:
        allow |= {l.strip() for l in open(a.allow_file, encoding="utf-8") if l.strip() and not l.startswith("#")}
    raw = open(a.file, encoding="utf-8", errors="replace").read()
    is_tex = a.file.endswith(".tex")
    text = strip_latex(raw) if is_tex else raw
    abs_t, abs_off, body, body_off = split_scopes(text, is_tex)
    if not a.keep_end_matter:
        m = END_MATTER.search(body)
        if m and m.start() > len(body) * 0.5:
            body = body[:m.start()]
    if a.abstract:
        abs_raw = open(a.abstract, encoding="utf-8", errors="replace").read()
        abs_t, abs_off = (strip_latex(abs_raw) if a.abstract.endswith(".tex") else abs_raw), 0

    issues = []
    scopes = []
    if abs_t.strip():
        i, d = scan("abstract", abs_t, abs_off, allow, 1)
        issues += i
        scopes.append(f"abstract ({len(d)} defined)")
    i, d = scan("body", body, body_off, allow, a.min_uses)
    issues += i
    scopes.append(f"body ({len(d)} defined)")
    print(f"== {a.file}: scopes checked: {', '.join(scopes)}"
          + ("" if abs_t.strip() else "; no abstract found (pass --abstract to check it)"))
    if not issues:
        print("  no issues")
    for no, scope, msg in issues:
        print(f"  line {no:>5}  [{scope}]  {msg}")
    return 1 if any(not m.startswith("note:") for _, _, m in issues) else 0


if __name__ == "__main__":
    sys.exit(main())
