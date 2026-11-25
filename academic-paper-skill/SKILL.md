---
name: academic-paper-skill
description: Write a complete STEM/engineering journal article from the user's results and a local reference repository: literature review, intro, methods with LaTeX, results, discussion, references.
---

# Academic Paper Skill (STEM)

Use this skill to draft or revise an engineering/STEM research article (IMRaD or a close variant) from the user's own results and a repository of papers (PDFs, BibTeX, Zotero export, Markdown conversions). The rules below are distilled from eleven writing guides and genre studies (listed at the end of Section 14). They are written for chemical/process engineering but apply across STEM.

Golden rules, in order of importance:
1. Never invent a fact, number or reference. Every claim about others' work traces to a paper in the repository or a verified DOI.
2. Every result has a method, every method has a result, and both appear in the same order.
3. Results report; the Discussion interprets. Keep them distinct even inside a combined "Results and Discussion" section.
4. One objective, worded the same way in the title, abstract, introduction, results and discussion.
5. Claim exactly as much as the data support: no more (overclaiming), no less (hedging measured facts).

---

## 1. Intake (ask once, briefly, before writing)

- Target journal and its author guidelines: article type, word/page limits, abstract limit and type (structured or not), highlights, graphical abstract, reference style, figure limits, LaTeX/Word template. If no journal yet, default to an Elsevier-style chemical engineering journal, numbered references, and say so.
- Output format: LaTeX (default) or Word.
- Where the repository is, and where the results are (data files, figures, tables, notes, code).
- The contribution in one sentence: what is new compared with the closest prior work.
- Section structure the journal expects. Engineering papers commonly use Introduction – Literature review – Methods – Results and Discussion – Conclusion (ILM[RD]C) rather than strict IMRD; a separate literature review section and a merged Results and Discussion are both normal. Check recent papers in the target journal and copy their pattern.

Write for one precisely identified journal and its readers. A specialty journal allows denser technical background than a broad one.

## 2. Build the evidence base before writing

1. Inventory every paper in the repository: title, authors, year, venue, DOI, and a 2–3 line note (problem, method, key quantitative result, stated limitation). Save as `lit_notes.md`, plus `refs.bib` with one stable key per paper.
2. Convert PDFs to Markdown (MarkItDown) for reading. Equations, tables and figures convert poorly: check the original PDF before quoting any number, equation or table value.
3. Tag each paper with themes, from broad to narrow (field → sub-area → closest prior work). Mark review papers; use them to cover background efficiently.
4. Build a comparison matrix of the closest studies (method, system, conditions, metric, result, limitation). It feeds the literature review, the gap statement and the Discussion comparisons.
5. Citation rules:
   - Cite only papers in the repository or verified by DOI (title, authors, year must match). Never guess a reference.
   - Each cited claim must match what the paper actually says. If unsure, write `[CHECK: key]` instead of citing.
   - Keep a citation map: claim → key → page/section.
   - Cite for relevance, not to show reading. Common knowledge needs no citation; a named method, criterion, correlation or dataset always does (cite its original source).
   - Prefer peer-reviewed journal papers; cite books with chapter and pages; avoid websites, personal communications and unpublished data where possible.
   - Insert the citation the moment a claim is written; never "add references later".
   - Report which repository papers were not used, and any topic that is too thin to support the claim being made.

## 3. Introduction: from the broad field to your niche

Shape: a funnel. Start general, narrow step by step, end on your specific question. Every sentence must move the reader toward the gap.

### 3.1 The four-part model (use in this order)
1. **Establish the territory.** Why the field matters (industrial, environmental, economic relevance, with 2–4 strong citations). Background facts. Define key terms in the title. Present the general problem or current research focus.
2. **Review previous and current research.** What has been done and what it achieved, grouped by approach, not paper by paper.
3. **Locate the gap.** What is unknown, contradictory, untested, or limited in prior work. State the specific problem you address and, if appropriate, a prediction or hypothesis.
4. **Present the current work.** Objective (precise parameter or property, system, and means), approach, and 2–4 specific contributions. Optionally one sentence on the main finding and a paper outline.

### 3.2 Engineering variant: problem → solution → evaluation (recommended for applied/process work)
Engineering introductions often read better as a problem-solution cycle in place of a generic "territory" opening:
- Situation: the process, material, or system and why it matters in practice.
- Problem: what goes wrong or is limited in that situation.
- Previous solutions and their evaluation: what others proposed and how well it worked. Repeat solution → evaluation for each family of approaches; progress in engineering is usually incremental.
- The remaining unsolved problem is the gap; your study is the next proposed solution.
- Also justify the choice of method ("procedural justification"): why this modelling approach, reactor configuration, or technique over alternatives.

### 3.3 Rules
- Selective citation: cite the most pertinent work, especially conflicting data that show genuine uncertainty. Do not try to cite everything here; the exhaustive review goes in the literature review section.
- Do not state the obvious or wander off topic. Each paragraph earns its place.
- Gap statement must be evidence-based: "X and Y studied A under B, but C under D has not been examined", not "little is known about this interesting topic". Interesting is not a justification; say why the gap matters.
- Prefer explicit hypotheses or research questions; keep them few (no more than about five).
- Typical length: about 1–1.5 pages unless the journal says otherwise.
- Write the Introduction draft early (context and references are fresh), and finalize it after the Discussion so the promised contribution matches what was delivered.

### 3.4 Tense in the Introduction
- Established knowledge, accepted facts: present simple ("Ethylene oxide is produced by …").
- A specific earlier study's finding: past simple ("Smith et al. showed that …").
- A research area active up to now, or a gap still open: present perfect ("Several studies have investigated …"; "It has not yet been determined whether …").
- Your hypothesis: past for the first verb, present for the second ("We hypothesized that X increases Y").
- Your objective and your own findings: past ("This study aimed to …").
- Choosing present simple for a finding signals you treat it as established; past simple keeps it tied to that one study. Choose deliberately.

## 4. Literature review (comprehensive, synthesized, critical)

Purpose: place the work in context, compare and contrast studies, show differing interpretations, and expose the gap. It is not a list of summaries.

Process:
1. Define the question the review must answer (what the reader needs to accept your gap).
2. Select sources against that question; extract only what serves it.
3. Group sources into themes tied to the research question, ordered from broad to narrow and ending with the studies closest to yours.
4. Within each theme, compare and contrast: same axes for every study (method, system, conditions, metric, result, limitation). Use a summary table for the closest 10–20 studies when it helps.
5. Close each theme with a synthesis sentence: what is settled, what disagrees, what is missing.
6. End the review with the gap, stated so the introduction's objective follows naturally.

Writing rules:
- Synthesize, do not string summaries: "Three approaches dominate … [1–5]; they differ mainly in … [3,6]" beats "Author A did X. Author B did Y."
- Be balanced: include results that disagree with your expectation and explain why they differ.
- Keep your own voice present: open or close each discussion of sources with your evaluation.
- Paraphrase; quote only when exact wording matters (rare in engineering).
- Be diplomatic about others' weaknesses: state the strength of your approach rather than attacking ("this study resolves the axial and radial profiles simultaneously" instead of "previous models were inadequate"); hedge criticism ("may have been limited by …").
- Citation count: aim for the number the user requested (e.g. 70+) only with genuinely relevant, verified sources. If the repository cannot support the target, report the gap in coverage instead of padding.
- Tense: present for what the field knows, past for what a specific study did, present perfect for ongoing lines of research.

## 5. Methodology

Goal: an average expert with the same resources could reproduce the work. Every result reported later needs a method here; methods already published can be summarized with a citation.

### 5.1 Structure (select what applies)
1. Overview: restate the purpose; give the overall approach (experimental, numerical, hybrid); source of materials and equipment (manufacturer, model, city, country); essential background.
2. Specific, precise details: quantities, concentrations, temperatures, pressures, flow rates, durations, sequence, dimensions, conditions; for models: governing equations, assumptions, boundary and initial conditions, kinetics and parameters with sources, numerical scheme, solver, mesh/discretization, convergence and tolerance, software and version. Justify each non-obvious choice and show that appropriate care was taken (calibration, repeats, mesh independence, validation).
3. Relation to other studies: which parts follow an established method (cite it) and what was modified.
4. Problems or limitations encountered, if any, and how they were handled.
5. Data analysis: post-processing, error metrics (RMSE, MAE, R², relative error), uncertainty and error propagation, statistical tests, train/validation/test splits for ML models.

Use subheadings (e.g. 2.1 Reactor and catalyst, 2.2 Model equations, 2.3 Numerical solution, 2.4 Validation data). Reuse the same subheadings in Results. Past tense for what was done ("The reactor was discretized …"); present tense for equations and what tables/figures show.

### 5.2 Mathematics in LaTeX
- Introduce each equation in the sentence that uses it; equations are punctuated as part of the sentence.
- Define every symbol at first use, with units; for many symbols add a Nomenclature table (Latin, Greek, subscripts, superscripts, abbreviations).
- Number only equations referenced later; refer to them as "Eq. (3)" or as the journal requires.
- Notation: italic for variables, upright for units, labels and function names (`\mathrm{d}`, `\exp`, `\ln`); bold for vectors and matrices; consistent symbols throughout the paper.
- Units with `siunitx` (`\SI{250}{\celsius}`, `\si{\mol\per\second}`); SI units only; a thin space between number and unit.
- Use `equation` for single equations, `align` for systems; `\label`/`\eqref` for cross-references; do not hard-code numbers.
- State assumptions next to the equations they simplify.
Example:
```latex
The steady-state mass balance for species $i$ in the gas phase reads
\begin{equation}
  u_\mathrm{s}\,\frac{\mathrm{d}C_i}{\mathrm{d}z}
  = \rho_\mathrm{b}\sum_{j=1}^{N_\mathrm{r}} \nu_{ij}\,\eta_j\,r_j ,
  \label{eq:mass_balance}
\end{equation}
where $u_\mathrm{s}$ is the superficial velocity (\si{\metre\per\second}),
$C_i$ the molar concentration (\si{\mol\per\cubic\metre}), and $\eta_j$ the
effectiveness factor of reaction $j$.
```

## 6. Results: report, compare, but do not interpret

- Order: the same order and subheadings as the Methods; give a result for every method.
- From macro to micro: open each subsection with the main finding (the big picture), then the specific supporting numbers.
- Paragraph pattern for each figure/table:
  1. (Optional) recall the aim or the analysis briefly.
  2. Point to the figure/table and state the main trend ("Fig. 4 shows that the hot-spot temperature increases with inlet O₂ fraction").
  3. Support with numbers: values, differences, % change, uncertainty.
  4. Secondary trends.
  5. Exceptions or anomalies.
  6. Comparisons with validation data, model predictions, or other studies, with a clear metric.
- Guide the reader. "The results are shown in Fig. 3" alone is not acceptable; say what the figure shows.
- Report negative and null findings too: absence of evidence is not evidence of absence.
- Do not present material preparation as a result; do not include a method that was forgotten in Methods; do not present every number you have.
- Never present the same data twice (text and table and figure). A key value read from a figure may be quoted in the text.
- No commentary words ("surprisingly", "interestingly") in a pure Results section; in a combined Results and Discussion section, separate clearly what was measured or computed from what is inferred.
- Statistics: test name, statistic, degrees of freedom, exact p-value where software gives it. For models: error metric and the data it was computed on.
- Numbers:
  - Do not report more decimals than measurement precision supports (at most one extra digit for means).
  - Do not start a sentence with a numeral; spell it out or rephrase.
  - Leading zero for values below 1 (0.25, not .25).
  - Ranges with "to" or an en dash in a consistent journal style; avoid a hyphen that looks like a minus sign.
  - SI units; distinguish mass and weight, yield, selectivity and conversion precisely, and define each on first use.
  - Use numerals with units; small counts without units may be spelled out per journal style.
- Tense: past for your findings ("Selectivity reached 82 %"); present for what a figure shows ("Fig. 5 compares …"). Present simple for your own result signals that you consider it established; use it only when the evidence is strong.

## 7. Figures and tables

When to use what: a result that fits in one or two sentences stays in the text; repetitive, precise values go in a table; trends and relationships go in a figure. If numbers show no trend, use a table, not a graph.

Figures (economy, integrity, clarity):
- As simple as possible; no 3D effects, shading, or decoration; maximize the data-to-ink ratio.
- Every axis labeled with quantity and unit, e.g. "Temperature, T (K)" or "T / K" per journal style.
- Axis range fitted to the data; ticks pointing outward; readable font at final printed column width (8–10 pt).
- Consistent axes, colors, markers and line styles across related panels and figures; colorblind-safe palette; distinguishable in grayscale.
- Vector output (PDF/EPS/SVG); generated from a script (Python/matplotlib) that the user can rerun.
- Experimental data as markers, model results as lines; show error bars or bands where available and state what they represent.
- Captions below figures; self-explanatory without the text, but also integrated into the narrative.

Tables:
- Captions above tables; concise title that identifies content without the text ("Group 1" is meaningless; name the condition).
- Three horizontal rules (`booktabs`: `\toprule`, `\midrule`, `\bottomrule`), no vertical rules.
- Units in column headers; avoid exponents in headers where possible (they are ambiguous); consistent significant figures; like elements read down columns.
- Remove columns that are constant (state the constant once in a note or in Methods) and tables that contain mostly zeros or a single message.
- Number tables and figures separately, consecutively, in the order cited; place each after its first mention.

## 8. Discussion: what the results mean

Answer one question: what do the data mean? A weak Discussion is the most common reason for rejection.

### 8.1 Structure (select what applies)
1. Revisit: restate the main findings briefly, using the same wording as the objective.
2. Map: relate findings to existing research. Agree, disagree, extend. When results differ from others, give plausible, specific reasons (conditions, catalyst, model assumptions, scale, data).
3. Explain mechanisms: why the trends occur (kinetics, heat/mass transfer limitations, thermodynamics, deactivation).
4. Achievement and contribution: what is new, whether the hypothesis is supported and the gap from the Introduction is closed; principles, relationships and generalizations that follow from the results; the "new picture" if there is one.
5. Implications: theoretical and practical (design, operation, scale-up, safety, control).
6. Limitations: state them honestly and, where justified, explain why their effect is small. This shows reviewers you know them.
7. Future work: specific and justified by the limitations or by new observations.

### 8.2 Rules
- Do not repeat the Results; do not introduce new results (if a result becomes relevant, add it to Results and its method to Methods).
- Do not over-interpret: a result on 25 samples does not license a statement about all cases. Generalize only as far as the data reach.
- Summarize the evidence behind each conclusion; do not leave the inference to the reader.
- Do not pretend everything is solved; do not discuss every speculative possibility.
- Avoid throwaway endings ("more research is needed", "the implications are discussed"). End on a precise, well-founded statement.
- Keep proportion: a Discussion much longer than about twice the Results is usually too long.
- Negative results from a well-designed study are a valid contribution; discuss what they challenge or confirm.
- Stance that marks strong discussions (from high-impact chemical engineering papers): clear authorial presence when stating claims, evaluative statements followed by explanation or elaboration, and a balanced mix of hedges and boosters. Be confident where evidence is strong and cautious where it is not.
- Tense: present for established knowledge and for generalizations from your data; past for your specific results; modals for interpretation.

### 8.3 Hedging scale (choose the strength the evidence supports)
- Evidence proves it: no modal. "The pressure drop was caused by catalyst fouling."
- Virtually certain but not proven: "must have been caused by …" (note: "must" signals certainty without proof).
- Probable: "is likely due to"; "should".
- Possible: "may", "might", "could"; "a possible explanation is …".
- Other hedges: "suggests", "indicates", "appears to", "is consistent with", "to some extent", "under the conditions studied".
Do not hedge measured facts, and do not stack hedges ("it might possibly suggest").

## 9. Conclusion

- Answer the objective directly; give the key quantitative findings; state the main limitation and the outlook.
- No new data, no new citations, no repetition of the abstract word for word.
- If the journal has no separate Conclusion, end the Discussion with a short concluding paragraph doing the same job.

## 10. Abstract, title, keywords, highlights

Abstract (write last):
- Self-contained: no references, no figure or table citations, no undefined abbreviations, no statement that is not in the paper.
- Components: background/problem (1–2 sentences), aim, methodology/materials, main results with numbers (primary result first), contribution or implication; optionally applications, limitations or future work. Structured abstracts keep these as separate parts; compact abstracts combine 2–3 components per sentence, with methods before results.
- Concentrate on results, not on a list of what was done; mostly past tense; no evaluative remarks ("surprisingly").
- Avoid empty endings ("the results are discussed"). Paraphrase rather than paste sentences from the paper. Respect the word limit; using less is fine.

Title:
- Turn the research question into a title ("How does X affect Y?" → "Effect of X on Y in …"). State the main factor, system and, where possible, the finding; put the most important element first.
- Include searchable key terms; avoid filler ("A study of …", "Investigation on …"); keep it within the journal's limit.
- Check compound nouns for ambiguity and prepositions for meaning ("with" = using or having; "evidence for" vs "evidence of").
- Use sentence case unless the journal says otherwise; reflect the scope accurately (case study vs general study).

Keywords: specific, searchable terms not already in the title (method, material, process, property); avoid general words ("study", "experiment"); within the journal's limit.

Highlights / graphical abstract: 3–5 bullet results within the character limit; a new figure for the graphical abstract unless one result figure captures the paper.

## 11. Academic style and paragraphs

Paragraph construction (one idea per paragraph):
- Topic sentence near the start: what the paragraph claims and how it links to the argument.
- Supporting sentences: data, citations, explanation, analysis.
- Closing sentence: interpretation or link to the next paragraph.
- Check focus, coherence and development; start a new paragraph for each new idea or contrasting argument; give introduction and conclusion their own paragraphs.
- Use signalling language to connect sentences and paragraphs (however, in contrast, consequently, similarly).

Academic style:
- Evidence-based, precise, objective, concise, cautious where appropriate; no contractions, no rhetorical questions, no clichés or emotive or promotional words ("revolutionary", "obviously").
- One sentence, one point; simple sentences carry new information best. Long, convoluted sentences hide the argument.
- Cut deadweight words and wordy phrases ("due to the fact that" → "because"; "in order to" → "to"); replace vague words with specific ones.
- Nominalization makes text compact but dense; do not stack noun phrases until meaning is lost.
- Define jargon and abbreviations at first use; keep terminology consistent (do not vary terms for style).
- First person ("we") is accepted in most engineering journals for decisions and claims; passive voice suits procedures. Choose what keeps the actor clear; follow the journal's practice.
- Keep tense consistent within a passage; shift only for a reason (see the tense rules in each section).
- Use inclusive, unbiased language.

## 12. Phrase bank (generic stems; adapt to the content)

Establishing importance: "X is widely used in …"; "X plays a key role in …"; "Growing demand for X has led to …".
Reviewing literature: "Previous studies have shown that …"; "Several approaches have been proposed to …"; "X et al. [12] reported that …"; "These studies differ mainly in …".
Synthesizing: "Similar trends were reported by [3–5]"; "In contrast to [7], [8] found …"; "Taken together, these studies indicate that …".
Highlighting a problem or gap: "However, …remains unclear"; "Few studies have addressed …"; "To date, no study has examined …"; "These models neglect …, which limits …".
Stating purpose: "This study aims to …"; "The objective of this work is to …"; "To address this gap, we …"; "The main contributions are as follows: …".
Describing methods: "X was used to …"; "Following the procedure of [9], …"; "To ensure …, …"; "The model was validated against …".
Reporting results: "As shown in Fig. 3, …"; "X increased from A to B as Y …"; "A significant difference was observed between …"; "No significant effect of X on Y was found".
Comparing: "These values agree well with …"; "This is consistent with …"; "This discrepancy may be attributed to …"; "In contrast to …".
Explaining: "This can be explained by …"; "A possible explanation is that …"; "This behaviour is likely due to …".
Cautious interpretation: "These results suggest that …"; "Under the conditions studied, …"; "These findings should be interpreted with caution because …".
Limitations and future work: "One limitation of this study is …"; "Further work is required to establish …"; "Future studies should investigate …".
Conclusions: "This study has shown that …"; "The results demonstrate that …"; "These findings have implications for …".
For a fuller list, see the Manchester Academic Phrasebank (https://www.phrasebank.manchester.ac.uk/).

## 13. References

- Use the journal's style exactly (numbered/Vancouver, Elsevier, IEEE, APA, Harvard); manage references with BibTeX or a reference manager, never by hand.
- Generate the list from the verified `refs.bib`. Check: every in-text citation has an entry and vice versa; no duplicates; DOIs present; author names, years, volume, pages correct; journal abbreviations consistent; page ranges with an en dash.
- Run a final citation audit (e.g. resolve every DOI) and list open `[CHECK]` items.
- Ethics: paraphrase properly, cite ideas as well as words, avoid text recycling from your own earlier papers without disclosure, and declare AI assistance as the journal requires.

## 14. Workflow and delivery

1. Intake (Section 1) → evidence base (Section 2) → outline with one-line purpose per paragraph → user approves.
2. Draft order: Methods → Results → Literature review → Discussion → Introduction → Conclusion → Abstract → Title and keywords.
3. Work section by section: draft → user review → revise.
4. Deliver LaTeX source (journal template), `refs.bib`, figure scripts and figures; compile to PDF to check layout, equations, tables and figure readability.
5. Final self-review before handing over:
   - Objective worded identically throughout; title, abstract and conclusion match the results.
   - Each method has a result and vice versa; same order and subheadings.
   - No data duplicated across text, tables and figures; numbers consistent everywhere.
   - All symbols defined; units SI; significant figures consistent.
   - Every citation verified; no `[CHECK]` left unreported.
   - Likely reviewer attacks addressed: novelty, validation, uncertainty, limitations, overclaiming.
   - Revision pass for concision: cut what does not serve the argument.

Source guides this skill is distilled from (not included in this repository; obtain them from their publishers):
- Ecarnot et al. (2015), *Writing a scientific article: a step-by-step guide for beginners*.
- Lövei (2021), *Writing and Publishing Scientific Papers* (Open Book Publishers, https://doi.org/10.11647/OBP.0235).
- Glasman-Deal (2010), *Science Research Writing for Non-Native Speakers of English* (Imperial College Press): section models, tense, modal verbs.
- Gastel and Day (2022, 9th ed.), *How to Write and Publish a Scientific Paper*: tables, graphs, style.
- Morley, *Academic Phrasebank* (Manchester, 2014b).
- University of Hohenheim Academic Writing Aid Series: paragraphs, concision, tenses, literature reviews.
- Chair in E-Business, *Guidelines for Academic Paper Writing*: formatting, captions, formulas.
- Lin and Evans (2012), structural patterns in empirical research articles (ILM[RD]C).
- Maswana, Kanamaru and Tajino (2015), move analysis of articles in five engineering fields.
- Khaw (2017), problem-solution framework for engineering introductions.
- Jin (2018), discussion sections of high- vs low-impact chemical engineering articles.
