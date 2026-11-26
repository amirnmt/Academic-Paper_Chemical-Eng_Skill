# Results: reporting, comparing and the language of findings

For modelling, simulation, optimization and data-driven papers, see also `results-discussion-writing.md` (paragraph frameworks, quantitative description, interpretation, validation, metrics, computational performance, ML and hybrid results, traceability).

The Results are the reason the paper exists: the new knowledge you contribute. The Introduction and Methods say why and how you obtained them; the Discussion says what they mean. The whole paper stands or falls on the Results, so they must be presented with complete clarity. The section is often short when the Methods and Discussion are well written.

Use with `paragraphs-and-sentences.md`, `figures-tables.md`, `vocabulary-by-section.md` §5 and `phrasebank.md` (Results).

## 1. Why write Results in words at all?

Figures and tables show the data. The text is needed because:
- some results matter more than others, and a graph cannot say which;
- results must be related to the aims of the study;
- some results need brief background to explain why they occurred;
- results must be compared with validation data, predictions or other studies;
- problems with some results must be explained;
- above all, the reader must know **your understanding** of the results. Results do not speak for themselves. If you write only "the effect occurred in 23 % of cases", the reader may consider 23 % low when you consider it high, and your conclusions will later look surprising or unjustified.

## 2. Section names and structure

- Names: Results; Results and Discussion; Data analysis; sometimes followed by a separate Discussion and/or Conclusion(s). Check the journal and recent papers in it.
- Two ingredients: (1) a brief overall description of what was done (the big picture, without repeating method details); (2) the data, selected and organized.
- Organization options: the same order and subheadings as the Methods (usual); chronological; or most important result first. Field conventions may fix the order.
- Every method gets a result, and the results follow the order (and subheadings) of the Methods.
- Present representative data, not every repetition. Selecting is part of the scientist's job.

## 3. How to start, what to include, how to end

**First sentence of the section or subsection:**
- the main finding: "All five correlations predicted the position of the hot spot within 0.1 m, but they differed strongly in its magnitude (Fig. 4)."
- or a short recall of the aim or analysis, followed at once by the main finding: "To assess the correlations under reacting conditions, the predicted and measured centreline temperatures were compared (Fig. 4). The predictions differed mainly in the magnitude of the hot spot."

Do not start with a method that was forgotten in the Methods section, and do not start with "The results are shown in Fig. 1".

**Components (a menu):**
1. Revisit the aim, existing research or methodology (briefly) and give a general overview of the results.
2. Invite the reader to look at a figure or table; present key results in detail (with short explanations where needed); compare with other studies or with model predictions.
3. Problems with the results (scatter, outliers, deviations, failed runs), stated honestly and in proportion.
4. Possible implications (late in the section, as the bridge to the Discussion).

**Moves in engineering results sections** (move analysis of five fields): restate the analysis or research question → state general findings → state specific findings (usually with a figure or table) → comment: interpret, compare with previous studies, evaluate. In chemical engineering papers, writers cycle frequently between a specific finding and its interpretation and compare with previous studies, which is why "Results and Discussion" is a common combined section.

**End of the section:** possible implications of the results ("These results suggest that …"), or a one-sentence summary that leads to the Discussion.

## 4. The results paragraph

1. (Optional) Recall the aim or the analysis in one clause.
2. State the main trend, with the figure or table in brackets.
3. Support with numbers: values, differences, percentage changes, uncertainty.
4. Describe secondary trends.
5. Note exceptions or anomalies.
6. Compare with validation data, model predictions or other studies, with a named metric.
7. (Combined Results and Discussion only) Give a short interpretation, then link to the next point.

Example (placeholders in brackets):
> All five correlations reproduced the position of the hot spot within [value] m, but they differed markedly in its magnitude (Fig. 4). The correlation of [Author] overpredicted the hot-spot temperature by [value] K, whereas that of [Author 2] underpredicted it by [value] K. Downstream of the hot spot (z > [value] m), all predictions agreed with the measurements within [value] K. The lowest overall error was obtained with [correlation] (RMSE = [value] K over [n] measurement points).

## 5. Citing figures and tables economically

- Make the finding the subject and put the figure in brackets: "The hot spot moved 0.3 m downstream as the coolant temperature decreased (Fig. 5)."
- Avoid empty openings such as "It is clearly shown in Fig. 5 that …", which put the figure, not the finding, in the focus.
- When the figure is the subject, choose a precise verb: Fig. 5 shows / compares / summarizes / plots / illustrates.
- "As can be seen **from** Fig. 5" = deduced from it; "**in** Fig. 5" = appears in it.
- Never repeat in the text what the figure or table already shows. Quote a key value from a figure only when its exact number matters.
- Integrate every figure and table into the narrative; do not rely on captions to carry the argument.

## 6. Objective and evaluative description

- Objective: higher, lower, increased, decreased, peaked at, remained constant, by 12 %, from 480 to 510 K.
- Evaluative: slightly, markedly, substantially, sharply, negligibly; good, satisfactory, poor; consistent, comparable.
- A purely objective description repeats what the figure shows; published results usually add an evaluative word to the objective one ("slightly lower", "considerably higher") and always give the number.
- "Higher than" is objective; "high" is an evaluation. Use evaluations deliberately.

## 7. Language of sequence, frequency, quantity and causality

**Sequence and time.** Readers who want to compare or repeat need order and timing, not only "then" and "next". Distinguish: before the run (beforehand, previously), start (initially, at t = 0), order (then, subsequently), short gap (soon after, within 5 min), long gap (later, eventually, after 300 days), simultaneous (while, as, at the same time; often implies a causal link), end (finally, at the end of), after the end (afterwards).

**Frequency.** How often a result occurred determines how reliable it is. From always to never: always / invariably → generally / usually → regularly / repeatedly → frequently / often → more often than not → as often as not (50 %) → sometimes → occasionally → rarely / seldom → hardly ever → never. Frequency words are judged against expectations; give counts where possible ("in 9 of 12 runs").

**Quantity.** Your words shape how readers perceive the same number: "in as many as 23 % of cases" vs "in only 23 % of cases". Five kinds of quantity words: make it look large (considerable, substantial, as many as), make it look small (only, barely, negligible), emphasize (by far, well above), close to a value (approximately, nearly, virtually), non-committal (some, relatively, to some extent). Always give the number as well.

**Causality.** Choose the strength you can support:
- strong (evidence of mechanism): causes, leads to, results in, is due to;
- partial: contributes to, is a factor in, influences;
- initial cause: originates in, stems from, is triggered by;
- weak (link, direction uncertain): is associated with, is related to, correlates with.
"X results in Y": X is the cause. "X results from Y": Y is the cause. "A cause of" = one of several; "the cause of" = the only one.

## 8. The strength of a claim: a ladder

The same finding can be stated at different strengths. Choose the rung your evidence supports:
1. "Wall heat transfer controls the hot-spot temperature." (present simple: established fact)
2. "Wall heat transfer controlled the hot-spot temperature in all runs." (past: true for this study)
3. "Wall heat transfer was the main factor affecting the hot-spot temperature." (partial cause)
4. "The hot-spot temperature was strongly correlated with the wall heat-transfer coefficient." (association)
5. "The results suggest that wall heat transfer may control the hot-spot temperature." (tentative)
6. "There is some evidence that, under certain conditions, wall heat transfer may contribute to …" (too weak; says almost nothing)

Present simple "unlocks" an interpretation from your study and presents it as general; past simple keeps it tied to your data. Do not stack hedges until the sentence says nothing.

## 9. Comparisons

- With validation data or models: name the metric and the data ("RMSE of 3.2 K against 120 thermocouple readings"; "mean absolute percentage error of 4 % on the test set").
- Use parity plots (predicted vs measured with a 1:1 line and error bands) and residual plots.
- Report where agreement is good and where it fails, and under which conditions.
- Data-driven models: report errors on the test set only, compare with a simple baseline, and state the forecast horizon.
- With other studies: "These values agree with [12] within 5 %"; "The predicted hot spot is 8 K higher than in [14], who assumed plug flow." Place the citation exactly where the other study's result is mentioned, so that readers do not attribute your result to them (or theirs to you).

## 10. Negative results and problems

- Report what you did not find; absence of evidence is not evidence of absence. Variables with no effect can be mentioned briefly without tables.
- Research is not invalidated by imperfect results, provided they are reported professionally:
  - state the problem precisely ("three of 120 points lie outside the ±10 % band");
  - give a likely reason ("probably because the thermocouple at z = 0.2 m was displaced");
  - say how it affects the conclusions ("excluding these points changes the RMSE by 0.2 K");
  - if relevant, say how it will be addressed.
- Avoid vague phrases that readers interpret as hiding weaknesses: "typical results are shown" (are only the best ones shown?), "agreement was reasonable" (how close?), "within experimental error" (what error?).

## 11. Numbers and statistics

- Statistical support: name the test, give the statistic, the degrees of freedom and the exact p-value where software provides it (or the journal's format).
- Statistics must be meaningful: percentages of very small samples mislead (for n < 20, give counts).
- No false precision: 17 of 59 is 29 %, not 28.8136 %. Means may carry at most one more digit than the raw data.
- Do not begin a sentence with a numeral; rephrase ("In total, 12 runs …") or spell it out.
- Use numerals with units (3 mL, 12 K); spell out small numbers without units if the journal style does; in a series containing a number of two or more digits, use numerals for all.
- Leading zero for values below 1 (0.25).
- SI units; consistent significant figures in text, tables and figures.
- Define derived quantities (conversion, selectivity, yield, space-time yield) once, in the Methods, and use them consistently.

## 12. Tense and voice

- Your findings: past simple ("The outlet temperature increased by 12 K").
- What a figure or table shows: present simple ("Figure 5 compares …").
- Results of calculations or statistics, and their meaning: present simple ("These values are significantly higher, indicating that …").
- Generalization you consider established: present simple, only when the evidence is strong.
- Active voice with "we" is acceptable for observations and decisions ("We observed …"); keep sentences short and direct.

## 13. Combined Results and Discussion

Allowed and common in engineering. In every paragraph, make clear what was measured or computed (the evidence) and what is inferred (the interpretation): present the finding first, then the comment. Keep comparisons with literature specific and cited. Do not let the interpretation hide the data. Structure, subsection pattern and paragraph templates: `results-and-discussion-combined.md`.

## 14. Supplementary material

Extra data, additional figures and repetitive tables can go into supplementary material if the journal allows. Refer to it precisely ("Fig. S3").

## 15. Checklist

- [ ] Same order and subheadings as Methods; every method has a result.
- [ ] Each subsection opens with the main finding.
- [ ] Every claim backed by a number, figure, table or statistic.
- [ ] Figures cited economically, with the finding as subject; nothing duplicated between text, tables and figures.
- [ ] Evaluative words paired with numbers and matching them.
- [ ] Causal verbs match the evidence; claim strength chosen deliberately.
- [ ] Comparisons use named metrics and named data; citations placed precisely.
- [ ] Negative results and anomalies reported in proportion, with reasons.
- [ ] No false precision; statistics complete; units SI.
- [ ] Measurement and interpretation clearly separated.
- [ ] The section ends with implications or a summary that leads into the Discussion.
