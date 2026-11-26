# How Computers & Chemical Engineering papers are built

A move analysis of 21 papers from the journal (2006–2026), made to model a manuscript on the journal's own conventions. Everything here is observed practice [J-obs] unless marked [J-req] (stated in the Guide for Authors, see `journal_requirements.md`); where the skill's citation rule [Rule] is stricter, the rule applies. All descriptions are paraphrased; papers are identified by the last digits of their PII (ScienceDirect identifier, S0098-1354(yy)xxxxx-x). Use this together with `journal_requirements.md`.

## 0. What was analysed

- 21 papers: 4 on ethylene and ethylene oxide plants (…0433, …2326, …3434 and an ANN model of an industrial EO plant, 2022) and 17 recent papers from 2026 on various topics. The review on kinetic Monte Carlo (…4187) was left out of the section analysis because reviews are organized differently, which leaves 20 research articles.
- Method: top-level and second-level headings of all 20 papers; sentence-by-sentence analysis of all 20 abstracts and Introductions up to the methods (citations counted per sentence and per part, §3) and of their Methodology parts (§4); subsection-level reading of the Results and Discussion of 6 papers on modelling and data-driven methods (…4321 hybrid GNN, …4448 data-augmented MPC, …4436 industrial propylene reactor model, …4357 robustness benchmarking of data-driven models, …4497 industrial soft sensing, and the EO-plant ANN paper); abstracts and conclusions of 8 papers; and phrase counts from `scripts/build_section_phrases.py`.
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

## 2. Abstract [J-req, J-obs]

Required [J-req, `journal_requirements.md`]: at most 250 words; purpose, procedure, main findings, principal conclusions; stand-alone; references avoided (author and year if essential).

Observed in 19 readable abstracts [J-obs]:

| Step | Content | Observed |
|---|---|---|
| A1 Context and problem | Importance of the process or task, often with its difficulty in the same sentence ("X is critical for …, yet …"); or a separate "However, existing …" sentence | Background first in 12; problem or pointed claim first in 2; problem stated explicitly in 12 |
| A2 What this work does | "This work / paper / study proposes …", "We propose / present …" | 18 of 19; 5 open with it (focused model) |
| A3 How | Components of the method and the data, 2–5 sentences; "Specifically, …" introduces the detail | All |
| A4 Main results | Metrics with numbers (R², RMSE, % change, NPV, time) and the baseline they are compared with | With numbers in 11 of 19 |
| A5 Significance | "These results demonstrate …", "… provide guidance for …", "Overall, …" | 13 of 19; the others end on a result or a limitation |
| (A6) Scope or limitation | One sentence or clause | 6 of 19, mostly 2026 papers |

Length median 184 words (157–244; 86–261), 9 sentences, about 26 words per sentence. Present tense dominates; three abstracts report what was done and found in the past tense. "We" in 6 of 20. Citations in 3 of 20, each to the earlier study the paper extends.

## 3. Introduction (up to the first methods section) [J-obs]

What was analysed: the abstract and the full Introduction of all 20 research articles, sentence by sentence, from a layout-aware extraction of the PDFs (front matter, nomenclature boxes and page furniture removed), up to the first methodology, model or problem-statement section; "Related work" parts placed before the methods were included. Citation counts are automatic and were spot-checked; the role of each sentence (opening, literature, gap, present work, roadmap) was assigned by rules and is approximate. Numbers: `citation_benchmarks.json`.

### 3.1 Moves in order

| Move | Content | Observed |
|---|---|---|
| I1 Territory | Importance of the process, product or property: production scale, uses, cost, energy, emissions, safety | Opening move in 17/20; two open with the importance of a class of methods; one with a pointed claim about evaluation practice |
| I2 Problem | Why modelling, prediction or control of this system is hard: coupled phenomena, unknown parameters, scarce or noisy data, delays, nonlinearity | Nearly all; often in the first paragraph, joined to I1 |
| I3 Literature by approach family | Previous work grouped by type of method, problem or line of work, ordered toward the authors' approach; chronological within a group | All; patterns in §3.3 |
| I4 Evaluation | Strength and limitation of each group, at the end of the group | Nearly all; often every paragraph ends with a "However, …" sentence |
| I5 Gap | What is missing | Types in §3.4 |
| I6 Present work | Linked back to the gap: "To address these limitations, …", "To this end, …", "Accordingly, …", "Against this background, …" | All |
| I7 Approach in steps | "First, … Second, … Finally, …" | Common in method papers |
| I8 Contributions | Numbered or "First/Second/Third" list of 2–5 items | 12/20 enumerate objectives or contributions; in papers with enumerated limitations, contributions answer them in order |
| I9 Scope and validity | Virtual vs real plant, operating range, what is outside the study | 6/20, all recent |
| I10 Roadmap | "The remainder of this paper is organized as follows. Section 2 …" | 11/20 |

Length: median 55 sentences (38–73), 9 paragraphs (7–13), 1,364 words (1,037–1,704). Three papers use subheadings inside the Introduction; one has a separate "Related works" section. A two-part paper (Part 2) refers to Part 1 for the literature review and has a short Introduction.

### 3.2 Citation density

| Measure (per paper) | Median | IQR | Range |
|---|---|---|---|
| Citation instances in the Introduction | 40.5 | 27–54 | 1–117 |
| Unique references cited | 36 | 25–43 | 1–59 |
| Share of sentences with at least one citation | 0.38 | 0.26–0.47 | 0.03–0.62 |
| Citations per sentence | 0.69 | 0.43–1.00 | 0.03–1.58 |
| Citations per cited sentence | 1.79 | 1.56–2.34 | 1.00–4.42 |
| Share of cited sentences with two or more sources | 0.49 | 0.32–0.60 | 0–1 |
| Largest number of sources after one sentence | 4.5 | 3–7.5 | 1–12 |
| Citations per paragraph (…4485 excluded: paragraphs not recoverable) | 2.7 | 1.8–6.1 | 0.1–12 |
| Citations per 100 words | 2.6 | 2.0–3.6 | 0.1–4.6 |
| Share of citations that are narrative | 0.02 | 0–0.29 | 0–1 |

By part of the Introduction (per-paper median share of sentences cited; pooled share and citations per sentence in brackets): opening 0.54 (0.53; 1.11), literature 0.44 (0.50; 0.98), gap 0.38 (0.41; 0.62), present work and contributions 0.04 (0.13; 0.23), roadmap 0. First paragraph: half of the sentences cited, 0.95 citations per sentence; first sentence cited in 6 of 20.

Sources per cited sentence (pooled, 824 citation instances): one 52 %, two 27 %, three 9 %, four 4 %, five 2 %, six or more 5 %. 69 % of cited sentences end with the citation; the rest place it after the clause it supports. Narrative ("Author et al. (year) …") citations: under 5 % of the citations in most papers, 18 % pooled, because a few papers write most of the review as a chain of named studies. Cited works were a median of 4 years older than the citing paper; 58 % at most 5 years old, 77 % at most 10.

Uncited sentences in the background and literature parts: about half of all such sentences. By a rough classification of 338 of them: general factual statements 69 %, evaluations or limitations 16 %, continuations of a study cited in the previous sentence 9 %, definitions 5 %, topic sentences whose sources follow 1 %. **This is where the skill's citation rule [Rule] is stricter than the journal's average practice**: cite the factual statements, attribute the limitations; the target densities are in `references/citation-practice.md` §6.

Spread: the most thoroughly cited Introductions (…3434, …4321, …4370, …4424, …4497) cite 53–62 % of all sentences and 0.9–1.6 citations per sentence; the least cited are a short methodological paper (…4473: 1 citation) and the Part 2 paper (…4217).

### 3.3 How the literature part is built

Patterns, each seen in several papers (most papers combine two or three); described in general form in `references/introduction.md` §6a:
- **Approach families**, one paragraph each, ordered toward the authors' approach (…3434, …4321, …4448, …4497).
- **Taxonomy sentence** with a citation group per class (…3434, …431X, …4321, …4382).
- **Limitation chain:** each paragraph ends with the same kind of limitation measured against the capability the paper adds; the gap paragraph numbers them (…4369, …4394).
- **Problem → remedy → residual limitation**, one paragraph per practical difficulty (…4412, …4448).
- **Lineage** within a family: early models → extensions → recent work (…4436, sgbs4).
- **Chain of named studies** in author-prominent sentences, then a synthesis sentence stating the trait they share (…4400, parts of …4370 and …4436).
- **The authors' earlier work** as the closest study, just before the gap (…431X, …4217, …4321, …4424).

Concepts are introduced with acronyms at first use (median 4 defined per Introduction), definition or appositive sentences with a citation, "hereafter referred to as", glosses in brackets ("i.e.", "e.g."), and, once, a definition quoted from a named source.

Limitations of earlier work are placed at the end of the description of each group, usually opened by "However", "Yet", "Although …" or "These methods … but …"; 42 % of limitation sentences carry a citation, against 52 % of other background and literature sentences.

### 3.4 Gap types used in this journal

| Type | Paraphrased pattern | Papers |
|---|---|---|
| Integration | No approach yet handles A, B and C together / within one framework; methods developed separately | 6 (…431X, …4321, …4369, …4382, …4412, …4497) |
| Assumption or representation | Existing models assume / represent … only as … | 5 (…4321, …4357, …4394, …4400, …4473) |
| Enumerated limitations | Several limitations remain: first …, second …, third … | 4 (…4321, …4369, …4394, …4497) |
| Scale or realism | Few studies at industrial scale or with plant data | 3 (…0433, …4436, …4485) |
| Focus mismatch | Most studies address A rather than B | …431X, …4448, …4497 |
| Novelty of scale | To our knowledge, not yet demonstrated on a problem of this size | …3434 |

Types overlap. About 40 % of gap sentences cite the closest or the few existing studies ("One of the few exceptions is …, which, however, only …"). The justification of the gap is usually one sentence on its consequence for prediction, operation or decisions.

### 3.5 From the gap to the aim and the contributions

- The aim sentence points back at the gap ("To address these gaps, this study develops …"; "These limitations motivate an integrated framework that …").
- Novelty is stated with "novel" (7 papers), with "to our knowledge", "the first study to …" or "not previously demonstrated" (4), with "the (key) novelty is …" (2); two recent papers calibrate it explicitly (the methods are standard; their use, or the measurement, is new).
- Several recent papers preview the main findings in the Introduction, with numbers.

### 3.6 Language of the Introduction

Per paper, medians: 27 words per sentence (16–35); "we/our" 0.9 per 1,000 words (0–6.7; first person is rare in about half of the papers); hedges (may, can, often, typically …) 7.5 per 1,000 words; present perfect in about one in eight background and literature sentences; past simple for individual studies (proposed, developed, used, indicated, showed, found). Paragraphs open mostly with a topic noun phrase (64 %), rarely with a connector (`references/paragraphs-and-sentences.md` §7a).

## 4. Methodology [J-req, J-obs]

Required [J-req, `journal_requirements.md`]: numbered sections and subsections (2.1, 2.1.1), cross-referenced by number; SI units; equations as editable text, numbered consecutively in the order cited, variables in italics, exp for powers of e, solidus for small fractions, simple formulas inline; appendices lettered A, B with equations (A.1), (B.1); supplementary files cited in the text with captions; research-data Option C (deposit the data or explain why not). The guide describes optional Theory and Calculation sections (theory extends the background of the Introduction; calculation develops it practically). It does not prescribe the content of the Methodology.

What was analysed [J-obs]: the Methodology part of all 20 research articles, from the end of the Introduction to the first results section (case-study sections that mainly report results were cut at their start; methodological text inside them was not analysed). Layout-aware extraction; equations counted by their numbers; citations, voice and tense counted per sentence; reading of the structure, the first sentence of every subsection, and samples of sentences on assumptions, model adoption, parameters, numerics, data, metrics and appendices. Details: `references/methodology-writing.md`; numbers: `citation_benchmarks.json` → `methods`.

### 4.1 Structure

| Structure | Papers |
|---|---|
| System or problem description → model → solution or estimation | …0433, …2326, …4217, …4436, …4473, sgbs4 |
| Overview (workflow figure or list of stages) → one subsection per module → evaluation metrics | …431X, …4321, …4357, …4370, …4400, …4412, …4448, …4497 |
| Problem statement → formulation (sets, objective, constraints by category) → solution strategy | …3434, …4369, …4382, …4424, …4485 |
| Problem statement → preliminaries (definitions, lemmas) → theorems with proofs and remarks | …4394 |

- Opening: a description of the system or problem in about 12 of 20; an overview of the stages, often with a workflow figure, in about 9.
- A separate "Evaluation metrics" section or subsection in several data-driven and hybrid papers; a "Computation and verification" subsection in one optimization paper; a section on assumptions inherited from earlier work in one.
- Subsections are linked by forward maps ("as described in the following subsections"), backward links in first sentences, and step numbers of the workflow figure.
- Main text vs elsewhere: 12 of 20 refer to an appendix or supplementary file for full parameter tables, per-component equations, algorithm listings, process-block details, datasets or networks, and implementation or verification details.

### 4.2 Size and density

| Measure (per paper) | Median | IQR | Range |
|---|---|---|---|
| Words | 2,676 | 2,118–3,714 | 555–6,619 |
| Sentences | 123 | 99–210 | 22–329 |
| Words per sentence | 20.9 | 19.8–22.7 | 12.5–33.3 |
| Subsections | 4 | 3–8 | 0–16 |
| Numbered equations | 15.5 | 4–22 | 0–75 |
| Equations per 1,000 words | 5.5 | 2.8–7.3 | 0–30.5 |
| "Eq. (n)" references in the text | 1 | 0–5 | 0–41 |
| Figures / tables first referred to here | 2 / 1 | 2–3 / 0–2 | 1–7 / 0–6 |
| Citation instances | 15.5 | 7–24 | 1–51 |
| Unique references | 9 | 6–15 | 1–35 |
| Share of sentences cited | 0.10 | 0.03–0.14 | 0.01–0.28 |
| Citations per sentence | 0.13 | 0.05–0.21 | 0.01–0.45 |
| Sentences with a passive verb | 0.46 | 0.42–0.57 | 0.16–0.66 |
| Sentences with present / past markers | 0.56 / 0.04 | 0.46–0.65 / 0.01–0.12 | – |

By type: first-principles and process simulation (…0433, …2326, …4217, …4436, …4473) about 1,100 words and 21 % of sentences cited, but equation counts from 0 (simulator-based) to 75 (…4436); optimization and control (…3434, …4369, …4382, …4394, …4424, …4485) about 4,100 words, 22 equations, 13 equation references, 7 % cited; data-driven (…4357, …4370, …4400, …4412, …4497, sgbs4) about 3,200 words, 9 equations, 3 % cited; hybrid (…431X, …4321, …4448) about 2,700 words, 17 equations, 11 % cited. Citation share by subsection type (pooled): system and case description 14 %, data-driven components 10 %, physical model 8 %, evaluation 7 %, numerics and solution 6 %.

### 4.3 Writing conventions observed

- **Physical model** (…4436 is the closest to a reactor-modelling paper): the reactor and reaction system in prose with a schematic; a bulleted list of model assumptions taken from the source model; a justification of the chosen variant against plant data; species and energy balances introduced with lead-ins that name their conditions; each closure (velocities, transfer coefficients, phase fractions) with its source in the lead-in; all symbols and parameter values with units in appendices.
- **Equations:** lead-ins mostly run into the display ("is defined as", "is calculated as", "as follows"); symbols defined in a following "where" clause (14 of 20 papers); equations referred to by number in 12; one control paper uses definitions, lemmas, theorems, proofs and remarks.
- **Assumptions:** stated in 17 of 20, either as a list at the start of the model or inline; justifications by plant documentation, by comparison with data, by purpose; one paper states that its simplifications may make the estimate optimistic.
- **Adopted vs new:** "adapted from [refs] … the original formulation is extended to …", "builds upon … and extends …", "the model proposed by … (hereafter …) is used", "we propose a … formulation, which we refer to as …".
- **Numerics and implementation:** software named in 11 of 20, versions in 3, solvers in 6, tolerances or stopping criteria in 5, discretization in 9, hardware or run time in about 9; no grid- or time-step-independence study (no paper solved a PDE reactor model).
- **Data-driven parts:** data provenance with sizes, periods and access restrictions; splits in 12; leakage control in 6 (fixed training length instead of early stopping, train–test overlap analysis, causal convolution); seeds or repetitions in 4–5; baselines defined in the Methodology with what each isolates; metrics defined with formulas in 12.
- **Language:** present tense for the model and framework, past for data collection and runs; passive in about half of the sentences; "we" rare except in a few papers.
- **Citations:** of 256 cited sentences, about 41 % support a fact or justification, 18 % parameters, properties or correlations, 14 % adopted models, 14 % datasets, 12 % named methods, 2 % software.

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

- Put the literature review in the Introduction and organize it by approach family (I3–I4, patterns in §3.3); end with a gap of one of the types in §3.4, the present work linked back to it, its steps and a numbered contributions list that answers the stated limitations; add a scope sentence.
- Cite every factual and literature-based sentence [Rule]; expect about 35–55 unique references in an Introduction of 1,200–1,800 words, and check the draft with `scripts/citation_density.py audit … --benchmarks citation_benchmarks.json`.
- If the method is applied to a real or industrial system, add a description section (process, plant, data) before the methodology and a "Case study" section, or a case-study subsection in the results.
- Methodology: choose the structure by the type of work (§4.1); describe the physical picture before the balances; list the assumptions with their sources and justifications; give every closure, parameter and dataset its origin; give more numerical detail (discretization, solver, tolerances, independence checks, versions) than the journal average; check with `citation_density.py audit … --section methods` and `references/methodology-writing.md` §15.
- Use a combined Results and discussion with the R1–R7 pattern in every subsection (see `references/results-and-discussion-combined.md`); compare mainly with your own baselines and alternatives; use literature for validation data and benchmark values; state the range of validity; end with computational performance, implications and limitations where relevant.
- Conclusion: C1–C6, with the same key numbers as the abstract.
