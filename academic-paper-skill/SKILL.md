---
name: academic-paper-skill
description: Write or revise a STEM/engineering journal article from the user's results and a repository of reference papers: evidence base, introduction, literature review, methods with LaTeX, results, figures, discussion, conclusion, abstract and references. Covers how each section and paragraph is built, first sentences, phrases and vocabulary per section, the field's own phrasing mined from papers, searchable writing guides, avoiding AI-typical prose, simulated peer review, citation checking and reviewer responses.
---

# Academic Paper Skill (STEM)

Use this skill to draft, revise or check an engineering or STEM research article (IMRaD or a close variant such as Introduction – Literature review – Methods – Results and Discussion – Conclusion) from the user's own results and a repository of papers (PDFs, BibTeX, a reference-manager export, Markdown conversions). It also covers the cover letter and the response to reviewers.

This file is the core. Detailed guidance lives in `references/`; full texts that can be searched live in `resources/`. Before working on a section, read the matching reference files; do not rely on memory of them.

## Golden rules

1. **Never invent a fact, number or reference.** Every claim about other work traces to a paper in the repository or a verified DOI. If unsure, write `[CHECK: key — what to verify]`.
2. **Every result has a method and every method has a result**, in the same order and under the same subheadings.
3. **Results report; the Discussion interprets.** Keep them distinct, even inside a combined Results and Discussion section.
4. **One objective, worded the same way** in the title, abstract, Introduction, Results, Discussion and Conclusion.
5. **Claim exactly as much as the data support.** No overclaiming, and no hedging of measured facts.
6. **Paraphrase, never copy** from sources, guides or converted PDFs; check numbers and equations against the original PDF.
7. **Specific, not generic.** Replace inflated or vague statements with facts, numbers and citations (`references/avoid-ai-signs.md`). Disclose AI assistance as the journal requires.

## Which reference to read

| Task | Read |
|---|---|
| Planning the work: target journal, writing order, drafting, revising rounds, co-authors, AI use | `references/writing-process.md` |
| Searching for missing papers, reading them, notes, theme map, comparison matrix, what and how to cite | `references/evidence-base.md` |
| Introduction: functions, first sentence, moves, gap, objective, contributions, worked example | `references/introduction.md` |
| Literature review: organization, synthesis, critical comparison, reporting verbs, planning a large citation count | `references/literature-review.md` |
| Methods: content by study type, order, language that shows care, LaTeX equations, units, chemistry, nomenclature | `references/methods-latex.md` |
| Results: structure, reporting pattern, language of sequence, frequency, quantity and causality, numbers and statistics | `references/results-language.md` |
| Figures and tables: choice of form, design rules, chart types, matplotlib style, captions, booktabs, referring to them in the text | `references/figures-tables.md` |
| Discussion and Conclusion: structure, explanation, comparison with literature, hedging and modal verbs, limitations | `references/discussion-hedging.md` |
| Abstract, title, keywords, highlights, graphical abstract | `references/abstract-title-keywords.md` |
| **Paragraphs:** topic sentences, development patterns, linking sentences, old → new information, the first and last sentence of each section, paragraph templates per section | `references/paragraphs-and-sentences.md` |
| **Words per section:** linking words and the vocabulary of each section and move; words to replace; confused words | `references/vocabulary-by-section.md` |
| **Sentence stems** by section and move, and for general functions (defining, comparing, cause and effect, trends, caution) | `references/phrasebank.md` |
| Academic style, tense map, voice, concision, articles, numbers, abbreviations, common non-native errors | `references/style-grammar.md` |
| Academic Word List and precise word choice | `references/academic-vocabulary.md` |
| Avoiding generic, inflated or AI-typical prose; self-check | `references/avoid-ai-signs.md` and `scripts/check_ai_signs.py` |
| Simulated peer review: editor, methods, domain, devil's advocate, readability; triage | `references/self-review.md` |
| Checking `refs.bib` against OpenAlex/Crossref and the LaTeX citations | `scripts/check_citations.py` |
| Revising, submission package, cover letter, decisions, response to reviewers | `references/submission-and-reviewers.md` |
| Section and final checklists, the Eight Cs | `references/checklists.md` |
| The guides and studies this skill is based on | `references/sources.md` |

Read `style-grammar.md` and `avoid-ai-signs.md` once at the start of any drafting session.

**For every section you draft, read four things:** the section file; its part of `paragraphs-and-sentences.md` (first sentence and paragraph template); its part of `vocabulary-by-section.md`; and its part of `phrasebank.md`. If a phrase list built from papers of the field or target journal exists (a `section_phrases*.md` file, for example in `resources/journal-papers/`), use its openers and phrases first and the general phrase bank second.

## Resources and helper scripts

`resources/` holds full texts the summaries are based on or that the user adds (see `resources/README.md`):
- `resources/open/`: openly licensed guides shipped with the skill (Lövei 2021, CC BY 4.0).
- `resources/guides/`: the user's own converted writing guides (local only).
- `resources/journal-papers/`: the user's converted papers, ideally from the target journal (local only).

| Script | Use |
|---|---|
| `python scripts/convert_to_markdown.py <pdf_dir> <out_dir>` | Convert PDFs to Markdown (MarkItDown, PyMuPDF or pypdf, whichever is installed). |
| `python scripts/search_resources.py "term" [more terms] [--dir DIR]` | Find what the guides or papers say about a topic, with file, line and nearest heading. `--list`, `--headings` show what is available. |
| `python scripts/build_section_phrases.py <papers_dir> --out section_phrases.md` | For each section of the papers: how the section begins, frequent sentence openers, phrases typical of the section, common phrases and recurring terms, counted by number of papers. |
| `python scripts/check_ai_signs.py <draft>` | Flag generic and AI-typical prose. |
| `python scripts/check_citations.py refs.bib --tex *.tex` | Verify references and citation keys. |

When the summaries in `references/` do not answer a question, or the user asks what a guide says, search `resources/` and report the findings in your own words with file and line. Never paste passages from the guides or papers into the manuscript.

## Workflow

### 1. Intake (ask once, briefly)
- Target journal and its author guidelines: article type, word and page limits, abstract type and limit, highlights, graphical abstract, reference style, figure limits, template. If none is chosen, default to an Elsevier-style engineering journal with numbered references, and say so.
- Output: LaTeX (default, in the journal template) or Word.
- Location of the paper repository and of the results (data, figures, tables, code, notes).
- The contribution in one sentence: what is new compared with the closest prior work.
- Section structure used by recent papers in the target journal, and whether 15–30 of those papers are available to build a phrase list.

### 2. Evidence base and phrase list (before writing)
- Follow `references/evidence-base.md`: check the repository against a database search, note every paper, build `refs.bib`, the theme map and the comparison matrix of the closest studies. Identify the gap from the matrix. Report thin themes.
- If papers are available as PDFs, convert them (`convert_to_markdown.py`) and run `build_section_phrases.py`. Keep `section_phrases.md` open while drafting.

### 3. Outline
For each section, list the paragraphs with a one-line purpose (its topic sentence in note form), the development pattern, and the citations and figures each needs (`paragraphs-and-sentences.md` §8). Get the user's approval before drafting.

### 4. Draft, section by section
Recommended order (`writing-process.md`): Methods → Results (with figures and tables) → Literature review → Discussion → Introduction → Conclusion → Abstract → Title, keywords, highlights.
For each section: read the four files listed above → draft paragraph by paragraph from the outline → run the section checklist → run `python scripts/check_ai_signs.py <file>` and rewrite every flagged sentence with a specific fact, number or citation, or delete it → hand to the user → revise.

### 5. Self-review
Follow `references/self-review.md`: review the complete draft in five independent roles (editor, methods, domain expert, devil's advocate, readability), collect the comments in a triage table, revise, and re-review the changed parts.

### 6. Final check and delivery
- Run `python scripts/check_citations.py refs.bib --tex *.tex --out citation_report.md` and resolve every RETRACTED, DOI NOT FOUND, MISMATCH and missing-key item. It needs internet access; if this environment cannot reach OpenAlex or Crossref, run it on the user's computer or verify the DOIs with another tool.
- Run the final checklist and the Eight Cs in `references/checklists.md`.
- Report open `[CHECK]` items and unused repository papers.
- Deliver: LaTeX source in the journal template, `refs.bib`, figure scripts and figures, compiled PDF; plus a short list of weak points a reviewer may attack (novelty, validation, uncertainty, limitations, overclaiming).
- On request: cover letter and point-by-point response to reviewers (`references/submission-and-reviewers.md`).

## Defaults

- British or American spelling as the journal requires; consistent throughout.
- SI units with `siunitx`; chemical formulas with `mhchem`; tables with `booktabs`.
- Numbered citations unless the journal says otherwise.
- First person "we" for decisions and claims where the journal allows; passive for procedures.
- Present tense for established knowledge and for what the paper shows; past tense for what was done and found.
- Figures generated from rerunnable Python scripts, exported as vector PDF at final column width.
