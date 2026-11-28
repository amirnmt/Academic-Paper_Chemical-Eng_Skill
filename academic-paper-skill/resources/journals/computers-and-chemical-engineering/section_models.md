# How Computers & Chemical Engineering papers are built

A move analysis of 21 papers from the journal (2006–2026), made to model a manuscript on the journal's own conventions. Everything here is observed practice [J-obs] unless marked [J-req] (stated in the Guide for Authors, see `journal_requirements.md`); where the skill's citation rule [Rule] is stricter, the rule applies. All descriptions are paraphrased; papers are identified by the last digits of their PII (ScienceDirect identifier, S0098-1354(yy)xxxxx-x). Use this together with `journal_requirements.md`.

## 0. What was analysed

- 21 papers: 4 on ethylene and ethylene oxide plants (…0433, …2326, …3434 and an ANN model of an industrial EO plant, 2022) and 17 recent papers from 2026 on various topics. The review on kinetic Monte Carlo (…4187) was left out of the section analysis because reviews are organized differently, which leaves 20 research articles.
- Method: top-level and second-level headings of all 20 papers; sentence-by-sentence analysis of all 20 abstracts and Introductions up to the methods (citations counted per sentence and per part, §3), of their Methodology parts (§4) and of their Results and Discussion parts (§5); subsection-level reading of the Results and Discussion of 6 papers on modelling and data-driven methods (…4321 hybrid GNN, …4448 data-augmented MPC, …4436 industrial propylene reactor model, …4357 robustness benchmarking of data-driven models, …4497 industrial soft sensing, and the EO-plant ANN paper); sentence-by-sentence coding of all 20 abstracts and all conclusions (19; the short communication …4473 has none) (§2, §6); titles and keywords of all 20 and the Highlights of 7 papers read from their article pages (§2a); all 181 figure and 138 table captions and every in-text reference to them (§8); all 418 numbered equations, with the equation pages of 13 papers read from the rendered PDF (§9); and phrase counts from `scripts/build_section_phrases.py`. Where the Markdown conversion lost or scrambled text (one abstract, captions of one paper, all equations), the PDF page itself was read.
- Counts below refer to these papers. With 20 papers they show conventions, not rules.
- The papers, for traceability (the review on kinetic Monte Carlo is not listed):

| ID | Topic | DOI |
|---|---|---|
| …0433 | EO plant security, dynamic simulation | 10.1016/j.compchemeng.2006.02.011 |
| …2326 | Shale gas to ethylene (OCM, MTO) | 10.1016/j.compchemeng.2017.05.023 |
| …3434 | Surrogate-based superstructure optimization, ethylene plant | 10.1016/j.compchemeng.2020.107015 |
| …sgbs4 | Superstructure ANN, industrial EO plant | 10.1016/j.compchemeng.2022.107850 |
| …4217 | Thermochemical storage in eco-industrial parks (Part 2) | 10.1016/j.compchemeng.2026.109969 |
| …431X | MBDoE-SINDy kinetic model discovery | 10.1016/j.compchemeng.2026.109979 |
| …4321 | Hybrid GNN for mixture viscosity | 10.1016/j.compchemeng.2026.109980 |
| …4357 | Robustness benchmarking of data-driven forecasts | 10.1016/j.compchemeng.2026.109983 |
| …4369 | Dynamic-aware scheduling of integrated energy systems | 10.1016/j.compchemeng.2026.109984 |
| …4370 | ML sorting of retired Li-ion cells | 10.1016/j.compchemeng.2026.109985 |
| …4382 | Reactive scheduling under disruptions | 10.1016/j.compchemeng.2026.109986 |
| …4394 | Fault-tolerant control with time delays | 10.1016/j.compchemeng.2026.109987 |
| …4400 | Per-burner fuel prediction, reheating furnace | 10.1016/j.compchemeng.2026.109988 |
| …4412 | Adaptive open-set fault diagnosis | 10.1016/j.compchemeng.2026.109989 |
| …4424 | Palm-oil supply chain LCA fronts | 10.1016/j.compchemeng.2026.109990 |
| …4436 | Industrial propylene reactor, parameter estimability | 10.1016/j.compchemeng.2026.109991 |
| …4448 | TimeGAN-augmented MPC of crystallization | 10.1016/j.compchemeng.2026.109992 |
| …4473 | Parameterized cryogenic refrigeration cost | 10.1016/j.compchemeng.2026.109995 |
| …4485 | National SAF supply chain MILP | 10.1016/j.compchemeng.2026.109996 |
| …4497 | Delay-aware soft sensing, copper smelting | 10.1016/j.compchemeng.2026.109997 |


## 1. Architecture of the paper

Typical order of top-level sections:

| Position | Section | How often |
|---|---|---|
| 1 | Introduction (with the literature review inside it) | 20/20 |
| 2 | Process, system or data description, or problem statement | about 7/20 |
| 2–3 | Methodology / Modelling framework / Mathematical model (often several sections) | 20/20 |
| (3) | Evaluation metrics as a separate section | occasionally |
| 3–5 | Case study (applies the method to a defined system) | 7/20 |
| 4–7 | Results and discussion (combined) | titled so in 11/20; "Results" in 2; case studies or experiments in 7; no separate top-level Discussion (§5.1) |
| (end of R&D) | Implications; Limitations (subsection or own section) | a few, but limitations appear in most conclusions |
| last | Conclusion(s) | nearly all |

Other observations:
- A separate literature-review section is rare. One paper has "Related works" as Section 2, and one has a "Related work" subsection (1.1) inside the Introduction; all others review the literature inside the Introduction.
- A Nomenclature list appears in 6 of 20 papers; mostly in model-heavy papers.
- Median numbers: 8.5 figures (2–16) and 5.5 tables (0–16) per paper, about 0.9 figures and tables per page; 18 numbered equations (0–80) (§8, §9).
- Lengths (words): abstract 86–260 (median about 190; limit 250); Introduction usually 1,000–2,500; Conclusion 140–1,000 (median about 330).
- Method-and-application papers often use the pattern **method section(s) → "Case study" section → results**. The case study names the industrial system and its data.

## 2. Abstract [J-req, J-obs]

Required [J-req, `journal_requirements.md`]: at most 250 words; purpose, procedure, main findings, principal conclusions; stand-alone; references avoided (author and year if essential).

Observed in all 20 research abstracts [J-obs] (one abstract, scrambled in the conversion, was read from the PDF page):

| Step | Content | Observed (n = 20) |
|---|---|---|
| A1 Context | Importance of the process, property or task, often in the same sentence as its difficulty ("X is critical for …, yet …") | First sentence in 13; 2 open with a pointed claim or finding (…4357, …4424); 5 open directly with A3 |
| A2 Problem or gap | "However, existing …", "Existing … are tied to …", "…, but is often hindered by …" | Explicit in 11 |
| A3 This work | "This work proposes / presents / estimates", "This paper proposes / measures", "This study investigates", "We propose / present"; once "The aim of this work is …" | 19 of 20; …4400 describes its method without such a sentence |
| A4 How | Components of the method and the data, 1–5 sentences; "Specifically, …" introduces the detail (2) | All |
| A5 Validation or application | "validated on …", "applied to …", "Simulation results … verify …" | 7 |
| A6 Results | Metric values with the baseline they are compared with | Numerical metrics in 10; only data sizes or scenario levels in 2; qualitative only in 8 ("outperforms", "reasonable") |
| A7 Scope or limitation | One sentence or clause on what was not covered or what the method requires (e.g. interactions only partly explored; a simulator needed) | 6 |
| A8 Final sentence | Significance or contribution ("These findings provide …", "Overall, …", "In summary, …") in 11; a result in 7; a recommendation (1); a scope statement (1) | |

- **Length:** median 184 words (86 to about 250); median 8–9 sentences (3–13).
- **Numbers:** papers that report a comparison with a baseline name the baseline in the abstract (9 of 20). The strongest abstracts give the metric, its value, the baseline and the condition in one sentence (…3434, …4369, …4400).
- **Voice and tense:** present tense for what the work does and what the results show; past tense in 4 abstracts that narrate the steps (…4485, …4497). "We" in 6.
- **Citations:** 2 of 20, each to the study the paper builds on or contrasts with; one abstract quotes an external statistic with its source named in the sentence.
- **Abbreviations:** defined at first use inside the abstract (full term, then the abbreviation in brackets).

## 2a. Title and keywords [J-req, J-obs]

**Titles** (n = 20): median 13 words (10–17). Mostly a noun phrase naming the method and the system ("A … framework for …", "… of an industrial … reactor"); 8 contain "framework" or "protocol"; 5 use a colon (name or topic before it, description after it); one is a full statement of the finding (…4424). Ten name the concrete industrial system or material (ethylene oxide plant, propylene polymerization reactor, reheating furnace, copper smelting).

**Keywords** (n = 20, 104 keywords): median 5 (2–7) [J-req: 1–7]. 41 of 104 only repeat title words, 23 overlap partly, 40 add terms that are not in the title. Typical mix per paper: one or two method terms (e.g. "Parameter estimation", "Model predictive control"), the system or process ("Industrial polymerization reactor", "Reheating furnace") and one application or task term ("Process monitoring"). Capitalization varies (sentence case in 18, lower case in 2).

**Highlights** [J-req]: required, 3–5 bullets of at most 85 characters each, published on the article web page (not in the PDF).

Observed [J-obs] in 7 published papers (29 bullets, read from the article pages; the 2006 paper has none) and one submitted pre-proof:

| Feature | Observed |
|---|---|
| Number of bullets | 3–5 (median 4) |
| Length | median 77 characters (48–215); 9 of 29 over 85, in 3 papers (one older paper has every bullet at 118–215) |
| Content | what was done 18; findings 6 (in 3 papers: …431X, …4321, …4217); background 3 (one 2017 paper); scope or what is discussed 2; novelty wording 2 |
| Numbers | none in any bullet |
| Form | full sentences 19 (about half passive: "… is proposed", "… are identified"); noun phrases 6; past-tense verb without subject 4 ("Developed …", "Incorporated …"); one form per paper |
| Order | method first, then findings; a review lists what is reviewed, organized and identified |
| Pre-proof as submitted (…4412) | 4 bullets, each a bold label plus a 250–340-character sentence: far over the limit |

What this means: the journal's highlights are usually short method statements without numbers. A highlight list that stays within 85 characters and states two or three results with numbers and conditions is both compliant and more informative than the average.

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

### 3.7 Review articles (one in the sample)
…4187 (a review) states the gap of a review as the way earlier reviews are organised (by application, by implementation class, by framework) and names its intended reader ("a practical entry point"). Its outline paragraph says what each section contributes rather than listing section numbers. Use this only for a review; a research article needs a research gap (§3.4).

### 3.8 Instruction study (v2.11)
All 21 Introductions were coded against the skill's instructions (introduction.md B1–B10). Confirmed: funnel 18/21, explicit objective 20/21, contributions explicit in 12/21, outline paragraph in 12/21. Below the skill's standard in many papers: generic first sentence in 7/21 ("With the rapid advancement of …"), author-by-author literature passages in 10/21, uncited factual sentences in 8/21. The best Introductions (…4424, …3434) open on a cited number, classify prior work by how it treats one key choice, and state what is standard and what is new.

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

## 5. Results and Discussion [J-obs]

Not prescribed by the guide [J-req: none beyond figures, tables, equations and data rules]. What was analysed: the Results and Discussion part of all 20 research articles, from the first results section to the Conclusion (case-study and experiment sections included; their set-up paragraphs were read but not counted as findings). Layout-aware extraction with page numbers; every sentence coded for numbers, explanation, comparison, hedging, limitation, implication, figure/table/equation references and citations; reading of structure, subsection openings and samples of each kind of sentence. Guidance distilled from it: `references/results-discussion-writing.md`; numbers: `citation_benchmarks.json` → `results_discussion`.

### 5.1 Section level

- **Titles:** "Results and discussion" in 11 of 20; "Results" in 2; case studies or experiments in 7. No paper has a separate top-level Discussion; some end with synthesis subsections: a discussion of the results together (…431X 4.3, …4424 7.8), positioning against prior work (…4400 3.8, with a comparison table), generality (…4400 3.9), implications (…4357 3.5), limitations (…4357 3.6; …4424 Section 8).
- **Opening:** orientation (what is evaluated, on which data, how reported: …4321, …4370), implementation details (software, solver, hardware, time step: …4436), the scenario and its data (…4369, …4382), the headline result (…4400), or an organizing claim (…4357).
- **Order:** credibility first, then analysis, then use: validation or accuracy → behaviour, sensitivity, interpretation → optimization, control, scenarios, decisions → computational performance → positioning and limitations (…4436, …4321, …4448, …4497, …3434).
- **Subsections:** median 3.5 (0–16); several papers state the finding in the subsection title (…4400 phrases each results subsection as a short claim, e.g. that individual slab inputs beat zone averages at equal inputs, or that a lag of about an hour connects slab load and burner fuel).

### 5.2 Subsection level

The R1–R7 pattern holds across the sample (purpose or link → set-up → headline result with numbers → figure-led detail → comparison → explanation → consequence or bound); typical wording and paragraph frameworks are in `references/results-and-discussion-combined.md` §3 and `references/results-discussion-writing.md` §2. Openers: "To further evaluate …", "To assess …", "Having established …, we now examine whether …", "Based on the above analysis, …", "As shown in Fig. …", "Table … summarizes …".

### 5.3 What the numbers say

| Measure (per paper) | Median | IQR | Range |
|---|---|---|---|
| Words | 2,865 | 2,065–3,984 | 379–6,617 |
| Sentences | 140 | 90–184 | 16–279 |
| Words per sentence | 22.2 | 20.2–24.3 | 16.7–31.6 |
| Figures / tables referred to | 4.5 / 4 | 3.8–9.3 / 2–7.5 | 0–14 / 0–12 |
| Sentences referring to a figure or table | 0.12 | 0.09–0.19 | 0.03–0.28 |
| Sentences referring to an equation | 0 | 0–0.01 | 0–0.02 |
| Citation instances / groups / unique references | 8.5 / 6.5 / 5 | 2–18 / 2–12 / 1–8 | 0–55 / 0–55 / 0–17 |
| Sentences with a citation | 0.045 | 0.02–0.09 | 0–0.16 |
| Sentences comparing with published results | 0.011 | 0–0.024 | 0–0.06 (in 12 of 20 papers) |
| Sentences with a number | 0.35 | 0.30–0.41 | 0.16–0.60 |
| Sentences with an explanation marker | 0.18 | 0.14–0.22 | 0.09–0.25 |
| Sentences comparing within the study | 0.26 | 0.19–0.29 | 0.11–0.39 |
| Sentences with a hedge | 0.06 | 0.04–0.08 | 0.01–0.12 |
| Sentences with a limitation or scope | 0.03 | 0.02–0.05 | 0–0.10 |
| Sentences with an implication | 0.05 | 0.03–0.07 | 0–0.18 |
| Sentences with present / past markers / passive | 0.53 / 0.29 / 0.36 | – | – |

By type (medians): physics-based papers cite most (8 % of sentences); data-driven papers refer to figures most (10 %) and cite least (2 %); hybrid papers hedge most (12 %) and state limitations most (6 %); optimization papers quantify most (38 % of sentences with a number).

### 5.4 Practices observed

- **Validation:** training, testing and a fully independent campaign reported separately, against an unestimated nominal model, with Pearson, MSE and relative bias, and the choice of metrics justified (…4436 p12–13); held-out test sets with ensemble predictions (…4321); unseen cells (…4370).
- **Benchmarking:** baselines with the same inputs, data split and metric (…4400); state-of-the-art methods re-run on public benchmark datasets (…4412); comparisons with three published controllers (…4394); ablations removing one component at a time (…4394, …4400, …4412).
- **Variability and statistics:** seeds (…4400 four, …4357 three to five), Monte Carlo runs with different random seeds (…4394, 50 runs), paired bootstrap intervals (…4357). "Significant(ly)" appears in 62 sentences in 15 papers, almost always without a test.
- **Computational performance:** problem size, CPU time per iteration and hardware (…3434); runtime by module with bottlenecks, and the explicit statement that two cases do not establish a scaling law (…431X); a time index relative to the scheduling period (…4369); fewer optimization variables by move blocking (…4448).
- **Physical interpretation:** temperature zones from the rate constants of desired and combustion reactions (…0433 p7); mechanism chains for trade-offs (…4448 p9); patterns attributed to the process because they appear also in the nominal model (…4436 p12); results explained by the structure of the model, with the limit stated (…4424 p11).
- **Literature comparison:** published ranges and values (…3434 p11–14: production cost within 1 %, energy against a range, a different optimum attributed to a different problem definition), earlier dataset results with different partitions noted (…4321 p6), parameter values consistent with published kinetic studies (…4436 p15); a positioning table (…4400 Table 6).
- **Unexpected results and limits:** physically paradoxical measurements flagged (…4321 p6); augmented data worse than real data (…4448 p7); observational association not read as causal (…4400 p14); conclusions conditional on simulators and choices (…4357 p8); what a small effect does not show (…4424 p15); confidential units handled by standardized outputs and relative bias (…4436 p11–13).

## 6. Conclusion [J-obs]

All 19 conclusions were coded sentence by sentence (the short communication …4473 has none; the review …4187 is excluded). Heading: "Conclusions" in 11, "Conclusion" in 8; never combined with "Outlook" or "Future work".

**Size:** median about 330 words (140–1,000), median 3 paragraphs (1–9). Five are long (760–1,000 words) and work through the findings one by one; five are short (140–240 words), a single paragraph or a few one-sentence paragraphs.

| Step | Content | Observed (n = 19) |
|---|---|---|
| C1 Restatement | What the work did, in one sentence: "This work presented / developed …", "We present …", "This paper proposes …"; or the aim: "To address …, this study …", "We set out to …" | First sentence in 16; 2 open with the problem context (older papers), 1 with the main finding stated as a general claim (…4424) |
| C2 Method recap | Components and data, 1–4 sentences | 15 |
| C3 Link back to the Introduction | The objectives or challenges stated in the Introduction, named again and answered one by one | 5 |
| C4 Findings | Main results; with the same metrics as the abstract | Numerical in 11; qualitative only in 8 |
| C5 Comparison | Against the baseline or the alternative technology | 11 |
| C6 Explanation or condition | Why a result holds, or under which conditions ("under the tested conditions", "within the examined …") | 9 |
| C7 Significance | "These results demonstrate …", "This study offers …", "… provides a promising foundation for …"; practical implication for operators or designers | 16 |
| C8 Novelty claim | "To the best of our knowledge, this is the first …", "Its main novelty lies in …" | 5 |
| C9 Limitations | Explicit, introduced by a signal sentence ("Nevertheless, several limitations remain …" and similar) and then listed | Explicit in 8; a scope or validity condition only in 4; none in 7 |
| C10 Future work | Specific: names the extension, data or validation still needed ("validation on real industrial data", "a multi-plant study") | Specific in 12; vague in 1; none in 6 |

Further observations:
- **Order:** C1 → C2 → C4/C5 → C7, then C9 → C10 at the end. Limitations usually come in the last or second-to-last paragraph and lead into the future work in the same paragraph; one paper places its main limitation first, as a frame for reading the findings (…4217).
- **Enumeration:** findings are listed with numbers in 1 conclusion ((1), (2), (3) after an introductory "… shows that:"), counted in the prose in 3 (a sentence announcing the number of conclusions, then "First, … Second, …"), and written as continuous prose in the rest.
- **Numbers:** the most informative conclusions repeat the key metric values with their baseline and condition (…4321, …4400, …4497); qualitative conclusions use "outperforms", "effective", "reasonable".
- **Citations:** 2 of 19 cite literature (one to an industrial demonstration, one to the published example used for comparison); 2 refer to their own sections.
- **Tense:** restatement in the past ("presented", "developed") in 8 and in the present ("proposes", "focuses") in 9; findings in the present or past.
- **Strength of claims:** most significance sentences are bounded by the tested system or data; three make unbounded claims (that the method is proven or powerful in general), and one ends with an instruction to the reader.
- **Data or validation limits stated as limitations:** simulation-only validation, a single plant, benchmark datasets only, no industrial experiment.

**Bulleted conclusions** (variant): …4217 writes its Conclusion as 37 short items (1,256 words) and …4448 in 14 short paragraphs. This works for multi-case studies but turns easily into a list of results (…4217 repeats about 23 numbers). The prose model above (about 330 words, 3 paragraphs) is the safer default.

**Limitations and future work by date:** the four older EO papers (2006–2022) have neither in the Conclusion; most 2026 papers have both. Follow the recent practice.

## 7. Applying this to a manuscript

- Put the literature review in the Introduction and organize it by approach family (I3–I4, patterns in §3.3); end with a gap of one of the types in §3.4, the present work linked back to it, its steps and a numbered contributions list that answers the stated limitations; add a scope sentence.
- Cite every factual and literature-based sentence [Rule]; expect about 35–55 unique references in an Introduction of 1,200–1,800 words, and check the draft with `scripts/citation_density.py audit … --benchmarks citation_benchmarks.json`.
- If the method is applied to a real or industrial system, add a description section (process, plant, data) before the methodology and a "Case study" section, or a case-study subsection in the results.
- Methodology: choose the structure by the type of work (§4.1); describe the physical picture before the balances; list the assumptions with their sources and justifications; give every closure, parameter and dataset its origin; give more numerical detail (discretization, solver, tolerances, independence checks, versions) than the journal average; check with `citation_density.py audit … --section methods` and `references/methodology-writing.md` §15.
- Use a combined Results and discussion with the R1–R7 pattern in every subsection (see `references/results-and-discussion-combined.md` and `references/results-discussion-writing.md`): validation before use, then analysis, then application; compare with your own baselines under equal conditions and, for a reactor model, with published data and models wherever they exist; report variability; label each interpretation by its evidence; end with computational performance, positioning against prior work, implications and limitations; check with `citation_density.py audit … --section results`.
- Conclusion: C1–C10 (§6): restate, recap, link back to the stated objectives, give the key numbers with their baseline (the same as the abstract), significance bounded by the tested system, explicit limitations and specific future work.
- Title, keywords, highlights: §2a. Highlights within 85 characters, with numbers for the results. Figures and tables: §8. Equations: §9.

## 8. Figures and tables [J-obs]

All captions (181 figures, 138 tables) and all in-text references of the 20 papers. The captions of one older paper, split in the conversion, were taken from the PDF text.

**Number and size**
- Figures: median 8.5 per paper (2–16); tables: median 5.5 (0–16); together about 0.9 per page. Modelling and optimization papers have more tables (parameters, results); data-driven papers more figures.
- In two-column papers, 81 of 171 figure captions span both columns (full-width figures), 90 sit in one column.

**What the figures show** (keywords in the caption; one figure can match more than one type)

| Type | Share of figures |
|---|---|
| Scheme of the method, framework, flowsheet, superstructure or process | 29 % |
| Predicted versus measured, comparison with a baseline, validation | 28 % |
| Profiles, trajectories, time series, dynamic responses | 14 % |
| Distributions, errors, uncertainty, residuals | 13 % |
| Sensitivity, importance, ablation (Sobol, SHAP, effect of a parameter) | 12 % |
| Optimal solutions, Pareto fronts, costs | 10 % |
| Maps | 2 % |

Nearly every paper has one framework or process scheme early (Fig. 1 or 2) and its first results figure is a comparison with data or a baseline.

**What the tables show:** parameters, properties, data and inputs (46 %); results, performance and comparisons (39 %); method settings, hyperparameters, reaction mechanisms (9 %). Tables of literature values state the source in the caption or in a footnote ("Source: Adapted from …", reference footnotes per column).

**Captions**
- Figure captions: median 14 words (quartiles 8–42; up to 163). About a third are several sentences long: a title-like first phrase, then what is plotted, the conditions (often with numbers) and the meaning of panels, lines or colours. 36 label panels ((a), (b)). Short captions are noun phrases: "Flow diagram of …", "Comparison of …", "Effect of … on …", "Evolution of …".
- Table captions: median 10 words (7–15), a noun phrase above the table: "Parameters of …", "Summary of …", "Comparison of …", "Results of …"; explanations go into table footnotes.
- Elsevier layout: "Fig. 1." in bold with a full stop, "Table 1" on its own line above the caption. Author manuscripts use "Figure 1:" (accepted-manuscript versions of two papers).

**References in the text**
- Every paper writes "Fig." in the running text (335 times against 16 for "Figure"); tables as "Table 1".
- Most references are part of the sentence, not in parentheses: only 15 % of figure references and 9 % of table references are parenthetical.
- Sentences that begin with the figure use present-tense verbs: shows (32, in 13 papers), presents (16), illustrates (7), compares, summarizes, lists, depicts, reports. "As shown in Fig. …" opens a sentence 24 times; "shown in Fig./Table" appears 103 times, "presented in" 18, "given in" and "summarized in" 10–12.
- Each figure and table is mentioned in the text; in 260 of 279 checked cases the first mention is on the same page as the caption or before it.

## 9. Equations [J-obs]

All 418 numbered equations of the 20 papers were located in the PDFs (equation numbers at the right margin); the lead-in and follow-up of the equations on one equation-heavy page of 13 papers were read from the rendered page, because the Markdown conversion does not preserve equations.

**Amount:** median 18 numbered equations per paper (0–80). Two papers (process simulation, ML sorting) have none; model-heavy papers 50–80 (MILP formulations, reactor balances, control proofs). Two papers continue in an appendix with "(A.1)".

**Numbering and references:** consecutive "(1)", "(2)" for the whole paper, right-aligned; reactions can be numbered like equations (…0433) or collected in a table with their source (…4436). In the text: "Eq. (5)" in 13 papers, "Eqs. (1)–(2)" for ranges; a bare "(5)" in 2; "Equation (5)" at the start of a sentence. Supplementary equations as "Eq. (S1)".

**Before the equation (lead-in)**
- Most often a sentence naming the quantity, the phase or unit, and the principle, ending in a colon: "The mass balance of species i in the [phase] is [defined / derived] as:", "The [cost term] is calculated as:", "… are expressed as follows:".
- The source of an adopted equation is cited in the lead-in sentence, before the colon.
- A forward reference by number is also common: a sentence such as "… is given by Eq. (1)." or "Eq. (4) expresses …", with the equation displayed after it.
- Some authors let the sentence run into the equation without a colon ("… the score is", then the equation, then "where …"); one uses imperatives ("Write …", "compute").

**After the equation**
- A "where" clause defining every new symbol in one sentence, separated by commas or semicolons, often with "respectively" at the end; units or values are added in the clause when they matter (a time step and its value in this study; parameter values with their source). 14 of the 18 papers with equations use it.
- Alternatives: a separate sentence after a group of equations that defines their variables, "in which …", or a pointer to the nomenclature or an appendix table that lists all variables with units and values.
- The best-written model sections add one or two sentences on what the term or the equation does physically and why it has this form (sign conventions, which term carries the coupling, what is assumed).

**Typesetting conventions seen**
- Equations treated as part of the sentence (comma or full stop at the end) in about 5 of 13 papers read; the others leave equations unpunctuated. Either is accepted; be consistent.
- Long equations broken before an operator, with the operator at the start of the continuation line; one number for the whole block.
- Optimization models: domain of each constraint written after it ("∀r, t", "∀i ∈ I"); sets defined in the text or in a display; upper and lower bounds marked with overline and underline.
- Vectors and matrices in bold (data-driven and control papers); descriptive subscripts upright in the better-typeset papers, italic in others; multi-letter variable names (NPV, CCTotal) occur but are hard to read.
- Units are given in the where-clause, the nomenclature or a parameter table, not inside the equation; an empirical correlation with numeric coefficients states the units of its variables in the text.
- Nomenclature or abbreviation list: 6 of 20 papers, mostly model-heavy ones.
- Algorithms as numbered pseudocode boxes ("Algorithm 1", with Input/Output lines) in data-driven papers.

