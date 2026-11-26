# Checklists

Use the section checklist after drafting each section and the final checklist before submission. Each section reference file has a fuller checklist at its end; this file collects the essentials in one place.

How to self-edit: let the draft rest for at least a day, print it or change the font, and read with one question at a time (content, then structure, then language, then format). Reading for everything at once misses most problems.

## Evidence base
- [ ] Every repository paper has a note in your own words, with numbers, conditions and relevance.
- [ ] Repository checked against a structured database search; search strings recorded.
- [ ] Theme map and comparison matrix built; gap visible in the matrix.
- [ ] `refs.bib` keys stable and matching the notes; no paper cited that you have not read.

## Paragraphs (any section)
- [ ] Each paragraph has one job, stated or clearly implied in its first sentence.
- [ ] Sentences in a paragraph follow one development pattern (general → specific, cause → effect, chronological, comparison, problem → solution).
- [ ] Each sentence starts with known information and ends with new information.
- [ ] Links between sentences are explicit (repeated key term, pronoun with a clear referent, linking word) and not decorative.
- [ ] Paragraph length varies with content; no one-sentence paragraphs except for a deliberate transition.
- [ ] The last sentence closes the point or leads to the next paragraph.

## Title
- [ ] States system, property or variable, and method; fewest words that describe the content.
- [ ] No "A study of", "Investigation of", "Novel"; no abbreviations except universally known ones.
- [ ] Prepositions say what you mean ("in", "of", "for", "from", "with").
- [ ] Promises nothing the paper does not deliver (specific system, specific conditions).

## Abstract
- [ ] Context, aim, method, main results with numbers, conclusion; in that order.
- [ ] Self-contained: no citations, figure references, undefined abbreviations or new information.
- [ ] Tense by component: present for context and conclusion, past for method and results.
- [ ] Within the word limit and in the journal's structure (single paragraph or headings).

## Introduction
- [ ] Moves from the field to the problem to the gap, each step cited.
- [ ] The first sentence is specific to the field, not a generic statement about the world.
- [ ] Gap specific (what is unknown or unsolved, for which system or conditions) and justified (why it matters).
- [ ] Objective states property, system and means, in the same words used later.
- [ ] Contributions specific; method choice justified; "first" claims checked.
- [ ] Optional outline of the paper if the journal uses it.

## Literature review
- [ ] Organized by themes, not by paper; each paragraph synthesizes several sources.
- [ ] Sources compared and evaluated, not only listed; disagreeing results included.
- [ ] Closest studies summarized in a comparison table.
- [ ] Criticism is about the work and is constructive.
- [ ] Ends at the gap that this paper fills.

## Methods
- [ ] Enough detail to repeat the work and to judge whether it was done properly.
- [ ] Materials with purity and source; equipment with model and accuracy; software with version.
- [ ] Conditions, parameters with units and sources; assumptions next to the equations they simplify.
- [ ] Boundary and initial conditions complete; numerical accuracy (grid, tolerance) and validation described.
- [ ] Data-driven details complete: data split by time, scaling on training data only, hyperparameter search, baseline.
- [ ] Choices justified where a reviewer could ask "why this one?".
- [ ] Past tense, mostly passive for procedures; present for equations and what the model is.
- [ ] Every later result has a method here, under the same subheadings.

## Results
- [ ] Same order and subheadings as Methods.
- [ ] Each paragraph: what was examined → what was found (with numbers) → brief comment if the journal combines Results and Discussion.
- [ ] Main finding first, then supporting numbers; most important results get most space.
- [ ] No duplication across text, tables and figures; text says what the figure means, not what it shows point by point.
- [ ] Every figure and table is cited in the text in numerical order.
- [ ] Negative and unexpected results reported; outliers and exclusions explained.
- [ ] Uncertainty given with every compared value; significant figures match the uncertainty.
- [ ] Measurement and interpretation separated.

## Figures and tables
- [ ] Each one earns its place; the form (graph, table, schematic) fits the message.
- [ ] Axes with quantity and unit; readable at final print size; colour-blind safe; works in greyscale.
- [ ] Consistent style, fonts and symbols across all figures; uncertainty shown.
- [ ] Captions self-explanatory: what, which conditions, what the symbols and lines mean.
- [ ] Tables in booktabs style; units in the column heads; no vertical lines.
- [ ] Permission obtained for reused figures.

## Discussion
- [ ] Opens with the main finding answering the objective.
- [ ] Explains each important result: mechanism, cause, alternative explanations considered.
- [ ] Compares with named studies, saying where and why results agree or differ.
- [ ] States the contribution and how the gap is closed.
- [ ] Limitations bounded (what effect, how large, in which direction); not hidden, not exaggerated.
- [ ] Implications for design, operation or further research specific.
- [ ] Claims at the strength the evidence allows; hedges only where uncertainty is real.
- [ ] No new results; no repetition of the Results section number by number.

## Conclusion
- [ ] Answers the objective with the key numbers.
- [ ] Main conclusions, limits of validity, one specific next step.
- [ ] No citations, no new data, no general statement about the importance of the field.

## Language and style
- [ ] Tense follows function (see `style-grammar.md`); tense changes only when the function changes.
- [ ] Active voice for your decisions and claims where the journal allows; passive where the actor is irrelevant.
- [ ] Technical terms identical throughout; general words varied only where meaning is unchanged.
- [ ] No contractions, colloquial words, opinion adverbs ("luckily", "interestingly") or decorative intensifiers.
- [ ] Concise: no deadweight words, redundant pairs, padded verbs or empty openers.
- [ ] Articles, plurals, countable nouns and prepositions checked (`style-grammar.md`).
- [ ] Each abbreviation defined at first use in the abstract and again in the main text, and used at least a few times.
- [ ] Numbers with SI units, a space before the unit, consistent decimals.
- [ ] Each pronoun ("it", "this", "they") refers to one clear noun; "This" followed by a noun ("This increase").
- [ ] No sentence longer than about 30 words without a reason.

## Final check before submission
- [ ] Objective worded identically in title, abstract, Introduction, Discussion and Conclusion.
- [ ] Each method has a result and each result a method.
- [ ] Numbers identical wherever they appear (abstract, text, tables, figures, conclusion).
- [ ] All symbols defined, units SI, significant figures consistent, abbreviations defined once.
- [ ] `scripts/check_citations.py` run: no RETRACTED, DOI NOT FOUND or MISMATCH entries; no cited keys missing; uncited entries removed or justified; no open `[CHECK]` items.
- [ ] Each cited source supports the sentence that cites it, at the same strength.
- [ ] Self-review done in all five roles (`self-review.md`); every major comment fixed, acknowledged as a limitation, or answered with evidence.
- [ ] Journal guidelines met, item by item against the journal profile (`resources/journals/<journal>/journal_requirements.md`): template, length, abstract, keywords, highlights, reference style, figure format and resolution, declarations (funding, conflicts, data availability, author contributions, AI use).
- [ ] Eight Cs checked:
  - compliance (journal instructions followed),
  - completeness (nothing needed is missing; nothing unneeded is present),
  - composition (organization at the level of paper, section and paragraph),
  - correctness (facts, numbers, equations, grammar, spelling),
  - clarity (each sentence has one clear meaning),
  - conciseness (no wasted words),
  - consistency (terms, numbers, symbols, formats, order of items),
  - courtesy (respectful wording about other work; "did not examine", not "failed to").
- [ ] Likely reviewer objections answered in the text: novelty, validation, uncertainty, limitations, overclaiming.
- [ ] `scripts/check_ai_signs.py` run on every section; each flag rewritten with a specific fact, number or citation, or deleted; no placeholders left.
- [ ] Plain words where they are precise (is, has, used); academic words where they add precision; no decorative intensifiers.
- [ ] Spell-check run, then each suggested change checked by eye (spell-checkers introduce wrong words).
- [ ] A colleague in the field has read it; if possible a fluent English speaker from the field, since general editors may change technical terms.
- [ ] AI assistance disclosed as the journal requires.
- [ ] Read aloud once from beginning to end.
