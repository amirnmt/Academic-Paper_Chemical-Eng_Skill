# Academic style and grammar

Scientific style is plain: state facts as simply as possible. Simple, precise language makes new information easier to understand, for native and non-native readers alike. Write to communicate the science, not to show your vocabulary or your command of long sentences and the passive voice.

Paragraph and sentence construction is covered in `paragraphs-and-sentences.md`; word choice in `vocabulary-by-section.md`; patterns of generic or AI-typical prose in `avoid-ai-signs.md`.

## 1. Features of academic style

- **Evidence-based:** claims are supported by data or citations; general statements are supported by examples.
- **Precise:** numbers, conditions and specific terms instead of vague words ("30 runs", not "many runs").
- **Cautious where appropriate:** certainty matches evidence; avoid absolute generalizations ("all", "always", "never") unless proven.
- **Objective and controlled in person:** the focus is on what was done and found. "We" is accepted in most engineering journals for the authors' decisions and claims; never use "we" for people in general and avoid addressing the reader as "you" ("It can be argued that …" rather than "You could say that …").
- **Formal vocabulary:** words of classical origin are common (concern, considerable, eradicate, method, synthesize, insufficient, difficulty rather than worry, a lot of, get rid of, way, bring together, not enough, trouble). But prefer the short word when it is equally precise (use, not utilize).
- **Nominalization** (processes as nouns, "the reduction of the catalyst") makes text compact; overuse makes it dense and hides the action (§6).
- **No contractions** (do not, it is), **no rhetorical questions**, no clichés, no euphemisms, few metaphors, no exclamation marks, no capitals or bold for emphasis.
- **No opinion adverbs** (luckily, unfortunately, interestingly, surprisingly) in factual statements.
- **Unbiased, inclusive language.**
- **Specific, not generic:** avoid inflated significance and decorative words (see `avoid-ai-signs.md`).

Cultural note: international journals expect direct expression. State the main point first, then the details. Do not approach the point indirectly or leave it implied.

## 2. Sentences

- One sentence, one main point; at most one interpretive clause.
- Subject early, verb soon after it.
- Old information at the start (topic position), new information at the end (stress position).
- Most sentences 15–25 words; split longer ones. Avoid the sentence structure of your native language when it produces very long or reversed sentences.
- Use a simple declarative structure (subject – verb – object) by default.
- Prefer the active voice when the actor matters ("We chose …", "Smith et al. [4] showed …"); use the passive when the action matters more than the actor (procedures).

## 3. Tense: a matter of scientific convention

Once a finding is published in a peer-reviewed journal, it is treated as established knowledge and stated in the **present** tense, with a citation ("Cu catalysts sinter above 300 °C [7]"). Your own new results are not yet established and are stated in the **past** tense ("The catalyst sintered above 300 °C"). A paper therefore moves between past and present.

| Section | Main tense | Exceptions |
|---|---|---|
| Abstract | past (what was done and found) | present for the gap, what the paper does, implications |
| Introduction | present (known facts) | past for specific studies; present perfect for research to date and open gaps |
| Literature review | present and past | present perfect for continuing lines of research |
| Methods | past | present for standard procedures, equations, and describing tables and figures |
| Results | past | present for what a figure or table shows, for calculations and statistics, and for findings you treat as established |
| Discussion | present (meaning, generalization, literature) | past for your specific results; modals for interpretation |
| Conclusion | present perfect, past and present | present perfect for what the study achieved |

Further exceptions:
- **Attribution:** "Smith (9) showed that streptomycin inhibits …" (past for the act of showing, present for the established fact).
- **Presentation:** "Table 4 shows that the yield increased …" (present for the table, past for your result).
- **Calculations and statistics:** "These values are significantly higher, indicating that …" (present).
- **General truths:** present.

Tense pairs that change meaning:
- **Present simple vs present continuous:** present simple for facts and accepted truths; present continuous for temporary situations (rare in papers except for trends: "Interest is growing").
- **Past simple vs present perfect:** past simple for a completed study at a definite time ("[12] measured …"); present perfect for something still relevant now ("Several studies have shown …"; "little attention has been paid to …" means the gap still exists).
- **Present simple for your own result** presents it as a general fact; **past simple** ties it to your study. Choose deliberately.
- **Present vs past passive in Methods:** present for standard procedures, past for what you did; the switch marks your contribution (`methods-latex.md` §6).

Tense changes always signal a change of function. Never change tense randomly, and remember to change it when the function changes. Most papers need mainly two tenses: simple present and simple past.

## 4. Active and passive voice

- Passive keeps the focus on the action or object and suits procedures: "The catalyst was reduced in H2 at 513 K."
- Active is shorter and clearer when the actor matters: "We chose a finite-volume scheme because …".
- "It was found that …" is wordier and less precise than "We found that …"; "the authors found" is pretentious. Do not use "we" for a single author.
- The agentless passive hides who did something; mark your own work with "here", "in this study", or a dummy subject ("This study compares …").
- Avoid dangling constructions: "Using the model, the hot spot was predicted" → "The model predicted the hot spot" or "Using the model, we predicted …".

## 5. Concision

Remove:
- **Deadweight words:** actually, basically, really, very, quite, particular, various (when not needed).
- **Redundant pairs:** end result, past history, true fact, each and every, completely eliminate, final outcome, future plans.
- **Category words:** "in a confused state" → confused; "period in time" → period; "blue in colour" → blue.
- **Formulaic phrases:** due to the fact that → because; with regard to → about; in order to → to; at this point in time → now; in the event that → if; a large number of → many.
- **Padded verbs:** have an expectation → expect; make an inquiry → inquire; carry out an analysis of → analyse; give rise to (when "cause" fits).
- **Needless "to be":** "is considered to be the best" → "is considered the best".
- **Needless relative clauses:** "the model, which is described in Section 2" → "the model described in Section 2".
- **Empty openers:** It is well known that, It should be mentioned that, It is important to note that.
- **Repetition** of what a figure already shows.
Combine short sentences that repeat their subject. Delete tangential content. But never cut clarity or meaning for brevity.

## 6. Nouns: nominalization and noun stacks

- **Turn hidden verbs back into verbs:** "Examination of the samples was carried out" → "We examined the samples"; "Separation of the phases was achieved" → "The phases were separated"; "Optimization of the parameters was performed" → "The parameters were optimized".
- **Noun stacks** (several nouns used as adjectives) become ambiguous: "reactor wall temperature measurement error correction method". The last noun is the real noun; the others modify it. Break long stacks with prepositions: "a method for correcting errors in wall temperature measurements".
- **Hyphens** show which words belong together as a modifier: fixed-bed reactor, two-dimensional model, low-ratio tubes, drought-hit farmers (without the hyphen, the meaning changes).
- **Commas** can change meaning too: "a single, certified analyst" (an analyst who is single) vs "a single certified analyst" (one analyst).

## 7. Modifiers and word order (hidden errors)

The most dangerous errors are grammatically correct sentences that say something you did not mean. Proofreaders and editors do not see them.
- **Dangling participles:** a participle (-ing/-ed phrase) attaches to the subject of the sentence. "Having completed the measurements, the reactor was shut down" (the reactor did not complete the measurements) → "After the measurements were completed, the reactor was shut down." "Using a thermocouple, the temperature was measured" (the temperature did not use the thermocouple) → "The temperature was measured with a thermocouple."
- **Misplaced phrases:** put the phrase next to the word it modifies. "The reactor was filled with pellets from the supplier with a high silver content" leaves unclear whether the pellets or the supplier have the high silver content; write "The reactor was filled with high-silver pellets obtained from the supplier".
- **Adverb location:** "only" changes the meaning wherever it moves ("The model only fails at high flow" vs "The model fails only at high flow"). Put sentence adverbs (last year, as a result, clearly) at the start; avoid clusters of adverbs and prepositional phrases at the end of a sentence; split the sentence if needed.
- **Unclear antecedents:** "it", "this", "they" must point to one obvious noun. Prefer "this increase", "this model".
- **Agentless actions:** "To determine its activity, the catalyst was …" (the catalyst did not determine anything) → "To determine the activity of the catalyst, we …".

## 8. Articles and countable nouns

- Singular countable nouns need a determiner (a, the, this, each, one …): "a reactor", "the model".
- "The" for something specific or already mentioned; "a/an" for one of many or first mention; no article for general plural or uncountable nouns ("Catalysts deactivate"; "Heat is removed").
- Uncountable in general use: information, equipment, research, evidence, knowledge, advice, progress, software, machinery. No plural, no "a" ("further research", not "researches"; "a piece of equipment").
- Many nouns can be countable or uncountable depending on meaning: "industry" (in general) vs "industries" (several particular ones); "steel" vs "steels" (grades); "analysis" vs "analyses".
- Latin and Greek plurals: data (datum), criteria (criterion), phenomena (phenomenon), spectra (spectrum), maxima/minima, formulae or formulas, analyses (analysis), hypotheses (hypothesis). Follow the journal for "data is/are"; most engineering journals use "data are".
- Quantities: "10 g was added" (one amount) vs "10 g were added" (in portions).

## 9. Numbers and units

- Numerals with units, always (3 mL, 12 K, 5 bar).
- Without units: many journals spell out one-digit numbers and use numerals from 10; in a series where any number has two or more digits, use numerals for all.
- Do not begin a sentence with a numeral: rephrase ("In total, 12 runs …") or spell out number and unit.
- Leading zero for decimals below 1 (0.25).
- No more significant figures than the measurement supports.
- SI units only; mass (kg), not weight; a space between number and unit; units are never plural or followed by a full stop.
- Ranges: "20–30 K" or "from 20 to 30 K"; avoid a hyphen that can be read as a minus sign.

## 10. Abbreviations and jargon

- Keep abbreviations to a minimum. SI units and their prefixes need no definition; journals also allow e.g., i.e., et al., etc. without definition (e.g. = for example; i.e. = that is; both are often confused, so many editors prefer the words).
- Define at first use: full term, then the abbreviation in parentheses. Define again in the main text even if defined in the abstract.
- Never use abbreviations in the title, and almost never in the abstract.
- Draft with full terms first; then abbreviate only long terms that occur often. Do not abbreviate a term used once or twice; for terms used a few times, use a standard abbreviation if one exists; do not invent abbreviations unless a long term is used very often.
- Alternatives to abbreviations: a clear pronoun, or a short substitute noun ("the catalyst", "the model", "the correlation").
- Introduce abbreviations one by one at first use, or in an abbreviations list if the journal requires one.
- Technical terms are fine for readers who know them; define the unusual ones. Write for the hundreds of researchers in neighbouring fields, not only the handful doing exactly your work.
- Avoid pompous jargon ("mumblespeak"): utilize → use, perform → do, initiate → start, terminate/finalize → end, fabricate → make, prior to → before, subsequent to → after, sufficient → enough, at this point in time → now. See `vocabulary-by-section.md` §9.

## 11. Linking words

See `vocabulary-by-section.md` §1 for linking words by function, and `paragraphs-and-sentences.md` §4 for the four ways to connect sentences. Grammar points:
- "However" at the start of a sentence followed by a comma, or after the first phrase ("The model, however, …"). Do not join two clauses with "however" and a comma only.
- "Despite" + noun ("despite the high temperature"); "although" + clause ("although the temperature was high").
- Do not start a sentence with "So" or "And" in formal papers.
- "Since" and "while" can be ambiguous (time vs cause/contrast); choose another word if the meaning could be misread.

## 12. Counterarguments

To strengthen a claim, raise the strongest credible objection (one with evidence or that is well known) and answer it:
1. Introduce it fairly and clearly as not your own view: "It could be argued that …"; "[7] suggested that …".
2. Answer with evidence: "However, the sensitivity analysis shows …".
3. Agree in part where it is valid: "This holds for …, but …".
4. Reaffirm your claim in its qualified form.
Do not dismiss counterarguments without evidence, and do not choose weak ones that nobody holds.

## 13. Common problems for non-native writers

- Long sentences that should be two or three; native-language word order.
- Missing plural -s, or -s on uncountable nouns ("informations", "equipments").
- Articles (§8) and prepositions: keep a list of the prepositional phrases used in your field (depend on, consist of, comparable with, effect of X on Y, agreement with, sensitive to, independent of).
- "Respectively" only for pairing two parallel lists: "The inlet and outlet temperatures were 500 and 530 K, respectively."
- Which (adds information, with commas) vs that (defines, no commas).
- Comparatives: "higher than", never "more higher"; "compared with" to show differences.
- Capitalization (do not capitalize common nouns for emphasis) and spacing (space after a full stop, none inside parentheses).
- Translation: draft directly in English. Improving imperfect English is easier than translating a finished text.
- Phrase lists: for each section, collect words and phrases used in recent papers in your target journal and use them as models (see `scripts/build_section_phrases.py`). Keep a list of corrections that editors make to your writing.
- Feedback: ask a fluent colleague from your field to read the paper. An editor outside the field may change technical terms incorrectly.

## 14. Proofreading

- Spell-checkers and autocorrect introduce errors (a correctly spelled wrong word passes every check). Proofread yourself.
- Read the text aloud: sentences that sound wrong usually are.
- Check consistency: terms, symbols, units, number formats, abbreviations, British or American spelling.
- Check the title, abstract, equations, table values and reference list with special care; errors there are the most visible.
