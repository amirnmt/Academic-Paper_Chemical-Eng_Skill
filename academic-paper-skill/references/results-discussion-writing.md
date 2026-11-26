# Writing Results and Discussion: from numbers to evidence-based arguments

A pattern-by-pattern guide to presenting, interpreting, comparing and bounding results in modelling, simulation, optimization, data-driven and hybrid papers in chemical and process engineering. It extends `results-and-discussion-combined.md` (section and subsection pattern R1–R7), `results-language.md` (reporting language, numbers, statistics) and `discussion-hedging.md` (interpretation, hedging, limitations); read those first for the basics.

Levels (see `journal-profile.md` §0): **[G]** general academic writing · **[M]** general scientific practice · **[D]** chemical and process engineering · **[PB]** physics-based modelling · **[NUM]** numerical and computational · **[ML]** machine learning · **[HY]** hybrid modelling · **[J-obs]** observed in the Results and Discussion of 20 *Computers & Chemical Engineering* research articles (convention; numbers in §24 and in the journal profile) · **[J-req]** journal requirement · **[Rule]** standing rule of this skill.

Examples are original and illustrative (the skill's running example is a fixed-bed methanol reactor; numbers are placeholders). Where a pattern was seen in the analysed papers, "Seen in" names the paper by the last digits of its PII and the page; the DOIs are listed in the journal profile.

---

## 0. Integrity rules and the six kinds of evidence [Rule]

Every interpretation in the Results and Discussion is traceable to at least one of:

| Evidence | Wording that signals it | Citation |
|---|---|---|
| E1 Our numerical or experimental results | "Fig. 5 shows …", "The error is …" | none |
| E2 An interpretation directly supported by our results | "The hot spot moves downstream as …; the shift therefore follows the coolant temperature." | none |
| E3 An explanation derived from our governing equations | "Because the heat-generation term in Eq. (4) grows exponentially with temperature while removal grows linearly, …" | the equation number |
| E4 Established scientific knowledge | "As expected for an exothermic reversible reaction, …" | a textbook or review |
| E5 Previously published research | "…, in agreement with the measurements of [ref]" | the paper |
| E6 A hypothesis that needs further work | "A possible explanation is …; testing it would require …" | evidence for plausibility if any; marked as unconfirmed |

Never: invent or adjust numbers; fabricate references or comparisons; claim statistical significance without a test; claim causation from correlation alone; claim a mechanism the evidence does not support; omit unfavourable results or select metrics because they favour the proposed method; extrapolate beyond the investigated range without justification; present a hypothesis as a conclusion; claim superiority without a fair benchmark. When the evidence is insufficient, say what is missing and what would supply it.

When the user names directories of papers, the literature-based explanations (E4, E5) are taken from them (`citation-practice.md` §3 and §13); if no paper supports an explanation, it is either dropped, or written as E6 with the uncertainty stated.

---

## 1. Architecture

### 1.1 Combined or separate [J-obs, G]

In the analysed papers, the results part was titled "Results and discussion" in 11 of 20, "Results" (with further result sections or a separate comparison) in 2, and was framed as case studies or experiments in the rest (7); none had a separate top-level Discussion. Interpretation appears inside the result subsections; some papers end with short subsections that discuss the findings together (a "Discussion" or "Results discussion" subsection, positioning against prior work, generality, implications, limitations).

| | Combined | Separate |
|---|---|---|
| Strength | each result is explained before the next one depends on it; no repetition of numbers | a synthesis across results; room for comparison with literature and for the wider meaning |
| Risk | interpretation becomes thin and figure-by-figure; the overall argument is lost | results repeated in the Discussion; results without explanation in the Results |
| Fits | method papers, case studies, sequential analyses, computational journals | experimental studies with several measurements that are interpreted together; journals that require it |

A good compromise for a computational paper [G]: combined subsections (each with interpretation), followed by one or two closing subsections that synthesize (contribution relative to prior work, implications, limitations).

### 1.2 How the section begins [J-obs]

- **Orientation paragraph:** what is evaluated, on which data, how results are reported ("Results are reported on the held-out test set using ensemble predictions", …4321 p6; "This section evaluates the framework on cells not used for fitting", …4370 p6).
- **Implementation and set-up first:** software, solver, hardware, time step (…4436 p8), or the scenario and its data (…4369 p11, …4382 p5).
- **Headline result first:** "The central result is that …, as summarized in Table 3 and Fig. 4" (…4400 p7).
- **Organizing claim:** "Seven choices change the conclusions, in two groups" (…4357 p5).

Template: "This section [evaluates / reports] … on … . Section 4.1 validates the model against …, Section 4.2 analyses …, and Section 4.3 uses the validated model to … . All errors refer to the [independent / test] data unless stated otherwise."

### 1.3 Order of subsections [J-obs, G]

The order follows the objectives and the Methodology, and credibility comes first: **verification and validation → analysis of the validated model (behaviour, sensitivity, mechanisms) → use of the model (optimization, control, scenarios, decisions) → computational performance → position relative to prior work → limitations.** Seen in …4436 (validation, then estimability and parameters), …4321 (accuracy, then extrapolation, then application to industrial systems: "Having established …, we now examine whether …", p9), …4448 (data-driven model, then optimization, then MPC), …4497 (prediction, classification, candidate recipes), …3434 (optimization results, energy, emissions, comparison with rigorous simulation, computational performance).

### 1.4 Emphasis

- Put the main finding in the subsection title when it is a claim ("Individual slab tokens exceed zone aggregation under the same inputs", …4400 p7) or in the first sentence of the subsection.
- State secondary findings briefly, after the main one, or in a table; move further detail to supplementary material.
- One subsection, one question; end it with the answer.

---

## 2. Paragraph frameworks

The generic results paragraph [G]: **purpose → setup → observation with number → comparison → explanation (with its evidence type) → bound → consequence or transition.** Not every paragraph has every step; observation, number and consequence are almost always there.

### 2.1 Validation paragraph [PB, M]
1. Data and status: which data, whether independent of calibration.
2. Agreement: metric(s) with values, per output.
3. Pattern of agreement: where and when the model is best and worst.
4. Systematic deviation: sign and size (bias), and where it occurs.
5. Explanation of the deviation: assumption, data quality, missing physics (E2–E5).
6. Verdict for the intended use, and its range.

Example: "On the independent campaign, the model reproduces the measured hot-spot temperature with a mean absolute error of 2.1 K and the outlet methanol fraction within 0.3 mol% (Table 5). The error is largest during load changes (up to 6 K), where the model reaches the new steady state about 10 min earlier than the plant. This lag is consistent with the thermal capacity of the tube wall, which the pseudo-homogeneous model neglects (Section 2.3). For the steady-state optimization in Section 4.4, the remaining error is below the 5 K margin used for the hot-spot constraint."

Seen in: …4436 p12–13 (training, testing and an independent campaign; Pearson, MSE, relative bias; the nominal unestimated model as reference; the pattern across outputs explained as a property of the process, not of the estimation).

### 2.2 Physical-interpretation paragraph [PB, D]
1. Observation in the figure, with location and condition.
2. Quantity.
3. Mechanism as a chain of cause and effect, each link supported (equation, principle, literature).
4. Check: another observation that the mechanism predicts.
5. Consequence for performance or operation.

Example: "Raising the coolant temperature from 230 to 236 °C moves the hot spot 0.12 m downstream and raises it by 9 K (Fig. 7a). The higher wall temperature reduces heat removal near the inlet, so the reaction rate, which grows with temperature (Eq. 6), accelerates over a longer length before removal catches up. The same mechanism predicts the lower selectivity observed downstream of the hot spot (Fig. 7b), where the by-product reaction, with its higher activation energy, gains relative to methanol formation [ref]. The coolant temperature therefore sets the trade-off between conversion and catalyst life that Section 4.4 optimizes."

Seen in: …0433 p7 (temperature zones derived from the crossing of the rate constants of desired and undesired reactions in a figure); …4448 p9 (seed load → growth surface → secondary nucleation → size distribution, used to explain the Pareto front).

### 2.3 Numerical-performance paragraph [NUM]
1. Baseline and conditions held equal (hardware, tolerance, problem size).
2. Time or cost with numbers, and how it scales.
3. Accuracy at that cost, relative to the reference.
4. Where the cost goes (bottleneck).
5. What the gain allows.

Seen in: …3434 p15–17 (problem size per iteration, CPU time growth explained by more binary variables, repeated runs; hardware stated); …431X p19–21 (runtime by module, bottlenecks identified, and an explicit statement that the comparison across cases does not establish a scaling law); …4369 p15 (a computational-time index relative to the scheduling period).

### 2.4 Parametric or sensitivity paragraph [M]
1. Purpose and the parameter range (and what is held constant).
2. Response with numbers: direction, size, linearity, thresholds.
3. Ranking of influence; interactions if varied jointly.
4. Physical origin of the sensitivity.
5. Practical meaning (which parameter to control or measure).

Seen in: …4217 p8–10 (scenarios defined, materials ranked, decision rule derived); …4394 p21 (single-parameter scans); …4424 p11 (two inputs varied because they dominate the score).

### 2.5 Machine-learning evaluation paragraph [ML]
1. Data split and what "test" means here.
2. Metrics on each split; gap between training and test.
3. Comparison with baselines under the same inputs.
4. Where it fails (cases, ranges, horizons).
5. Why (evidence from ablation or analysis; otherwise marked as plausible).
6. Variability (seeds, repetitions) and limits.

Seen in: …4400 p7–10 (four seeds with their spread; same inputs for all baselines; ablation attributing the gain); …4321 p6–8 (held-out sets; coverage of chemical species explains error growth; interpolation vs extrapolation); …4357 p6 (rankings flip across seeds).

### 2.6 Literature-comparison paragraph [G, D]
1. Our value and conditions.
2. The published value, its conditions and source.
3. Agreement or difference, quantified.
4. Explanation of the difference (assumptions, data, conditions, definitions).
5. What the comparison shows (and does not).

Example: "The predicted specific energy demand of 2.9 GJ t⁻¹ lies within the 2.6–3.4 GJ t⁻¹ reported for comparable plants [ref]. The value is near the upper end because the model recovers no heat from the purge stream, which the reference plants do."

Seen in: …3434 p13 (energy consumption against a literature range; a lower estimate explained by the rigorous hydrogen-recovery model); …4321 p6 (RMSE and R² against those of the original dataset publication, with the note that the partitions differ); …3434 p11 (a different optimal technology from a previous study, attributed to a fixed production level instead of a fixed feed).

### 2.7 Unexpected-observation paragraph [G]
1. State the observation plainly and where it occurs.
2. Rule out artifacts (numerics, data, implementation) with evidence.
3. Candidate explanations, each with what supports or contradicts it.
4. The conclusion you can draw, and what remains open.

Seen in: …4321 p6 (experimental viscosities that increase on dilution, flagged as physically paradoxical while the model predicts the expected trend); …4448 p7 (augmented data that performs worse than real data of the same size).

### 2.8 Limitation paragraph [G]
1. The limitation (assumption, data, range, method).
2. Its direction and likely size of effect on the results.
3. Which conclusions it affects and which it does not.
4. What would remove it.

Seen in: …4357 p8 ("conditional on the simulators, tasks, losses, references and seeds"); …4424 p15–17 (a structural limit stated as a bound, with what the small effect does not show); …4436 p14–15 (structural simplifications and unexcited parameter directions, with the experiment that would resolve them).

### 2.9 Implication paragraph [D]
1. The demonstrated result.
2. Its meaning for design, operation or decisions, under the tested conditions.
3. Potential (not demonstrated) uses, marked as such.

Seen in: …4217 p9 (a decision rule for material choice under spatial constraints); …4321 p9 (a 14.9 % MAPE judged useful for ranking recipes, not for exact prediction).

---

## 3. Presenting results quantitatively [G, M]

### 3.1 From general to quantitative

Replace "the temperature increases" by **what, how much, where, when, under which condition, compared with what**: "The hot-spot temperature rises by 14 K (from 262 to 276 °C) when the inlet temperature is raised by 5 K, and its position moves 0.08 m towards the inlet." Then add **why** and **so what** (§4).

### 3.2 Choosing the form of a number

| Form | Use for | Example |
|---|---|---|
| Exact value with unit | single key results, validation errors | "an RMSE of 1.8 K" |
| Percentage or percentage points | relative change; differences between shares (use pp) | "selectivity falls by 2.1 pp, from 92.4 to 90.3 %" |
| Range | spread over cases, seeds, conditions | "0.678–0.686 across four seeds" |
| Ratio or factor | large differences | "a seventeen-fold reduction in MSE" |
| Approximate value | orientation where precision is not the point | "about 10 min" |
| Rank | when only order is meaningful | "MnCl2 is the most stable of the eight" |

Say relative to what ("compared with the nominal model", "relative to the steady-state method") and on which data. In the analysed papers about a third of the sentences in this section contain a number [J-obs]; the papers that quantify most report each comparison with both values and the change.

### 3.3 Describing behaviour

| Behaviour | Vocabulary | Template |
|---|---|---|
| Extremes | maximum, minimum, peak, lowest, highest, reaches, attains | "… reaches a maximum of … at …" |
| Change | increases, decreases, rises, falls, drops, grows, declines, by …, from … to … | "… decreases by … % from … to … as … increases from … to …" |
| Trend shape | linearly, proportionally, exponentially, nonlinearly, monotonically, levels off, saturates, plateaus | "… increases almost linearly with …, then levels off above …" |
| Non-monotonic | passes through a maximum, first … then …, reverses | "… first rises, peaks at …, and falls beyond …" |
| Oscillation | oscillates, fluctuates, amplitude, period, damped, sustained | "… oscillates with an amplitude of … and a period of about …, damped within …" |
| Threshold | above/below …, beyond …, once … exceeds …, critical value, onset | "Above …, … increases sharply" |
| Transient vs steady | initially, during the first …, settles, relaxes, reaches steady state within …, overshoot, response time | "… overshoots by … and settles within … of the step" |
| Spatial | along the axis, near the wall, at the centreline, upstream/downstream of, gradient, profile, front | "… is highest near the inlet and decays along the bed" |
| Correlation | is associated with, co-varies with, correlates with (r = …) | "Higher … is associated with lower … (r = −0.71)" |
| Interaction | the effect of … depends on …, is amplified when …, offsets | "The effect of … is larger at high … than at low …" |
| Similar vs different | comparable, similar, agrees within …, differs by …, whereas, in contrast | "… are comparable (within 3 %), whereas … differs by …" |

---

## 4. Interpretation and explanation [G, PB, M]

### 4.1 Seven questions a strong explanation answers
1. What was observed? 2. Under which conditions? 3. How large, and how significant (practically, statistically)? 4. Why? 5. Through which mechanism (physical, chemical, mathematical, computational)? 6. Is it consistent with established knowledge and published results? 7. What follows from it?

### 4.2 Language of cause, matched to evidence

| Evidence | Wording |
|---|---|
| Demonstrated by a controlled comparison (ablation, one-factor change, equation) | "is caused by", "results from", "is due to", "because" |
| Strongly supported, mechanism plausible and consistent | "can be attributed to", "is explained by", "reflects" |
| Consistent with, not tested | "is consistent with", "suggests", "may result from", "a likely explanation is" |
| Association only | "is associated with", "coincides with", "co-varies with"; never "causes" |
| Speculative | "one possible explanation is …; this would require …" |

Correlation is not causation [Rule]: …4400 p14 states that an association between flagged hours and discharge temperatures "is an observational association rather than a causal effect" and does not show what would happen if firing were reduced. Write the same kind of sentence whenever the evidence is observational.

### 4.3 Using the model's equations to explain results [PB]

- Name the term that dominates: "Near the inlet, the reaction term in Eq. (5) exceeds the wall heat-removal term by a factor of three, which explains the steep initial rise."
- Use a dimensionless group: "Because the Damköhler number exceeds 5 at these conditions, conversion is limited by heat removal, not by kinetics."
- Use the structure of the model: "The agricultural score per tonne is identical in all solutions because cultivation enters through one national factor" (…4424 p11, paraphrased): a result that follows from the model's form is explained by it, and the limitation is stated.
- Do not repeat the derivation; refer to the equation by number.

### 4.4 Competing explanations

State the alternatives and the evidence that separates them: "The lag could arise from the wall's heat capacity or from sensor dynamics; because it also appears in the outlet composition, which is measured by a different instrument, the wall is the more likely cause." If the evidence cannot separate them, say so.

### 4.5 Distinguishing observation, interpretation and conclusion
- Observation (past or present simple, no modal): "The error increased with the recursion step."
- Interpretation (present, with evidence word): "This indicates that errors accumulate in the recursive prediction."
- Conclusion (present, scoped): "Within 20 steps, the model is therefore suitable for MPC."

---

## 5. Linking results to the Methodology [G]

- Refer back by section and equation number instead of repeating the method: "With the calibrated parameters (Section 2.6), …"; "The index defined in Eq. (12) …".
- Show that each methodological component does what it was designed for, with a test: ablation, removing one component, comparing with the variant without it (…4394 p20 ablation removes components step by step; …4412 p19 ablation per module).
- Trace discrepancies to assumptions: "The underprediction during start-up follows from the quasi-steady pellet assumption (Section 2.2)."
- State the effect of numerics on accuracy where relevant (time step, tolerance, surrogate error), for example how the gap between a surrogate-based and a rigorous result shrinks as the surrogates are refined (…3434 p17 reports a large NPV discrepancy in the first iterations, attributed to inaccurate initial surrogates). Template: "The difference between the surrogate-based and the rigorous value decreases from … to … as …".

---

## 6. Verification, validation and benchmarking [M, PB, ML]

### 6.1 Keep five things apart
| Activity | Question | Data |
|---|---|---|
| Verification | Are the equations solved correctly? | analytical solutions, balances, independence checks, code comparison |
| Calibration | Which parameter values fit the data? | calibration (training) data |
| Validation | Does the calibrated model predict data it has not seen, for the intended use? | independent data (other periods, campaigns, conditions) |
| Predictive assessment | How accurate is it where it will be used, including extrapolation? | test sets across the operating range |
| Benchmarking | Is it better than alternatives under equal conditions? | same data, same inputs, same metrics |

Agreement with calibration data is not validation [Rule]: say "the model fits the calibration data with …" and "it predicts the independent campaign with …". …4436 reports training, testing and a fully independent campaign separately, and compares with the unestimated nominal model to show what estimation adds.

### 6.2 Wording agreement and deviation
- "agrees with … within …"; "reproduces …"; "captures the trend but underpredicts the peak by …"; "deviates by up to … at …"; "a systematic overprediction of …, largest at …"; "a random scatter of ± … around the measurements".
- Never "excellent agreement" without numbers; avoid "perfect".
- Explain the discrepancy: missing physics, assumption, data uncertainty, operating regime, measurement location.

### 6.3 Establishing credibility before use
Close the validation subsection with what the model can and cannot be used for: "The model is therefore used below only within the validated range of …".

---

## 7. Error metrics and statistics [M, ML]

- **Combine metrics** with different sensitivities: an absolute error in physical units, a relative error, a correlation or R², and the maximum error; report bias separately from scatter. …4436 combines Pearson coefficients, MSE and relative mean bias and explains why MSE rather than RMSE is reported (confidential units; consistency with the estimation objective).
- **Interpret the numbers:** what an error of this size means for the use ("below the 5 K margin of the hot-spot constraint"; "useful for ranking recipes rather than exact prediction", cf. …4321 p9).
- **Practical vs statistical significance:** "significant" is reserved for a statistical test with its level and result; otherwise write "large", "substantial", "clear", or give the number. In the analysed papers, "significant(ly)" appeared in 62 sentences in 15 papers but only one of them reported a statistical quantity in the same sentence [J-obs]; do better.
- **Variability:** report spread across seeds, repetitions or bootstrap resamples (…4400 p7: four seeds, R² 0.678–0.686, SD 0.003; …4394 p20: 50 Monte Carlo runs to test statistical significance; …4357: paired bootstrap intervals).
- **Residuals:** describe their distribution and structure in time or space (…4400 p13–14: the residual shows spatial and temporal structure, which is reported, while its size is deliberately not interpreted).
- **Superiority claims:** a lower error on one dataset with one seed is not superiority; state data, conditions and the size of the margin relative to the variability.

---

## 8. Physical and chemical interpretation in reactor and process studies [D, PB]

Explain phenomena as **coupled**, not independent. Typical chains in fixed-bed catalytic reactors:
- temperature → rate constants (Arrhenius) → heat generation → temperature (feedback, hot spot, runaway sensitivity);
- temperature → relative rates of desired and undesired reactions (different activation energies) → selectivity and yield;
- conversion → composition → equilibrium approach or rate decline;
- flow rate → residence time and heat-transfer coefficient → conversion and hot-spot height;
- coolant temperature or wall heat transfer → radial gradients → local rates near the axis;
- intraparticle diffusion → effectiveness factor → apparent kinetics and selectivity;
- catalyst activity decline → shift of the reaction zone downstream → hot-spot migration → long-term performance;
- pressure drop → local partial pressures → rates.

For each claim of this kind, give: the observation, the link(s), the evidence for each link (E2–E5), and the consequence. Check mass and energy closure where the results allow it, and report it.

Seen in: …0433 p7 (reaction-rate constants of desired and combustion reactions used to set temperature zones; runaway risk from the heat of combustion); …0433 p12 (less cooling water → less heat removal → temperature rise); …4448 p9 (seed load → surface area → secondary nucleation → size distribution); …4436 p12 (reactor temperature predicted best, production rate worst, across all methods and the nominal model, so the pattern originates in the process, not in the estimation).

---

## 9. Spatial, temporal and multiscale results [PB, NUM]

- **Profiles:** describe the shape (rise, peak, decay), the location and value of the extremes, the gradients, and how they change with the condition varied. Use one or two representative profiles in the text and the full set in a figure.
- **Local to global:** connect the local feature to a system quantity: "The 9 K higher hot spot reduces the outlet selectivity by 0.8 pp."
- **Transients:** initial response, overshoot, time constants, approach to steady state, and which phenomenon sets each time scale (gas residence time, solid heat capacity, catalyst deactivation).
- **Propagation of disturbances:** where and how fast a step travels (thermal waves travel slower than gas).
- **Between scales:** what the particle scale contributes to the reactor scale (effectiveness, surface concentrations), and when it matters.
- **Simplifying multidimensional results:** select characteristic quantities (hot-spot temperature and position, outlet conversion, maximum gradient), show maps or contour plots for the full field, and say which information the reduction loses.

Seen in: …4400 p10–13 (per-burner accuracy projected onto the furnace geometry; a one-hour thermal lag identified by lagged correlation); …4369 p11–15 (closed-loop tracking over a day, with time-resolved comparisons).

---

## 10. Computational performance [NUM]

- Compare under equal conditions: same hardware, tolerance, problem size, operating cases; state them.
- Report accuracy together with speed: a faster method is better only if its error, stability, robustness and range of applicability are acceptable [Rule].
- Give absolute times, speed-up factors and their spread over runs; show scaling with problem size.
- Identify bottlenecks and what drives them.
- Do not generalize a scaling law from two cases (…431X p21 says so explicitly).
- Templates: "On the same workstation and tolerance, the surrogate evaluates one operating point in 4 ms against 38 s for the full model, a 9,500-fold speed-up, with a maximum hot-spot error of 1.2 K over the test set."; "CPU time grows with each iteration because …".

Seen in: …3434 p15–17, …431X p19–21, …4369 p15, …4448 p10 (move blocking reduces the number of optimization variables and the solution time while keeping tracking accuracy).

---

## 11. Parametric studies and sensitivity analysis [M]

- **Distinguish:** descriptive parametric study (vary one input, show responses); local sensitivity (derivatives at a point); global sensitivity (variance-based, over ranges, with interactions). Name which one each result comes from.
- **Isolate effects:** vary one factor with the others fixed, or use a design that separates them; never attribute a change to one parameter when several changed (…4424 p17 states that a reference case combines three changes "whose separate effects have not been measured").
- **Report:** range, baseline, response with numbers, ranking, interactions, nonlinearity, thresholds; then the physical origin; then the practical meaning.
- **Templates:** "Over the investigated range of …, … changes by …, whereas … changes by less than …"; "Total-order Sobol indices identify … (S_T = 0.62) and … (0.21) as dominant; the difference between first- and total-order indices of … indicates an interaction with …".

---

## 12. Machine-learning results [ML]

Report and discuss: training, validation and independent test performance separately; learning curves where they show over- or underfitting; generalization to unseen conditions (species, operating ranges, horizons); interpolation vs extrapolation (…4321 p8: models perform similarly when interpolating and differ when extrapolating); multi-step or long-horizon behaviour (…4448 p8: error grows with recursion steps); variability across seeds; ablations; physical consistency of predictions; limits of the data.

Check before claiming [Rule]: the test data were not used for selection or tuning; temporal order respected and no future information in inputs; baselines received the same inputs and tuning effort; performance reported beyond one aggregate metric (by case, range, horizon); dataset limitations stated.

Why a model performs better: give the experiment that shows it (ablation, controlled comparison: …4400 p9–10 attributes the gain to individual slabs and their live position by removing each); otherwise label the explanation as plausible and untested.

---

## 13. Hybrid models [HY]

- Evaluate each component and the whole: physical model alone, data-driven model alone, hybrid; an ablation of the coupling.
- Show how physics constrains the learned part (extrapolation, conservation, monotonicity) with a test where a purely data-driven model fails.
- Track error propagation between components (surrogate error → optimization result; generated data → downstream model, …4448 p7).
- Check physical consistency of predictions (signs, bounds, balances).
- Quantify the gain in accuracy and in cost relative to each pure approach.
- Templates: "Without the physical extrapolation term, the error above 330 K rises from … to …"; "The surrogate's error of … in hot-spot temperature changes the optimal coolant temperature by less than …".

---

## 14. Comparison with previous studies [G, D]

- Compare like with like: state the conditions, data, definitions and metrics of both; if they differ, say how and what that means for the comparison (…4321 p6: different partitions; …3434 p11: fixed production vs fixed feed).
- Quantify agreement or difference; explain differences by assumptions, data, conditions or methods.
- Do not read every numerical difference as an improvement [Rule].
- Integrate the citation into your argument: "Our value of … lies within the range of … reported for … [refs], which supports …" rather than a separate list of others' numbers.
- Position the whole contribution at the end of the section: a table of prior approaches against the capabilities the paper adds (…4400 p14, Table 6), written with neutral language about the others.

In the analysed papers, comparisons with the literature were few: about 1 % of sentences (12 of 20 papers had any), and 4.5 % of all sentences in the section carried a citation [J-obs]. Most comparison is with baselines inside the study. For a reactor-modelling paper, add comparisons with published data and models wherever they exist, because they are the external test of credibility.

---

## 15. Citations in the Results and Discussion

Own results need no citation; literature-based explanations, established mechanisms, published values, discrepancies with published data, and statements about other methods do. Full rules: `citation-practice.md` §13.

---

## 16. Figures in the text [G, J-obs]

- **Before the figure reference:** the purpose ("To see where the error arises, Fig. 6 maps …").
- **With it:** what is plotted and under which conditions (only what the caption does not make obvious).
- **After it:** the main trend, the key numbers, the comparison, the unusual feature, the mechanism, the consequence; then the link to the next result.
- **Panels:** refer to each panel in the order of the argument ("Fig. 3(a) … whereas Fig. 3(b) …"), not panel by panel for its own sake.
- **Parity and residual plots:** state the spread, the bias, and where points leave the band.
- **Do not** translate the whole figure into words; select the two or three facts the argument needs.
- Observed [J-obs]: about 12 % of sentences refer to a figure or table (IQR 9–19 %); figure-led openings ("As shown in Fig. …", "Fig. 5 shows …") appear in 19 of 20 papers.

## 17. Tables in the text [G]

- Introduce the table by its purpose and the comparison it supports; name the row or column to look at.
- Quote only the values that carry the argument; describe patterns across rows ("errors increase from training to validation for every output"), not each cell.
- Use tables for exact values and many cases, figures for trends and shapes, an equation for a fitted relation, and a sentence for a single number (`figures-tables.md` §1).

---

## 18. Unexpected results and anomalies [G]

Treat them as information. Check numerics, data and implementation; state the observation; consider explanations; report what can and cannot be concluded. Distinguish a physical phenomenon, a numerical artifact, measurement uncertainty and a limitation of the method; say which one the evidence supports. Do not hide unfavourable results or remove them silently (…4357 reports that existing checkpoints fail its admission rule; …4448 p7 reports that augmented data underperform real data at equal size).

---

## 19. Uncertainty, limitations and hedging [G]

### 19.1 Certainty ladder
| Strength | Use when | Expressions |
|---|---|---|
| Established | directly demonstrated in this study, controlled | "shows", "demonstrates", "is" |
| Strong | consistent across tests, mechanism supported | "indicates", "confirms within …", "is consistent with" |
| Moderate | supported but alternatives remain | "suggests", "is likely to", "can be attributed to" |
| Weak | plausible, untested | "may", "might", "a possible explanation is", "appears to be associated with" |
| Scoped | true only within limits | "within the investigated operating range", "under the considered assumptions", "for this data set" |
| Negative | evidence does not support a claim | "the available evidence does not establish …", "this does not show that …" |
| Open | needs work | "confirming this would require …" |

Hedges are not a substitute for evidence, and uncertain interpretations are not facts [Rule]. In the analysed papers, about 6 % of sentences carry a hedge and about 3 % state a limitation or a scope [J-obs]; hybrid papers hedge most.

### 19.2 Limitations
State them where they apply and, if several, in a closing subsection: assumptions, approximations, parameter and measurement uncertainty, data limits, range of validity, computational limits, possible systematic errors, unverified interpretations. For each: effect on which result, direction, rough size, and remedy. Distinctive practice seen: stating what a small effect does **not** show (…4424 p15), and stating that a cross-case comparison does not establish a scaling relationship (…431X p21).

---

## 20. Demonstrating novelty without promotion [G, Rule]

- Tie each result back to the gap and the contribution it supports (the traceability matrix in §22).
- Quantify the improvement against a fair baseline and the variability; say whether the gain is practically meaningful.
- Name what is new: a capability (prediction where others aggregate), a measurement, a speed-up at equal accuracy, an application at industrial scale.
- Avoid: "highly accurate", "significantly superior", "revolutionary", "unprecedented", "state-of-the-art" (unless defined by a benchmark), "excellent agreement" without numbers. Replace each with the number and the comparison.
- Distinguish incremental improvement from new capability honestly; calibrate as …4424 does ("the decomposition is a standard method; what is new is …").

---

## 21. Engineering and industrial implications [D]

- Separate what is demonstrated (in this model, these data, this range) from what is potential (future application, other plants).
- Make implications specific: operating windows, set-points, constraints, monitoring signals, design choices, energy or emission changes, economic indicators, with their conditions.
- Templates: "Within the validated range, operating at … raises selectivity by … at the cost of …; whether this holds for aged catalyst was not tested."; "The index could serve as a monitoring signal; its use in plant operation requires …".
- Do not present potential benefits as results.

---

## 22. Traceability: gap → objective → method → result → interpretation → contribution [Rule]

Build this table before writing and check it before submission:

| Gap (Introduction) | Objective / contribution | Method (section, equation) | Result (section, figure, table, number) | Interpretation (evidence type E1–E6) | Claim in abstract and conclusion |
|---|---|---|---|---|---|

Checks:
- every objective and contribution has a result row; every result supports an objective (otherwise move it to supplementary material or remove it);
- numbers are identical in text, tables, figures, abstract and conclusion;
- interpretations are consistent with the model's equations and assumptions;
- no claim in the abstract or conclusion lacks a row;
- the gap stated in the Introduction is closed to the extent the results show, and the remaining part is named.

---

## 23. Language [G, J-obs]

- **Tense:** present for what figures and tables show and for interpretations ("Fig. 5 shows …", "this indicates …"); past for what was done and observed in specific runs ("the model was evaluated …", "the error increased …"). In the analysed papers about half of the sentences contain present markers and about 30 % past markers; both are normal here.
- **Voice:** passive in about a third of the sentences; "we" is rare (median about 1 % of sentences) but natural for decisions and claims ("We first assess …").
- **Sentence length:** median 22 words.
- **Recurring moves and expressions:** purpose openers ("To further evaluate …", "To assess …", "Having established …, we now examine …"); figure leads ("As shown in Fig. …", "Fig. … shows …", "Table … summarizes …"); comparison ("compared with", "relative to", "whereas", "outperforms … by …"); explanation ("because", "due to", "can be attributed to", "this indicates that"); scoping ("within the investigated range", "for this data set").
- **Avoid:** "significantly" without a test; "clearly", "obviously"; adjectives that replace numbers.

---

## 24. Benchmarks from *Computers & Chemical Engineering* [J-obs]

Results and Discussion part (first results section to the Conclusion) of 20 research articles; medians with interquartile range; sentence shares from marker words, so treat them as approximate.

| Measure | Median (IQR; range) |
|---|---|
| Words | 2,865 (2,065–3,984; 379–6,617) |
| Sentences | 140 (90–184) |
| Words per sentence | 22.2 (20.2–24.3) |
| Subsections | 3.5 (1.5–8.5; 0–16) |
| Figures / tables referred to | 4.5 (3.8–9.3) / 4 (2–7.5) |
| Sentences referring to a figure or table | 0.12 (0.09–0.19) |
| Sentences referring to an equation | 0 (0–0.01) |
| Citation instances / citation groups / unique references | 8.5 / 6.5 / 5 (IQR of unique: 1–8) |
| Sentences with a citation | 0.045 (0.02–0.09) |
| Sentences comparing with the literature | 0.011 (0–0.024); in 12 of 20 papers |
| Sentences with a number | 0.35 (0.30–0.41) |
| Sentences with an explanation marker | 0.18 (0.14–0.22) |
| Sentences comparing within the study | 0.26 (0.19–0.29) |
| Sentences with a hedge | 0.06 (0.04–0.08) |
| Sentences with a limitation or scope | 0.03 (0.02–0.05) |
| Sentences with an implication | 0.05 (0.03–0.07) |
| Sentences with present / past markers / passive | 0.53 / 0.29 / 0.36 |

By type (medians): physics-based papers cite most (8 % of sentences) and quantify about as much as the others; data-driven papers refer to figures most (10 % of sentences) and cite least (2 %); hybrid papers hedge most (12 %) and state limitations most (6 %).
