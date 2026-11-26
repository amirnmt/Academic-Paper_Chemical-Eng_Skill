# Literature review: comprehensive, synthesized, critical

Many engineering papers have a separate literature review section between the Introduction and the Methods. In a cross-disciplinary analysis of 433 empirical articles, the most common structure was Introduction – Literature review – Method – Results and Discussion – Conclusion (ILM[RD]C), not plain IMRD. Some fields want a short, selective review inside the Introduction; others expect an extended review almost like a review article. Follow the conventions of your target journal: look at recent papers there.

In computational and process-systems chemical engineering the review usually sits inside the Introduction. In 20 recent *Computers & Chemical Engineering* papers, only two had a separate "Related work" part, and only 2–4 of 90 reactor-modelling and surrogate-modelling papers had a separate literature review section. Their Introductions are correspondingly long (often 1,000–2,500 words) and organized by families of approaches (see `introduction.md` §5a). Everything in this file still applies; the review then forms the middle of the Introduction instead of its own section.

The review shows the state of knowledge, compares approaches, and makes the gap inevitable. Every sentence in it that says something about other work carries a citation (`citation-practice.md` §1–2); when the user names directories of papers, write it from those papers through a claim–evidence map (`citation-practice.md` §3).

## 1. What a literature review is and is not

It is:
- context for your research within what is already known;
- a comparison of studies on the same topic;
- a presentation of different interpretations of the same evidence;
- a demonstration of where knowledge is missing or contested.

It is not:
- a list of summaries ("A did X. B did Y. C did Z.");
- a demonstration of how many papers you found (an excessive reference list signals insecurity rather than scholarship);
- a place for every paper you read.

## 2. Process

1. **Formulate the question the review must answer.** Usually: "Why is a study like ours needed, and what exactly is missing?"
2. **Search systematically.** Use several databases (they never overlap completely). Build search strings with Boolean operators (AND, OR, NOT, quotation marks for phrases). Do several small searches and combine them, narrowing step by step, rather than trying to write one perfect search string. Use citation maps (forward and backward citations) to find key papers.
3. **Read the papers, not just the abstracts.** An abstract is already an interpretation; summarize from the paper itself. Never cite a paper you have not seen. If unavoidable, cite it as "[original] cited in [source you read]".
4. **Make a mind map** of the sub-topics. It gives a proportional structure: decide which sub-topics deserve most space and spend your reading time accordingly.
5. **Take structured notes** (see `evidence-base.md`): what each study did, found, assumed and left open.
6. **Organize by themes** tied to the research question; order them from broad to narrow, ending with the studies closest to yours.
7. **Write each theme as a synthesis** (§4), then **end with the gap**.

## 3. Organization patterns

- **Thematic (default):** one subsection per approach or aspect (kinetics, reactor models, heat transfer, deactivation, data-driven models).
- **Methodological:** grouped by method (experimental, mechanistic modelling, CFD, machine learning, hybrid). Good when your contribution is a method.
- **Problem-solution:** each subsection is one problem and the solutions proposed for it, with their evaluation. Natural for engineering.
- **Chronological:** only within a theme, when the development itself matters (e.g., how reactor models evolved from 1D to 2D).
- **State of the art:** weighted by how much work exists on each aspect.
- **Controversy-focused:** organized around points where studies disagree.

Use subheadings for long reviews. Begin the review with one or two sentences that tell the reader how it is organized.

## 4. Writing a theme: the synthesis paragraph

**First sentence (topic sentence):** a claim about the group of studies, not a description of one paper.
- "Most models of fixed-bed methanol reactors are pseudo-homogeneous."
- "Three strategies have been used to estimate the wall heat-transfer coefficient."
- "Reported effects of the tube-to-particle ratio on wall heat transfer are inconsistent."

**Development:**
1. Group the studies by what they share, with citations where each claim applies.
2. Compare them on the same axes: method, system, conditions, metric, result.
3. Give key numbers where they matter ("errors of 5–15 K in the hot-spot temperature [12–15]").
4. Evaluate in your own voice: strengths, limitations, validity range.

**Last sentence:** what remains open, leading to the next theme or the gap.

Example (structure; replace with verified content):
> Fixed-bed methanol reactors have been modelled at several levels of detail [12–19]. One-dimensional pseudo-homogeneous models reproduce outlet conversion at low computational cost [12–15], whereas two-dimensional models also resolve radial temperature gradients and hot spots [16–19]. However, both groups rely on wall heat-transfer correlations fitted at large tube-to-particle diameter ratios, and none of the two-dimensional studies compared predicted radial profiles with measurements. Validation at low ratios has received far less attention [20,21].

## 5. Synthesis techniques

- **Group:** "Similar trends were reported for … [3–6]."
- **Contrast:** "In contrast to [7], [8] found …, probably because …"
- **Quantify the range:** "Reported wall heat-transfer coefficients range from A to B W m⁻² K⁻¹ depending on the Reynolds number [9–14]."
- **Classify:** "Three modelling strategies can be distinguished: …, … and …"
- **Trace development:** "Early models assumed …[2]; later studies added … [5,6]; recent work has … [9]."
- **Generalize carefully:** "Taken together, these studies indicate that …"
- **Taxonomy with a citation group per class:** "… has been addressed by A [3,4], B [5,6] and C [7–9]"; then one sentence per class.
- **Chain of named studies:** "X et al. (2019) fitted …, Y and Z (2021) extended … to …, and W et al. (2023) validated … against plant data." Keep to three or four studies, then synthesize.
- **Problem → remedy → residual limitation:** a practical difficulty, the methods proposed for it [refs], and what they still assume [refs].
- More paragraph patterns: `introduction.md` §6a; sentence patterns with several sources: `citation-practice.md` §7.
- **Tabulate:** a summary table of the closest 10–20 studies (method, system, regime, key assumption, validation, metric, result). Refer to it in the text and discuss the pattern it shows, not each row.

## 6. Citing within the review

- **Information-prominent** (the finding is the subject; most sentences): "Radial gradients are significant when … [5,7]."
- **Author-prominent** (the researcher is the subject; when the specific study, its method or a disagreement matters): "Smith et al. [5] measured …".
- Put names or dates into the sentence only when they matter: "The first two-dimensional model was proposed in 1965 [3]."
- Place each citation where its claim is, not all at the end of a long sentence: "We compared the model of Smith [4] with the correlation of Lee [9]" rather than "We compared the model and the correlation [4,9]."
- Order multiple citations as the journal requires (numerical, chronological or alphabetical).
- How many per sentence: one for a specific finding, two or three for a general statement, more only for "widely studied" claims (`citation-practice.md` §5). In *Computers & Chemical Engineering* papers [J-obs], a cited sentence carries a median of 1.8 sources and half of the literature sentences are cited; under the rule of this skill, all sentences about other work are.
- Tell the reader what each cited work found and how it relates to yours. A "handwaving reference" ("see the excellent work of Smith [4]") tells the reader nothing.

## 7. Reporting verbs and their strength

Choose the verb that matches the source's certainty and your attitude to it:
- **Neutral:** describe, report, present, examine, investigate, study, note, observe, measure, model.
- **Tentative (source is cautious):** suggest, propose, hypothesize, speculate, indicate.
- **Strong (source is confident, or you accept it):** show, demonstrate, establish, confirm (use "prove" rarely).
- **Distancing (you may disagree):** claim, assert, assume.

Do not upgrade a source: if the authors wrote "may", do not write "showed".

Tense: present simple for what the field accepts ("Cu/ZnO/Al2O3 is the standard industrial catalyst"); past simple for what a specific study did ("Lee et al. [5] modelled …"); present perfect for lines of research continuing to now ("Several authors have proposed …").

## 8. Being critical without being rude

- Evaluate, do not attack. "Smith (2015) did not study X" is acceptable; "Smith (2015) failed to/ignored/totally overlooked X" is not.
- Present the strength of your approach rather than the weakness of others: "The present model resolves both axial and radial profiles" instead of "previous models were inadequate".
- Hedge criticism: "may have been limited by", "did not account for", "was restricted to", "applies only to".
- Constructive criticism names what is missing and why it matters: "These correlations were fitted to non-reacting data; whether they hold under reaction conditions has not been tested."
- When paraphrasing, keep the original authors' emphasis; reordering their points can change the meaning.

## 9. Handling disagreement and counterarguments

- Include results that disagree with your expectation and explain why they may differ (conditions, methods, scale, assumptions). A one-sided review looks biased.
- Present the strongest opposing view fairly, with evidence, then explain why your position still holds, or acknowledge that it holds only under certain conditions.
- Signal clearly whose view is whose: "It has been argued that … [7]. However, …".

## 10. Your voice

Each paragraph should contain your evaluation before or after the sources. A review written only in the voice of the cited authors gives the reader no reason to believe the gap exists.

## 11. Ending the review: the gap

Close with a short paragraph that:
1. summarizes what the field has established (one or two sentences);
2. states what is missing, contradictory or untested, with reference to the studies reviewed;
3. explains why that matters;
4. leads directly to the objective of the present study.

Example structure:
> In summary, … has been established for … [refs]. However, … remains untested under … conditions, which limits … . The present study addresses this gap by …

Other closing forms:
- "These models are effective for …, yet they share one limitation: … [refs]."
- "Despite these advances, … remains [limited / unaddressed] [refs]: first, …; second, …"
- "Taken together, these studies show that … [refs], but none of them …"
The closing paragraph cites the closest studies again where it names their limitation.

## 12. Planning the review before searching: two levels and method groups

Plan what each part of the front matter must establish before searching, so the Introduction and the literature review do not cite the same papers for the same purpose. (Idea adapted from the outline stage of PaperOrchestra, Song et al., 2026; written for engineering articles.)

**Introduction: the broad level** (typically 10–20 sources)
- The context and why the problem matters, with numbers: production scale, energy use, emissions, cost, safety (each cited).
- One or two recent reviews of the field.
- The foundational papers of each sub-field the study draws on.
- The gap, stated only as widely as your own results can answer it.

**Literature review: the technical level** (typically 30–50 sources in a full article)
Divide the prior work closest to yours into **2–4 groups of methods** (for example: first-principles reactor models; data-driven surrogates; hybrid models; sensitivity and optimization studies). For each group, write down before searching:

| Item | Content | Example (EO reactor) |
|---|---|---|
| Group | the methodological category | transient fixed-bed reactor models |
| What it does well | established strengths, cited | accurate steady-state profiles against plant data [refs] |
| Suspected limitation | what you expect is missing, from your own study's idea | few validated transient models of industrial reactors |
| Searches for evidence | narrow queries that would document that limitation (or refute it) | "transient" AND "ethylene oxide" AND "reactor model"; papers that state their steady-state assumption |
| Bridge | how your study addresses it, limited to what your results show | transient model benchmarked against [plant data] |

Rules:
- A limitation enters the paper only when the papers found support it, with citations (§11). If the search does not support it, change the limitation, not the evidence.
- The bridge column may contain only claims that the results log supports (`research-integrity.md` §1, §4).
- Do not search for new competitors after your results are fixed in order to claim you beat them; later papers are concurrent work (`research-integrity.md` §4).

## 13. Planning a large citation count (e.g. 70+)

- Allocate citations per theme from the theme map (`evidence-base.md` §3), not per paragraph.
- Cover each theme with 1–2 reviews, the foundational papers, the most recent strong papers, and the closest competitors.
- One claim normally needs 1–3 citations; more only for "widely studied" statements.
- Every citation must be relevant and verified. If the repository cannot support the target, report the thin themes to the author instead of padding.

## 14. Paraphrase and quotation

- Paraphrase in your own words and sentence structure; changing a few words is not paraphrasing.
- Quote only when the exact wording matters (definitions, a disputed claim). Rare in engineering; use quotation marks and the source.
- Cite ideas, not only words. Reusing your own earlier text without citation is self-plagiarism.

## 15. Checklist

- [ ] Organized by themes linked to the research question, broad → narrow; organization announced at the start.
- [ ] Each theme opens with a claim and is synthesized (grouped, compared, evaluated), not listed.
- [ ] Closest studies compared on the same axes, ideally in a table.
- [ ] Disagreeing results included and explained.
- [ ] Your evaluation present in every paragraph; criticism constructive.
- [ ] Reporting verbs match the sources' certainty; tenses consistent.
- [ ] Every sentence about other work cited; limitations attributed to the works; citations placed where their claims are; no handwaving references; no unseen papers.
- [ ] Ends with a gap that the Introduction's objective answers.
- [ ] All citations verified; thin themes reported, not padded.
- [ ] Introduction and literature review planned at their two levels (§12); each method group has a cited limitation and a bridge supported by the results.
- [ ] Scored with the rubric in §16; every axis below 56 revised.

## 16. Scoring rubric for the literature review (self-review)

Score the Introduction and the literature review together, as a sceptical reviewer would, and only on what is written. (Axes and caps adapted from the literature-review rater of PaperOrchestra, Song et al., 2026; rewritten for engineering articles.)

**Scale (0–100 per axis):** up to 20, not publishable; 21–40, major gaps; 41–55, usable with clear weaknesses; 56–70, sound; 71–85, convincing; 86–92, outstanding; above 92, rare. Expect most drafts at 45–70; a score above 85 needs explicit evidence on every axis.

| Axis | What is judged | Cap |
|---|---|---|
| 1. Coverage | all relevant threads, foundational and recent work, no obvious omission; citation count compared with the journal's typical count (`citation_density.py` benchmarks) | count below half the journal's typical count for a broad problem: ≤ 55 |
| 2. Relevance and focus | citations serve the research question; no padding or tangents | – |
| 3. Critical analysis and synthesis | grouped by theme, compared, evaluated; trade-offs and disagreements discussed | mostly paper-by-paper description: ≤ 60 |
| 4. Positioning | a gap grounded in cited work; explicit difference from the closest studies; why it matters | novelty asserted without comparison to the closest work: ≤ 60 |
| 5. Organization and language | logical order (broad → narrow), signposting, defined terms | – |
| 6. Citation practice | key claims cited; sources credible and verified; balance of foundational and recent | many citations but poorly integrated: ≤ 65 |

Overall score: rarely above 75 if any axis is below 50. Write two sentences of evidence for each score, then revise the lowest axis first. A high citation count alone never raises a score; relevance and synthesis must justify it.
