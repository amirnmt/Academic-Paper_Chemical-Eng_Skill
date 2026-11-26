#!/usr/bin/env python3
"""Measure how densely an Introduction is cited, and compare it with a journal benchmark.

Two modes:

  audit FILE       Analyse the Introduction (and abstract) of a draft (.tex, .md or .txt).
                   Prints the citation metrics, compares them with a benchmark file if given,
                   and lists the sentences in the background, literature and gap parts that
                   carry no citation, so that each one can be supported or rewritten.
                   With --section methods (or any heading text), analyses that section instead
                   and lists uncited sentences that name an external element (correlation,
                   model of others, dataset, named method, solver) or give a value without origin.

  benchmark DIR    Build a benchmark from sample papers of a journal that were converted to
                   Markdown (for example with convert_to_markdown.py or journal_profile.py init).
                   Writes medians and quartiles to a JSON file for use with `audit --benchmarks`.

Citations recognised: LaTeX \\cite-family commands (each key counts once); numbered [12], [3-5],
[1, 4]; superscript markers [^12]; author-year groups "(Smith et al., 2020; Lee, 2019a)" and
narrative "Smith et al. (2020)". Sentence roles (opening, literature, gap, objectives, roadmap)
are assigned by simple rules and are approximate; read the listed sentences rather than trusting
the numbers alone.

Examples
  python citation_density.py audit paper/main.tex --benchmarks ../resources/journals/<slug>/citation_benchmarks.json
  python citation_density.py audit draft_intro.md --list 40
  python citation_density.py audit paper/main.tex --section methods --benchmarks …/citation_benchmarks.json
  python citation_density.py benchmark ../resources/journals/<slug>/papers --out ../resources/journals/<slug>/citation_benchmarks.json
"""
import argparse
import json
import re
import statistics as st
import sys
from pathlib import Path

# --------------------------------------------------------------------------- text and sentences
ABBR = [("et al.", "et al"), ("e.g.", "eg"), ("i.e.", "ie"), ("Fig.", "Fig"), ("Figs.", "Figs"), ("Eq.", "Eq"),
        ("Eqs.", "Eqs"), ("vs.", "vs"), ("approx.", "approx"), ("Ref.", "Ref"), ("Refs.", "Refs"), ("No.", "No"),
        ("Sect.", "Sect"), ("cf.", "cf"), ("etc.)", "etc)"), ("U.S.", "US"), ("ca.", "ca")]
YEAR = r"(?:19|20)\d\d[a-z]?"
NAME = r"(?:[A-Z][A-Za-zÀ-ÿ'’\-]+|van|de|der|von|da|di|del|la|le)"
NARR_BEFORE = re.compile(rf"((?:{NAME}\s+){{0,3}}{NAME}(?:\s+et\s+al)?(?:\s*(?:,|and|&)\s*{NAME}(?:\s+{NAME})?)*)\s*$")
CITE_CMD = re.compile(r"\\(?:[a-zA-Z]*cite[a-zA-Z]*\*?)(?:\s*\[[^\]]*\]){0,2}\s*\{([^}]*)\}")


def protect(t):
    for a, b in ABBR:
        t = t.replace(a, b)
    t = re.sub(r"(\d)\.(\d)", r"\1<d>\2", t)
    t = re.sub(r"\b([A-Z])\.\s(?=[A-Z][a-z])", r"\1<i> ", t)
    return t


def sentences(par):
    t = protect(par)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z(\[\\])", t)
    return [s.replace("<d>", ".").replace("<i>", ".").strip() for s in parts if len(s.split()) >= 4]


def refs_in(s):
    keys = []
    for m in CITE_CMD.finditer(s):
        keys += [k.strip() for k in m.group(1).split(",") if k.strip()]
    s = CITE_CMD.sub(" ", s)
    s = re.sub(r"(?<=[, (])((?:19|20)) ?(\d) ?(\d)(?=\s*[a-z]?\s*[);,])", lambda m: m.group(1) + m.group(2) + m.group(3), s)
    for m in re.finditer(r"\[\^?([\d,\s–\-]+)\]", s):
        for part in m.group(1).split(","):
            part = part.strip()
            r = re.match(r"(\d+)\s*[–\-]\s*(\d+)", part)
            if r:
                a, b = int(r.group(1)), int(r.group(2))
                if 0 < b - a < 30:
                    keys += [f"#{i}" for i in range(a, b + 1)]
            elif part.isdigit():
                keys.append(f"#{part}")
    for m in re.finditer(r"\(([^()]*)\)", s):
        inner = m.group(1)
        if not re.search(YEAR, inner) or re.search(r"\b(?:19|20)\d\d\s*[–\-]\s*(?:19|20)?\d\d\b", inner):
            continue
        parts = [p.strip() for p in inner.split(";")]
        for p in parts:
            p = re.sub(r"^(e\.?g\.?|i\.?e\.?|see|cf\.?|for example|for instance|reviewed in|as reviewed by)[,:]?\s*", "", p, flags=re.I)
            years = re.findall(r"\b((?:19|20)\d\d)([a-z](?:\s*,\s*[a-z]\b)*)?", p)
            author = re.match(rf"\s*({NAME}(?:\s+{NAME})*)", p)
            if author and years:
                sur = author.group(1).split()[0].lower()
                for y, suf in years:
                    for x in (re.findall(r"[a-z]", suf or "") or [""]):
                        keys.append(f"{sur}{y}{x}")
            elif years and not author and len(parts) == 1:
                before = NARR_BEFORE.search(s[:m.start()])
                if before:
                    sur = before.group(1).split()[0].lower()
                    for y, suf in years:
                        for x in (re.findall(r"[a-z]", suf or "") or [""]):
                            keys.append(f"{sur}{y}{x}")
    return keys


def max_group(s):
    """Largest number of sources in one citation group (one bracket or one \\cite command)."""
    sizes = [len([k for k in m.group(1).split(",") if k.strip()]) for m in CITE_CMD.finditer(s)]
    s = CITE_CMD.sub(" ", s)
    for m in re.finditer(r"\[\^?([\d,\s–\-]+)\]", s):
        n = 0
        for part in m.group(1).split(","):
            r = re.match(r"\s*(\d+)\s*[–\-]\s*(\d+)", part)
            n += (int(r.group(2)) - int(r.group(1)) + 1) if r and 0 < int(r.group(2)) - int(r.group(1)) < 30 else (1 if part.strip().isdigit() else 0)
        sizes.append(n)
    for m in re.finditer(r"\(([^()]*)\)", s):
        if re.search(YEAR, m.group(1)):
            sizes.append(len(re.findall(r"\b(?:19|20)\d\d[a-z]?", m.group(1))))
    return max(sizes or [0])


def narrative_count(s):
    n = len(re.findall(r"\\(?:citet|textcite|citeauthor)\b", s))
    return n + len(re.findall(rf"{NAME}(?:\s+et\s+al\.?)?(?:\s+(?:and|&)\s+{NAME})?\s*\(\s*{YEAR}", s))


# --------------------------------------------------------------------------- roles
AIM = re.compile(r"\b(we (propose|present|develop|introduce|investigate|address|apply|aim|focus|formulate|show|study)|in this (work|paper|article|study)|"
                 r"this (paper|work|article|study|contribution) (propos|present|develop|introduc|investigat|address|focus|aim|make|is)|"
                 r"in the present (work|study)|the present (work|study|paper)|main contributions?|"
                 r"the (objective|aim|goal|purpose) of (this|the present|the study|the work|the paper)|novel contribution|our (framework|approach|method|contribution)|"
                 r"(this|the present|the current) (paper|work|study|article),? (therefore |thus |hence |here |accordingly )?[a-z]+s\b|we (therefore|thus|here|accordingly) [a-z]+)", re.I)
GAP = re.compile(r"\b(however|nevertheless|despite|although|few (studies|works|papers)|little attention|lack|lacking|remain(s|ed)? (unclear|unaddressed|open|challenging|limited)|"
                 r"to date|no (existing|study|studies|approach|work)|has not been|have not been|not yet|gap|limitation|limited|drawback|shortcoming|challenge|rarely|insufficient|neglect)", re.I)
STRONG_GAP = re.compile(r"\b(to date|few (studies|works|papers|attempts)|little attention|received (relatively )?little|no (existing|study|studies|approach|work|single)|"
                        r"has not (yet )?been|have not (yet )?been|not yet been|research gap|literature gap|remains? (unclear|unaddressed|open|unexplored|limited)|"
                        r"lack of|is lacking|are lacking|rarely|unaddressed|not been (addressed|considered|investigated|studied)|still (lacks|missing|limited))", re.I)
ROAD = re.compile(r"(remainder|rest) of (this|the) (paper|article|work)|organi[sz]ed as follows|structured as follows|^(section \d|in section \d)", re.I)
OWN = re.compile(r"\b(this (paper|work|study|article)|the present (paper|work|study)|in this (paper|work|study)|we|our|us|here(in)?|the proposed|section \d)\b", re.I)


def analyse(paragraphs):
    rows = []
    for pi, p in enumerate(paragraphs):
        for s in sentences(p):
            ks = refs_in(s)
            rows.append({"p": pi, "s": s, "refs": ks, "n": len(ks), "narr": narrative_count(s), "group": max_group(s),
                         "aim": bool(AIM.search(s)), "gap": bool(GAP.search(s)), "road": bool(ROAD.search(s))})
    if not rows:
        return rows
    single_par = len(paragraphs) <= 2
    first_aim = next((i for i, r in enumerate(rows) if r["aim"] and (r["p"] >= 1 or single_par) and i >= 2), len(rows))
    aim_par = rows[first_aim]["p"] if first_aim < len(rows) else None
    n_open = max(2, round(0.15 * len(rows)))
    for i, r in enumerate(rows):
        if i >= first_aim:
            r["role"] = "roadmap" if r["road"] else "objectives"
        elif STRONG_GAP.search(r["s"]) and i >= 2:
            r["role"] = "gap"
        elif r["gap"] and aim_par is not None and r["p"] >= aim_par - 1 and r["p"] >= 2 and not single_par:
            r["role"] = "gap"
        elif (r["p"] < 2 and not single_par) or (single_par and i < n_open):
            r["role"] = "opening"
        else:
            r["role"] = "literature"
    by_p = {}
    for r in rows:
        by_p.setdefault(r["p"], []).append(r)
    for p, rs in by_p.items():
        if aim_par is not None and p > aim_par and not any(r["aim"] or r["road"] for r in rs):
            if sum(1 for r in rs if r["n"]) / len(rs) >= 0.4:
                for r in rs:
                    r["role"] = "literature"
    return rows


def summary(rows, nparas):
    n = len(rows)
    cited = [r for r in rows if r["n"]]
    tot = sum(r["n"] for r in rows)
    words = sum(len(r["s"].split()) for r in rows)
    return {"sentences": n, "paragraphs": nparas, "words": words, "cit_instances": tot,
            "unique_refs": len({k for r in rows for k in r["refs"]}),
            "share_cited": round(len(cited) / n, 3) if n else 0.0,
            "cit_per_sentence": round(tot / n, 2) if n else 0.0,
            "cit_per_cited_sentence": round(tot / len(cited), 2) if cited else 0.0,
            "multi_ref_share": round(sum(1 for r in cited if r["n"] >= 2) / len(cited), 3) if cited else 0.0,
            "max_per_sentence": max([r["n"] for r in rows] or [0]),
            "cit_per_paragraph": round(tot / nparas, 2) if nparas else 0.0,
            "cit_per_100_words": round(100 * tot / words, 2) if words else 0.0,
            "narrative_share": round(sum(min(r["narr"], r["n"]) for r in rows) / tot, 3) if tot else 0.0}


ROLES = ("opening", "literature", "gap", "objectives", "roadmap")


def role_summaries(rows):
    out = {}
    for role in ROLES:
        rs = [r for r in rows if r["role"] == role]
        if rs:
            out[role] = summary(rs, len({r["p"] for r in rs}))
    return out


# --------------------------------------------------------------------------- reading drafts
def strip_tex(t):
    t = re.sub(r"(?<!\\)%.*", "", t)
    t = re.sub(r"\\begin\{(equation|align|figure|table|eqnarray)\*?\}.*?\\end\{\1\*?\}", " ", t, flags=re.S)
    t = re.sub(r"\$[^$]*\$", "x", t)
    t = re.sub(r"\\(ref|eqref|label|autoref|cref)\{[^}]*\}", "1", t)
    t = re.sub(r"\\(textbf|textit|emph|mathrm|text)\{([^}]*)\}", r"\2", t)
    return t


METHOD_RX = r"method|model|formulation|framework|problem statement|materials|approach|theory|data|process description|system description"
RESULT_RX = r"result|discussion|case stud|experiment|conclusion|application|validation of"


def tex_parts(text, section=None):
    text = strip_tex(text)
    ab = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", text, re.S)
    if section:
        rx = METHOD_RX if section.lower() in ("methods", "methodology") else re.escape(section)
        secs = list(re.finditer(r"\\section\*?\{([^}]*)\}", text))
        start = next((i for i, m in enumerate(secs) if re.search(rx, m.group(1), re.I) and not re.search("introduction", m.group(1), re.I)), None)
        if start is None:
            return (ab.group(1) if ab else ""), []
        end = len(text)
        for m in secs[start + 1:]:
            if section.lower() not in ("methods", "methodology") or re.search(RESULT_RX, m.group(1), re.I):
                end = m.start(); break
        body = text[secs[start].end():end]
        body = re.sub(r"\\(sub)+section\*?\{[^}]*\}", "\n\n", body)
        paras = [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", body)]
        return (ab.group(1) if ab else ""), [p for p in paras if len(p.split()) >= 5]
    m = re.search(r"\\section\*?\{[^}]*Introduction[^}]*\}(.*?)(?=\\section\*?\{|\\end\{document\}|$)", text, re.S | re.I)
    body = m.group(1) if m else text
    body = re.sub(r"\\(sub)+section\*?\{[^}]*\}", "\n\n", body)
    paras = [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", body)]
    return (ab.group(1) if ab else ""), [p for p in paras if len(p.split()) >= 5]


HEAD = re.compile(r"^\s*(#{1,6}\s*)?(\d+(\.\d+)*\.?\s+)?([A-Z][A-Za-z ,&\-]{2,80})\s*$")


def md_parts(text, keep_related=True):
    lines = text.splitlines()
    abstract, intro, mode = [], [], None
    for ln in lines:
        h = HEAD.match(ln)
        title = h.group(4).strip().lower() if h else ""
        if h and len(ln.split()) <= 10:
            if "abstract" in title and mode is None:
                mode = "abstract"; continue
            if "introduction" in title:
                mode = "intro"; continue
            if mode == "intro" and not (h.group(1) or h.group(2)) and len(ln.split()) <= 6 and not ln.rstrip().endswith(".") \
                    and re.match(r"(problem (statement|formulation)|methods?|methodology|mathematical model|model\b|materials|case stud|"
                                 r"proposed|framework|data\b|process description|system description|preliminar|formulation)", title):
                break
            if mode == "intro" and (h.group(1) or h.group(2)):
                if keep_related and re.search(r"related work|literature|background|state of the art", title):
                    continue
                if h.group(2) and not re.match(r"1(\.|\s)", h.group(2).strip()):
                    break
                if h.group(1) and not h.group(2):
                    break
            if mode == "abstract" and (h.group(1) or "keyword" in title or "highlight" in title):
                mode = "after-abstract"
                if "introduction" not in title:
                    continue
        if mode == "abstract":
            abstract.append(ln)
        elif mode == "intro":
            intro.append(ln)
    if not intro:
        intro = lines
    blocks = re.split(r"\n\s*\n", "\n".join(intro))
    if len(blocks) <= 2:
        # converted PDF text: no blank lines between paragraphs; join lines and treat as one block
        joined = []
        for ln in intro:
            ln = ln.rstrip()
            if joined and joined[-1] and joined[-1][-1:].isalpha() and ln[:1].islower() and not joined[-1].endswith(" "):
                joined[-1] += ln.strip()
            else:
                joined.append(ln.strip())
        blocks = [" ".join(joined)]
    paras = [re.sub(r"\s+", " ", b).strip() for b in blocks]
    return " ".join(abstract), [p for p in paras if len(p.split()) >= 5]


def md_section(text, section):
    """Paragraphs of a Markdown section: Methods (from the first method-like heading after the
    Introduction to the first results-like heading) or the section whose heading contains `section`."""
    lines = text.splitlines(); out = []; mode = None; seen_intro = False
    methods = section.lower() in ("methods", "methodology")
    for ln in lines:
        h = HEAD.match(ln)
        if h and (h.group(1) or h.group(2)) and len(ln.split()) <= 12 and not ln.rstrip().endswith("."):
            title = h.group(4).strip().lower()
            top = bool((h.group(1) and len(h.group(1).strip()) <= 2) or (h.group(2) and "." not in h.group(2).strip().rstrip(".")))
            if "introduction" in title:
                seen_intro = True; mode = None if mode != "in" else "done"; continue
            if mode is None and top and (re.search(METHOD_RX, title) if methods else section.lower() in title) and (seen_intro or not methods):
                mode = "in"; continue
            if mode == "in" and top and (re.search(RESULT_RX, title) if methods else True):
                break
        if mode == "in":
            out.append(ln)
    blocks = re.split(r"\n\s*\n", "\n".join(out))
    return [re.sub(r"\s+", " ", b).strip() for b in blocks if len(b.split()) >= 5]


def read_parts(path, section=None):
    text = Path(path).read_text(encoding="utf-8", errors="replace")
    if path.suffix == ".tex":
        return tex_parts(text, section)
    if section:
        return md_parts(text)[0], md_section(text, section)
    return md_parts(text)


# --------------------------------------------------------------------------- benchmarks
def quartiles(xs):
    xs = sorted(xs)
    if len(xs) < 4:
        return {"median": st.median(xs), "q1": xs[0], "q3": xs[-1], "n": len(xs)}
    q = st.quantiles(xs, n=4, method="inclusive")
    return {"median": round(q[1], 3), "q1": round(q[0], 3), "q3": round(q[2], 3), "n": len(xs)}


METRICS = ["sentences", "paragraphs", "words", "cit_instances", "unique_refs", "share_cited", "cit_per_sentence",
           "cit_per_cited_sentence", "multi_ref_share", "max_per_sentence", "cit_per_100_words", "narrative_share"]


def build_benchmark(folder, out):
    papers = sorted(Path(folder).glob("*.md"))
    per, roles, meth = {}, {r: [] for r in ROLES}, {}
    for p in papers:
        text = p.read_text(encoding="utf-8", errors="replace")
        mp = md_section(text, "methods")
        mrows = [{"s": s, "refs": refs_in(s), "n": len(refs_in(s)), "narr": 0} for q in mp for s in sentences(q)]
        if len(mrows) >= 20:
            meth[p.stem] = summary(mrows, len(mp))
        ab, paras = md_parts(text)
        rows = analyse(paras)
        if len(rows) < 10:
            print(f"skip {p.name}: Introduction not found or too short", file=sys.stderr)
            continue
        per[p.stem] = summary(rows, len(paras))
        per[p.stem]["abstract_words"] = len(ab.split())
        for role, s in role_summaries(rows).items():
            roles[role].append(s)
    if not per:
        sys.exit("no usable papers")
    bench = {"source": str(folder), "papers": len(per),
             "note": "Built from converted Markdown; paragraph counts are unreliable for PDF conversions.",
             "overall": {m: quartiles([v[m] for v in per.values()]) for m in METRICS},
             "by_role": {r: {m: quartiles([s[m] for s in L]) for m in ("share_cited", "cit_per_sentence", "multi_ref_share")}
                         for r, L in roles.items() if L},
             "per_paper": per,
             "methods": {"papers": len(meth), "overall": {m: quartiles([v[m] for v in meth.values()]) for m in
                         ("sentences", "words", "cit_instances", "unique_refs", "share_cited", "cit_per_sentence")} if meth else {}}}
    Path(out).write_text(json.dumps(bench, indent=1), encoding="utf-8")
    print(f"wrote {out} ({len(per)} papers)")
    for m in ("share_cited", "cit_per_sentence", "cit_per_cited_sentence", "multi_ref_share", "cit_per_100_words"):
        q = bench["overall"][m]
        print(f"  {m:24s} median {q['median']:.2f} (IQR {q['q1']:.2f}-{q['q3']:.2f})")


# --------------------------------------------------------------------------- audit
EXT = re.compile(r"\b(correlation|equation of state|model of|approach of|method of|proposed by|developed by|according to|taken from|obtained from|"
                 r"reported (by|in)|literature|data ?set|database|kinetic (model|scheme|parameters|expression)|rate expression|Arrhenius|Peng|Soave|"
                 r"Ergun|Langmuir|Hinshelwood|Hougen|Wilke|Fuller|Chilton|Colburn|Gnielinski|Sobol|SHAP|LSTM|transformer|XGBoost|random forest|"
                 r"Adam\b|Runge|BDF|DASSL|IPOPT|CPLEX|Gurobi|BARON|is adopted|is adapted|adapted from|follows? (the )?(work|model|approach)|"
                 r"well[- ]known|widely used|commonly used|standard (method|model|approach))", re.I)
VALUE = re.compile(r"\b(set to|taken as|equal to|fixed at|value of|chosen as|assumed to be)\s*[-−]?\d", re.I)
ORIGIN = re.compile(r"\b(because|since|estimated|measured|calibrated|fitted|Table|Appendix|chosen|selected|Section|so that|to ensure)\b", re.I)


def audit_section(path, section, bench, list_n):
    ab, paras = read_parts(Path(path), section)
    rows = []
    for pi, p in enumerate(paras):
        for s in sentences(p):
            ks = refs_in(s)
            rows.append({"p": pi, "s": s, "refs": ks, "n": len(ks), "narr": narrative_count(s), "group": max_group(s)})
    if not rows:
        sys.exit(f"no '{section}' section found")
    s = summary(rows, len(paras))
    b = (bench or {}).get("methods", {}).get("overall") if section.lower() in ("methods", "methodology") else None
    print(f"Section '{section}': {s['sentences']} sentences, {s['paragraphs']} paragraphs, {s['words']} words\n")
    print(f"{'metric':26s} {'draft':>8s}   benchmark median (IQR)")
    for m in ("sentences", "words", "cit_instances", "unique_refs", "share_cited", "cit_per_sentence"):
        line = f"{m:26s} {s[m]:8.2f}" if isinstance(s[m], float) else f"{m:26s} {s[m]:8d}"
        if b and m in b:
            q = b[m]; line += f"   {q['median']:.2f} ({q['q1']:.2f}-{q['q3']:.2f})"
        print(line)
    ext = [r for r in rows if r["n"] == 0 and EXT.search(r["s"])]
    val = [r for r in rows if r["n"] == 0 and VALUE.search(r["s"]) and not ORIGIN.search(r["s"])]
    print(f"\nUncited sentences that name an external element ({len(ext)}): cite the source, or say it is your own:")
    for r in ext[:list_n]:
        print(f"  [P{r['p'] + 1}] {r['s'][:220]}")
    print(f"\nValues without a stated origin ({len(val)}): give the reference, measurement, estimation or reason:")
    for r in val[:list_n]:
        print(f"  [P{r['p'] + 1}] {r['s'][:220]}")


def audit(path, bench_path, list_n, section=None):
    if section and section.lower() != "introduction":
        bench = json.loads(Path(bench_path).read_text(encoding="utf-8")) if bench_path else None
        return audit_section(path, section, bench, list_n)
    ab, paras = read_parts(Path(path))
    rows = analyse(paras)
    if not rows:
        sys.exit("no Introduction text found")
    s = summary(rows, len(paras))
    bench = json.loads(Path(bench_path).read_text(encoding="utf-8")) if bench_path else None
    print(f"Introduction: {s['sentences']} sentences, {s['paragraphs']} paragraphs, {s['words']} words")
    print(f"Abstract: {len(ab.split())} words, {sum(len(refs_in(x)) for x in sentences(ab))} citations\n")
    print(f"{'metric':26s} {'draft':>8s}   benchmark median (IQR)")
    for m in METRICS:
        line = f"{m:26s} {s[m]:8.2f}" if isinstance(s[m], float) else f"{m:26s} {s[m]:8d}"
        if bench and m in bench.get("overall", {}):
            q = bench["overall"][m]
            flag = "  below range" if s[m] < q["q1"] else ("  above range" if s[m] > q["q3"] else "")
            line += f"   {q['median']:.2f} ({q['q1']:.2f}-{q['q3']:.2f}){flag}"
        print(line)
    print("\nBy part of the Introduction (share of sentences cited / citations per sentence):")
    for role, r in role_summaries(rows).items():
        line = f"  {role:11s} {r['sentences']:3d} sentences  {r['share_cited']:.2f} / {r['cit_per_sentence']:.2f}"
        if bench and role in bench.get("by_role", {}):
            b = bench["by_role"][role]
            line += f"   benchmark {b['share_cited']['median']:.2f} / {b['cit_per_sentence']['median']:.2f}"
        print(line)
    flagged = [r for r in rows if r["role"] in ("opening", "literature", "gap") and r["n"] == 0 and not OWN.search(r["s"])]
    heavy = [r for r in rows if r["group"] >= 6]
    print(f"\nUncited sentences in the background, literature and gap parts: {len(flagged)}")
    print("Each needs a citation, unless it only announces a group whose sources follow, or draws an inference from sources cited in the same paragraph:")
    for r in flagged[:list_n]:
        print(f"  [P{r['p'] + 1} {r['role']}] {r['s'][:220]}")
    if len(flagged) > list_n:
        print(f"  ... {len(flagged) - list_n} more (use --list)")
    if heavy:
        print(f"\nCitation groups of 6 or more sources ({len(heavy)}): check that each source supports the claim, or split it:")
        for r in heavy:
            print(f"  [P{r['p'] + 1}] ({r['group']}) {r['s'][:200]}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("audit", help="analyse a draft")
    a.add_argument("file")
    a.add_argument("--benchmarks", help="citation_benchmarks.json of the target journal")
    a.add_argument("--list", type=int, default=25, help="how many uncited sentences to print")
    a.add_argument("--section", help="analyse this section instead of the Introduction, e.g. methods")
    b = sub.add_parser("benchmark", help="build a benchmark from converted sample papers")
    b.add_argument("folder")
    b.add_argument("--out", default="citation_benchmarks.json")
    args = ap.parse_args()
    if args.cmd == "audit":
        audit(args.file, args.benchmarks, args.list, args.section)
    else:
        build_benchmark(args.folder, args.out)


if __name__ == "__main__":
    main()
