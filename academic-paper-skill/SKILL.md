---
name: academic-paper-skill
description: Write or revise a STEM/engineering journal article from the user's results and a repository of reference papers, adapted to the target journal. Builds a journal profile from the Guide for Authors and sample papers (defaults otherwise), then covers evidence base, introduction, literature review, methods with LaTeX, results, figures, discussion, conclusion, abstract and references, with paragraph structure, first sentences, phrases and vocabulary per section, phrase mining, searchable writing guides, avoiding AI-typical prose, simulated peer review, citation checking and reviewer responses.
---

# Academic Paper Skill (STEM)

Use this skill to draft, revise or check an engineering or STEM research article (IMRaD or a close variant such as Introduction – Literature review – Methods – Results and Discussion – Conclusion) from the user's own results and a repository of papers (PDFs, BibTeX, a reference-manager export, Markdown conversions). It also covers the cover letter and the response to reviewers.

This file is the core. Detailed guidance lives in `references/`; full texts that can be searched live in `resources/`. Before working on a section, read the matching reference files; do not rely on memory of them.

## Golden rules

1. **Never invent a fact, number or reference.** Every claim about other work traces to a paper in the repository or a verified DOI. If unsure, write `[CHECK: key — what to verify]`.
2. **Every scientific or literature-based statement carries a citation** (Introduction, literature review, and wherever else such statements appear); only the authors' own objectives, methods, contributions and findings are exempt. When the user names directories of papers, write from them through a claim–evidence map and mark unsupported claims `[CITATION NEEDED]`; cite for relevance, not for count (`references/citation-practice.md`).
3. **Every result has a method and every method has a result**, in the same order and under the same subheadings.
4. **Results report; the Discussion interprets.** Keep them distinct, even inside a combined Results and Discussion section.
5. **One objective, worded the same way** in the title, abstract, Introduction, Results, Discussion and Conclusion.
6. **Claim exactly as much as the data support.** No overclaiming, and no hedging of measured facts.
7. **Paraphrase, never copy** from sources, guides or converted PDFs; check numbers and equations against the original PDF.
8. **Specific, not generic.** Replace inflated or vague statements with facts, numbers and citations (`references/avoid-ai-signs.md`). Disclose AI assistance as the journal requires.

## Which reference to read

| Task | Read |
|---|---|
| Planning the work: target journal, writing order, drafting, revising rounds, co-authors, AI use | `references/writing-process.md` |
| Searching for missing papers, reading them, notes, theme map, comparison matrix, what and how to cite | `references/evidence-base.md` |
| Introduction: functions, first sentence, moves, gap, objective, contributions, worked example; the long, literature-rich Introduction of computational journals (§5a) | `references/introduction.md` |
| Literature review: organization, synthesis, critical comparison, reporting verbs, planning a large citation count | `references/literature-review.md` |
| **Citations:** the citation rule, which sentences need a source, writing from the user's paper directories, sources per claim, placement, synthesis sentences, density benchmarks by part of the Introduction, audit | `references/citation-practice.md` and `scripts/citation_density.py` |
| Methods: content by study type, order, language that shows care, LaTeX equations, units, chemistry, nomenclature | `references/methods-latex.md` |
| Results: structure, reporting pattern, language of sequence, frequency, quantity and causality, numbers and statistics | `references/results-language.md` |
| Combined Results and Discussion: section and subsection pattern (R1–R7), paragraph templates for validation, model comparison, sensitivity, case studies, optimization, computational performance, limitations | `references/results-and-discussion-combined.md` |
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
| Journal profiles: how to turn a Guide for Authors into rules, the requirements template, the default profile | `references/journal-profile.md` |
| Section and final checklists, the Eight Cs | `references/checklists.md` |
| The guides and studies this skill is based on | `references/sources.md` |

Read `style-grammar.md` and `avoid-ai-signs.md` once at the start of any drafting session.

**For every section you draft, read four things:** the section file (for a combined Results and discussion, `results-and-discussion-combined.md` plus `results-language.md`); its part of `paragraphs-and-sentences.md` (first sentence and paragraph template); its part of `vocabulary-by-section.md`; and its part of `phrasebank.md`. For the Introduction and the literature review, also read `citation-practice.md`. Follow the active journal profile (below) for structure and limits; its `section_models.md` labels observed habits [J-obs] and its `journal_requirements.md` holds the binding rules [J-req] (`journal-profile.md` §0). If a phrase list exists for the target journal (`resources/journals/<journal>/section_phrases.md`) or the field (`resources/field-papers/*section_phrases*.md`), use its openers and phrases first and the general phrase bank second.

## Resources and helper scripts

`resources/` holds full texts the summaries are based on or that the user adds (see `resources/README.md`):
- `resources/open/`: openly licensed guides shipped with the skill (Lövei 2021, CC BY 4.0).
- `resources/guides/`: the user's own converted writing guides (local only).
- `resources/journals/<journal>/`: one **journal profile** per target journal: `journal_requirements.md` (rules from the Guide for Authors), optionally `section_models.md` and `section_phrases.md` (from sample papers), plus the converted guide and papers (local only). An example profile for *Computers & Chemical Engineering* is included.
- `resources/field-papers/`: the user's converted papers from the research field, e.g. the reference repository (local only).

| Script | Use |
|---|---|
| `python scripts/journal_profile.py init "Journal" --guide <file> [--papers <dir>]` | Start a journal profile: converts the Guide for Authors, sorts its lines by requirement field into `requirements_draft.md`, converts sample papers and builds their phrase list. `check "Journal"` finds gaps in the finished profile; `list` shows all profiles. |
| `python scripts/convert_to_markdown.py <pdf_dir> <out_dir>` | Convert PDFs to Markdown (MarkItDown, PyMuPDF or pypdf, whichever is installed). |
| `python scripts/search_resources.py "term" [more terms] [--dir DIR]` | Find what the guides or papers say about a topic, with file, line and nearest heading. `--list`, `--headings` show what is available. |
| `python scripts/build_section_phrases.py <papers_dir> --out section_phrases.md` | For each section of the papers: how the section begins, frequent sentence openers, phrases typical of the section, common phrases and recurring terms, counted by number of papers. |
| `python scripts/check_ai_signs.py <draft>` | Flag generic and AI-typical prose. |
| `python scripts/check_citations.py refs.bib --tex *.tex` | Verify references and citation keys. |
| `python scripts/citation_density.py audit <draft> --benchmarks resources/journals/<journal>/citation_benchmarks.json` | Citation density of the Introduction by part, compared with the journal; lists uncited background, literature and gap sentences and oversized citation groups. `benchmark <papers_dir>` builds the benchmark from sample papers. |

When the summaries in `references/` do not answer a question, or the user asks what a guide says, search `resources/` and report the findings in your own words with file and line. Never paste passages from the guides or papers into the manuscript.

## Workflow

### 1. Intake and journal profile (ask once, briefly)
- **Target journal and its Guide for Authors.** Ask the user to send the guide (file or link) and, if possible, 10–20 recent research papers from the journal. Then follow `references/journal-profile.md`:
  - a profile for the journal already exists in `resources/journals/` → read it; ask whether the guide has changed; rebuild if a newer guide is sent;
  - the user sends a guide → `journal_profile.py init`, write `journal_requirements.md` (and `section_models.md` from the papers), run `journal_profile.py check`;
  - no guide and no profile → use the default profile (`journal-profile.md` §4) and tell the user which defaults apply until the guide arrives.
- The active profile overrides the defaults of this skill everywhere (structure, limits, reference style, figure formats, statements, final checklist).
- Output: LaTeX (default, in the journal template) or Word.
- Location of the paper repository and of the results (data, figures, tables, code, notes).
- The contribution in one sentence: what is new compared with the closest prior work.

### 2. Evidence base and phrase list (before writing)
- Follow `references/evidence-base.md`: check the repository against a database search, note every paper, build `refs.bib`, the theme map and the comparison matrix of the closest studies. Identify the gap from the matrix. Report thin themes.
- If papers from the field are available as PDFs, convert them into `resources/field-papers/` and run `build_section_phrases.py`. Keep the journal's and the field's phrase lists open while drafting.

### 3. Outline
For each section, list the paragraphs with a one-line purpose (its topic sentence in note form), the development pattern, and the citations and figures each needs (`paragraphs-and-sentences.md` §8). Get the user's approval before drafting.

### 4. Draft, section by section
Recommended order (`writing-process.md`): Methods → Results (with figures and tables) → Literature review → Discussion → Introduction → Conclusion → Abstract → Title, keywords, highlights.
For each section: read the four files listed above → draft paragraph by paragraph from the outline (Introduction and literature review: from the claim–evidence map, citing as each sentence is written) → run the section checklist → for the Introduction, run `python scripts/citation_density.py audit <file> --benchmarks …` and support, rewrite or delete every listed sentence → run `python scripts/check_ai_signs.py <file>` and rewrite every flagged sentence with a specific fact, number or citation, or delete it → hand to the user → revise.

### 5. Self-review
Follow `references/self-review.md`: review the complete draft in five independent roles (editor, methods, domain expert, devil's advocate, readability), collect the comments in a triage table, revise, and re-review the changed parts.

### 6. Final check and delivery
- Run `python scripts/check_citations.py refs.bib --tex *.tex --out citation_report.md` and resolve every RETRACTED, DOI NOT FOUND, MISMATCH and missing-key item. It needs internet access; if this environment cannot reach OpenAlex or Crossref, run it on the user's computer or verify the DOIs with another tool.
- Run the final checklist and the Eight Cs in `references/checklists.md`, and check every item of the journal profile (limits, statements, files).
- Report open `[CHECK]` items and unused repository papers.
- Deliver: LaTeX source in the journal template, `refs.bib`, figure scripts and figures, compiled PDF; plus a short list of weak points a reviewer may attack (novelty, validation, uncertainty, limitations, overclaiming).
- On request: cover letter and point-by-point response to reviewers (`references/submission-and-reviewers.md`).

## Defaults

These apply only where the journal profile is silent; the full default profile is in `references/journal-profile.md` §4.
- British or American spelling as the journal requires; consistent throughout.
- SI units with `siunitx`; chemical formulas with `mhchem`; tables with `booktabs`.
- Numbered citations (`elsarticle-num`) unless the journal profile says otherwise (e.g. author–year, `elsarticle-harv`).
- First person "we" for decisions and claims where the journal allows; passive for procedures.
- Present tense for established knowledge and for what the paper shows; past tense for what was done and found.
- Figures generated from rerunnable Python scripts, exported as vector PDF at final column width.
