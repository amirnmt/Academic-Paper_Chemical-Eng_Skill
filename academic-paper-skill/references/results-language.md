# Results: reporting, comparing and the language of findings

The Results are the reason the paper exists. They must be new, clearly organized, supported by evidence, and presented so the reader grasps their meaning quickly. Results do not speak for themselves: guide the reader.

## 1. Structure

**Order:** the same order and subheadings as the Methods. Every method gets a result.

**From macro to micro:** open each subsection with the main finding (the big picture: what was shown), then the specific numbers that support it.

**Components (a menu; select what applies):**
1. Revisit the aim, existing research or methodology briefly; give a general overview of the results.
2. Invite the reader to view a figure or table; present the key results in detail, with or without short explanations; compare with other studies or with model predictions.
3. Problems with the results (scatter, outliers, deviations), stated honestly and in proportion.
4. Possible implications (brief; the full discussion comes later).

**Moves in engineering results sections:** restate the analysis procedure or research question → state general findings → state specific findings (usually referring to a figure or table) → comment: interpret, compare with previous studies, evaluate. In chemical engineering papers, writers cycle frequently between stating a specific finding and interpreting it, and often compare with previous studies. This is why "Results and Discussion" is a common combined section in the field.

## 2. Separate results from discussion, even when combined

- **Pure Results section:** report only. No "surprisingly", "interestingly", no explanation of mechanisms, no literature-based interpretation.
- **Combined Results and Discussion:** allowed and common, but make it clear in every paragraph what was measured or computed (the evidence) and what is inferred (the interpretation). Present the finding first, then the comment.

## 3. Paragraph pattern for each figure or table

1. (Optional) Recall the aim or the analysis in one clause.
2. Point to the figure or table and state the main trend.
3. Support with numbers: values, differences, percentage changes, uncertainty.
4. Secondary trends.
5. Exceptions or anomalies.
6. Comparison with validation data, model predictions or other studies, with a clear metric.
7. (Combined section only) Short interpretation, then link to the next point.

Example (placeholders in brackets):
> Figure 4 compares the predicted and measured axial temperature profiles at the tube centreline. All five correlations reproduce the position of the hot spot within [value] m, but they differ markedly in its magnitude. The correlation of [Author] overpredicts the hot-spot temperature by [value] K, whereas [Author 2] underpredicts it by [value] K. Downstream of the hot spot (z > [value] m), all predictions agree with the measurements within [value] K. The lowest overall error was obtained with [correlation] (RMSE = [value] K over [n] measurement points).

Avoid: "The results are shown in Figure 4." alone. Say what the figure shows.

## 4. What not to put in Results

- A method that was forgotten in Methods (move it there).
- Material preparation or data collection as a "result" (how many samples you collected is not a finding; what you measured on them is).
- Every number you have. Select significant data; mention insignificant variables briefly without detail.
- The same data twice (text and table and figure). A key value read from a figure may be quoted in the text, because exact values cannot be read from a graph.
- References, except for brief comparisons in a combined section.

Report negative and null results too: what you did not find matters, and absence of evidence is not evidence of absence.

## 5. Language of sequence and time

Readers who want to reproduce or compare need the order and timing, not just "then" and "next".
- Before the run: beforehand, prior to, initially, at the outset.
- Start: at the beginning, at start-up, at t = 0, immediately.
- Order without time: first, subsequently, then, following this, afterwards, finally.
- Simultaneous: at the same time, meanwhile, during, while, as.
- Duration and speed: within [t] min, over [t] h, rapidly, gradually, steadily.
- End and after: eventually, by the end of, after [t] h, thereafter.
- Repeated cycles: in each cycle, after every [n] runs.

## 6. Language of frequency

State how often a result occurred; reliability depends on it. From always to never: always, invariably, in all cases, consistently, generally, usually, in most cases, frequently, often, in many cases, sometimes, occasionally, in some cases, rarely, seldom, in a few cases, never. Prefer counts where you have them: "in 9 of 12 runs".

## 7. Language of quantity and evaluation

Your wording shapes how readers perceive a result: "the two curves are very similar" and "the two curves are noticeably different" make readers see the same figure differently. Choose words that match the numbers.
- Large: substantial, considerable, marked, pronounced, significant (only with a statistical test or a stated threshold), sharp, steep.
- Small: slight, minor, marginal, modest, negligible.
- Close agreement: in good agreement, within [value] %, closely matches, consistent with.
- Deviation: deviates by, overpredicts, underpredicts, overestimates, underestimates, departs from.
- Change: increased/decreased by [value] % or from [a] to [b]; rose, fell, peaked at, levelled off, remained constant, fluctuated around.
- Minimizing a problem honestly: "a small number of points (3 of 120) lie outside the ±10 % band".
- Always pair the adjective with the number. "A considerable increase (from 12 to 31 %)".

## 8. Language of causality (choose the strength you can support)

- **Strong (you have evidence of the mechanism):** causes, produces, leads to, results in, is due to, is caused by, gives rise to.
- **Partial:** contributes to, is a factor in, plays a role in, partly explains.
- **Initial cause in a chain:** originates in, initiates, triggers.
- **Weak (connection, direction uncertain):** is related to, is associated with, is linked to, correlates with, coincides with.

Note the word order: in "X results in Y", X is the cause; in "X results from Y", X is the effect.

## 9. Comparing with validation data, models and other studies

- Name the metric and the data: "RMSE of [value] K against [n] thermocouple readings", "mean absolute percentage error of [value] % on the test set".
- Use parity plots (predicted vs measured with a 1:1 line and error bands) and residual plots.
- Report where agreement is good and where it fails, and under which conditions.
- For data-driven models: report errors on the test set only, compare with a simple baseline (persistence, linear model), and state the horizon for forecasts.
- Comparison with other studies: "These values agree with [12] within [value] %"; "The predicted hot-spot temperature is [value] K higher than in [14], who assumed …".

## 10. Numbers and statistics

- Statistical support: name the test, the statistic, the degrees of freedom and the exact p-value where software provides it ("t(114) = 5.43, p < 0.001", or the journal's format).
- No more decimals than the measurement precision supports; means may carry at most one more digit than the raw data.
- Percentages: for small samples (n < 20) give counts, not percentages.
- Do not begin a sentence with a numeral; spell it out or rephrase.
- Leading zero for values below 1 (0.25, not .25).
- SI units; a space between number and unit; consistent significant figures in text, tables and figures.
- Define derived quantities (conversion, selectivity, yield) once, in Methods, and use them consistently.

## 11. Tense

- Your findings: past simple ("The outlet temperature increased by [value] K").
- What a figure or table shows: present simple ("Figure 5 compares …"; "Table 3 lists …").
- Generalization you consider established: present simple ("Wall heat transfer controls the hot-spot temperature at low ratios"). Use only when the evidence is strong; past simple keeps the finding tied to your study.

## 12. Style

- One sentence, one point. Short, clear sentences carry new information best.
- Integrate every figure and table into the narrative; do not rely on captions to carry the argument.
- Keep the same terms and symbols as in the Methods.

## 13. Checklist

- [ ] Same order and subheadings as Methods; every method has a result.
- [ ] Each subsection opens with the main finding.
- [ ] Every claim backed by a number, figure, table or statistic.
- [ ] No data duplicated across text, tables and figures.
- [ ] Comparisons use named metrics and named data.
- [ ] Negative results and anomalies reported in proportion.
- [ ] Evaluative words match the numbers; causal verbs match the evidence.
- [ ] Measurement and interpretation clearly separated.
