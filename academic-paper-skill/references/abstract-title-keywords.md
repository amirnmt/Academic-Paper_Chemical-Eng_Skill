# Abstract, title, keywords, highlights and graphical abstract

Many more people read the title than the abstract, and many more read the abstract than the paper. In online databases the abstract competes for attention and must persuade readers to obtain the full paper; editors use it to judge the manuscript and to choose reviewers. A poor abstract usually predicts a poor paper. Write these parts last, from the finished paper.

## 1. Abstract

### 1.1 What it is
A miniature version of the paper: the problem and objective, the methods, the main results and the principal conclusions. It must stand alone: a reader who never sees the paper should understand the key points.

Two types:
- **Informative abstract** (research papers): states the problem, method, principal data and conclusions.
- **Indicative (descriptive) abstract** (review papers, reports): lists the topics covered without giving results, like a table of contents. Do not use it for a research paper.

Two models of informative abstract (the journal usually decides):
- **Structured / summary model:** covers all main sections in order (background, aim, methods, results, conclusions), sometimes with headings.
- **Focused model:** concentrates on two or three components, usually method and results, often combined in one sentence. Common in narrow fields where readers know the background. Methods come before results.

### 1.2 Rules
- Self-contained: no references (rare exceptions: a paper that directly replies to another, or one that extends a named earlier study, cited by author and year), no figure or table citations, no undefined abbreviations (define a long term only if it is used several times).
- Every statement and conclusion in the abstract must also appear in the body of the paper.
- Concentrate on results, with numbers; do not list what was done.
- No evaluative or judgemental remarks ("surprisingly …").
- Keep the body's qualifiers when shortening [Rule]: scope ("for the tested operating range", "on plant data"), strength ("suggests", not "proves") and conditions of each number. The abstract may be shorter than the body, not stronger (`research-integrity.md` §5).
- Respect the word limit (often 150–250 words; many are 80–150). Do not exceed it: the editor may cut it in a way that misrepresents the work. Using fewer words is fine.
- Usually a single paragraph unless the journal requires headings.
- Avoid empty endings: "The results are discussed", "More research is needed", "Implications are considered".
- Build the abstract from the paper: select and adapt phrases from each section rather than inventing new statements or pasting whole sentences.
- Include the exact words and phrases people search for, so the paper appears in searches.
- The abstract may be slightly less technical than the paper to reach a wider audience; explain a technical term or acronym at first use ("granules of hydroxyapatite (HA)").

### 1.3 Components and their order
1. Background, problem or gap (1–2 sentences).
2. Aim / what the paper does.
3. Methodology or materials.
4. Results (primary result first), achievement or contribution, implications.
5. Applications (if any).
6. Limitations or future work (rarely, and briefly).

Engineering abstracts typically state background, purpose, methods, results and conclusion. Chemical engineering abstracts emphasize the methods and state the purpose less often than other engineering fields [D], so a clearly stated purpose helps the abstract stand out. In process-systems papers the purpose is almost always explicit (§1.9).

### 1.4 Word budget (for about 250 words)
- Background and gap: 40–50 words.
- Aim and approach: 30–40 words.
- Methods: 40–50 words.
- Results with numbers: 80–100 words.
- Contribution or implication: 30–40 words.

### 1.5 Tense by component
- Problem or gap: present simple ("However, these correlations are not valid when …").
- What the paper does: present simple ("This paper presents …"; "We compare …").
- What was done: past simple ("Five correlations were evaluated …"); present simple for analyses that are part of the paper ("The model is validated against …").
- Results: past simple ("The error decreased by …"), or present simple to state them directly ("The model consistently underpredicts …").
- Achievement: present perfect ("We have shown …"; "This study has identified …") or present simple ("The approach presented here predicts …").
- Implications and applications: present simple with a modal where needed ("The results indicate that …"; "This approach can be applied to …"). Avoid weak forms such as "seem to suggest" in an abstract.

### 1.6 First and last sentences
- First sentence: the problem or context in one sentence, or (focused model) what the paper does and how. Not a generality.
- Last sentence: the implication or application, specific to the results. Not "Further research is needed".

### 1.7 Drafting
Write the first draft freely, including everything that seems important; then cut words, phrases and sentences that are not essential. Example of condensing: a 35-word opening about scientists needing to write but rarely receiving training can become a 12-word sentence that says the same thing.

### 1.8 Skeleton (placeholders)
> [Process/system] is [importance]. [Current models/methods] rely on [assumption/limitation], which [consequence]. This study [aim] by [approach]. [Method details: model, data, validation]. [Main result with number]. [Second result with number]. [Comparison or validation metric]. These results [implication for design, operation or modelling].

Focused variant (aim first):
> This work proposes [method] for [task] in [system]. [Method] combines [component A] with [component B] so that [capability]. It is applied to [case, data size]. [Main result with number, compared with baseline]. [Second result]. [Scope or limitation in one clause]. [Implication].

### 1.9 Abstracts in process-systems papers [J-obs]
From all 20 research abstracts of *Computers & Chemical Engineering* papers analysed (one read from the PDF page; full table in `resources/journals/computers-and-chemical-engineering/section_models.md` §2):

| Feature | Observed |
|---|---|
| Length | median 184 words (86 to about 250), 8–9 sentences (3–13); sentences of about 26 words |
| Opening | context, often with the difficulty, 13; a pointed claim or finding 2; the work itself 5 |
| Problem or gap stated | 11 of 20: in the same sentence as the context ("X is important for …, yet …"), as a "However, existing …" sentence, or as "Existing [models] [assume / neglect] …" |
| Aim sentence | 19 of 20; subject "This work", "This paper", "This study" or "We"; verb mostly *propose(s)* or *present(s)* |
| Method | 1–5 sentences; detail introduced with "Specifically, …"; names the methods, the data and its size |
| Validation or application named | 7 of 20 |
| Results with numbers | metric values in 10 of 20 (percent changes, R², errors, cost or time reductions), with the baseline named in 9; data sizes or scenario levels only in 2; qualitative only in 8 |
| Closing | significance in 11 ("These findings provide …", "Overall, …"); a result in 7; a recommendation or a scope statement in 2 |
| Limitation or scope | 6 of 20 |
| Citations | 2 of 20, each to the study the paper builds on or contrasts with |
| Tense | present for method and results in most; past in the few that narrate the steps; consistent within each abstract |
| "We" | 6 of 20 |

How these abstracts stay short [G]:
- **Importance and difficulty in one sentence:** "[X] is critical for [use], yet its [prediction / control] remains difficult because [reason]."
- **Aim and method in one sentence:** "This work proposes [name], a [type] that integrates [A] with [B] for [task]."
- **Method components as one list:** "The framework combines [A], [B], [C] and [D]."
- **Result, metric and comparison in one sentence:** "Compared with [baseline], [method] reduces [metric] by [value] and [metric 2] by [value]."
- **A clause for scope**, not a sentence: "…, within the investigated operating range, …".
- **No meta-sentences** ("The results are discussed", "Conclusions are drawn").

## 2. Title

### 2.1 What a good title is
The fewest words that describe the content of the paper accurately. Indexing services and search engines depend on it; a poorly titled paper may never reach its readers. The title is a label, not a sentence.

### 2.2 Building it
- Answer What (system, process, property measured), Where (laboratory, pilot plant, industrial reactor, simulation) and How (method), as far as space allows.
- Start from the research question: "How does X affect Y?" → "Effect of X on Y in Z"; "What is the difference between X and Y?" → "Comparison of X and Y for …".
- Be specific: name the actual system, compound or condition, or a precise group name. "Action of antibiotics on bacteria" says nothing; "Inhibition of growth of [organism] by [compound]" says what was found.
- Define vague verbs: replace "Effect of …" with what the effect was when the finding is clear and important.
- Put the most important element first.
- Reflect the scope accurately (a case study vs a general survey); if the study covered only some systems or conditions, name them.

### 2.3 Avoid
- Waste words: "Studies on", "Investigation of", "A study of", "Some aspects of", leading "A/An/The", "Novel".
- Abbreviations, chemical formulas, trade names, jargon and outdated terms. Ask: how would someone search for this?
- Faulty word order: modifiers attached to the wrong noun ("pneumonia in mice induced by a virus" suggests the mice were induced). Check every prepositional phrase and every "using" (a dangling "using" makes the object of the study perform the method).
- Long stacks of nouns; ambiguous prepositions ("with" = using or having; "evidence for" = supporting vs "evidence of" = sign of; "from" vs "in" can change meaning).
- Series titles ("Part IV"); journals rarely accept them.
- Questions (uncommon in engineering journals) and jokes or cryptic titles.
- Overclaiming: no "reliable", no modal verbs, no promise the paper does not fulfil. A title stating the result as a sentence is acceptable only if the result is a major, well-supported achievement and the journal allows it.

Hanging titles with a colon ("Low-ratio packed beds: validation of …") are accepted by some journals; check recent issues.

Use sentence case unless the journal requires title case. Prepare a running title if required (check the character limit). Write a provisional title early, refine it while drafting, and finalize it last. Have the title checked by a fluent colleague: errors here are the most visible in the paper.

Examples (illustrative):
- Weak: "A study of heat transfer in methanol reactors"
- Better: "Wall heat-transfer correlations for low tube-to-particle diameter ratios: validation against pilot-scale temperature profiles in methanol synthesis"

## 3. Keywords

- Specific, searchable terms: methods, materials, processes, properties, systems.
- Do not repeat words already in the title (the title is already indexed); some journals forbid it.
- Avoid general words (study, analysis, experiment, change) and fashionable terms that return thousands of hits.
- Add a broader or a narrower term than the title (e.g. title has "methanol synthesis" → keyword "CO2 hydrogenation" or "packed-bed heat transfer").
- Use the journal's controlled list if it has one; look at keywords of similar papers.
- Stay within the journal's limit; fewer is allowed.
- Observed in *Computers & Chemical Engineering* [J-obs] (20 papers, 104 keywords): median 5 (2–7); about 40 % only repeat title words, 40 % add new terms. A useful mix: one or two method terms, the system or process, and one task or application term (`section_models.md` §2a).

**Titles observed in the same journal** [J-obs]: median 13 words (10–17); mostly a noun phrase naming method and system; a quarter use a colon; half name the concrete industrial system or material; a statement title (the finding as a sentence) is rare (`section_models.md` §2a).

## 4. Highlights, nontechnical summaries, graphical abstract

- **Highlights:** usually 3–5 bullet points, each within a character limit (often 85 characters including spaces). Main results and contributions, not background. Concrete: "Five wall heat-transfer correlations compared at low d_t/d_p" rather than "Heat transfer was studied".
- **Observed in Computers & Chemical Engineering** [J-obs] (Highlights of 7 published papers, 29 bullets, read from the article pages; details in `section_models.md` §2a of the C&CE profile):
  - 3–5 bullets per paper (median 4); median 77 characters (48–215). 9 of 29 bullets in 3 papers exceed the 85-character limit, so the limit is not always enforced, but stay within it.
  - **No bullet contains a number.** Most describe what was done (18 of 29); findings appear in 3 papers only (6 bullets); 2017-era bullets also spend space on background ("X has become an important …").
  - Forms: full sentences in the present or present perfect (19, about half passive: "… is proposed", "… are identified"), noun phrases (6), or sentences without a subject in the past tense ("Developed a …", 4). Each paper keeps one form.
  - Novelty words in 2 papers ("A new … formulation", "First application of …").
  - One submitted pre-proof had four labelled bullets of 250–340 characters each: far beyond the limit.
- **Doing better than the average** [G, with the observation above]: use the 85 characters for one method contribution and two or three results with numbers and their condition, e.g. "Transient model reproduces plant outlet temperature within 2 K" (62 characters). Drop background bullets. One form for all bullets, no labels, no abbreviations the reader cannot decode.
- **Nontechnical summary or statement of significance:** some journals request one; write it for an educated non-specialist.
- **Graphical abstract:** one image summarizing the main message (often the system, the method and the key result in one panel). Prefer a new, simple figure; reuse a paper figure only if it already shows the main result clearly. Readable at small size; little text.

## 5. Checklist

- [ ] Abstract self-contained: no references, figures or undefined abbreviations; nothing not in the paper.
- [ ] Contains aim, method, main quantitative results, implication; results take most of the words.
- [ ] Tense matches each component; no weak hedges; no empty last sentence.
- [ ] Within the word limit; contains the search terms readers use.
- [ ] Title accurate, specific, searchable, without waste words; word order, prepositions and "using" checked; no abbreviations.
- [ ] Keywords specific and not repeating title words.
- [ ] Highlights concrete and within the character limit (count characters, spaces included); at least two carry a result with a number; no background bullet.
- [ ] Objective wording consistent with Introduction and Conclusion.
- [ ] Every claim in the abstract and highlights has the same scope and strength as in the body.
