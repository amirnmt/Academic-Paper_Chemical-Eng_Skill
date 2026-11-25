# Academic Paper Skill (STEM)

A [Claude skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) for writing STEM and engineering journal articles from a repository of reference papers and your own results.

It guides Claude through the whole article and its publication:

- **Writing process:** choosing the journal first, the order in which to write the sections, drafting without blocking, revising in rounds, working with co-authors, using AI responsibly.
- **Evidence base:** search for missing papers, read papers rather than abstracts, turn a folder of papers into notes, a `refs.bib`, a theme map and a comparison matrix, and cite only verified sources at the strength they support.
- **Every section, from first sentence to last:** what the section does, how it starts, which moves it makes and in what order, how its paragraphs are built, its tenses, and worked examples:
  - Introduction (problem → solution → evaluation framework, gap types, objective and contributions),
  - Literature review (thematic synthesis, critical comparison, reporting verbs, planning a large citation count honestly),
  - Methods (content checklists for experimental, mechanistic-model and data-driven studies; LaTeX equations, `siunitx`, `mhchem`, nomenclature),
  - Results (reporting pattern; language of sequence, frequency, quantity and causality; numbers and statistics),
  - Figures and tables (design rules, chart types, matplotlib style, captions, `booktabs`, referring to them in the text),
  - Discussion and Conclusion (explaining, comparing with the literature, hedging and modal verbs, limitations),
  - Abstract, title, keywords, highlights.
- **Paragraphs and sentences:** topic sentences, development patterns, linking sentences, old → new information, the first and last sentence of each section, paragraph templates per section.
- **Language:** a large phrase bank of sentence stems by section and move, vocabulary per section, linking words, words to replace, confused words, the Academic Word List, tense and voice, concision, articles, numbers, common non-native errors.
- **Your field's own phrasing:** `scripts/build_section_phrases.py` reads converted papers from your target journal and lists, for each section, how the section begins, frequent sentence openers, phrases typical of that section, and recurring terms, counted by the number of papers that use them.
- **Searchable full texts:** `scripts/search_resources.py` searches the writing guides and papers in `resources/` so Claude can look up what the guides say when the summaries are not enough. An open-access guide (Lövei 2021, CC BY 4.0) is included; add your own guides and papers locally.
- **Avoiding generic, AI-typical prose:** patterns to avoid and `scripts/check_ai_signs.py`, which flags them in a LaTeX, Markdown or text draft.
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
│   ├── introduction.md
│   ├── literature-review.md
│   ├── methods-latex.md
│   ├── results-language.md
│   ├── figures-tables.md
│   ├── discussion-hedging.md        Discussion and Conclusion
│   ├── abstract-title-keywords.md
│   ├── paragraphs-and-sentences.md  topic sentences, linking, first sentences, templates
│   ├── vocabulary-by-section.md     words for each section and move
│   ├── phrasebank.md                sentence stems by section and function
│   ├── style-grammar.md
│   ├── academic-vocabulary.md
│   ├── avoid-ai-signs.md
│   ├── self-review.md
│   ├── submission-and-reviewers.md
│   ├── checklists.md
│   └── sources.md
├── resources/
│   ├── README.md                    how to add, search and mine full texts
│   ├── open/                        openly licensed guides (Lövei 2021, CC BY 4.0) + NOTICE
│   ├── guides/                      your own converted guides (git-ignored)
│   └── journal-papers/              your own converted papers (git-ignored)
└── scripts/
    ├── convert_to_markdown.py       PDFs → Markdown (MarkItDown, PyMuPDF or pypdf)
    ├── search_resources.py          search the full texts in resources/
    ├── build_section_phrases.py     section-by-section phrase list from papers
    ├── check_ai_signs.py            flags generic or AI-typical prose in a draft
    └── check_citations.py           checks refs.bib against OpenAlex/Crossref and the .tex citations
```

`SKILL.md` stays short. Claude opens the detailed reference files only when it works on that section, and searches `resources/` only when it needs more.

The guidance in `references/` is distilled, in our own words, from established writing guides and genre studies of engineering research articles (see `references/sources.md`). Apart from the openly licensed text in `resources/open/`, those sources are not included here. Copyrighted guides and papers you own can be added to `resources/guides/` and `resources/journal-papers/`; git ignores them so they stay on your computer.

## Install

**Claude apps (claude.ai / desktop):** download `academic-paper-skill.zip` from the [latest release](https://github.com/amirnmt/academic-paper-skill/releases/latest), or zip the `academic-paper-skill` folder yourself. Then upload it under *Settings → Capabilities → Skills*. To include your own guides or a phrase list from your target journal, add them to `resources/` before zipping.

**Claude Code:**

```bash
git clone https://github.com/amirnmt/academic-paper-skill.git
mkdir -p ~/.claude/skills
cp -R academic-paper-skill/academic-paper-skill ~/.claude/skills/
```

Then ask Claude, for example: *"Use the academic-paper-skill to build the evidence base from the papers in this folder, then outline the introduction."*

## Building a phrase list from your target journal

```bash
pip install pymupdf            # or: pip install 'markitdown[pdf]'
python academic-paper-skill/scripts/convert_to_markdown.py my_journal_pdfs academic-paper-skill/resources/journal-papers
python academic-paper-skill/scripts/build_section_phrases.py academic-paper-skill/resources/journal-papers --out section_phrases.md
```

The list contains only openers and phrases shared by several different papers, i.e. the conventions of the field, not any single author's sentences.

## Author

Amir Nematollahi

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You may share and adapt this skill with attribution. `resources/open/` contains third-party text under its own licence; see `resources/open/NOTICE.md`.
