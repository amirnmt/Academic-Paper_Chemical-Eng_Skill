#!/usr/bin/env python3
"""Check a BibTeX file against OpenAlex and Crossref, and against the LaTeX sources.

For every entry it reports whether the DOI resolves and whether title, first
author and year match the registered record. It also flags retracted papers,
entries without DOI (and suggests one when the title matches), duplicate keys,
DOIs and titles, missing fields, keys cited in the .tex files but absent from
the .bib file, and entries never cited.

Usage:
    python check_citations.py refs.bib
    python check_citations.py refs.bib --tex main.tex sections/*.tex --out citation_report.md
    python check_citations.py refs.bib --offline          # structure checks only
    python check_citations.py refs.bib --mailto you@uni.de  # polite API use (recommended)

Only the Python standard library is needed. Exit code 1 means problems were found.
A match is evidence that the reference exists and is described correctly; it does
not show that the paper supports the sentence citing it. Check that by reading it.
"""
import argparse
import difflib
import glob
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

OPENALEX = "https://api.openalex.org/works/"
CROSSREF = "https://api.crossref.org/works/"


# ----------------------------------------------------------------- BibTeX parsing
def parse_bib(text):
    """Return a list of entries: {'type', 'key', 'fields': {name: value}}."""
    entries, i = [], 0
    while True:
        m = re.compile(r"@(\w+)\s*\{", re.I).search(text, i)
        if not m:
            break
        etype = m.group(1).lower()
        start = m.end()
        depth, j = 1, start
        while j < len(text) and depth:
            depth += {"{": 1, "}": -1}.get(text[j], 0)
            j += 1
        body = text[start:j - 1]
        i = j
        if etype in ("comment", "preamble", "string"):
            continue
        key, _, rest = body.partition(",")
        entries.append({"type": etype, "key": key.strip(), "fields": parse_fields(rest)})
    return entries


def parse_fields(s):
    fields, i, n = {}, 0, len(s)
    while i < n:
        m = re.compile(r"\s*([\w-]+)\s*=\s*").match(s, i)
        if not m:
            i += 1
            continue
        name, i = m.group(1).lower(), m.end()
        if i < n and s[i] == "{":
            depth, j = 1, i + 1
            while j < n and depth:
                depth += {"{": 1, "}": -1}.get(s[j], 0)
                j += 1
            value, i = s[i + 1:j - 1], j
        elif i < n and s[i] == '"':
            j = s.find('"', i + 1)
            j = n if j == -1 else j
            value, i = s[i + 1:j], j + 1
        else:
            j = i
            while j < n and s[j] not in ",\n":
                j += 1
            value, i = s[i:j].strip(), j
        fields[name] = " ".join(value.split())
        while i < n and s[i] in ", \n\t\r":
            i += 1
    return fields


# ------------------------------------------------------------------- normalising
def plain(s):
    """Lower-case ASCII text without LaTeX commands, braces or punctuation."""
    s = re.sub(r"\\[a-zA-Z]+\s*", "", s or "")
    s = re.sub(r"\\.", "", s)
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-z0-9 ]", " ", s.lower())
    return " ".join(s.split())


def first_surname_bib(authors):
    first = (authors or "").split(" and ")[0].strip()
    if not first:
        return ""
    if "," in first:
        last = plain(first.split(",")[0]).split()
        return last[-1] if last else ""
    words = plain(first).split()
    return words[-1] if words else ""


def clean_doi(doi):
    doi = (doi or "").strip()
    doi = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:\s*)", "", doi, flags=re.I)
    return doi.lower()


def similarity(a, b):
    return difflib.SequenceMatcher(None, plain(a), plain(b)).ratio()


# ------------------------------------------------------------------------ lookups
def get_json(url, mailto):
    ua = "academic-paper-skill-citation-check/1.0" + (f" (mailto:{mailto})" if mailto else "")
    req = urllib.request.Request(url, headers={"User-Agent": ua, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def lookup_doi(doi, mailto):
    """Return a normalised record {'title','year','surname','retracted','source'} or None."""
    q = f"?mailto={urllib.parse.quote(mailto)}" if mailto else ""
    data = get_json(OPENALEX + "https://doi.org/" + urllib.parse.quote(doi, safe="/") + q, mailto)
    if data:
        auths = data.get("authorships") or []
        name = (auths[0].get("author") or {}).get("display_name", "") if auths else ""
        return {"title": data.get("title") or "", "year": data.get("publication_year"),
                "surname": plain(name).split(" ")[-1] if name else "",
                "retracted": bool(data.get("is_retracted")), "source": "OpenAlex"}
    data = get_json(CROSSREF + urllib.parse.quote(doi, safe="/"), mailto)
    if data and data.get("message"):
        msg = data["message"]
        title = (msg.get("title") or [""])[0]
        year = None
        for k in ("published-print", "published-online", "issued", "created"):
            parts = (msg.get(k) or {}).get("date-parts") or [[None]]
            if parts[0] and parts[0][0]:
                year = parts[0][0]
                break
        auths = msg.get("author") or []
        surname = plain(auths[0].get("family", "")) if auths else ""
        return {"title": title, "year": year, "surname": surname.split(" ")[-1] if surname else "",
                "retracted": False, "source": "Crossref"}
    return None


def search_title(title, mailto, year=None):
    """Find the best OpenAlex match for a title among the top results."""
    best = None
    q = plain(title)[:250]
    for params in ({"filter": f"title.search:{q}", "per-page": "5"}, {"search": q, "per-page": "5"}):
        if mailto:
            params["mailto"] = mailto
        data = get_json(OPENALEX.rstrip("/") + "?" + urllib.parse.urlencode(params), mailto)
        for r in (data or {}).get("results") or []:
            sim = similarity(title, r.get("title") or "")
            if year and r.get("publication_year") and abs(int(year) - int(r["publication_year"])) > 1:
                sim -= 0.05
            if not best or sim > best["sim"]:
                best = {"title": r.get("title") or "", "doi": clean_doi(r.get("doi")),
                        "year": r.get("publication_year"), "sim": sim}
        if best and best["sim"] >= 0.9:
            break
    return best


# ------------------------------------------------------------------------- checks
REQUIRED = {"article": ["author", "title", "journal", "year"],
            "inproceedings": ["author", "title", "booktitle", "year"],
            "book": ["title", "publisher", "year"],
            "incollection": ["author", "title", "booktitle", "year"],
            "phdthesis": ["author", "title", "school", "year"],
            "mastersthesis": ["author", "title", "school", "year"]}


def structural_checks(entries):
    issues = []
    seen_keys, seen_dois, seen_titles = {}, {}, {}
    for e in entries:
        f, k = e["fields"], e["key"]
        for name in REQUIRED.get(e["type"], ["title", "year"]):
            if not f.get(name) and not (name == "author" and f.get("editor")):
                issues.append((k, f"missing field '{name}'"))
        if e["type"] == "article" and not f.get("doi"):
            issues.append((k, "article without DOI"))
        if k in seen_keys:
            issues.append((k, "duplicate key"))
        seen_keys[k] = True
        d = clean_doi(f.get("doi"))
        if d:
            if d in seen_dois:
                issues.append((k, f"same DOI as '{seen_dois[d]}'"))
            seen_dois.setdefault(d, k)
        t = plain(f.get("title"))
        if t:
            if t in seen_titles:
                issues.append((k, f"same title as '{seen_titles[t]}' (preprint and published version?)"))
            seen_titles.setdefault(t, k)
    return issues


CITE_RX = re.compile(r"\\(?:[a-zA-Z]*cite[a-zA-Z]*|nocite)\*?(?:\[[^\]]*\]){0,2}\{([^}]*)\}")


def tex_keys(paths):
    keys = set()
    for pattern in paths:
        for p in glob.glob(pattern) or [pattern]:
            text = open(p, encoding="utf-8", errors="replace").read()
            text = re.sub(r"(?<!\\)%.*", "", text)
            for m in CITE_RX.finditer(text):
                keys.update(k.strip() for k in m.group(1).split(",") if k.strip())
    return keys


def online_checks(entries, mailto, delay):
    rows = []
    for e in entries:
        f, k = e["fields"], e["key"]
        doi = clean_doi(f.get("doi"))
        try:
            if doi:
                rec = lookup_doi(doi, mailto)
                if rec is None:
                    rows.append((k, "DOI NOT FOUND", f"{doi} does not resolve in OpenAlex or Crossref"))
                else:
                    serious, minor = [], []
                    sim = similarity(f.get("title", ""), rec["title"])
                    if sim < 0.85:
                        serious.append(f"title differs ({sim:.0%} similar): registered title is '{rec['title']}'")
                    by = re.sub(r"\D", "", f.get("year", ""))[:4]
                    if by and rec["year"]:
                        diff = abs(int(by) - int(rec["year"]))
                        if diff > 1:
                            serious.append(f"year {by} vs registered {rec['year']}")
                        elif diff == 1:
                            minor.append(f"year {by} vs registered {rec['year']} (online-first vs print?)")
                    sb = first_surname_bib(f.get("author"))
                    if sb and rec["surname"] and sb != rec["surname"]:
                        serious.append(f"first author '{sb}' vs registered '{rec['surname']}'")
                    if rec["retracted"]:
                        rows.append((k, "RETRACTED", f"{doi} is marked as retracted ({rec['source']})"))
                    elif serious or minor:
                        rows.append((k, "MISMATCH" if serious else "CHECK", "; ".join(serious + minor)))
                    else:
                        rows.append((k, "OK", f"matches {rec['source']} record"))
            elif f.get("title"):
                by = re.sub(r"\D", "", f.get("year", ""))[:4] or None
                hit = search_title(f["title"], mailto, by)
                if hit and hit["doi"] and hit["sim"] >= 0.9:
                    rows.append((k, "NO DOI", f"title matches a record with DOI {hit['doi']} ({hit['year']}); add it if it is the same work"))
                else:
                    rows.append((k, "NO DOI", "no matching record found by title; verify manually"))
            else:
                rows.append((k, "NO DOI", "no DOI and no title"))
        except Exception as ex:  # network or parsing problem: report, continue
            rows.append((k, "ERROR", f"lookup failed: {ex}"))
        time.sleep(delay)
    return rows


# --------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("bib", nargs="+", help="BibTeX file(s)")
    ap.add_argument("--tex", nargs="*", default=[], help="LaTeX file(s) or glob patterns to compare cited keys")
    ap.add_argument("--mailto", default="", help="your e-mail for the OpenAlex/Crossref polite pool")
    ap.add_argument("--offline", action="store_true", help="skip online lookups")
    ap.add_argument("--delay", type=float, default=0.2, help="seconds between requests (default 0.2)")
    ap.add_argument("--out", help="write the Markdown report to this file")
    args = ap.parse_args()

    entries = []
    for b in args.bib:
        entries += parse_bib(open(b, encoding="utf-8", errors="replace").read())

    lines = ["# Citation check report", "", f"Entries: {len(entries)}", ""]
    problems = 0

    struct = structural_checks(entries)
    lines += ["## Structure", ""]
    lines += [f"- `{k}`: {msg}" for k, msg in struct] or ["- no structural problems"]
    problems += sum(1 for _, msg in struct if "duplicate" in msg or "same DOI" in msg or "missing field" in msg)

    if args.tex:
        cited = tex_keys(args.tex)
        keys = {e["key"] for e in entries}
        missing, unused = sorted(cited - keys), sorted(keys - cited)
        lines += ["", "## Cited keys vs bibliography", "",
                  f"Cited in .tex: {len(cited)}; in .bib: {len(keys)}", ""]
        lines += [f"- cited but not in .bib: `{k}`" for k in missing] or ["- every cited key is in the .bib file"]
        lines += [f"- in .bib but never cited: `{k}`" for k in unused] or ["- every .bib entry is cited"]
        problems += len(missing)

    if not args.offline:
        rows = online_checks(entries, args.mailto, args.delay)
        counts = {}
        for _, status, _ in rows:
            counts[status] = counts.get(status, 0) + 1
        lines += ["", "## Registry check (OpenAlex, Crossref)", "",
                  "Summary: " + ", ".join(f"{s} {n}" for s, n in sorted(counts.items())), "",
                  "| Key | Status | Details |", "|---|---|---|"]
        order = {"RETRACTED": 0, "DOI NOT FOUND": 1, "MISMATCH": 2, "ERROR": 3, "CHECK": 4, "NO DOI": 5, "OK": 6}
        for k, status, det in sorted(rows, key=lambda r: (order.get(r[1], 9), r[0])):
            lines.append(f"| `{k}` | {status} | {det.replace('|', '/')} |")
        problems += sum(n for s, n in counts.items() if s in ("RETRACTED", "DOI NOT FOUND", "MISMATCH"))

    lines += ["", "A match shows the reference exists and is described correctly. It does not show that the "
              "paper supports the sentence that cites it; check that against the source."]
    report = "\n".join(lines) + "\n"
    if args.out:
        open(args.out, "w", encoding="utf-8").write(report)
        print(f"Report written to {args.out}")
    sys.stdout.write(report)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
