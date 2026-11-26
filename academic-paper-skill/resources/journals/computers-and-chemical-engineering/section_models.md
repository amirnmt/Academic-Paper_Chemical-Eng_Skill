# How Computers & Chemical Engineering papers are built

A move analysis of 21 papers from the journal (2006–2026), made to model a manuscript on the journal's own conventions. All descriptions are paraphrased; papers are identified by the last digits of their PII (ScienceDirect identifier, S0098-1354(yy)xxxxx-x). Use this together with `journal_requirements.md`.

## 0. What was analysed

- 21 papers: 4 on ethylene and ethylene oxide plants (…0433, …2326, …3434 and an ANN model of an industrial EO plant, 2022) and 17 recent papers from 2026 on various topics. The review on kinetic Monte Carlo (…4187) was left out of the section analysis because reviews are organized differently, which leaves 20 research articles.
- Method: top-level and second-level headings of all 20 papers; sentence-by-sentence reading of the Introductions of 8 papers and a skim of 11 more; subsection-level reading of the Results and Discussion of 6 papers on modelling and data-driven methods (…4321 hybrid GNN, …4448 data-augmented MPC, …4436 industrial propylene reactor model, …4357 robustness benchmarking of data-driven models, …4497 industrial soft sensing, and the EO-plant ANN paper); abstracts and conclusions of 8 papers; and phrase counts from `scripts/build_section_phrases.py`.
- Counts below refer to these papers. With 20 papers they show conventions, not rules.

## 1. Architecture of the paper

Typical order of top-level sections:

| Position | Section | How often |
|---|---|---|
| 1 | Introduction (with the literature review inside it) | 20/20 |
| 2 | Process, system or data description, or problem statement | about 7/20 |
| 2–3 | Methodology / Modelling framework / Mathematical model (often several sections) | 20/20 |
| (3) | Evaluation metrics as a separate section | occasionally |
| 3–5 | Case study (applies the method to a defined system) | 7/20 |
| 4–7 | Results and discussion (combined) | 10/20; separate Results in most others, separate Discussion rare |
| (end of R&D) | Implications; Limitations (subsection or own section) | a few, but limitations appear in most conclusions |
| last | Conclusion(s) | nearly all |

Other observations:
- A separate literature-review section is rare. One paper has "Related works" as Section 2, and one has a "Related work" subsection (1.1) inside the Introduction; all others review the literature inside the Introduction.
- A Nomenclature list appears in 6 of 20 papers; mostly in model-heavy papers.
- Median numbers: about 8–9 figures and 5–6 tables per paper.
- Lengths (words): abstract 86–260 (median about 190; limit 250); Introduction usually 1,000–2,500; Conclusion 140–1,250 (median about 340).
- Method-and-application papers often use the pattern **method section(s) → "Case study" section → results**. The case study names the industrial system and its data.

## 2. Abstract (5–11 sentences)

| Step | Content | Notes |
|---|---|---|
| A1 | Context and problem in one or two sentences | Often importance plus difficulty in one sentence ("X is critical for …, yet …"). |
| A2 | What this work does | "This work proposes / develops / estimates …" or "We propose …" (present tense). |
| A3 | How: components of the method and the data | Names the methods; gives data sizes (samples, trajectories, records). Past or present tense. |
| A4 | Main results with numbers | Metrics (RMSE, R², % improvement, NPV change, speed-up); 1–3 sentences. |
| A5 | Significance or use | "These results demonstrate …", "… provide quantitative guidance for …", or a final validation step. |

No citations except when the paper builds directly on a named earlier study (then author and year).

## 3. Introduction

### 3.1 Moves in order

| Move | Content | Observed |
|---|---|---|
| I1 Territory | Importance of the process, product or property: production scale, uses, cost, energy, safety | Opening move in about 17/20; two open with the method (ANN, kinetic models); one opens with a provocative claim about evaluation practice. |
| I2 Problem | Why modelling, prediction or control of this system is hard: coupled phenomena, unknown parameters, scarce or noisy data, delays, nonlinearity | Present in nearly all; often the second paragraph. |
| I3 Literature by approach family | Previous work grouped by type of method (first-principles → data-driven → hybrid; or "Regarding A … Regarding B …"), chronological within each group | Present in all; mostly author-prominent citations, one study per sentence ("Author et al. (year) developed …"), with what each did and found. |
| I4 Evaluation | Strengths and limits of each family, usually at the end of a group | Often a short sentence closing the group ("These studies established …, but …"). |
| I5 Gap | What is missing | See gap types in 3.2. Signalled with "However", "Despite", "To date", "few studies", "has received little attention". |
| I6 Present work | "In this work, we …", "Therefore, this article focuses on …", "To address these challenges, this paper proposes …", "Against this background, this study investigates …" | Present in all. |
| I7 Approach in steps | "First, … Second, … Third, … Finally, … is compared with …" | Common in method papers. |
| I8 Contributions | "The main contributions of this work are as follows: (1) … (2) …" (often 3–4 items, sometimes "threefold") | About half (10/20). |
| I9 Scope and validity | What the study does and does not claim: virtual plant vs real plant, observed operating range, validation data | In several of the industrial and data-driven papers. |
| I10 Roadmap | "The remainder of this paper is organized as follows. Section 2 …" | About half. |

### 3.2 Gap types used in this journal

| Type | Paraphrased pattern | Example paper |
|---|---|---|
| Focus mismatch | Most studies address A rather than B. | …431X, …4448, …4497 |
| Scale gap | Few studies apply this at industrial scale or with plant data. | …4436 |
| Combination gap | No approach yet handles A, B and C together / within one framework. | …4321, …431X |
| Integration gap | Combining X with workflow Y has received little attention. | …4448 |
| Enumerated limitations | Several limitations remain: first …, second …, third …, finally … | …4497 |
| Specific omission | Method M does not consider X. | EO-plant ANN paper |
| Novelty of scale | To our knowledge, not yet demonstrated on a problem of this size. | …3434 |

### 3.3 Citation practice
- Author–year style. Narrative citations dominate the literature part ("Author et al. (2023) found …"); parenthetical groups are used for background facts and for families of methods.
- Each reported study gets the method and the result, often with a number, in one sentence.
- The literature part is the longest move; the gap and present-work moves together are usually the last two or three paragraphs.

## 4. Methods / model sections

Observed conventions (from headings and openings):
- A description section first when the system is industrial: the process, the plant and its data (sampling, number of records, measured variables).
- Model sections ordered from the governing equations to closures, numerical solution and parameter estimation; algorithms written as numbered steps.
- Data-driven parts: data sources, preprocessing and splits, model architecture, training, hyperparameters, evaluation metrics (sometimes a separate "Evaluation metrics" section).
- Implementation details (software, solver, hardware) appear either at the end of the methods or as the first paragraph of the results.

## 5. Results and Discussion (combined)

### 5.1 Section level
- Opening: either a short orientation paragraph (what is evaluated, on which data, where the summary table is) or directly the first subsection. Some papers open with implementation details and computing times.
- Subsections follow the order of the method or of the questions in the Introduction (accuracy → extrapolation → application; or model → optimization → control).
- Final subsections, where present: computational performance, implications, limitations.

### 5.2 Subsection level

| Step | Content | Typical wording (paraphrased) |
|---|---|---|
| R1 Purpose or link | What this subsection tests, linked to the previous one | "We first assess …", "This section evaluates …", "Having established …, we now examine whether …", "Following …, … was further …", "Based on the above analysis, …" |
| R2 Setup | Data set, case or condition used | "To address this, the models are evaluated on …" |
| R3 Headline result | Main metric(s) with numbers | "Model X achieves an RMSE of …, a MAPE of … and an R² of …" |
| R4 Figure-led detail | Trends shown in figures and tables | "Fig. 5a presents …", "As shown in Fig. …", "Table 3 summarizes …" |
| R5 Comparison | With baselines, alternative models or the nominal case; occasionally with published values | "outperforms", "compared with", "lower than that of", "comparable to"; "in close agreement with the values reported by …" |
| R6 Explanation | Why the result occurs | "This is due to …", "can be attributed to …", "because …" |
| R7 Consequence | What the result means for the next step, for operation or for validity | "This establishes the basis for …", "These results indicate that …", "These patterns hold within the investigated data range and do not …" |

### 5.3 What the numbers say
In the six closely read papers:
- In five of them, 15–31 % of sentences refer to a figure or table: the discussion is built around figures. (The benchmarking paper, …4357, argues mostly in text.)
- Only 0–6 % of sentences contain a literature citation. Comparison is mostly **with baselines and alternatives inside the study**, not with other papers. Where literature appears, it is a benchmark value or a method justification.
- Up to about 20 % of sentences compare, and up to about 18 % hedge; explanations are explicit but short.
- Claims are bounded: several papers state that conclusions hold within the investigated range, data set or simulator.

## 6. Conclusion

| Step | Content |
|---|---|
| C1 | "This work developed / presented …" or "To address …, this study …" (one sentence restating the aim and method) |
| C2 | Method recap in 1–4 sentences (components, data) |
| C3 | Key results with numbers (often the same metrics as the abstract) |
| C4 | Significance: "These results demonstrate / highlight …"; sometimes a "first" claim |
| C5 | Limitations: "Nevertheless, several limitations remain …", "These results should be interpreted in light of …" (5 of 8 conclusions read) |
| C6 | Future work, specific |

Conclusions rarely cite literature and are usually written as continuous prose, sometimes with numbered findings.

## 7. Applying this to a manuscript

- Put the literature review in the Introduction and organize it by approach family (I3–I4); end with a gap of one of the types in 3.2, the present work, its steps and a numbered contributions list.
- If the method is applied to a real or industrial system, add a description section (process, plant, data) before the methodology and a "Case study" section, or a case-study subsection in the results.
- Use a combined Results and discussion with the R1–R7 pattern in every subsection (see `references/results-and-discussion-combined.md`); compare mainly with your own baselines and alternatives; use literature for validation data and benchmark values; state the range of validity; end with computational performance, implications and limitations where relevant.
- Conclusion: C1–C6, with the same key numbers as the abstract.
