# Introduction: from the broad field to your niche

The Introduction gives readers enough background to understand and evaluate your results without reading earlier papers, explains why the study was needed, and states what it does. Readers decide here whether to continue; reviewers decide here whether the work is new. If the problem is not stated clearly, nobody will care about the solution.

Use with `paragraphs-and-sentences.md` (how to build each paragraph), `vocabulary-by-section.md` §2 (words) and `phrasebank.md` (sentence stems).

## 1. What the Introduction must do

1. State the nature and scope of the problem and why the field matters.
2. Review the most relevant previous work briefly and selectively.
3. Identify the gap the study addresses.
4. State the objective (and, if appropriate, hypotheses or research questions).
5. State the approach and, if needed, why this method was chosen.
6. In many engineering journals: state the principal results and contributions, and outline the paper.

Do not keep readers in suspense. A research article is not a detective story: readers want to know early what was found. Some overlap with the abstract is acceptable.

## 2. Shape: the funnel (and its mirror)

The paper has an hourglass shape. The Introduction narrows from the general field to your specific question; the Methods and Results are the narrow centre; the Discussion widens again. What the Introduction opens, the Discussion closes in reverse order:

| Introduction | Discussion (mirror) |
|---|---|
| importance of the field (getting the reader in) | wider implications (getting the reader out) |
| map of previous research | where your results sit on that map |
| the gap or problem | to what extent the gap is closed |
| the present work (interface into Methods) | restatement of your findings (interface out of Results) |

Example narrowing (illustrative running example used throughout this skill: a fixed-bed methanol synthesis reactor):
1. Methanol is a major chemical and energy carrier; its production is large-scale and energy-intensive.
2. It is produced over Cu/ZnO/Al2O3 catalysts in multitubular fixed-bed reactors; heat removal governs conversion, selectivity and catalyst life.
3. Reactor models are used for design, optimization and scale-up.
4. Most models rely on wall heat-transfer correlations derived for large tube-to-particle diameter ratios, while industrial tubes often have small ratios.
5. Gap: the accuracy of these correlations at low ratios has not been assessed against measured temperature profiles.
6. This work: a two-dimensional model that compares several correlations against pilot-scale temperature profiles.

## 3. How to start: the first sentence

Most published introductions do **not** start with the problem or the aim. They start by establishing the importance of the field or with a key background fact.

Good openings:
- **Importance with a number and citation:** "Methanol is produced at a scale of about [value] Mt per year, mainly in multitubular fixed-bed reactors [1,2]."
- **Role of the process or system:** "Fixed-bed reactors are the standard equipment for strongly exothermic gas–solid catalytic reactions [3]."
- **Current focus of the field:** "The design of fixed-bed reactors increasingly relies on detailed two-dimensional models [4–6]."
- **A key practical problem stated as a fact:** "Hot spots limit the conversion that can be reached in exothermic fixed-bed reactors [7]."

Avoid:
- vague universal truths ("Energy is important for modern society");
- dramatic or promotional openings ("In today's rapidly evolving world …");
- starting with your aim ("The aim of this paper is …") or your method;
- a question as the first sentence.

## 4. The four-part model (general STEM)

Use all four parts in this order. Parts 1 and 2 often alternate before the gap.

**Part 1. Establish the importance of the field**
- Practical, industrial, environmental or economic relevance, with 2–4 strong citations.
- Background facts the reader needs.
- Definitions of key terms in the title.
- The general problem area or current research focus.

**Part 2. Previous and current research**
- What has been done and what it achieved, grouped by approach rather than listed paper by paper.

**Part 3. The gap**
- What is unknown, contradictory, untested, oversimplified or limited. Signal it with: however, although, while, despite, nevertheless.
- State the specific problem you address and, where useful, a prediction to be tested.

**Part 4. The present paper**
- Objective, approach and its justification, contributions; optionally the main finding and the paper outline.

## 5. Engineering framework: problem → solution → evaluation

Engineering research is usually problem-solving and incremental. An introduction often reads better when Part 1 is written as a problem-solution cycle (from an analysis of 33 engineering introductions).

**Move 1. Establish the territory as a problem-solution cycle**
- 1.1 Situation: the process, material, technique or system and why it matters in practice.
- 1.2 Problem area: what goes wrong or is limited in that situation.
- 1.3 Previous solutions and their evaluation: what others proposed and how well it worked. Repeat for each family of approaches: solution → evaluation → remaining issue → next solution → evaluation.

**Move 2. Establish the niche**
- 2.1 The gap or problem not yet solved (present in most engineering introductions).
- 2.2 Positive justification: why solving it is worthwhile (rare, but strong when the benefit is concrete).

**Move 3. Present the study** (approximate frequency in engineering introductions)
- 3.1 Announce the study, descriptively or by purpose (always).
- 3.4 Summarize the methods or justify the procedure: why this method over alternatives (almost always).
- 3.5 Announce the principal outcomes (about two thirds).
- 3.8 Outline the structure of the paper (about two thirds).
- 3.6 State the value of the study (sometimes).
- 3.2 Research questions or hypotheses (rare in engineering; useful for validation studies).
- 3.3 Definitions, 3.7 related work, 3.9 notation (rare here; put them in their own section).

**Chemical and process engineering** (move analysis of five engineering fields): introductions often give a short statement of established knowledge and then move quickly to previous research; background and literature review may alternate several times. Many papers have a separate literature review section; then the Introduction stays short.

## 6. Paragraph-by-paragraph plan

A typical engineering Introduction has 4–6 paragraphs (about 1–1.5 pages, or 300–700 words).

**Paragraph 1. Importance and context**
- First sentence: importance or key fact, with citation.
- Develop: how the process works → what determines performance → the general problem area.
- Last sentence: narrows towards the aspect your paper studies.

**Paragraphs 2–3. What has been done (state of the art)**
- First sentence: a claim about the group of studies ("Two modelling approaches dominate the literature on …").
- Develop: what each group did and achieved, with citations placed where each applies; compare them; evaluate what each leaves open.
- Last sentence: the remaining limitation that leads to the next paragraph or to the gap.
- Tense: past for specific studies, present perfect for research up to now, present for accepted knowledge.

**Paragraph 4. Gap**
- First sentence: "However, …" + the specific gap, supported by the studies just cited.
- Develop: why the gap matters (accuracy, safety, cost, design decisions, understanding).

**Paragraph 5. The present work**
- First sentence: "This study therefore …" / "To address this gap, we …" with the objective.
- Develop: approach and why it suits the problem; contributions (2–4, specific and checkable); optionally main finding; optionally outline ("Section 2 describes …").
- Last sentence: leads into the Methods.

## 7. Writing the gap

The gap is the pivot of the paper. It must be specific and supported by the studies you cited.

Types of gap:
- Not studied: "To date, no study has coupled X with Y under Z."
- Limited scope: "Previous models were restricted to steady-state operation [8–11]."
- Oversimplification: "These models neglect radial gradients, which become significant at high heat release."
- Contradiction: "Reported effects of X on Y conflict: [5] found an increase, [6] a decrease."
- Lack of validation: "Few models have been validated against pilot- or industrial-scale data."
- Method limitation: "Purely data-driven models do not guarantee closure of mass and energy balances."

Good gap statements name the studies, the limitation and the condition. Weak ones say "little is known" or "this topic is interesting". Interesting is not a justification: say why the gap matters.

Tense matters here: "little attention **has been** paid to X" means the gap still exists now (and this paper addresses it). "Little attention **was** paid to X in 2015" means only then; the gap may have been closed since.

## 8. Objective, hypotheses, contributions

- One objective stating the exact property or parameter, the system, and the means. Example: "This study aims to quantify the error of five wall heat-transfer correlations in predicting the axial and radial temperature profiles of a pilot-scale methanol synthesis reactor with a tube-to-particle diameter ratio of [value], using a two-dimensional pseudo-homogeneous model."
- Use the same wording of the objective in the abstract, Results, Discussion and Conclusion. This repetition helps the reader.
- Hypotheses: state what you expect and why, based on prior knowledge; keep them few (no more than about five). Statistical testing works through a null hypothesis; keep the scientific hypothesis and its null form distinct.
- Contributions: 2–4 specific, checkable items. "(i) a comparison of …; (ii) a validation against …; (iii) a recommendation for …".
- Justify the method briefly (why 2D, why pseudo-homogeneous, why this data-driven model). Details belong in Methods.
- If a preliminary version (conference paper) or closely related papers exist, cite them here, usually near the end.

## 9. Citations in the Introduction

- Be selective: the most relevant and the most recent strong work. The exhaustive review belongs in the literature review.
- Tell the reader why each citation matters ("Smith et al. [4] showed that …"), not "see the elegant work of Smith [4]".
- Place the citation where the claim it supports appears in the sentence, not all at the end.
- Use review papers for broad background; cite original studies for specific findings.
- Cite conflicting data where it shows genuine uncertainty.

## 10. Tense

| Content | Tense | Example |
|---|---|---|
| Established facts | present simple | "Methanol synthesis is strongly exothermic." |
| A specific study's finding | past simple | "Smith et al. [4] reported that …" |
| Research up to now; open gaps | present perfect | "Several studies have modelled …"; "No study has yet …" |
| What this paper does | present simple | "This paper presents …" |
| Your hypothesis | past + present | "We hypothesized that wall heat transfer controls the hot-spot temperature." |
| Your objective; your findings | past simple | "This study aimed to …"; "We found that …" |

Present simple for a published finding treats it as established knowledge; past simple ties it to one study. Choose deliberately.

## 11. Voice and terms

- "We" means the authors or research team, never people in general. For general statements use "It is known that …" or the fact itself.
- A dummy subject ("This paper presents …", "The present study compares …") is clearer than an agentless passive ("A comparison is presented").
- Define specialized terms and abbreviations at first use; readers from neighbouring fields will read the paper.
- Mark your own work clearly: "here", "in this study", "the present model".

## 12. Worked example (structure annotated; content illustrative)

> [P1: importance → background → problem area] Methanol is one of the most widely produced chemicals, with an annual production of about [value] Mt [1]. Most of it is synthesized from syngas over Cu/ZnO/Al2O3 catalysts in multitubular fixed-bed reactors cooled by boiling water [2,3]. Because the reaction is strongly exothermic, the rate of heat removal through the tube wall determines the hot-spot temperature, which in turn limits conversion and catalyst life [4].
>
> [P2: previous research, approach 1 → evaluation] Reactor models are therefore widely used for design and scale-up. One-dimensional pseudo-homogeneous models predict outlet conversion at low computational cost [5–7], but they cannot resolve the radial temperature profile that controls the hot spot. Two-dimensional models resolve this profile [8–11]; their accuracy, however, depends on the effective radial conductivity and the wall heat-transfer coefficient, which are taken from correlations [12–14].
>
> [P3: previous research, approach 2 → remaining issue] Most of these correlations were derived for tube-to-particle diameter ratios above about 10 [12,13]. Industrial methanol reactors often operate at lower ratios, where wall effects and channelling become important [15]. Corrections for low ratios have been proposed [16,17], but they were validated mainly with non-reacting heat-transfer experiments.
>
> [P4: gap → why it matters] To date, the performance of these correlations has not been assessed against temperature profiles measured in a reacting methanol synthesis bed at low tube-to-particle ratios. Without such an assessment, the predicted hot-spot temperature, and therefore the safe operating window, remains uncertain.
>
> [P5: present work → approach → contributions → outline] This study therefore compares five wall heat-transfer correlations in a two-dimensional pseudo-homogeneous model against axial and radial temperature profiles measured in a pilot-scale reactor with a tube-to-particle ratio of [value]. The contributions are (i) a quantitative comparison of the correlations under reacting conditions, (ii) an identification of the conditions under which each correlation fails, and (iii) a recommendation for reactor design at low ratios. Section 2 describes the reactor and the model, Section 3 presents the comparison, and Section 4 discusses its implications.

(Citations, authors and values in this example are placeholders, not real references.)

## 13. Common mistakes

- Starting with the aim, a method, or a sweeping generalization.
- A list of studies without grouping, comparison or evaluation.
- A gap that is not supported by the cited literature, or a vague gap ("little research exists").
- The objective stated differently in the abstract, introduction and conclusion.
- Citing every paper read; citations not placed where they apply.
- Undefined abbreviations; jargon from a narrow subfield.
- Tense changes without reason (past ↔ present perfect changes meaning).
- Holding back the main finding until the end of the paper.

## 14. Checklist

- [ ] Opens with importance or a key fact (with citation), not with the aim.
- [ ] Funnel from broad to narrow; each paragraph narrower than the one before.
- [ ] Previous work grouped, compared and evaluated; citations placed where they apply.
- [ ] Gap specific, supported by cited studies, and justified (why it matters).
- [ ] Objective states property, system and means; same wording in abstract and conclusion.
- [ ] Method choice justified briefly; contributions specific and checkable.
- [ ] Tense matches function; "we" used only for the authors.
- [ ] Abbreviations and specialized terms defined; within length.
- [ ] First sentences of the paragraphs, read alone, tell the argument.
