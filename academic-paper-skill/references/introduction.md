# Introduction: from the broad field to your niche

The Introduction gives readers enough background to understand and evaluate your results without reading earlier papers, explains why the study was needed, and states what it does. Readers decide here whether to continue; reviewers decide here whether the work is new. If the problem is not stated clearly, nobody will care about the solution.

Use with `citation-practice.md` (which sentences need a citation, and how many), `paragraphs-and-sentences.md` (how to build each paragraph), `vocabulary-by-section.md` §2 (words) and `phrasebank.md` (sentence stems). For the target journal's own habits, read its `section_models.md` and `citation_benchmarks.json` in `resources/journals/<journal>/`.

Levels: **[Rule]** standing rule of this skill; **[G]** general; **[D]** chemical and process engineering; **[J-obs]** observed in published papers of one journal (here *Computers & Chemical Engineering*, 20 research articles). See `journal-profile.md` §0.

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

In 20 *Computers & Chemical Engineering* papers [J-obs], 17 opened with the importance of the process, product or property, two with the importance of a class of methods, and one with a pointed claim about current practice. Several combined importance and difficulty in the first one or two sentences ("X governs …, yet its prediction remains difficult because …"). Only 6 of the 20 first sentences carried a citation. **Under the rule of this skill, the first sentence is a factual claim and is cited** [Rule].

Avoid:
- vague universal truths ("Energy is important for modern society");
- dramatic or promotional openings ("In today's rapidly evolving world …");
- starting with your aim ("The aim of this paper is …") or your method;
- a question as the first sentence.

## 3a. Introducing concepts and terms

A term from the title, a method or a quantity the argument depends on is introduced once, where it first matters, and then used consistently.

| Device | Pattern (placeholders) | Use |
|---|---|---|
| Acronym at first use | "model predictive control (MPC)" | Only for terms used again; define again in the abstract if used there |
| Definition sentence | "[Term] is a [class] that [distinguishing function] [ref]." | A method or concept the reader may not know |
| Appositive definition | "[Term], a [class] that [function], has been applied to … [refs]." | Defines and makes a claim in one sentence |
| Fixed short name | "[Full term], hereafter [short term], …" | When a longer term is shortened for the rest of the paper |
| Gloss in brackets | "(i.e., …)", "(e.g., …, …)" | Clarifies one word or gives examples without a new sentence |
| Definition attributed to a source | "[Author] (year) defines [term] as …" | When the exact definition matters; rare in engineering |
| Classification | "[Property] can be static (…) or dynamic (…) [refs]." | Introduces the categories the review will use |

Order inside a paragraph [G]: define the concept → state why it matters for the problem (cited) → state its limitation (attributed to the works that show it) → lead to the next concept or approach. Definitions of methods carry a citation to the original or a standard source [Rule].

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

**Chemical and process engineering** [D] (move analysis of five engineering fields): introductions often give a short statement of established knowledge and then move quickly to previous research; background and literature review may alternate several times. Many papers have a separate literature review section; then the Introduction stays short. Computational and process-systems journals are an exception: there the review sits inside the Introduction (§5a).

## 5a. Computational and process-systems papers

Based on 20 recent research articles in *Computers & Chemical Engineering* (methods applied to processes: modelling, surrogates, optimization, control, soft sensing). The literature review is part of the Introduction, which is therefore long (often 1,000–2,500 words).

| Move | Content | How common |
|---|---|---|
| I1 Territory | Importance of the process, product or property (scale, uses, energy, cost, safety) | Opening move in most papers; a few open with the method or with a striking claim |
| I2 Problem | Why modelling, prediction or control of this system is hard (coupled phenomena, unknown parameters, scarce data, delays) | Nearly all |
| I3 Literature by approach family | First-principles → data-driven → hybrid, or "Regarding A … Regarding B …"; chronological within a family; mostly citation groups in brackets (narrative citations under 5 % in most papers), with a few papers writing the review as a chain of named studies, each with its method and result | All |
| I4 Evaluation | Strength and limit of each family, closing each group | Common |
| I5 Gap | Focus mismatch (A studied, not B); scale gap (no industrial data); combination gap (no approach handles A, B and C together); integration gap; enumerated limitations ("First … Second … Finally …") | All |
| I6 Present work | "In this work, we …"; "To address these challenges, this paper proposes …" | All |
| I7 Approach in steps | "First, … Second, … Finally, … is compared with …" | Common in method papers |
| I8 Contributions | Numbered or "First … Second … Third" list, often 3–4 items, each answering one stated limitation | 12 of 20 enumerate objectives or contributions |
| I9 Scope | What is and is not claimed: virtual plant vs. real plant, operating range, validation data | Several industrial and data-driven papers |
| I10 Roadmap | "The remainder of this paper is organized as follows …" | 11 of 20 |

Length and citation density [J-obs]: median 9 paragraphs (7–13), 1,364 words (1,037–1,704), 36 unique references (25–43); 38 % of all sentences cited, falling from about 54 % in the opening and 44 % in the literature part to 4 % in the present-work part (`citation-practice.md` §6). Three of the 20 used subheadings inside the Introduction, and one placed the review in a separate "Related works" section.

The usual section order that follows is: Introduction → process, system or data description → methodology (one or more sections) → case study → Results and discussion (combined in about half) → Conclusions.

## 6. Paragraph-by-paragraph plan

A typical engineering Introduction with a separate literature review has 4–6 paragraphs (about 1–1.5 pages, or 300–700 words) [G]. When the review sits inside the Introduction, paragraphs 2–3 below expand into one paragraph per approach family or sub-problem, and the Introduction grows to 8–14 paragraphs (C&CE median 9; §5a) [J-obs].

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

## 6a. The literature part: paragraph patterns

Seven ways of building the paragraphs between the background and the gap [G, J-obs]. Most Introductions combine two or three.

1. **Approach family.** Topic sentence naming the family → what its members do, with citation groups → strongest study in more detail → limitation relative to your problem. One paragraph per family, ordered toward the approach closest to yours.
2. **Taxonomy sentence.** One sentence that classifies the field, with a citation group after each class ("… have been addressed by decomposition [refs], surrogate-based [refs] and … [refs] methods"); the following sentences take the classes one by one.
3. **Limitation chain.** Every paragraph ends with the same kind of limitation, measured against the capability your work provides ("… does not represent the closed-loop response of the equipment"). The gap paragraph then collects these limitations, numbered. Strong when the contribution is one missing capability.
4. **Problem → remedy → residual limitation.** "Another challenge is [problem]. To address it, [remedies] have been proposed [refs]. These methods, however, assume [assumption] [refs]." One paragraph per practical difficulty (scarce labels, changing conditions, delays).
5. **Lineage.** "Early models … [ref]. Building on this, … [ref] … More recently, … [refs]." Within one family, when the development itself explains the gap.
6. **Chain of named studies.** Author-prominent sentences, one or two studies each, with what they did and found; then a synthesis sentence ("These models are effective for …, but all represent … as …"). Use when the specific studies are few and close to yours.
7. **Position of the authors' own earlier work.** "In previous work (ref), we … This showed … but left … open." Placed last before the gap, because it is the closest study.

Close the literature part with a synthesis sentence that states what the reviewed work shares and what it lacks, attributed to the works ("In summary, … [refs]; however, none of these … ").

Limitations of earlier work [G, Rule]:
- State them where the work is described, not in a separate list of complaints.
- Attribute them: a limitation of specific studies cites those studies; a limitation of a whole family cites representative members or a review. In the analysed papers [J-obs], sentences stating limitations were cited less often (42 %) than other background and literature sentences (52 %); under the rule they are claims about other work and are cited.
- Describe what the work does not cover or assumes ("assumes full state measurement", "was validated only with pilot-plant data"), not that it is poor.

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

Forms of the gap sentence seen in process-systems papers [J-obs; templates in `phrasebank.md` §1.6; a paper may use more than one]:
- **Integration gap** (most frequent, 6 of 20): "No existing approach combines A, B and C within one framework." / "These methods were developed separately and lack …"
- **Assumption or representation gap** (5 of 20): "Existing models assume … / represent … only as …, which …"
- **Scale or realism gap** (3 of 20): "Few studies use industrial data / address … at plant scale."
- **Enumerated limitations** (4 of 20): "Although these studies have …, several limitations remain. First, … Second, … Third, …", each limitation with its citations, followed by "These limitations motivate …".
- **Focus mismatch:** "These studies focus on A, whereas B has received little attention."
- **Closest-work gap:** "To our knowledge, no study has …; the closest are [refs], which …"

Justify the gap [G]: say what it costs (accuracy, safety margin, design decision, operating cost, computation) and for whom. In the analysed papers the justification is usually one sentence directly after the gap or folded into it ("…, so a prediction that cannot be explained is difficult to turn into an operating decision").

Cite in the gap paragraph [Rule]: the few studies that exist, the closest studies and their limitation, or the review that supports a "widely assumed" claim. In the analysed papers about 40 % of gap sentences carried a citation.

Tense matters here: "little attention **has been** paid to X" means the gap still exists now (and this paper addresses it). "Little attention **was** paid to X in 2015" means only then; the gap may have been closed since.

## 8. Objective, hypotheses, contributions

From gap to objective [G, J-obs]: the sentence that states the present work begins by pointing back at the gap ("To address these limitations, …", "To this end, …", "Accordingly, …", "Against this background, …", "These limitations motivate …"). Use the gap's own key terms in the objective so that the link is visible.

Mirror the limitations [J-obs]: in papers with enumerated limitations, the contributions are listed in the same order and answer them one by one. Write the contributions list from the gap list, then check that every contribution answers a limitation and every limitation is answered or declared out of scope.

Novelty, stated with care [G]:
- Say exactly what is new and relative to what: "To our knowledge, this is the first … that both … and …"; "The novelty lies in combining … with …"; "The methods are established; what is new is their use on …". Overstated novelty invites the reviewer to find the counterexample.
- "Novel" in every second sentence weakens the claim; state the new element instead.
- A preview of the main finding ("The analysis shows that …") is common in recent papers and helps the reader.

Scope [J-obs: 6 of 20 recent papers]: state what the study does not claim or cover ("The models describe associations within the observed operating range, not the mechanism"; "Environmental and safety constraints are outside the scope"; "A simulated plant is used; experimental validation is future work"). Put it after the approach or after the contributions.

- One objective stating the exact property or parameter, the system, and the means. Example: "This study aims to quantify the error of five wall heat-transfer correlations in predicting the axial and radial temperature profiles of a pilot-scale methanol synthesis reactor with a tube-to-particle diameter ratio of [value], using a two-dimensional pseudo-homogeneous model."
- Use the same wording of the objective in the abstract, Results, Discussion and Conclusion. This repetition helps the reader.
- Hypotheses: state what you expect and why, based on prior knowledge; keep them few (no more than about five). Statistical testing works through a null hypothesis; keep the scientific hypothesis and its null form distinct.
- Contributions: 2–4 specific, checkable items. "(i) a comparison of …; (ii) a validation against …; (iii) a recommendation for …".
- Justify the method briefly (why 2D, why pseudo-homogeneous, why this data-driven model). Details belong in Methods.
- If a preliminary version (conference paper) or closely related papers exist, cite them here, usually near the end.

## 9. Citations in the Introduction

The full guidance is in `citation-practice.md`. The essentials:
- **Every sentence that states a fact about the world or about other work carries a citation** [Rule]; exempt are your own objectives, methods, contributions, findings and outline, and inferences drawn visibly from sources cited in the same paragraph.
- When the user gives directories of papers, write from them through a claim–evidence map; mark `[CITATION NEEDED]` where they do not support a claim. Never fill the gap from memory.
- Density falls across the Introduction: high in the background and literature parts, some in the gap, almost none in the present work and roadmap. Check with `scripts/citation_density.py audit`.
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
> [P2: previous research, approach 1 → evaluation] Reactor models are therefore widely used for design and scale-up [5,8]. One-dimensional pseudo-homogeneous models predict outlet conversion at low computational cost [5–7], but they cannot resolve the radial temperature profile that controls the hot spot. Two-dimensional models resolve this profile [8–11]; their accuracy, however, depends on the effective radial conductivity and the wall heat-transfer coefficient, which are taken from correlations [12–14].
>
> [P3: previous research, approach 2 → remaining issue] Most of these correlations were derived for tube-to-particle diameter ratios above about 10 [12,13]. Industrial methanol reactors often operate at lower ratios, where wall effects and channelling become important [15]. Corrections for low ratios have been proposed [16,17], but they were validated mainly with non-reacting heat-transfer experiments.
>
> [P4: gap → why it matters] To date, the performance of these correlations has not been assessed against temperature profiles measured in a reacting methanol synthesis bed at low tube-to-particle ratios; the closest studies used non-reacting beds [16,17] or compared only outlet conversion [8,9]. Without such an assessment, the predicted hot-spot temperature, and therefore the safe operating window, remains uncertain.
>
> [P5: present work → approach → contributions → outline] This study therefore compares five wall heat-transfer correlations in a two-dimensional pseudo-homogeneous model against axial and radial temperature profiles measured in a pilot-scale reactor with a tube-to-particle ratio of [value]. The contributions are (i) a quantitative comparison of the correlations under reacting conditions, (ii) an identification of the conditions under which each correlation fails, and (iii) a recommendation for reactor design at low ratios. Section 2 describes the reactor and the model, Section 3 presents the comparison, and Section 4 discusses its implications.

(Citations, authors and values in this example are placeholders, not real references.)

## 13. Common mistakes

- Starting with the aim, a method, or a sweeping generalization.
- A list of studies without grouping, comparison or evaluation.
- A gap that is not supported by the cited literature, or a vague gap ("little research exists").
- The objective stated differently in the abstract, introduction and conclusion.
- Citing every paper read; citations not placed where they apply.
- Factual sentences without a citation, especially the first sentence and the limitations of earlier work.
- Citation dumps: six or more sources after one sentence that none of them supports entirely.
- A gap paragraph that cites nothing, so the reader cannot check that the closest work was considered.
- Undefined abbreviations; jargon from a narrow subfield.
- Tense changes without reason (past ↔ present perfect changes meaning).
- Holding back the main finding until the end of the paper.

## 14. Checklist

- [ ] Opens with importance or a key fact (with citation), not with the aim.
- [ ] Funnel from broad to narrow; each paragraph narrower than the one before.
- [ ] Previous work grouped, compared and evaluated; citations placed where they apply.
- [ ] Every factual or literature-based sentence cited (`citation_density.py audit` lists the exceptions); each source supports its sentence; no `[CITATION NEEDED]` left unreported.
- [ ] Limitations of earlier work attributed to the works; the gap paragraph cites the closest studies.
- [ ] Contributions answer the stated limitations one by one; scope stated.
- [ ] Gap specific, supported by cited studies, and justified (why it matters).
- [ ] Objective states property, system and means; same wording in abstract and conclusion.
- [ ] Method choice justified briefly; contributions specific and checkable.
- [ ] Tense matches function; "we" used only for the authors.
- [ ] Abbreviations and specialized terms defined; within length.
- [ ] First sentences of the paragraphs, read alone, tell the argument.
