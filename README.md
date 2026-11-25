# Academic Paper Skill (STEM)

A [Claude skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) for writing STEM and engineering journal articles from a repository of reference papers and your own results.

It guides Claude through the whole article and its publication:

- **Evidence base:** turn a folder of papers into notes, a `refs.bib`, a theme map and a comparison matrix, and cite only verified sources.
- **Introduction:** move from the broad field to the research gap. Includes a problem → solution → evaluation framework for engineering papers.
- **Literature review:** thematic, synthesized and critical, with guidance for planning a large citation count honestly.
- **Methodology:** content checklists for experimental, mechanistic-model and data-driven studies, plus LaTeX equations, `siunitx` units, `mhchem` chemistry and nomenclature.
- **Results:** a reporting pattern and the language of sequence, frequency, quantity and causality, with rules for numbers and statistics.
- **Figures and tables:** design rules, engineering chart types, a matplotlib style, captions and `booktabs` tables.
- **Discussion and conclusion:** comparing with the literature, stance, hedging and modal verbs, and writing limitations.
- **Abstract, title, keywords, highlights.**
- **Style, paragraphs, tense, common non-native errors, and a phrase bank.**
- **Academic vocabulary:** how to use the Academic Word List (with links to the Oxford sublists) for precise word choice.
- **Avoiding generic, AI-typical prose:** patterns to avoid (inflated significance, decorative words, formulaic constructions, unverified citations) and a script, `scripts/check_ai_signs.py`, that flags them in a LaTeX, Markdown or text draft.
- **Simulated peer review:** review the full draft as an editor, a methods reviewer, a domain expert, a devil's advocate and a readability reviewer; triage the comments and revise.
- **Citation checking:** `scripts/check_citations.py` checks `refs.bib` against OpenAlex and Crossref (DOI resolves; title, first author and year match; retractions) and against the `\cite` keys in the LaTeX files.
- **Revision, cover letter and point-by-point response to reviewers.**

## Structure

```
academic-paper-skill/
├── SKILL.md                      core rules, workflow, and which reference to read
├── references/
│   ├── evidence-base.md
│   ├── introduction.md
│   ├── literature-review.md
│   ├── methods-latex.md
│   ├── results-language.md
│   ├── figures-tables.md
│   ├── discussion-hedging.md
│   ├── abstract-title-keywords.md
│   ├── style-grammar.md
│   ├── phrasebank.md
│   ├── academic-vocabulary.md
│   ├── avoid-ai-signs.md
│   ├── self-review.md
│   ├── submission-and-reviewers.md
│   ├── checklists.md
│   └── sources.md
└── scripts/
    ├── check_ai_signs.py         flags generic or AI-typical prose in a draft
    └── check_citations.py        checks refs.bib against OpenAlex/Crossref and the .tex citations
```

`SKILL.md` stays short. Claude opens the detailed reference file only when it works on that section.

The guidance is distilled, in our own words, from established writing guides and genre studies of engineering research articles (see `references/sources.md`). Those sources are not included here.

## Install

**Claude apps (claude.ai / desktop):** download `academic-paper-skill.zip` from the [latest release](https://github.com/amirnmt/academic-paper-skill/releases/latest), or zip the `academic-paper-skill` folder yourself. Then upload it under *Settings → Capabilities → Skills*.

**Claude Code:**

```bash
git clone https://github.com/amirnmt/academic-paper-skill.git
mkdir -p ~/.claude/skills
cp -R academic-paper-skill/academic-paper-skill ~/.claude/skills/
```

Then ask Claude, for example: *"Use the academic-paper-skill to build the evidence base from the papers in this folder, then outline the introduction."*

## Author

Amir Nematollahi

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You may share and adapt this skill with attribution.
