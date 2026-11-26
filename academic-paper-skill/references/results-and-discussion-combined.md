# Combined Results and Discussion

Many engineering journals, and most computational ones, use one section, "Results and discussion", instead of separate Results and Discussion sections. This file describes how that section is built. It is based on an analysis of 20 research articles in *Computers & Chemical Engineering* (2006–2026) and of 90 papers on reactor modelling and surrogate models, in which about half of the papers used a combined section and a separate Discussion was rare. For reporting language see `results-language.md`; for explanation, hedging and limitations see `discussion-hedging.md`; for the full pattern-by-pattern guide (paragraph frameworks for validation, physical interpretation, numerical performance, sensitivity, ML, literature comparison, unexpected results, limitations and implications; evidence types; certainty ladder; traceability matrix; journal benchmarks) see `results-discussion-writing.md`.

## 1. When to combine

Combine when:
- the target journal's recent papers do (check 10–20 of them);
- each result needs an explanation before the next result makes sense (method papers, case studies, sequential analyses);
- the comparison is mainly with your own baselines and alternatives.

Keep separate sections when the journal expects them, or when the interpretation draws on many results together (a synthesis that would be repeated in every subsection).

## 2. Section level

- **Opening (optional, 2–5 sentences).** What is evaluated, on which data, and where the summary is ("Table 4 summarizes the accuracy of all models on the test set"). Some papers put implementation details here: software, solver, hardware, computing times.
- **Subsections in a logical order.** Follow the order of the methods or of the questions stated in the Introduction. Common orders:
  - validation → accuracy → extrapolation → application;
  - model → sensitivity → optimization → control;
  - nominal case → variations → robustness.
- **Closing subsections.** Computational performance (speed-up, scaling); implications for design or operation; limitations. A limitations subsection at the end of the section is common in this genre; the Conclusion then refers to it briefly.
- **No separate synthesis section needed**, but the Conclusion must then gather the main findings.

## 3. Subsection level: the R1–R7 pattern

| Step | Function | How it is usually written |
|---|---|---|
| R1 | Purpose or link: what this subsection tests and why now | "We first assess …"; "This section evaluates whether …"; "Having established …, we now examine …"; "Building on these results, …" |
| R2 | Setup: data set, case, condition | "To test this, the models were evaluated on …"; "The case considers …" |
| R3 | Headline result with numbers | "Model A reached an RMSE of … K and R² of … on the test set." |
| R4 | Figure-led detail | "Fig. 6a shows …"; "As Table 3 shows, …"; one sentence per point the reader must see. |
| R5 | Comparison | With baselines, alternative models, the nominal case, the first-principles model; occasionally with published values ("… agrees within … % with the value reported by …"). |
| R6 | Explanation | "This is because …"; "The deviation can be attributed to …"; one mechanism, stated with the evidence for it. |
| R7 | Consequence or bound | What it means for the next step, for operation or for validity: "This allows …"; "These results hold within the sampled operating range." |

Not every subsection needs all seven steps, but R1, R3 and R7 are almost always present. Put R3 early: readers look for the number first.

## 4. What distinguishes this genre

- **Figures carry the argument.** In the 20 papers analysed, a median of 12 % of sentences in this section refer to a figure or table (IQR 9–19 %, up to 28 %), and nearly every paper opens some subsections with a figure. Write the sentence about what the figure shows, then the sentence about what it means.
- **Comparison is mostly internal.** Literature citations are rare in the section (median 4.5 % of sentences; comparisons with published results in about 1 %, in 12 of 20 papers). Comparisons are with baselines, ablations, alternative methods and the nominal case. Literature appears for benchmark values, for validation data and to justify a method choice. If your field expects comparison with published results, put it in the validation subsection and in a dedicated comparison table.
- **Bounded claims.** Strong papers state the range of validity in the text: the data set, operating range, simulator or test conditions under which a conclusion holds.
- **Explanations are short and specific.** One mechanism per result, linked to physics or to the model structure; alternatives mentioned when plausible.
- **Numbers are repeated where they matter.** The headline metrics appear in the subsection, in the summary table, in the abstract and in the Conclusion: keep them identical.

## 5. Paragraph templates

Validation against data:
> R1 Purpose (which data, why they test the model) → R3 agreement metric (error, bias, maximum deviation) → R4 where it agrees and where not (figure) → R6 cause of the largest deviations → R7 conclusion on fitness for purpose and the range of validity.

Comparison of models or methods:
> R1 question → R2 common test conditions (same data, split, metric) → R3 ranking with numbers (table) → R5 differences and their size → R6 why the best model wins (structure, inductive bias, data) → R7 recommendation and its limits.

Sensitivity or interpretability analysis:
> R1 purpose → R3 dominant inputs with indices → R4 time or range dependence (figure) → R5 agreement between methods (e.g. variance-based indices vs. feature attributions) → R6 physical explanation → R7 what this implies for operation or for model reduction.

Case study or scenario:
> R1 scenario and why it matters in practice → R2 conditions → R3 effect on the key outputs with numbers → R4 profiles or trajectories → R6 mechanism → R7 trade-off and practical consequence.

Optimization:
> R1 objective and constraints → R3 optimum vs. nominal with numbers → R4 decision variables at the optimum (which hit bounds) → R5 agreement between solvers or with a check simulation → R6 why the optimum lies there → R7 practical meaning and caveats (constraints not modelled, verification needed).

Computational performance:
> R1 why speed matters for the intended use → R3 cost per evaluation and speed-up → R5 against the full model and alternatives → R7 what becomes feasible (real-time use, many-query tasks).

Limitations (end of section):
> one paragraph per limitation: what is not covered → likely effect and its direction → how it could be addressed.

## 6. Language

- Results (what was found): past tense or present tense for what a figure shows ("Fig. 4 shows …"; "the error decreased …").
- Explanations and general statements: present tense ("This is because the pellet temperature lags …").
- Compare with "than", "compared with", "lower than that of", "comparable to", "agrees within"; avoid "significantly" without a test.
- Hedge only the inference, not the measured or computed number (see `discussion-hedging.md`).
- Signal the move from result to interpretation explicitly: "These results indicate that …", "This suggests …", "This means that …".

## 7. Checklist

- [ ] Subsections follow the order of the methods or the research questions.
- [ ] Each subsection opens with its purpose and gives its headline number early.
- [ ] Each figure and table is introduced, described once and interpreted.
- [ ] Comparisons use the same data, splits and metrics; baselines are named.
- [ ] Each important result has an explanation, and the explanation is supported.
- [ ] Validity range stated for the main claims.
- [ ] Literature comparison present where published values exist (validation, benchmarks).
- [ ] Computational performance reported if speed is part of the contribution.
- [ ] Limitations stated (here or in the Conclusion) with likely effects.
- [ ] Numbers identical to those in the abstract, tables and Conclusion.
