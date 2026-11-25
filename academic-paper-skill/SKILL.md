---
name: academic-paper-skill
description: Write or revise a STEM/engineering journal article from the user's results and a repository of reference papers: evidence base, introduction, literature review, methods with LaTeX, results, figures, discussion, abstract, references, academic vocabulary, avoiding AI-typical prose, and reviewer responses.
---

# Academic Paper Skill (STEM)

Use this skill to draft, revise or check an engineering or STEM research article (IMRaD or a close variant such as Introduction – Literature review – Methods – Results and Discussion – Conclusion) from the user's own results and a repository of papers (PDFs, BibTeX, a reference-manager export, Markdown conversions). It also covers the cover letter and the response to reviewers.

This file is the core. Detailed guidance lives in `references/`. Before working on a section, read the matching reference file; do not rely on memory of it.

## Golden rules

1. **Never invent a fact, number or reference.** Every claim about other work traces to a paper in the repository or a verified DOI. If unsure, write `[CHECK: key — what to verify]`.
2. **Every result has a method and every method has a result**, in the same order and under the same subheadings.
3. **Results report; the Discussion interprets.** Keep them distinct, even inside a combined Results and Discussion section.
4. **One objective, worded the same way** in the title, abstract, Introduction, Results, Discussion and Conclusion.
5. **Claim exactly as much as the data support.** No overclaiming, and no hedging of measured facts.
6. **Paraphrase, never copy** from sources or converted PDFs; check numbers and equations against the original PDF.
7. **Specific, not generic.** Replace inflated or vague statements with facts, numbers and citations (`references/avoid-ai-signs.md`). Disclose AI assistance as the journal requires.

## Which reference to read

| Task | Read |
|---|---|
| Turning the paper repository into notes, a theme map, a comparison matrix and verified citations | `references/evidence-base.md` |
| Introduction: funnel, problem-solution framework, gap, objective, contributions | `references/introduction.md` |
| Literature review: themes, synthesis, critical comparison, planning a large citation count | `references/literature-review.md` |
| Methods: content by study type, language that shows care, LaTeX equations, units, chemistry, nomenclature | `references/methods-latex.md` |
| Results: structure, reporting pattern, language of sequence, frequency, quantity and causality, numbers and statistics | `references/results-language.md` |
| Figures and tables: choice of form, design rules, chart types, matplotlib style, captions, booktabs | `references/figures-tables.md` |
| Discussion and Conclusion: structure, comparison with literature, stance, hedging and modal verbs, limitations | `references/discussion-hedging.md` |
| Abstract, title, keywords, highlights, graphical abstract | `references/abstract-title-keywords.md` |
| Academic style, paragraphs, concision, tense map, linking words, common non-native errors | `references/style-grammar.md` |
| Sentence stems by function | `references/phrasebank.md` |
| Academic vocabulary (Academic Word List) and precise word choice | `references/academic-vocabulary.md` |
| Avoiding generic, inflated or AI-typical prose; self-check | `references/avoid-ai-signs.md` and `scripts/check_ai_signs.py` |
| Revising the draft, submission package, cover letter, decisions, response to reviewers | `references/submission-and-reviewers.md` |
| Section and final checklists | `references/checklists.md` |
| The guides and studies this skill is based on | `references/sources.md` |

Read `style-grammar.md` and `avoid-ai-signs.md` once at the start of any drafting session, and `phrasebank.md` and `academic-vocabulary.md` when drafting text.

## Workflow

### 1. Intake (ask once, briefly)
- Target journal and its author guidelines: article type, word and page limits, abstract type and limit, highlights, graphical abstract, reference style, figure limits, template. If none is chosen, default to an Elsevier-style engineering journal with numbered references, and say so.
- Output: LaTeX (default, in the journal template) or Word.
- Location of the paper repository and of the results (data, figures, tables, code, notes).
- The contribution in one sentence: what is new compared with the closest prior work.
- Section structure used by recent papers in the target journal.

### 2. Evidence base (before writing)
Follow `references/evidence-base.md`: note every paper, build `refs.bib`, the theme map and the comparison matrix of the closest studies. Identify the gap from the matrix. Report thin themes.

### 3. Outline
For each section, list the paragraphs with a one-line purpose and the citations and figures each needs. Get the user's approval before drafting.

### 4. Draft, section by section
Recommended order: Methods → Results (with figures and tables) → Literature review → Discussion → Introduction → Conclusion → Abstract → Title, keywords, highlights.
For each section: read its reference file → draft → run its checklist → run `python scripts/check_ai_signs.py <file>` and rewrite every flagged sentence with a specific fact, number or citation, or delete it → hand to the user → revise.

### 5. Final check and delivery
- Run the final checklist in `references/checklists.md`.
- Verify every citation (resolve DOIs); report open `[CHECK]` items and unused repository papers.
- Deliver: LaTeX source in the journal template, `refs.bib`, figure scripts and figures, compiled PDF; plus a short list of weak points a reviewer may attack (novelty, validation, uncertainty, limitations, overclaiming).
- On request: cover letter and point-by-point response to reviewers (`references/submission-and-reviewers.md`).

## Defaults

- British or American spelling as the journal requires; consistent throughout.
- SI units with `siunitx`; chemical formulas with `mhchem`; tables with `booktabs`.
- Numbered citations unless the journal says otherwise.
- First person "we" for decisions and claims where the journal allows; passive for procedures.
- Figures generated from rerunnable Python scripts, exported as vector PDF at final column width.
