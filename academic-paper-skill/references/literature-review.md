# Literature review: comprehensive, synthesized, critical

Many engineering papers have a separate literature review section between the Introduction and the Methods (the most common structure in empirical articles is Introduction – Literature review – Method – Results and Discussion – Conclusion). Its job is to show the state of knowledge, compare approaches, and make the gap inevitable.

## 1. What a literature review is and is not

It is:
- context for your research within what is already known;
- a comparison of studies on the same topic;
- a presentation of different interpretations of the same evidence;
- a demonstration of where knowledge is missing.

It is not:
- a list of summaries ("A did X. B did Y. C did Z.");
- a demonstration of how many papers you found;
- a place for every paper you read.

## 2. Process

1. **Formulate the question the review must answer.** Usually: "Why is a model or experiment like ours needed?"
2. **Select sources** against that question (use the theme map and comparison matrix in `evidence-base.md`).
3. **Evaluate** which sources are most significant: relevance, rigour, recency, influence.
4. **Organize** by themes tied to the research question.
5. **Analyze** each theme against your own study.
6. **Conclude** with the gap.

## 3. Organization patterns

- **Thematic (default):** one subsection per approach or aspect (kinetics, reactor models, heat transfer, deactivation, data-driven models).
- **Methodological:** grouped by method (experimental, mechanistic modelling, CFD, ML, hybrid). Good when your contribution is a method.
- **Problem-solution:** each subsection is one problem and the solutions proposed for it, with evaluation.
- **Chronological:** only within a theme when the development itself matters (e.g., how models evolved from 1D pseudo-homogeneous to 2D heterogeneous).

Order themes from broad to narrow and end with the studies closest to yours.

## 4. Inside each theme: the synthesis paragraph

Pattern:
1. **Claim (topic sentence):** what this group of studies establishes or how it divides.
2. **Evidence:** the studies, grouped by what they share, with citations and key numbers.
3. **Comparison:** how they differ (method, system, conditions, metric) and why the differences matter.
4. **Evaluation:** strengths and limitations, in your own voice.
5. **Link:** what remains open and leads to the next theme or the gap.

Example (structure only; replace with verified content):
> Fixed-bed methanol reactors have been modelled at several levels of detail [12–19]. One-dimensional pseudo-homogeneous models reproduce outlet conversion at low computational cost [12–15], whereas two-dimensional models also resolve radial temperature gradients and hot spots [16–19]. However, both groups rely on wall heat-transfer correlations fitted at large tube-to-particle diameter ratios, and none of the two-dimensional studies compared predicted radial profiles with measurements. Validation at low ratios has received far less attention [20,21] …

## 5. Synthesis techniques

- Group citations by shared finding: "Similar trends were reported for … [3–6]."
- Contrast: "In contrast to [7], [8] found …, probably because …"
- Quantify the range: "Reported wall heat-transfer coefficients range from A to B W m⁻² K⁻¹ depending on the Reynolds number [9–14]."
- Classify: "Three modelling strategies can be distinguished: … , … and …"
- Generalize carefully: "Taken together, these studies indicate that …"
- Use a summary table for the closest studies (method, system, regime, deactivation, validation, metric, result). Refer to it in the text and discuss the pattern it shows, not each row.

## 6. Reporting verbs and their strength

Choose the verb that matches the source's certainty and your attitude:
- **Neutral:** describe, report, present, examine, investigate, study, note, observe.
- **Tentative (source is cautious):** suggest, propose, hypothesize, speculate, indicate.
- **Strong (source is confident or you accept it):** show, demonstrate, establish, confirm, prove (use "prove" rarely).
- **Critical or distancing:** claim, assert, assume (signals you may disagree).

Do not upgrade a source: if the authors wrote "may", do not write "showed".

## 7. Critical but diplomatic

- Evaluate, do not attack. Present the strength of your approach rather than the weakness of others: "The present model resolves both axial and radial temperature profiles" instead of "previous models were inadequate".
- Hedge criticism: "may have been limited by", "did not account for", "was restricted to".
- Include results that disagree with your expectation and explain the disagreement. Ignoring them is easy for reviewers to spot.
- When paraphrasing, keep the original emphasis; reordering a source's points can change its meaning.

## 8. Your voice

Each paragraph should contain your evaluation, before or after the sources. A review written only in the voice of the cited authors gives the reader no reason to believe the gap exists.

## 9. Planning a large citation count (e.g. 70+)

- Allocate citations per theme from the theme map (`evidence-base.md` §3), not per paragraph.
- Cover each theme with: 1–2 reviews, the foundational papers, the most recent strong papers, and the closest competitors.
- One claim normally needs 1–3 citations; more only for "widely studied" statements.
- Every citation must be relevant and verified. If the repository cannot support the target, report the thin themes to the author instead of padding.

## 10. Tense

- What the field knows: present simple ("Cu/ZnO/Al2O3 is the standard industrial catalyst …").
- What a specific study did: past simple ("Lee et al. [5] modelled …").
- Lines of research continuing to now: present perfect ("Several authors have proposed …").

## 11. Paraphrase and quotation

- Paraphrase in your own words and structure; changing a few words is not paraphrasing.
- Quote only when exact wording matters (definitions, a disputed claim). Rare in engineering.
- Cite ideas, not only words.

## 12. Checklist

- [ ] Organized by themes linked to the research question, broad → narrow.
- [ ] Each theme synthesized (grouped, compared, evaluated), not listed.
- [ ] Closest studies compared on the same axes, ideally in a table.
- [ ] Disagreeing results included and explained.
- [ ] Your evaluation present in every paragraph.
- [ ] Reporting verbs match the sources' certainty.
- [ ] Ends with a gap that the Introduction's objective answers.
- [ ] All citations verified; thin themes reported, not padded.
