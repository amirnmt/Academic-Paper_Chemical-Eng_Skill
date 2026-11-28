# Academic Paper Skill (STEM)

A [Claude skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) for writing STEM and engineering journal articles from a repository of reference papers and your own results.

It guides Claude through the whole article and its publication:

- **Any target journal:** send the journal's Guide for Authors at the start (and, if possible, 10–20 recent papers from it). The skill turns it into a journal profile (limits, structure, reference style, figures, required statements, and how the journal's papers are built) that overrides its defaults. Guidance is labelled by level: general writing [G], chemical and process engineering [D], patterns observed in the journal [J-obs], and the journal's explicit requirements [J-req]. Without a guide it uses a default profile and tells you which defaults apply. One profile per journal, so you can switch journals for the next paper.
- **Writing process:** choosing the journal first, the order in which to write the sections, drafting without blocking, revising in rounds, working with co-authors, using AI responsibly.
- **Evidence base:** search for missing papers, read papers rather than abstracts, turn a folder of papers into notes, a `refs.bib`, a theme map and a comparison matrix, and cite only verified sources at the strength they support.
- **Citation rule and citation density:** every scientific or literature-based statement in the Introduction carries a citation from your own paper folders (written through a claim–evidence map, never from memory); how many sources per claim, where they go, how to synthesize several sources in one sentence; benchmarks of citation density per part of the Introduction from a target journal's papers; `scripts/citation_density.py` audits a draft against them and lists every uncited background or literature sentence.
- **Every section, from first sentence to last:** what the section does, how it starts, which moves it makes and in what order, how its paragraphs are built, its tenses, and worked examples:
  - Introduction (problem → solution → evaluation framework; introducing concepts; seven paragraph patterns for the literature part; gap types and gap sentences; from gap to aim, contributions and scope),
  - Literature review (thematic synthesis, critical comparison, reporting verbs, planning a large citation count honestly),
  - Methods (content checklists for experimental, mechanistic-model and data-driven studies; LaTeX equations, `siunitx`, `mhchem`, nomenclature) and a pattern-by-pattern Methodology guide for modelling, simulation, optimization and data-driven papers: structures by type of research, physical foundations, assumptions, equations in the narrative, numerics, algorithms, ML and hybrid models, parameter origin, verification and validation, a reproducibility checklist and journal benchmarks,
  - Results (reporting pattern; language of sequence, frequency, quantity and causality; numbers and statistics),
  - Combined Results and discussion (subsection pattern and paragraph templates) and a pattern-by-pattern Results-and-Discussion guide: six kinds of evidence and integrity rules, paragraph frameworks for validation, physical interpretation, numerical performance, sensitivity, ML and hybrid results, literature comparison, unexpected results, limitations and implications; quantitative description; cause language matched to evidence; certainty ladder; a traceability matrix from gap to contribution; journal benchmarks,
  - Figures and tables (design rules, chart types, matplotlib style, captions, `booktabs`, referring to them in the text),
  - Discussion and Conclusion (explaining, comparing with the literature, hedging and modal verbs, limitations),
  - Abstract (including the patterns of process-systems abstracts), title, keywords, highlights.
- **Paragraphs and sentences:** topic sentences, development patterns, linking sentences, old → new information, the first and last sentence of each section, paragraph templates per section.
- **Language:** a large phrase bank of sentence stems by section and move, vocabulary per section, linking words, words to replace, confused words, the Academic Word List, tense and voice, concision, articles, numbers, common non-native errors.
- **Your field's own phrasing:** `scripts/build_section_phrases.py` reads converted papers from your target journal and lists, for each section, how the section begins, frequent sentence openers, phrases typical of that section, and recurring terms, counted by the number of papers that use them.
- **Searchable full texts:** `scripts/search_resources.py` searches the writing guides and papers in `resources/` so Claude can look up what the guides say when the summaries are not enough. An open-access guide (Lövei 2021, CC BY 4.0) is included; add your own guides and papers locally.
- **Avoiding generic, AI-typical prose:** word-level patterns, plus 33 discourse-level patterns from the StoryScope study of 61,608 human and AI texts (Russell et al., COLM 2026), each turned into a rule and a check for research articles, with model fingerprints. `scripts/check_ai_signs.py --structure` flags what can be detected automatically.
- **Research integrity of AI-assisted work:** a results log as the single source of truth for every number (template included), with `scripts/check_numbers.py` listing every number in a draft that is not in the log; seven failure modes of AI-assisted research to rule out before submission (after Lu et al., *Nature* 2026); checking that each cited source supports its sentence; rules for comparison claims and concurrent work; qualifiers that must survive the abstract.
- **Literature-review planning and scoring:** the Introduction and the literature review planned at two levels, prior work split into method groups (limitation → evidence → bridge), and a six-axis scoring rubric with caps against inflated self-assessment.
- **Plagiarism and paraphrasing:** the forms of plagiarism as they appear in a modelling paper, the standard an acceptable paraphrase must meet (stricter than some tutorials, as the guides disagree), a note-taking and drafting workflow that prevents copying, step-by-step paraphrasing techniques with worked reactor-modelling examples, quoting and citation placement, reuse of your own thesis or methods text (COPE, Elsevier), and the journal's similarity check. `scripts/check_overlap.py` finds passages in a draft that repeat runs of words from your sources before the journal's check does.
- **Acronyms:** `scripts/check_acronyms.py` checks definition at first use, once per scope (abstract and body), and use frequency.
- **Figure and table references:** `scripts/check_figrefs.py` finds captions never cited, numbers cited without a caption, and citations out of order.
- **Technical terms:** `references/technical-terms.md` lists about 60 terms of reactor modelling, estimation, validation, optimization and economics with the term each is confused with.
- **Calibrated on published papers:** the instructions and script thresholds were tested against 21 published *Computers & Chemical Engineering* papers, instruction by instruction (v2.11). The skill keeps its own standard where published papers fall below it; the samples set the floor, not the ceiling.
- **Simulated peer review:** review the full draft as an editor, a methods reviewer, a domain expert, a devil's advocate and a readability reviewer; triage the comments and revise.
- **Citation checking:** `scripts/check_citations.py` checks `refs.bib` against OpenAlex and Crossref (DOI resolves; title, first author and year match; retractions) and against the `\cite` keys in the LaTeX files.
- **Revision, cover letter and point-by-point response to reviewers.**

## Structure

```
academic-paper-skill/
├── SKILL.md                         core rules, workflow, and which reference to read
├── references/
│   ├── writing-process.md           planning, order of writing, drafting, revising
│   ├── evidence-base.md             finding, reading, noting and citing papers
│   ├── citation-practice.md         the citation rule, sources per claim, placement, density benchmarks, audit
│   ├── introduction.md
│   ├── literature-review.md
│   ├── methods-latex.md
│   ├── methodology-writing.md       Methodology patterns, equations, numerics, ML/hybrid, reproducibility
│   ├── results-language.md
│   ├── results-and-discussion-combined.md   one-section Results and discussion
│   ├── results-discussion-writing.md        evidence, interpretation, validation, metrics, traceability
│   ├── figures-tables.md
│   ├── discussion-hedging.md        Discussion and Conclusion
│   ├── abstract-title-keywords.md
│   ├── paragraphs-and-sentences.md  topic sentences, linking, first sentences, templates
│   ├── vocabulary-by-section.md     words for each section and move
│   ├── phrasebank.md                sentence stems by section and function
│   ├── style-grammar.md
│   ├── academic-vocabulary.md
│   ├── avoid-ai-signs.md
│   ├── plagiarism-and-paraphrasing.md   forms, standard, method, worked examples, text reuse, similarity check
│   ├── research-integrity.md    results log, failure modes F1–F7, claim–source check, comparison rules
│   ├── self-review.md
│   ├── submission-and-reviewers.md
│   ├── journal-profile.md       turning a Guide for Authors into rules; template; default profile
│   ├── technical-terms.md       reactor, estimation, validation, optimization and economics terms
│   ├── checklists.md
│   └── sources.md
├── resources/
│   ├── README.md                    how to add, search and mine full texts
│   ├── open/                        openly licensed guides (Lövei 2021, CC BY 4.0) + NOTICE
│   ├── templates/results_log.md     single source of truth for every number in the paper
│   ├── guides/                      your own converted guides (git-ignored)
│   ├── field-papers/                your own converted papers from your field (git-ignored)
│   └── journals/                    one profile per target journal
│       └── computers-and-chemical-engineering/   example profile (20 papers: every section, abstracts,
│                                                  conclusions, titles, keywords, figures, tables, equations)
└── scripts/
    ├── journal_profile.py           start, check and list journal profiles
    ├── convert_to_markdown.py       PDFs → Markdown (MarkItDown, PyMuPDF or pypdf)
    ├── search_resources.py          search the full texts in resources/
    ├── build_section_phrases.py     section-by-section phrase list from papers
    ├── check_ai_signs.py            flags generic or AI-typical prose (--structure: discourse level)
    ├── check_overlap.py             passages repeating runs of words from your sources
    ├── check_numbers.py             numbers in the draft that are not in the results log
    ├── check_acronyms.py            acronym definitions per scope
    ├── check_figrefs.py             figure/table citations: missing, uncaptioned, out of order
    ├── check_citations.py           checks refs.bib against OpenAlex/Crossref and the .tex citations
    └── citation_density.py          citation density of Introduction, Methods or Results vs. the journal; uncited or unsupported claims
```

`SKILL.md` stays short. Claude opens the detailed reference files only when it works on that section, and searches `resources/` only when it needs more.

The guidance in `references/` is distilled, in our own words, from established writing guides and genre studies of engineering research articles (see `references/sources.md`). Apart from the openly licensed text in `resources/open/`, those sources are not included here. Copyrighted guides and papers you own can be added to `resources/guides/`, `resources/field-papers/` and a journal profile's `papers/` folder; git ignores them so they stay on your computer.

## Install

**Claude apps (claude.ai / desktop):** download `academic-paper-skill.zip` from the [latest release](https://github.com/amirnmt/Academic-Paper_Chemical-Eng_Skill/releases/latest), or zip the `academic-paper-skill` folder yourself, and upload it under the skills section of *Settings*. If your app does not accept the zip, create or update a skill with only `academic-paper-skill/SKILL.md`: its first section tells Claude to fetch the reference files and scripts from this repository whenever they are not next to it, so the skill stays complete and up to date. To include your own guides or a phrase list from your target journal, add them to `resources/` before zipping.

**Claude Code** (terminal or the Code tab of the desktop app): clone the repository and link (or copy) the skill folder into your skills directory.

```bash
git clone https://github.com/amirnmt/Academic-Paper_Chemical-Eng_Skill.git
mkdir -p ~/.claude/skills
ln -s "$PWD/Academic-Paper_Chemical-Eng_Skill/academic-paper-skill" ~/.claude/skills/academic-paper-skill
# or copy it: cp -R Academic-Paper_Chemical-Eng_Skill/academic-paper-skill ~/.claude/skills/
```

On Windows (PowerShell), link without administrator rights:

```powershell
git clone https://github.com/amirnmt/Academic-Paper_Chemical-Eng_Skill.git
cmd /c mklink /J "$env:USERPROFILE\.claude\skills\academic-paper-skill" "$PWD\Academic-Paper_Chemical-Eng_Skill\academic-paper-skill"
```

With a link, `git pull` in the clone updates the skill. Start Claude Code in the folder that holds your paper and its sources, then call `/academic-paper-skill`.

Then ask Claude, for example: *"Use the academic-paper-skill to build the evidence base from the papers in this folder, then outline the introduction."*

## Starting a paper for a new journal

```bash
pip install pymupdf            # or: pip install 'markitdown[pdf]', or pypdf
python academic-paper-skill/scripts/journal_profile.py init "Journal Name" --guide guide_for_authors.pdf --papers sample_papers/
```

Then ask Claude to write the journal profile from `resources/journals/<journal>/requirements_draft.md`, or simply send Claude the guide and let the skill run these steps. `journal_profile.py check "Journal Name"` reports missing fields. The phrase list built from the sample papers contains only openers and phrases shared by several different papers, i.e. the conventions of the journal, not any single author's sentences.

## Author

Amir Nematollahi

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You may share and adapt this skill with attribution. `resources/open/` contains third-party text under its own licence; see `resources/open/NOTICE.md`.
