# Paragraphs and sentences: how to start, develop and connect ideas

Every section of a paper is built from paragraphs, and every paragraph from sentences that carry the reader from known information to new information. Read this file before drafting any section. The section files (`introduction.md`, `results-language.md`, etc.) say *what* each paragraph should contain; this file says *how* to build it.

## 1. The paragraph: one controlling idea

A well-built academic paragraph has three parts.

1. **Topic sentence (controlling idea).** States the paragraph's point in general terms, near the start, and shows how it connects to the argument of the section.
2. **Supporting sentences.** Explain, prove or develop that point. Every supporting sentence must relate to the topic sentence, and none should simply repeat it.
3. **Closing or linking sentence (optional).** Interprets what was shown, or prepares the next paragraph.

**Rules**
- One controlling idea per paragraph. A new idea, a contrasting argument, or a new aspect of an idea starts a new paragraph.
- Typical length in research articles: 4–8 sentences (about 100–200 words). Clusters of one-sentence paragraphs and paragraphs running over most of a page are both signs of poor organization.
- Check focus (no drift into other topics), coherence (sentences follow logically) and development (the idea is explained and supported, not just stated).
- Direct expression: international journals expect the main point first and the details after it. Do not circle around the point and reveal it at the end.

**The skim test.** Readers skim by reading the first sentence of each paragraph. Read only the first sentences of a section: they should tell the section's argument in order. If they do not, rewrite the topic sentences before anything else.

## 2. Writing the topic sentence

A good topic sentence is:
- **general enough** to cover the whole paragraph, but **specific enough** to make a claim (not "This section discusses heat transfer");
- **linked** to the previous paragraph (it reuses or refers to an idea from it);
- **about the subject**, not about the paper ("Wall heat transfer controls the hot-spot temperature" rather than "In this paragraph we will look at …").

Types of topic sentence, with the kind of paragraph each opens:

| Type | Example | Typical section |
|---|---|---|
| Statement of importance | Methanol synthesis is one of the largest-volume catalytic processes in the chemical industry. | Introduction, first paragraph |
| Claim about the literature | Two-dimensional models of packed-bed reactors fall into two groups. | Introduction, literature review |
| Problem statement | Heat removal limits the conversion that can be reached per pass. | Introduction |
| Gap statement | None of these studies compared predicted radial profiles with measurements. | Introduction, end |
| Purpose/approach | The model was validated in three steps. | Methods |
| Main finding | All five correlations reproduced the position of the hot spot. | Results |
| Trend | The hot-spot temperature increased linearly with the inlet CO2 fraction. | Results |
| Interpretation | The overprediction is most likely caused by the assumed plug-flow profile. | Discussion |
| Comparison | These errors are lower than those reported for comparable 1D models. | Discussion |
| Limitation | The present model does not account for catalyst deactivation. | Discussion |

## 3. Developing the paragraph

Supporting sentences can use any combination of these kinds of information:
- an explanation or reason;
- reference to previous research (with citation);
- examples or a specific case;
- statistics, measurements, numbers;
- specific aspects or details;
- a development in time (sequence, history of an approach);
- an effect or consequence;
- a contrast or exception;
- (rarely in engineering) a quotation.

Common development patterns:

| Pattern | Order of sentences | Use in |
|---|---|---|
| General → specific | broad claim → narrower claims → concrete detail or number | Introduction, Discussion |
| Claim → evidence → interpretation | statement → data/citation → what it means | Results and Discussion, literature review |
| Problem → solution → evaluation | situation → problem → proposed solution → how well it worked → remaining problem | Introduction (engineering), literature review |
| Comparison | point of comparison → A → B → similarity/difference → reason | Literature review, Discussion |
| Cause → effect | cause → mechanism → effect → evidence | Discussion |
| Chronological / procedural | first step → next steps → final step | Methods, history of a method |
| Trend description | main trend → magnitude → secondary trend → exception | Results |

Example (claim → evidence → interpretation):
> (Topic) The wall heat-transfer coefficient had the strongest influence on the predicted hot-spot temperature. (Evidence) A 20 % reduction of this coefficient raised the hot spot by 14 K, whereas the same change in the effective radial conductivity raised it by 5 K (Fig. 6). (Detail) The effect was largest near the reactor inlet, where the reaction rate is highest. (Interpretation) Accurate wall heat-transfer data are therefore more important for this reactor than refined radial conductivity models.

## 4. Connecting sentences: closing the gap between full stop and capital letter

After every full stop the reader does not yet know what the next sentence will do. Close that gap in one of four ways.

1. **Overlap:** repeat a word or idea from the previous sentence.
   "The reaction is strongly exothermic. *This heat release* must be removed through the tube wall."
2. **Pronoun or pro-form:** it, they, this method, these models, such conditions. Make sure the reference is unambiguous; "this" alone is often unclear, so prefer "this increase", "this approach".
3. **Joining:** a semicolon between two closely related clauses (one usually short), or a relative clause ("…, which …").
4. **Signalling connector:** a word that states the logical relation (see `vocabulary-by-section.md` §1).

**Thematic linking.** In a strong paragraph each sentence begins with something already mentioned and ends with something new. Example of a chain:
> Packed-bed reactors are widely used for exothermic reactions. *In these reactors*, heat is removed through the tube wall. *The rate of this heat removal* depends on the wall heat-transfer coefficient. *This coefficient* is usually estimated from correlations derived for large tube-to-particle diameter ratios.

## 5. Inside the sentence: old information first, new information last

- **Topic position (start of the sentence):** what the reader already knows or what the sentence is about.
- **Stress position (end of the sentence):** the new information, the point you want to emphasize.
- Put the subject early and follow it quickly with its verb. Long phrases between subject and verb hide the action.
- One sentence, one main point. Add at most one interpretive clause.
- Most sentences in a paper should be 15–25 words. Very long sentences are a common problem for writers whose first language favours long sentences; split them.
- Prefer a simple declarative structure (subject – verb – object). It is clearest for non-native readers and busy readers.

Weak: "Using a 2D model and five correlations from the literature, which were all tested against measured profiles, the hot-spot temperature, which is important for catalyst life, was predicted."
Better: "Five wall heat-transfer correlations were tested in a two-dimensional model. Each model was compared with measured temperature profiles. The comparison focused on the hot-spot temperature because it limits catalyst life."

## 6. The first sentence of a section

| Section | Good first sentences | Avoid |
|---|---|---|
| Introduction | the importance of the field, or a key fact with a number and citation (a "hook") | starting with your aim; vague universal truths ("Energy is important") |
| Literature review | an overview of how the literature divides, or what the review covers and why | "Many researchers have studied X" without a claim |
| Methods | an overview of the approach or the experimental design, or the source of materials/data | jumping into step 1 with no overview |
| Results | the main finding, or a short recall of the aim/analysis followed by the main finding | a method forgotten in Methods; "The results are shown in Fig. 1" |
| Discussion | a restatement of the main finding in the words of the objective | repeating all results; a new result |
| Conclusion | what was done, in one sentence, then what was found | "In this paper, many interesting things were found" |

Examples:
- Introduction: "Methanol synthesis converts about [value] Mt of syngas per year and is strongly exothermic [1,2]."
- Methods: "The study combined pilot-plant measurements with a two-dimensional reactor model."
- Results: "All five correlations predicted the position of the hot spot within 0.1 m, but they differed strongly in its magnitude."
- Discussion: "This study shows that wall heat-transfer correlations derived for large tube-to-particle ratios overpredict the hot-spot temperature at low ratios."

## 7. The last sentence of a section and transitions

- **End of Introduction:** the present work (objective, approach, contributions, optionally main finding and paper outline). It leads the reader into the Methods.
- **End of a Results subsection:** a one-sentence summary or a pointer to the next analysis ("These profiles were then used to test …").
- **End of Results:** possible implications of the results, the bridge to the Discussion.
- **End of Discussion/Conclusion:** a clear, specific statement of what the work contributes, not a general wish for future research.
- **Between sections and subsections:** short transition statements: "Having established …, we now examine …"; "The next section compares …".

## 8. Paragraph templates by section

**Introduction, importance paragraph:** importance (topic sentence with number and citation) → how the process/system works → what determines performance → the general problem area.

**Introduction, previous-work paragraph:** claim about the group of studies → studies with what they did and achieved (cited where each applies) → evaluation of what remains open.

**Introduction, gap and aim paragraph:** "However, …" + specific gap → why it matters → "This study therefore …" objective → approach and justification → contributions → (main finding) → (outline).

**Methods paragraph:** purpose of this step → what was used (with source) → what was done, in order, with quantities and conditions → why (justification) → how care was taken / how it was checked.

**Results paragraph:** main finding (topic sentence, with figure reference) → numbers → secondary trend → exception → comparison with validation data or other studies → (in combined R&D) short interpretation.

**Discussion paragraph:** claim (interpretation) → evidence from your results → comparison with named studies → explanation of agreement/disagreement → implication.

**Limitation paragraph:** limitation → effect on results → why it does not overturn the conclusions (or how large the effect may be) → how future work can remove it.

## 9. Paragraph errors to fix during revision

- No topic sentence: the paragraph starts with detail and the point emerges at the end.
- Two ideas in one paragraph: split.
- Supporting sentences that repeat the topic sentence in other words.
- A paragraph that is one long list of studies without a claim.
- Unclear "this", "it", "they".
- Missing links between sentences: the reader must guess whether a sentence is a cause, a result, an example or a contrast.
- Paragraphs whose first sentences do not form a logical sequence.
- Every paragraph ending with "In summary, …" (summaries belong at the end of sections, not paragraphs).
