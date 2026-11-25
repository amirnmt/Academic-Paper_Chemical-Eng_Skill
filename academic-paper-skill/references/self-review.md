# Self-review: simulating peer review before submission

Reviewers find the problems the authors stopped seeing. A structured self-review, done from several reviewer viewpoints before submission, catches most of them while they are still cheap to fix.

Run it on a complete draft (all sections, figures, tables and references), after the section checklists and `scripts/check_ai_signs.py`, and before the final checklist.

A simulated review is not peer review. It cannot confirm that experiments were performed as described, that data are authentic, or that a reviewer in the field would agree. It is a quality filter, not a guarantee.

## 1. Rules for every reviewer role

- **Review independently.** Do each role as a separate pass, ideally in a fresh context (a new session or a sub-agent) that sees only the manuscript, the figures and the journal's guidelines, not the drafting notes. A reviewer who knows what the authors meant will read it into the text.
- **Read as the journal's reader,** with the target journal's scope and standards in mind.
- **Point to the location** of every comment (section, paragraph, line, equation, figure or table) and to the evidence for it.
- **Separate major from minor.** Major: affects validity, novelty or the main conclusions. Minor: clarity, presentation, small errors.
- **Do not invent problems,** and do not soften real ones. If a role finds nothing major, it says so. Every role still names the single weakest point it sees.
- **No vague praise or vague criticism.** "The discussion is weak" is useless; "Section 5.2 attributes the deviation to sintering without evidence; no characterization supports it" is useful.
- **Check the claims, not only the prose.** Recompute a key number from a table; check one equation's units; open one cited paper and confirm it says what the text claims.

## 2. The five reviewer roles

### Role 1: Editor (desk screen)
Decides in a few minutes whether the paper goes out for review. Reads the title, abstract, introduction's last paragraph, figures and conclusion.
- Does the paper fit the journal's scope and readership?
- Is the contribution clear and new within the first page? Can it be stated in one sentence?
- Is the gap supported by recent literature, including papers from this journal?
- Does the abstract give quantitative results?
- Is the presentation professional (template, figures, English, references)? Are the journal's formal requirements met?
- Decision: send to review, or desk reject (and why).

### Role 2: Methods and technical reviewer
Asks whether the work is correct and reproducible.
- Could an expert reproduce the study from the Methods? List every missing parameter, condition, version or setting.
- Are the assumptions stated and justified? Which one, if wrong, would change the conclusions most?
- Models: are balances, boundary and initial conditions, kinetics and property methods complete and consistent? Are units consistent in every equation? Is numerical accuracy shown (grid or time-step independence, tolerances, convergence)?
- Validation: is the model compared with independent data, with a stated metric, over the range of the conclusions? Is any validation data also used for fitting?
- Data-driven models: is the split appropriate (time-ordered for time series), is there leakage (scaling or feature selection fitted on test data, future information in inputs), are baselines and test-set errors reported, are seeds and hyperparameter searches described?
- Statistics and uncertainty: are repeats, error bars, tests and significant figures appropriate? Is sensitivity analysed for the key parameters?
- Does every result have a method and every method a result?

### Role 3: Domain expert reviewer
Knows the field and the closest papers.
- Is the literature review complete for the closest work? Are important recent or competing papers missing?
- Are cited papers represented correctly (spot-check at least five citations against the source)?
- Is the novelty real compared with the closest three studies, or incremental? Is that stated honestly?
- Are the physical, chemical or engineering explanations in the Discussion plausible and supported? Are alternative mechanisms considered?
- Are comparisons with other studies made on comparable conditions?
- Are the practical implications realistic for industry or design?

### Role 4: Devil's advocate
Tries to break the main conclusion.
- What is the strongest alternative explanation for the main result?
- Which single weakness would make a reviewer recommend rejection?
- Where does the text claim more than the data show (generalization beyond the tested range, causal language from correlations, "significant" without a test)?
- What happens to the conclusions if the most uncertain input (a kinetic parameter, a correlation, a data interpolation) is wrong by 20 %?
- Is there a simpler model or baseline that would perform almost as well? Was it tested?
- Are inconvenient results, failed cases or outliers missing?

### Role 5: Readability and presentation reviewer
Reads as a busy non-specialist in a neighbouring field.
- Can the argument be followed from the first sentences of the paragraphs alone?
- Is terminology consistent? Are all symbols and abbreviations defined?
- Are figures readable at print size, consistently styled, and discussed in the text?
- Generic or AI-typical prose (see `avoid-ai-signs.md`): inflated importance, decorative words, vague attributions, formulaic endings.
- Is the abstract self-contained? Do the title and keywords match the content?
- Length: which paragraphs could be cut without loss?

## 3. Report format (each role)

```markdown
## Review: [Role], [date]

**Summary of the paper** (2–3 sentences, in the reviewer's words)

**Assessment** (novelty, soundness, presentation: one sentence each)

**Major comments**
M1. [Location] Problem. Why it matters. What would fix it.
M2. …

**Minor comments**
m1. [Location] …

**Weakest point** (one sentence)

**Recommendation:** accept / minor revision / major revision / reject
```

A recommendation of "accept" without any comment is a sign the review was not done properly.

## 4. Triage: from reviews to a revision plan

Collect all comments into one table and decide an action for each.

| ID | Role | Location | Comment (short) | Severity | Action | Effort | Status |
|---|---|---|---|---|---|---|---|
| R2-M1 | Methods | §2.5 | grid independence not shown | major | new analysis | medium | open |
| R4-M2 | Devil | §5.1 | causal claim from correlation | major | rewrite + hedge | low | open |

Actions:
- **Fix in text:** clarify, add missing information, correct errors.
- **New analysis:** additional simulation, sensitivity study, baseline, validation case.
- **Acknowledge as limitation:** when the fix is out of scope; state it in the Discussion and bound its effect.
- **Rebut with evidence:** when the comment is wrong; record the evidence (citation, data, derivation) in case a real reviewer raises it.

Order of work: major comments that affect conclusions first, then major presentation problems, then minor comments.

## 5. Revise and re-review

1. Revise according to the triage table.
2. Re-run the relevant section checklists and `scripts/check_ai_signs.py` on changed sections.
3. Re-review only what changed, with the role that raised the comment, and close each item.
4. Keep the triage table: it becomes the draft of the response letter if a real reviewer raises the same points (`submission-and-reviewers.md` §8).

## 6. Engineering red flags reviewers often raise

- Model validated only against the data used to fit it.
- Conclusions extrapolated beyond the validated range of temperature, pressure, flow or time.
- Steady-state assumptions applied to transient behaviour, or vice versa, without justification.
- Property or transport correlations used outside their validity range.
- Unit inconsistencies in equations or tables.
- Interpolated or digitized data presented as measurements; the source and processing of literature data not stated.
- Time-series models evaluated with random splits.
- No comparison with a simple baseline or with the closest published model.
- Error metrics given without the data set they refer to.
- Figures with different scales for compared cases.
- References that are old, self-citations dominating, or the journal's own recent papers missing.
