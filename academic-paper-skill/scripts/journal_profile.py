#!/usr/bin/env python3
"""Create and check journal profiles (one folder per target journal).

Usage:
  python scripts/journal_profile.py init "Journal Name" --guide GUIDE [--papers DIR [DIR ...]] [--force]
  python scripts/journal_profile.py check "Journal Name"
  python scripts/journal_profile.py list

init   creates resources/journals/<slug>/ and writes
         guide.md               the Guide for Authors as text (from PDF, Word, HTML, Markdown or text)
         requirements_draft.md  the guide's lines sorted by the fields of the requirements template,
                                with line numbers, plus a list of all lines containing limits
       and, with --papers (a folder of PDFs and/or Markdown files of sample papers),
         papers/                the papers as Markdown
         section_phrases.md     openers and phrases per section (build_section_phrases.py)
       The draft is raw material: journal_requirements.md is then written from it
       (template in references/journal-profile.md, section 3).
check  reports missing sections, empty fields and TODOs in journal_requirements.md.
list   lists the profiles and which files each one has.

Options: --root DIR (default: resources/journals next to this script's folder).
Standard library only, apart from the PDF engines used by convert_to_markdown.py.
"""
import argparse
import importlib.util
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_ROOT = HERE.parent / "resources" / "journals"
TEXT_EXTS = {".md", ".txt", ".markdown"}

# (heading in the requirements template, field, regex for guide lines)
FIELDS = [
    ("Fit and article types", "Scope, article types and limits",
     r"aims? and scope|article types?|full[- ]length|research (paper|article)s?|short (note|communication)|"
     r"review (article|paper)s?|letters?|word (limit|count)|\bwords\b|\bpages?\b|not (exceed|be longer)"),
    ("Fit and article types", "Review model",
     r"anonymi[sz]ed|double[- ]blind|single[- ]blind|peer review"),
    ("Files and layout", "Source files, template, layout",
     r"\.docx?\b|\.tex\b|latex|template|single[- ]column|double[- ]column|line number|file format|editable"),
    ("Files and layout", "Section numbering, appendices",
     r"numbered sections|subsection|appendi(x|ces)|cross-referenc"),
    ("Files and layout", "Language",
     r"british|american english|us english|uk english|language editing"),
    ("Title page", "Title page",
     r"title page|article title|affiliation|corresponding author|author names?|orcid"),
    ("Abstract, keywords, highlights, graphical abstract", "Abstract",
     r"\babstract\b(?!.*graphical)"),
    ("Abstract, keywords, highlights, graphical abstract", "Keywords",
     r"key ?words?"),
    ("Abstract, keywords, highlights, graphical abstract", "Highlights",
     r"highlights?|key points|bullet points"),
    ("Abstract, keywords, highlights, graphical abstract", "Graphical abstract",
     r"graphical abstract|toc graphic|table of contents (graphic|entry)"),
    ("Structure", "Structure",
     r"article structure|manuscript structure|sections? (should|must)|introduction|nomenclature|"
     r"theory and calculation|results and discussion|conclusions?\b"),
    ("Units, equations, tables, figures", "Units and equations",
     r"\bSI\b|units?\b|equations?|formula|math"),
    ("Units, equations, tables, figures", "Tables",
     r"\btables?\b"),
    ("Units, equations, tables, figures", "Figures",
     r"figures?|artwork|images?|\bdpi\b|resolution|\btiff?\b|\beps\b|vector|colou?r|caption"),
    ("Units, equations, tables, figures", "Generative AI in figures",
     r"(generative ai|ai tools|ai-assisted).*(figure|image|artwork)|(figure|image|artwork).*(generative ai|ai tools)"),
    ("References", "References",
     r"references?\b|citations?|cited|et al|\bdoi\b|abbreviat|bibliograph|reference style|harvard|numbered|"
     r"preprint|\[dataset\]|in press|personal communication"),
    ("Declarations and statements", "Competing interests",
     r"competing interests?|conflicts? of interest|declaration of interest"),
    ("Declarations and statements", "Funding",
     r"funding|grant number|financial support"),
    ("Declarations and statements", "Author contributions",
     r"credit\b|author contributions?|contributor roles"),
    ("Declarations and statements", "Data availability",
     r"research data|data availability|data statement|data repository|deposit|option [a-f]\b"),
    ("Declarations and statements", "Generative AI use",
     r"generative ai|ai-assisted|ai tools|large language model|chatgpt"),
    ("Declarations and statements", "Acknowledgements, ethics, other",
     r"acknowledg|ethic|informed consent|inclusive language|sex and gender"),
    ("Submission and after acceptance", "Submission, proofs, open access",
     r"cover letter|suggest(ed)? reviewers?|potential reviewers|submission checklist|submit online|"
     r"preprint|proofs?\b|open access|article (publishing|processing) charge|\bapc\b|licen[cs]e"),
]
LIMIT_RX = re.compile(r"\b\d[\d,.]*\s*(words?|characters?|pages?|keywords?|bullet|points?|figures?|tables?|"
                      r"references?|dpi|pixels?|cm|mm|mb|gb|days?|lines?)\b|\b(maximum|at most|not exceed|"
                      r"no more than|limited to|up to|minimum|at least)\b", re.I)


def load_converter():
    spec = importlib.util.spec_from_file_location("convert_to_markdown", HERE / "convert_to_markdown.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def slugify(name):
    s = name.lower().replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return re.sub(r"-{2,}", "-", s)


def to_text(src, conv):
    """Return the text of a guide or paper file."""
    src = Path(src)
    if src.suffix.lower() in TEXT_EXTS:
        return Path(conv.long_path(src)).read_text(encoding="utf-8", errors="replace")
    name, convert, exts = conv.pick_engine("auto")
    if src.suffix.lower() not in exts:
        sys.exit(f"Cannot convert {src.suffix} with the available engine ({name}). "
                 "Save the guide as PDF or plain text, or install markitdown.")
    return conv.tidy(convert(src))


def write_draft(guide_md, draft_path, journal):
    lines = guide_md.splitlines()
    out = [f"# {journal}: requirements draft", "",
           f"Generated {date.today().isoformat()} from guide.md by journal_profile.py. Raw material for "
           "journal_requirements.md: guide lines sorted by field (L = line in guide.md). Lines can appear under "
           "several fields; some matches are irrelevant. Write the final profile in your own words using the "
           "template in references/journal-profile.md section 3.", ""]
    out += ["## Lines that state limits or numbers", ""]
    for i, l in enumerate(lines, 1):
        s = l.strip()
        if s and LIMIT_RX.search(s) and len(s) > 15:
            out.append(f"- L{i}: {s}")
    current = None
    for heading, field, pat in FIELDS:
        rx = re.compile(pat, re.I)
        if heading != current:
            out += ["", f"## {heading}"]
            current = heading
        out += ["", f"### {field}", ""]
        hits = [(i, l.strip()) for i, l in enumerate(lines, 1) if l.strip() and rx.search(l)]
        if not hits:
            out.append("(no lines found: probably not specified; keep the default and mark it)")
        for i, s in hits[:25]:
            out.append(f"- L{i}: {s}")
        if len(hits) > 25:
            out.append(f"- … {len(hits) - 25} more lines; search guide.md")
    Path(draft_path).write_text("\n".join(out) + "\n", encoding="utf-8")


def cmd_init(args):
    if not Path(args.guide).is_file():
        sys.exit(f"Guide not found: {args.guide}")
    for d in args.papers or []:
        if not Path(d).is_dir():
            sys.exit(f"Papers folder not found: {d}")
    conv = load_converter()
    root = Path(args.root)
    folder = root / slugify(args.journal)
    folder.mkdir(parents=True, exist_ok=True)
    guide_md = to_text(args.guide, conv)
    if len(guide_md.strip()) < 500:
        print("WARNING: very little text extracted from the guide; check guide.md or supply the text.")
    guide_path = folder / "guide.md"
    if guide_path.exists() and not args.force:
        print("guide.md exists; use --force to replace it. Using the existing file.")
        guide_md = guide_path.read_text(encoding="utf-8", errors="replace")
    else:
        header = f"<!-- {args.journal}: Guide for Authors, converted {date.today().isoformat()} from {Path(args.guide).name} -->\n"
        guide_path.write_text(header + guide_md, encoding="utf-8")
    write_draft(guide_md, folder / "requirements_draft.md", args.journal)
    print(f"Profile folder: {folder}")
    print("  guide.md, requirements_draft.md written")
    if args.papers:
        pdir = folder / "papers"
        pdir.mkdir(exist_ok=True)
        n_new = 0
        sources = sorted(f for d in args.papers for f in Path(d).rglob("*"))
        for f in sources:
            if not f.is_file():
                continue
            target = pdir / (f.stem + ".md")
            if target.exists() and not args.force:
                continue
            if f.suffix.lower() in TEXT_EXTS:
                shutil.copyfile(conv.long_path(f), conv.long_path(target))
            elif f.suffix.lower() in {".pdf", ".docx", ".html", ".htm"}:
                try:
                    text = to_text(f, conv)
                except SystemExit as e:
                    print(f"  skipped {f.name}: {e}")
                    continue
                except Exception as e:  # one broken PDF should not stop the batch
                    print(f"  FAILED {f.name}: {e}")
                    continue
                with open(conv.long_path(target), "w", encoding="utf-8") as fh:
                    fh.write(text)
            else:
                continue
            n_new += 1
        print(f"  papers/: {n_new} new or updated files")
        res = subprocess.run([sys.executable, "-I", str(HERE / "build_section_phrases.py"), str(pdir),
                              "--out", str(folder / "section_phrases.md")], capture_output=True, text=True)
        print("  " + (res.stdout.strip() or res.stderr.strip()))
    req = folder / "journal_requirements.md"
    print("Next: write" if not req.exists() else "Next: update", req.name,
          "from requirements_draft.md (template: references/journal-profile.md section 3)"
          + (", and section_models.md from the papers" if args.papers else "") + ".")


def cmd_check(args):
    folder = Path(args.root) / slugify(args.journal)
    req = folder / "journal_requirements.md"
    if not req.exists():
        sys.exit(f"No {req}. Run init first, then write the file.")
    text = req.read_text(encoding="utf-8", errors="replace")
    problems = []
    headings = [m.group(1).strip() for m in re.finditer(r"^##\s+(.+)$", text, re.M)]
    wanted = []
    for h, _, _ in FIELDS:
        if h not in wanted:
            wanted.append(h)
    wanted.append("Defaults kept (not specified in the guide)")
    for h in wanted:
        if not any(x.lower().startswith(h.lower().split(" (")[0]) for x in headings):
            problems.append(f"missing section: ## {h}")
    for i, l in enumerate(text.splitlines(), 1):
        s = l.strip()
        if re.search(r"\bTODO\b|<[a-z][^>]*>", s):
            problems.append(f"L{i}: placeholder: {s[:90]}")
        elif re.match(r"^- [^:]{3,80}:\s*$", s):
            problems.append(f"L{i}: empty field: {s}")
    if not re.search(r"\b(19|20)\d\d\b", text.split("\n## ")[0]):
        problems.append("no date for the guide near the top (journals change their guides)")
    if problems:
        print(f"{req}: {len(problems)} item(s) to fix")
        for p in problems:
            print("  - " + p)
        sys.exit(1)
    print(f"{req}: complete")


def cmd_list(args):
    root = Path(args.root)
    if not root.exists():
        print(f"No profiles yet ({root} does not exist).")
        return
    names = ["journal_requirements.md", "section_models.md", "section_phrases.md", "guide.md",
             "requirements_draft.md", "papers"]
    rows = [d for d in sorted(root.iterdir()) if d.is_dir()]
    if not rows:
        print("No profiles yet.")
    for d in rows:
        have = [n for n in names if (d / n).exists()]
        npapers = len(list((d / "papers").glob("*.md"))) if (d / "papers").exists() else 0
        print(f"- {d.name}: " + ", ".join(have) + (f" ({npapers} papers)" if npapers else ""))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=str(DEFAULT_ROOT), help="folder holding the journal profiles")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("init", help="create or refresh a profile from a Guide for Authors")
    p.add_argument("journal", help='journal name, e.g. "Computers & Chemical Engineering"')
    p.add_argument("--guide", required=True, help="Guide for Authors: PDF, DOCX, HTML, MD or TXT")
    p.add_argument("--papers", nargs="+", help="folder(s) with sample papers of the journal (PDF and/or Markdown)")
    p.add_argument("--force", action="store_true", help="replace guide.md and converted papers")
    p = sub.add_parser("check", help="check journal_requirements.md for gaps")
    p.add_argument("journal")
    sub.add_parser("list", help="list profiles")
    args = ap.parse_args()
    {"init": cmd_init, "check": cmd_check, "list": cmd_list}[args.cmd](args)


if __name__ == "__main__":
    main()
