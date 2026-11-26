#!/usr/bin/env python3
"""Build a phrase list per article section from converted research papers.

Usage:
  python scripts/build_section_phrases.py DIR_OR_FILES... [--out section_phrases.md]
         [--min-docs N] [--top N]

Each paper (Markdown or text, for example converted with MarkItDown) is split
into sections by its headings: Abstract, Introduction, Literature review,
Methods, Results, Results and Discussion, Discussion, Conclusion. References,
acknowledgements, appendices and nomenclature are skipped.

For every section the report lists
  * sentence openers: the first three and four words of sentences,
  * phrases typical of the section (used there clearly more often than in
    the other sections),
  * the most common recurring 3-6-word phrases, and
  * recurring terms (mostly content words),
counted by how many different papers use them. Only items used by at least
--min-docs papers are listed (default: 8 % of the papers that have the
section, and at least 2), so the result is a list of shared conventions, not
any single author's sentences. Numbers are shown as #.

Standard library only.
"""
import argparse
import os
import math
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

EXTS = {".md", ".txt", ".markdown"}

SECTION_ORDER = ["abstract", "introduction", "literature", "methods", "results",
                 "results_discussion", "discussion", "conclusion"]
SECTION_LABEL = {
    "abstract": "Abstract",
    "introduction": "Introduction",
    "literature": "Literature review / Background",
    "methods": "Methods",
    "results": "Results",
    "results_discussion": "Results and Discussion",
    "discussion": "Discussion",
    "conclusion": "Conclusion",
}
SECTION_PATTERNS = [
    ("abstract", r"abstract|summary of the article"),
    ("introduction", r"introduction( and (background|motivation|literature review))?"),
    ("literature", r"literature review|literature survey|review of (the )?literature|background|"
                   r"theoretical background|related work|related studies|previous work|state of the art|"
                   r"state-of-the-art"),
    ("results_discussion", r"results? (and|&) discussions?"),
    ("methods", r"methods?|methodology|materials and methods?|methods? and materials|experimental|"
                r"experimental (section|setup|set-up|details|procedures?|methods?|work)|experiments?|"
                r"materials|model(s)?|model (development|description|formulation|set-up|setup)|"
                r"mathematical model(s|l?ing)?|model(l)?ing|numerical (methods?|model(s)?|procedure)|"
                r"simulation( (setup|set-up|methods?|details))?|theory|theoretical (model|framework)|"
                r"computational (methods?|details)|methods? (and|&) data( analysis)?|data and methods?|"
                r"research (design|methods?|methodology)|methodology and data|process description|"
                r"(?:[a-z\-]+ ){1,2}(?:model(?:s|ling|ing)?|methodology|methods?|approach|framework|"
                r"formulation|description)|problem (statement|formulation|description)"),
    ("results", r"results?|findings|results? and analysis|results? analysis|"
                r"(simulation|experimental|numerical|model(ling|ing)?|optimi[sz]ation|validation|"
                r"sensitivity analysis|training) results?|"
                r"(model )?validation|case stud(y|ies)|performance evaluation|evaluation"),
    ("discussion", r"discussions?|general discussion|(further|overall) discussion"),
    ("conclusion", r"conclusions?|concluding remarks|summary|summary and conclusions?|"
                   r"conclusions? and (outlook|future work|perspectives?|recommendations?)"),
    ("skip", r"references|bibliography|literature cited|acknowledge?ments?|appendix( [a-z0-9]+)?|"
             r"appendices|nomenclature|notation|abbreviations|declaration.*|credit author.*|"
             r"author contributions?|data availability.*|funding|supplementary (material|data).*|"
             r"supporting information|associated content|author information|notes|"
             r"(declaration of )?(conflicts?|competing) (of )?interests?( statement)?|ethics statement|"
             r"list of symbols|symbols|greek (letters|symbols)|subscripts?|superscripts?"),
]
SECTION_RX = [(name, re.compile(rf"(?:{pat})", re.I)) for name, pat in SECTION_PATTERNS]
HEAD_RX = re.compile(r"^(?:#{1,6}\s*)?(?:(?:\d{1,2}(?:\.\d{1,2})*|[IVX]{1,5})\.?\s+)?"
                     r"(?P<title>[A-Za-z][A-Za-z &,/\-]{1,70}?)\s*[.:]?\s*$")
NUMBER_RX = re.compile(r"^(?:#{1,6}\s*)?(\d{1,2})((?:\.\d{1,2})+)?\.?\s")
INLINE_ABSTRACT_RX = re.compile(r"^(?:#{1,6}\s*)?abstract\s*[—–:\-.]\s*(?P<rest>.+)$", re.I)

STOP = set("""a about above after again against all also although am an and any are as at be because been
before being below between both but by can could did do does doing down during each either et al few for
from further had has have having here how however i if in into is it its itself least less may might more
most much must no nor not of off on once only or other our ours out over own per same shall should since so
some such than that the their them then there these they this those through thus to too under until up upon
very via was we were what when where whereas whether which while who whom whose why will with within without
would yet one two both well even further hence therefore i.e e.g namely respectively""".split())
BAD_START = {"and", "or", "the", "a", "an", "of", "which", "that", "et", "al"}
BAD_END = {"the", "a", "an", "and", "or", "et"}
JUNK_LINE_RX = re.compile(r"©|doi|https?://|www\.|e-?mail|corresponding author|available online|"
                          r"journal homepage|elsevier|springer|wiley|all rights reserved|"
                          r"creative ?commons|received \d|accepted \d|revised \d|license|contents lists available|"
                          r"sciencedirect|article history|article info|a r t i c l e|keywords?:|"
                          r"published by|copyright|\bvol\.|\bpp\.", re.I)
ABBREV = [("Figs.", "Figs"), ("Fig.", "Fig"), ("Eqs.", "Eqs"), ("Eq.", "Eq"), ("et al.", "et al"),
          ("e.g.", "eg"), ("i.e.", "ie"), ("Refs.", "Refs"), ("Ref.", "Ref"), ("vs.", "vs"),
          ("approx.", "approx"), ("No.", "No"), ("Sect.", "Sect"), ("Tab.", "Tab"), ("ca.", "ca"),
          ("resp.", "resp"), ("cf.", "cf")]
CITE_RXS = [re.compile(r"\[\s*\d+(?:\s*[,–\-]\s*\d+)*\s*\]"),
            re.compile(r"\(\s*[A-Z][^()]{0,90}?\d{4}[a-z]?(?:\s*[;,]\s*[^()]{0,60}?\d{4}[a-z]?)*\s*\)")]
WORD_RX = re.compile(r"[A-Za-z][A-Za-z'\-]*|\d+(?:[.,]\d+)?")


KEYWORD_HEAD = (r"abstract|introduction|literature review|background|related work|state of the art|"
                r"materials and methods|methods and materials|methodology|methods?|experimental|"
                r"model(?:l)?ing|model description|model development|mathematical model|"
                r"results? and discussions?|results? & discussions?|results?|discussions?|"
                r"conclusions?|concluding remarks|references|acknowledge?ments?|nomenclature")
# "1. Introduction <text of the other column>" (two-column conversions)
NUM_HEAD_TEXT_RX = re.compile(r"^(?:#{1,6}\s*)?\d{1,2}\.?\s+(?P<title>" + KEYWORD_HEAD +
                              r")\s+(?P<rest>[a-z(].*)$", re.I)
# "METHODOLOGY Analytical procedures ..." or "II. RESULTS & DISCUSSION" (upper-case headings)
UPPER_HEAD_RX = re.compile(r"^(?:[IVX]{1,5}\.\s*)?(?P<title>[A-Z][A-Z &]{2,40}?[A-Z])"
                           r"(?:\s+(?P<rest>[A-Z][a-z].*))?$")



def read_text(path):
    """Read a text file; on Windows also paths longer than 260 characters."""
    s = str(Path(path).resolve())
    if os.name == "nt" and len(s) >= 240 and not s.startswith("\\\\?\\"):
        s = "\\\\?\\" + s
    with open(s, encoding="utf-8", errors="replace") as fh:
        return fh.read()

def match_title(title):
    title = re.sub(r"\s+", " ", title.strip()).lower()
    title = re.sub(r"\s*&\s*", " & ", title)
    for name, rx in SECTION_RX:
        if rx.fullmatch(title):
            return name
    return None


def classify_heading(line):
    """Return (section name, text on the same line after the heading) or (None, None)."""
    s = line.strip().lstrip("\u25a0\u25a1\u2022\u25aa\u25cf\u25c6* ")  # ACS-style bullets before headings
    if not s:
        return None, None
    m = INLINE_ABSTRACT_RX.match(s)
    if m:
        return "abstract", m.group("rest")
    # 1. the whole line is a heading
    if len(s) <= 80:
        t = s.replace(" ", "") if re.fullmatch(r"(?:[A-Za-z] ){3,}[A-Za-z]", s) else s  # "a b s t r a c t"
        m = HEAD_RX.match(t)
        if m:
            name = match_title(m.group("title"))
            if name:
                return name, ""
    # 2. a heading followed by text from the other column (two-column conversions)
    if len(s) < 200:
        for rx in (NUM_HEAD_TEXT_RX, UPPER_HEAD_RX):
            m = rx.match(s)
            if m:
                name = match_title(m.group("title"))
                if name:
                    return name, m.group("rest") or ""
    return None, None


def split_sections(text, min_words=40, boilerplate=frozenset()):
    lines = text.splitlines()
    # running heads and footers repeat on every page: drop lines seen 3+ times
    norm = [re.sub(r"\d+", "#", l.strip().lower()) for l in lines]
    freq = Counter(n for n in norm if n)
    blocks = []  # [name, lines]; text before the first heading (title, authors) is ignored
    i = 0
    while i < len(lines):
        line, n = lines[i], norm[i]
        i += 1
        name, rest = classify_heading(line)
        num = NUMBER_RX.match(line.strip())
        top = num.group(1) if num else None
        if name and num and num.group(2) and blocks and blocks[-1][2] == top:
            name = None  # a subsection ("4.2 Kinetic model") stays in its section ("4. Results")
        if name:
            # headings broken over two lines: "3. Results" + "and discussion"
            nxt = lines[i].strip() if i < len(lines) else ""
            if not rest and re.match(r"^(and|&)\s+\w", nxt, re.I):
                name2, rest2 = classify_heading(line.strip() + " " + nxt)
                if name2 and name2 != name:
                    name, rest = name2, rest2
                    i += 1
            blocks.append([name, [rest] if rest else [], top])
            continue
        if blocks and n and freq[n] < 3 and n not in boilerplate and not JUNK_LINE_RX.search(line):
            blocks[-1][1].append(line)
    # headings before the Abstract or Introduction belong to the title page
    # (keywords, journal section labels): drop them
    starts = [i for i, b in enumerate(blocks) if b[0] in ("abstract", "introduction")]
    if starts:
        blocks = blocks[starts[0]:]
    # a "heading" followed by almost no text is a list item or a table cell, not a section
    merged = []
    for name, body, _ in blocks:
        words = sum(len(l.split()) for l in body)
        if merged and name != "skip" and words < min_words:
            merged[-1][1].extend(body)
        else:
            merged.append([name, body])
    sections, found = defaultdict(list), []
    for name, body in merged:
        if name == "skip":
            continue
        sections[name].extend(body)
        if name not in found:
            found.append(name)
    # a first section called "Background" with no Introduction is the Introduction
    if "introduction" not in sections and found and found[0] == "literature":
        sections["introduction"] = sections.pop("literature")
        found[0] = "introduction"
    return dict(sections), found


def clean_block(lines):
    text = ""
    for line in lines:
        line = line.strip()
        if not line:
            text += "\n"
            continue
        if text.endswith("-") and line[:1].islower():
            text = text[:-1] + line
        else:
            text += (" " if text and not text.endswith("\n") else "") + line
    text = re.sub(r"\s+", " ", text)
    # running heads such as "Computers and Chemical Engineering 210 (2026) 109716"
    text = re.sub(r"\b[A-Z][A-Za-z&,.\- ]{5,80}? \d{1,4} \((?:19|20)\d\d\) [\d\u2013\-]+", " ", text)
    for a, b in ABBREV:
        text = text.replace(a, b)
    for rx in CITE_RXS:
        text = rx.sub(" ", text)
    return text


def sentences(text):
    for s in re.split(r"(?<=[.!?])\s+(?=[A-Z(])", text):
        toks = [("#" if w[0].isdigit() else w.lower()) for w in WORD_RX.findall(s)]
        if len(toks) >= 5:
            yield toks


def looks_unspaced(text):
    words = WORD_RX.findall(text)
    if len(words) < 50:
        return False
    return sum(len(w) for w in words) / len(words) > 11


def keep_ngram(g):
    if g[0] in BAD_START or g[-1] in BAD_END:
        return False
    # author names left over from citations ("zheng et al")
    if any(g[i] == "et" and g[i + 1] == "al" for i in range(len(g) - 1)) or g[-1] == "et":
        return False
    # single letters are symbols or pieces of formulas (c # h, t # s)
    if any(len(t) == 1 and t not in ("a", "#") for t in g):
        return False
    if all(t in STOP or t == "#" for t in g):
        return False
    if sum(t == "#" for t in g) > 1:
        return False
    return True


def is_formulaic(g):
    return sum(t in STOP for t in g) / len(g) >= 0.3


def count_section(docs):
    open_df, open_tf, gram_df, gram_tf, start_df = Counter(), Counter(), Counter(), Counter(), Counter()
    for text in docs:
        seen_open, seen_gram = set(), set()
        for n_sent, toks in enumerate(sentences(text)):
            if n_sent == 0 and toks[0] != "#":
                start_df[tuple(toks[:3])] += 1
            if toks[0] != "#" and not any(toks[i:i + 2] == ["et", "al"] for i in range(4)):
                for k in (3, 4):
                    o = tuple(toks[:k])
                    open_tf[o] += 1
                    seen_open.add(o)
            for k in range(3, 7):
                for i in range(len(toks) - k + 1):
                    g = tuple(toks[i:i + k])
                    if keep_ngram(g):
                        gram_tf[g] += 1
                        seen_gram.add(g)
        open_df.update(seen_open)
        gram_df.update(seen_gram)
    return open_df, open_tf, gram_df, gram_tf, start_df


def analyse(papers, min_docs_arg, top):
    """papers: list of (name, sections_dict). Returns per-section statistics."""
    counts = {}
    for sec in SECTION_ORDER:
        docs = [s[sec] for _, s in papers if sec in s and s[sec].strip()]
        if docs:
            counts[sec] = (len(docs),) + count_section(docs)
    out = {}
    for sec, (n, open_df, open_tf, gram_df, gram_tf, start_df) in counts.items():
        min_docs = min_docs_arg or max(2, math.ceil(0.08 * n))
        openers = [o for o in open_df if open_df[o] >= min_docs]
        # drop a 3-word opener when its 4-word extension is used by as many papers
        four = [o for o in openers if len(o) == 4]
        openers = [o for o in openers
                   if not (len(o) == 3 and any(f[:3] == o and open_df[f] >= 0.8 * open_df[o] for f in four))]
        grams = {g for g in gram_df if gram_df[g] >= min_docs}
        # keep maximal phrases: drop a sub-phrase whose longer phrase has the same paper count
        subsumed = set()
        for g in grams:
            if len(g) > 3:
                for sub in (g[:-1], g[1:]):
                    if sub in grams and gram_df[sub] <= gram_df[g]:
                        subsumed.add(sub)
        grams -= subsumed
        # how much more often papers use a phrase here than in their other sections
        other_n = sum(c[0] for s, c in counts.items() if s != sec)

        def distinct(g):
            if not other_n:
                return 0.0
            other_df = sum(c[3].get(g, 0) for s, c in counts.items() if s != sec)
            return (gram_df[g] / n) / (other_df / other_n + 0.02)

        def rank(df, tf):
            return lambda x: (-df[x], -tf[x], x)
        openers.sort(key=rank(open_df, open_tf))
        form = sorted((g for g in grams if is_formulaic(g)), key=rank(gram_df, gram_tf))
        typical = sorted((g for g in form if distinct(g) >= 2.0), key=lambda g: (-distinct(g), -gram_df[g], g))
        terms = sorted((g for g in grams if not is_formulaic(g)), key=rank(gram_df, gram_tf))
        fmt = lambda g, df, tf: (" ".join(g), df[g], tf[g])
        starts = sorted((o for o in start_df if start_df[o] >= 2), key=lambda o: (-start_df[o], o))
        out[sec] = {
            "n": n, "min_docs": min_docs,
            "starts": [(" ".join(o), start_df[o], start_df[o]) for o in starts[:top]],
            "openers": [fmt(o, open_df, open_tf) for o in openers[:top]],
            "typical": [fmt(g, gram_df, gram_tf) + (round(distinct(g), 1),) for g in typical[:top]],
            "formulaic": [fmt(g, gram_df, gram_tf) for g in form[:top]],
            "terms": [fmt(g, gram_df, gram_tf) for g in terms[:top]],
        }
    return out


def gather(paths):
    files = []
    for p in paths:
        p = Path(p)
        if p.is_dir():
            files += [f for f in sorted(p.rglob("*")) if f.suffix.lower() in EXTS
                      and f.name.lower() not in ("readme.md", "notice.md")]
        elif p.is_file():
            files.append(p)
    return files


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("inputs", nargs="+", help="folders or files with converted papers")
    ap.add_argument("--out", default="section_phrases.md", help="output Markdown file")
    ap.add_argument("--min-docs", type=int, default=0,
                    help="minimum number of papers using an item (default: 8%% of the papers with the section, at least 2)")
    ap.add_argument("--top", type=int, default=30, help="items per list (default 30)")
    args = ap.parse_args()

    files = gather(args.inputs)
    if not files:
        sys.exit("No .md or .txt files found.")
    # lines repeated across many papers (journal mastheads, licence notes) are boilerplate
    texts = {f: unicodedata.normalize("NFKC", read_text(f)) for f in files}
    line_df = Counter()
    for raw in texts.values():
        line_df.update({re.sub(r"\d+", "#", l.strip().lower()) for l in raw.splitlines() if l.strip()})
    cut = max(3, math.ceil(0.3 * len(files)))
    boilerplate = frozenset(l for l, n in line_df.items() if n >= cut and len(l.split()) <= 12)
    papers, report = [], []
    for f in files:
        raw = texts[f]
        secs, found = split_sections(raw, boilerplate=boilerplate)
        cleaned = {k: clean_block(v) for k, v in secs.items()}
        joined = " ".join(cleaned.values())
        if looks_unspaced(joined or raw):
            report.append((f.name, "skipped: text has no spaces between words (convert again with another tool)"))
            continue
        if not cleaned:
            report.append((f.name, "skipped: no section headings recognized"))
            continue
        papers.append((f.name, cleaned))
        order = []
        for x in found:
            if x in cleaned and SECTION_LABEL[x] not in order:
                order.append(SECTION_LABEL[x])
        report.append((f.name, "sections: " + ", ".join(order)))

    stats = analyse(papers, args.min_docs, args.top)
    L = [f"# Section phrase list from {len(papers)} paper{'s' if len(papers) != 1 else ''}", "",
         "Counts are *papers* (how many different papers use the item) and *uses* (total occurrences). "
         "Numbers appear as #. Use these as conventions of the field: adapt them to your own content, "
         "and look up any phrase in context with `scripts/search_resources.py \"phrase\" --dir <folder>`.", ""]
    if len(papers) < 5:
        L += ["> Fewer than 5 papers were analysed; the lists are not yet representative. "
              "15–30 papers from the target journal give a useful list.", ""]
    for sec in SECTION_ORDER:
        if sec not in stats:
            continue
        s = stats[sec]
        L += [f"## {SECTION_LABEL[sec]}", "",
              f"{s['n']} paper{'s' if s['n'] != 1 else ''} with this section; items used by at least "
              f"{s['min_docs']} papers.", ""]
        tables = (
            ("starts", "How the section begins",
             "First words of the first sentence of the section, shared by at least 2 papers."),
            ("openers", "Sentence openers", "First words of sentences anywhere in this section."),
            ("typical", "Phrases typical of this section",
             "Used here at least twice as often as in the other sections (ratio in the last column)."),
            ("formulaic", "Common phrases", "Most frequent recurring phrases in this section."),
            ("terms", "Recurring terms", "Mostly content words: terminology of the field."),
        )
        for key, title, note in tables:
            L += [f"### {title}", "", note, ""]
            if not s[key]:
                L += ["(none above the threshold)", ""]
                continue
            if key == "starts":
                L += ["| Phrase | Papers |", "|---|---|"]
                L += [f"| {p} | {d} |" for p, d, _ in s[key]]
            elif key == "typical":
                L += ["| Phrase | Papers | Uses | Ratio |", "|---|---|---|---|"]
                L += [f"| {p} | {d} | {t} | {r} |" for p, d, t, r in s[key]]
            else:
                L += ["| Phrase | Papers | Uses |", "|---|---|---|"]
                L += [f"| {p} | {d} | {t} |" for p, d, t in s[key]]
            L.append("")
    L += ["## Papers analysed", ""] + [f"- {name}: {msg}" for name, msg in report] + [""]
    Path(args.out).write_text("\n".join(L), encoding="utf-8")
    print(f"Wrote {args.out}: {len(papers)} papers analysed, {len(files) - len(papers)} skipped.")


if __name__ == "__main__":
    main()
