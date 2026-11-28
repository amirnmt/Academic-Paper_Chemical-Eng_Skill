#!/usr/bin/env python3
"""Find passages in a draft that repeat runs of words from your sources.

Usage:
    python check_overlap.py draft.tex --sources papers_md/
    python check_overlap.py intro.md methods.md --sources papers_md/ thesis.md --min-words 7
    python check_overlap.py draft.tex --sources papers/ --pdf --report overlap_report.md

What it does (references/plagiarism-and-paraphrasing.md §11):
  - reads the draft (.tex, .md, .txt) and every source file (.md, .txt; with
    --pdf also .pdf, if PyMuPDF is installed) in the given files or folders;
  - normalizes both (lower case, ligatures, line-break hyphens, LaTeX commands,
    citations and math removed);
  - reports every run of at least --min-words consecutive words (default 8)
    that also occurs in a source, merged into the longest matching passage,
    with the draft line, the source file and the source line;
  - skips text inside quotation marks (marked quotations are allowed), unless
    --include-quotes is given;
  - prints, per source, the share of draft words covered by matches with it, because
    overlap concentrated on one source is what editors look at first.

It checks only against the files you give it: the papers you cite (converted to
Markdown) and your own earlier texts (thesis, earlier papers) are the most likely
places for accidental overlap. It is not a substitute for the journal's
iThenticate screening, which compares against a much larger database.

Short shared technical phrases ("effective radial thermal conductivity") are
normal and are below the default threshold. For orientation: a published C&CE
paper checked against three other papers of the same journal shares about 1 %
of its words with each of them (stock phrases, dataset and method names). Titles
in your reference list match their sources; use --skip-references to leave the
reference list out. A flagged run is resolved by
quoting it, rewriting it from notes, or, for your own methods text, citing the
earlier publication. Exit code 1 if any run is found.
"""
import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

LIG = {"\ufb00": "ff", "\ufb01": "fi", "\ufb02": "fl", "\ufb03": "ffi", "\ufb04": "ffl",
       "\u2019": "'", "\u2018": "'", "\u201c": '"', "\u201d": '"', "\u2013": "-", "\u2014": "-"}
WORD = re.compile(r"[a-z0-9]+(?:'[a-z]+)?")


def clean_text(t: str, latex: bool) -> str:
    for k, v in LIG.items():
        t = t.replace(k, v)
    t = re.sub(r"([a-z])-\s+([a-z])", r"\1\2", t)  # words broken at a line end ("re- action", "re-\naction")
    if latex:
        t = re.sub(r"(?<!\\)%.*", "", t)
        t = re.sub(r"\\begin\{(equation|align|gather|multline|table|figure)\*?\}.*?\\end\{\1\*?\}",
                   lambda m: "\n" * m.group(0).count("\n"), t, flags=re.S)
        t = re.sub(r"\$[^$]*\$", " ", t)
        t = re.sub(r"\\(cite[pt]?|citep|citet|ref|eqref|label|cref|Cref|url|href|includegraphics)\s*(\[[^\]]*\])?\{[^}]*\}", " ", t)
        t = re.sub(r"\\[a-zA-Z]+\*?", " ", t)
        t = t.replace("{", " ").replace("}", " ")
    t = re.sub(r"\[\d+(?:\s*[-–,]\s*\d+)*\]", " ", t)                     # [12], [3-5]
    t = re.sub(r"\([A-Z][A-Za-z-]+(?: et al\.)?,? \d{4}[a-z]?(?:; [^)]{0,80})?\)", " ", t)  # (Smith et al., 2020)
    return t


def tokens_with_lines(text: str, skip_quotes: bool):
    """Return [(word, line_no)] for the text, optionally dropping quoted passages."""
    out = []
    in_q = False
    for no, line in enumerate(text.splitlines(), 1):
        if skip_quotes:
            parts = re.split(r'("|``|\'\')', line)
            keep = []
            for p in parts:
                if p in ('"', "``", "''"):
                    in_q = not in_q
                    continue
                if not in_q:
                    keep.append(p)
            line = " ".join(keep)
        for w in WORD.findall(line.lower()):
            out.append((w, no))
        if skip_quotes and in_q and len(line) == 0:
            in_q = False  # a paragraph break ends an unclosed quote
    return out


def read_source(p: Path, use_pdf: bool) -> str:
    if p.suffix.lower() == ".pdf":
        if not use_pdf:
            return ""
        try:
            import pymupdf  # type: ignore
        except ImportError:
            try:
                import fitz as pymupdf  # type: ignore
            except ImportError:
                print(f"  (skipping {p.name}: install PyMuPDF to read PDFs)", file=sys.stderr)
                return ""
        doc = pymupdf.open(str(p))
        return "\n".join(pg.get_text() for pg in doc)
    return p.read_text(encoding="utf-8", errors="replace")


def collect_sources(items, use_pdf):
    files = []
    for it in items:
        p = Path(it)
        if p.is_dir():
            for q in sorted(p.rglob("*")):
                if q.suffix.lower() in (".md", ".txt") or (use_pdf and q.suffix.lower() == ".pdf"):
                    files.append(q)
        elif p.exists():
            files.append(p)
        else:
            print(f"  (not found: {it})", file=sys.stderr)
    # prefer .md over a .pdf of the same name
    stems = {f.stem for f in files if f.suffix.lower() == ".md"}
    return [f for f in files if not (f.suffix.lower() == ".pdf" and f.stem in stems)]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("draft", nargs="+", help="draft files (.tex, .md, .txt)")
    ap.add_argument("--sources", nargs="+", required=True, help="source files or folders")
    ap.add_argument("--min-words", type=int, default=8, help="shortest run reported (default 8)")
    ap.add_argument("--pdf", action="store_true", help="also read PDFs (needs PyMuPDF)")
    ap.add_argument("--include-quotes", action="store_true", help="also check text inside quotation marks")
    ap.add_argument("--report", help="write the findings to this Markdown file as well")
    ap.add_argument("--skip-references", action="store_true",
                    help="stop reading each draft at its reference list (References, Bibliography, Sources heading or \\bibliography)")
    a = ap.parse_args()
    n = max(4, a.min_words)

    srcs = collect_sources(a.sources, a.pdf)
    index = defaultdict(list)  # n-gram -> [(src_id, line)]
    src_names = []
    src_tokens = []
    for sid, f in enumerate(srcs):
        toks = tokens_with_lines(clean_text(read_source(f, a.pdf), f.suffix == ".tex"), skip_quotes=False)
        src_names.append(str(f))
        src_tokens.append(toks)
        words = [w for w, _ in toks]
        for i in range(len(words) - n + 1):
            index[" ".join(words[i:i + n])].append((sid, toks[i][1]))
    print(f"Sources: {len(srcs)} files indexed ({sum(len(t) for t in src_tokens):,} words); run length >= {n} words")

    lines_out = []
    total_flag = 0
    for dpath in a.draft:
        raw = Path(dpath).read_text(encoding="utf-8", errors="replace")
        if a.skip_references:
            m = re.search(r"^\s*(?:#+\s*|\\section\*?\{)?(?:References|Bibliography|Sources|Literature cited)\}?\s*$|\\bibliography\{|\\begin\{thebibliography\}",
                          raw, re.M | re.I)
            if m:
                raw = raw[:m.start()]
        toks = tokens_with_lines(clean_text(raw, dpath.endswith(".tex")), skip_quotes=not a.include_quotes)
        words = [w for w, _ in toks]
        hit = [None] * len(words)  # per word: set of src ids
        first_src_line = {}
        for i in range(len(words) - n + 1):
            g = " ".join(words[i:i + n])
            if g in index:
                ids = {s for s, _ in index[g]}
                for j in range(i, i + n):
                    hit[j] = (hit[j] or set()) | ids
                for s, ln in index[g]:
                    first_src_line.setdefault((i, s), ln)
        # merge consecutive hit words into passages
        passages = []
        i = 0
        while i < len(words):
            if hit[i]:
                j = i
                ids = set(hit[i])
                while j + 1 < len(words) and hit[j + 1]:
                    j += 1
                    ids |= hit[j]
                passages.append((i, j, ids))
                i = j + 1
            else:
                i += 1
        covered = defaultdict(int)
        for i, j, ids in passages:
            for s in ids:
                covered[s] += j - i + 1
        head = f"\n== {dpath}: {len(words):,} words checked; {len(passages)} overlapping passage(s)"
        print(head)
        lines_out.append(head)
        for i, j, ids in passages:
            s = min(ids, key=lambda x: first_src_line.get((i, x), 10 ** 9))
            sl = first_src_line.get((i, s))
            if sl is None:
                sl = next((v for (k, src), v in first_src_line.items() if src == s and i <= k <= j), "?")
            more = f" (+{len(ids) - 1} other source(s))" if len(ids) > 1 else ""
            text = " ".join(words[i:j + 1])
            line = (f"  draft line {toks[i][1]:>5}  {j - i + 1:>3} words  ~ {Path(src_names[s]).name}:{sl}{more}\n"
                    f"      \"{text[:220]}{'…' if len(text) > 220 else ''}\"")
            print(line)
            lines_out.append(line)
        if covered:
            print("  share of draft words matched, by source:")
            lines_out.append("  share of draft words matched, by source:")
            for s, c in sorted(covered.items(), key=lambda x: -x[1])[:10]:
                ln = f"    {100 * c / max(1, len(words)):5.1f} %  {Path(src_names[s]).name}"
                print(ln)
                lines_out.append(ln)
        total_flag += len(passages)

    tail = ("\nResolve each passage: quote it with the page, rewrite it from notes (own structure and "
            "wording), or, for your own earlier methods text, cite that publication. Shared technical terms "
            "are fine. See references/plagiarism-and-paraphrasing.md §5, §9, §11.")
    print(tail)
    if a.report:
        Path(a.report).write_text("# Overlap report\n" + "\n".join(lines_out) + "\n" + tail + "\n", encoding="utf-8")
        print(f"Report written to {a.report}")
    return 1 if total_flag else 0


if __name__ == "__main__":
    sys.exit(main())
