# Avoiding the signs of AI-generated writing

AI-generated text drifts toward the generic: it smooths specific facts into statements that could fit any topic, inflates importance, and repeats a small set of words and sentence patterns. In a research article these habits are not only recognizable, they are bad writing: they replace evidence with emphasis and precision with vagueness.

The goal of this file is precise, specific writing. It is not a way to hide AI use. Disclose AI assistance as the target journal requires, and make sure every claim, number and citation has been checked by the authors.

Read this file before drafting, and run the check in §9 on every draft section. §8 adds discourse-level patterns (what the text explains, omits and emphasizes) from a large study of AI and human writing; word-level fixes alone do not remove them.

## 1. The underlying problem: regression to the generic

Language models predict the most likely continuation, so they favour statements that are true of many subjects. A specific fact ("the hot spot moved 0.4 m downstream after 300 days") gets replaced by a generic one ("the reactor's behaviour evolved over time, reflecting the complex interplay of factors"). The fix is always the same: replace the generic statement with the specific fact, number, condition or citation, or delete it.

## 2. Content patterns to avoid

**Inflated significance.** Statements that a detail "marks a pivotal moment", "underscores the importance of", "reflects broader trends", "sets the stage for", "represents a shift", or "plays a crucial role", without evidence. In a paper, importance is shown with numbers and citations, not asserted.
- Weak: "This finding underscores the pivotal role of heat transfer in shaping reactor performance."
- Better: "Reducing the wall heat-transfer coefficient by 20 % raised the hot-spot temperature by 14 K (Fig. 6)."

**Superficial analysis attached with "-ing".** A sentence ending in ", highlighting …", ", underscoring …", ", emphasizing …", ", showcasing …", ", reflecting …", ", ensuring …", ", contributing to …", ", fostering …" adds an interpretation that nobody has shown. Either support the interpretation in its own sentence, or delete it.

**Vague connection.** "X is associated with Y", "in connection with", "linked to" when the actual relation is known. State the relation: "X increases Y", "X was measured in Y", "X is a parameter of Y". In a research paper, "associated with" should mean a statistical association, nothing else.

**Vague attribution and overgeneralization.** "Researchers have noted", "experts argue", "several studies suggest", "it is widely recognized" followed by one citation or none. Name the studies and cite them; do not present one or two sources as a consensus.

**Formulaic "challenges and future prospects".** A closing paragraph that begins "Despite its advantages, X faces several challenges …" and ends with a vaguely optimistic sentence about future potential. Replace it with specific limitations of this study and specific next steps (see `discussion-hedging.md` §6).

**Hedging disclaimers about information.** "While specific details are limited …", "based on available information …", "it is important to note that …", "should be interpreted as … rather than …" used as filler. If a limitation of the data matters, state it once, specifically, with its effect. Never write about what "is not documented" unless you have checked.

**Section summaries that repeat.** Ending every paragraph or section by restating its point ("In summary, …", "Overall, …"). One summary belongs in the Conclusion.

## 3. Vocabulary to use with care

These words are heavily over-represented in AI-generated text, especially when several appear together. Each is acceptable in its literal technical sense (a *robust* controller, a *key* in a table, a *crucial* step that is in fact necessary). Avoid them as decoration; prefer a plain or specific word.

| Avoid as decoration | Plain alternatives |
|---|---|
| delve into, deep dive | examine, analyse, study |
| crucial, pivotal, vital, key (as an adjective of importance) | important, necessary, main, or state why it matters |
| underscore, highlight, emphasize, showcase (figurative) | show, indicate, demonstrate, or give the number |
| enhance, bolster | increase, improve (with the amount) |
| foster, cultivate | promote, support, cause |
| leverage | use |
| robust (figurative) | reliable, accurate within …, insensitive to … |
| intricate, multifaceted, complex interplay | name the interacting factors |
| landscape, tapestry, realm (abstract) | field, area, set of studies |
| testament to, stands as, serves as | is, shows |
| align with, resonate with | agree with, match, is consistent with |
| boast, feature, offer (meaning "has") | has, includes, contains |
| garner | receive, attract |
| meticulous(ly) | careful(ly), or describe the procedure |
| seamless(ly), groundbreaking, renowned, vibrant | delete, or give evidence |
| Additionally, (at the start of many sentences) | vary or delete; often no connector is needed |

One or two of these words in a paper is normal. A cluster of them in one paragraph is the problem.

## 4. Sentence patterns to avoid

**Avoiding "is" and "has".** "X serves as a …", "X stands as …", "X functions as …", "X represents …", "X features …" where "X is …" or "X has …" says the same thing. Write "is" and "has".

**Negative parallelism.** "Not only X but also Y", "It is not just X, it is Y", "not X but Y", "Y rather than X", especially when nobody claimed X. Use them only to correct a real, stated misconception.

**Rule of three.** Automatic triplets of adjectives or phrases ("efficient, scalable and robust"; "accuracy, reliability and efficiency"). List what is true and supported; two items or four are fine.

**Elegant variation.** Changing the term for the same thing to avoid repetition ("the reactor … the unit … the system … the vessel"). In technical writing, repeat the same term; varying it suggests different objects.

**One template for every section.** Each subsection built the same way (claim sentence, three points, summary sentence). Let the structure follow the content: Methods can be procedural, Results led by the main finding, Discussion exploratory. Parallel structure is right only where it helps comparison (for example, the same order for each case study).

**Uniform sentences.** Every sentence the same length and shape. Mix short statements of fact with longer explanatory sentences.

**Formulaic transitions.** "Additionally," "Furthermore," "Moreover," "Notably," opening most sentences. Most sentences need no connector; use one only for a real logical relation (contrast, cause, concession).

## 5. Formatting and punctuation patterns

- Em dashes used as all-purpose punctuation, especially with spaces around them ( — ). In papers, use commas, parentheses, colons or a new sentence. Reserve dashes for what the journal's style allows; en dashes belong in ranges and paired names (Peng–Robinson).
- Bold text inside paragraphs, inline-header bullet lists, and emoji. Papers are written in paragraphs; lists only where the journal allows them (e.g. contributions).
- Title Case Headings when the journal uses sentence case.
- Leftover chat language: "Certainly!", "I hope this helps", "Here is a revised version", "Let me know if …", "As an AI …".
- Placeholders that were never filled: "[insert value]", "XX", "20XX-XX-XX", "example.com", "[Author, Year]", "[CHECK]". Search for them before every hand-over.
- Markdown in a LaTeX or Word manuscript (`**bold**`, `#` headings, backticks).

## 6. Citation patterns (the most serious problem)

AI tools produce references that look correct but are not. Reviewers and editors check.
- References that do not exist, or DOIs that resolve to an unrelated paper. Resolve every DOI and compare title, authors and year.
- Real papers cited for claims they do not make. Check each claim against the cited text (page, table or figure).
- Book citations without pages, or with pages that do not contain the claim.
- Citation numbers or keys that are declared but never used, or used but not defined.
- One source presented as "several studies".

Follow `evidence-base.md`: cite only verified papers, keep the claim → source → page map, and mark uncertain citations `[CHECK]` instead of guessing.

## 7. What is not a sign of AI writing

Do not "fix" these; they are normal in good human writing:
- correct grammar and formal academic vocabulary in general;
- transition words used where the logic needs them;
- the words *is*, *has*, *used*, *wrote*, *tried*, plain verbs instead of stiff synonyms (utilized, attempted, authored); these are signs of natural writing;
- definite statements where the evidence is direct ("is the only", "was the first", with citation);
- ordinary qualifiers where the evidence is indirect ("tends to", "perhaps");
- repeating the same technical term.

Detection tools and human judges are unreliable; the aim is clear, specific, verified writing, not a score.

## 8. Discourse-level patterns: what changes when only the words are fixed

Everything above is about words and sentences. A large study of fiction shows that AI writing also differs in **how the text is built** (what it explains, what it leaves out, how it orders things), and that these differences survive when the surface wording is cleaned up. This section turns its findings into checks for a research article.

### 8.1 The study and what it can and cannot tell us

Russell, Rajendhran, Pham, Iyyer and Wieting (2026), *StoryScope: Investigating idiosyncrasies in AI fiction*, COLM 2026 (arXiv:2604.03136v6):
- **Data:** 10,272 prompts derived from published human short stories; for each, the human original plus versions by five models (Claude Sonnet 4.6, GPT-5.4, Gemini 3 Flash, DeepSeek V3.2, Kimi K2.5): 61,608 stories of about 4,750 words. Each story was scored on 304 discourse-level features in 10 narrative dimensions.
- **Detection without style:** narrative features alone separate human from AI stories with 93.2 % macro-F1 (96.0 % with style features added); 30 "core" features alone reach 84.8 %. Six-way attribution (which source wrote it): 68.4 % (chance 16.7 %).
- **Surface editing does not remove the signal:** after a professional-writer-style rewrite of seven kinds of surface artifact (cliché, redundant exposition, purple prose and others), AI stories were still detected at 93.9 % macro-F1, against 95.5 % before editing: a drop of 1.6 points.
- **Surface signals are fading:** the paper notes that newer models already use fewer em dashes, and that fine-tuning to mimic human style dropped AI detection on creative writing from 97 % to 3 % (citing Chakrabarty et al., 2026). The structural patterns are the durable ones.
- **Robustness:** results are unchanged when stories are matched for length (93.2 % before and after), do not differ significantly by topic (Kruskal–Wallis *H* = 4.69, *p* = 0.46), and are unchanged after removing possibly memorized stories (93.18 → 93.23 %).

**Limits of transfer.** The study is about fiction, not research articles, and its models are 2026 versions. The numbers below are the paper's; the **"In a research article"** rules are this skill's translation of each pattern to scientific prose. Each rule is marked by how directly it transfers:
- **[T1] direct:** the same behaviour occurs in any expository text (for example, stating the moral of a passage);
- **[T2] analogue:** a corresponding behaviour exists in papers (for example, a single-track story ↔ a results section without side findings);
- **[T3] fiction only:** no useful equivalent in a paper; listed for completeness and for narrative passages (case descriptions, histories, popular summaries).

Two cautions. A human-leaning feature in fiction is not automatically good in a paper: breaking the fourth wall or nonlinear chronology would be wrong in a journal article, so those rules are inverted or marked T3. And none of these checks proves authorship; the aim, as in the rest of this file, is writing that is specific, honest about complexity, and grounded in sources.

### 8.2 The 33 core patterns as rules

Values are human vs AI (AI = mean of the five models). Scales are 1–5 means unless marked "ord" (ordinal code means) or given as % of stories. Source: Table 16 and §4.1 of the paper.

**A. AI over-explains its meaning ("thematic over-determination")**

| # | Finding (human vs AI) | In a research article | Check |
|---|---|---|---|
| A1 | Thematic explicitness and moralizing: 3.28 vs 3.94 (about 20 % higher for AI) [T1] | Do not end paragraphs or sections by stating the lesson ("This underscores the importance of …", "Ultimately, this shows that …") unless that sentence carries a number, a test or a citation. Let the evidence carry the point. | Read the last sentence of every paragraph. If it is an evaluative statement with no number, citation or figure reference, delete it or replace it with the specific result. |
| A2 | Narrator explicitly comments on the theme: 52 % vs 77 % [T1] | No commentary layer on top of the results: interpretive asides ("…, highlighting the need for …", "This is a reminder that …") need their own evidence. | `check_ai_signs.py --structure` lists paragraph endings and "-ing" tails that comment without evidence; each must be supported or cut. |
| A3 | Moral or philosophical weighting: 3.26 vs 3.68 [T2] | Keep implications at the scale the study supports. A reactor-model paper does not need sentences on the future of the chemical industry or humanity's energy transition. | Every sentence about broad significance (industry, society, sustainability, "the field") has a citation or a number from this study; otherwise remove it. |
| A4 | Thematic unity (everything serves one theme): 4.41 vs 4.74 [T2] | Do not bend every result to the main message. Report results that complicate it. | The Results section contains at least one finding stated as a limitation, a surprise, or a case where the method does not help, if such results exist. They usually do. |
| A5 | Dialogue used for philosophical debate: 34 % vs 59 % [T2] | Discussion paragraphs debate the results, not abstractions ("the role of data-driven methods in process engineering"). | Each Discussion paragraph refers to a specific result of this paper (number, figure or table) in its first two sentences. |
| A6 | References are vague allusions ("implicit echoes"): 50 % vs 72 % [T1] | Never "previous studies have shown" or "it is well known" without naming and citing the studies. | No sentence about other work lacks a citation; `citation_density.py audit` lists them. |

**B. AI performs description: bodies, senses, settings**

| # | Finding (human vs AI) | In a research article | Check |
|---|---|---|---|
| B1 | Emotion conveyed through the body and bodily metaphors: 38 % vs 81 % [T2] | Name quantities and phenomena plainly instead of figuratively ("the heart of the process", "the reactor breathes", "the catalyst struggles"). | No metaphor stands in for a technical term; search for heart, backbone, breathe, struggle, journey, landscape, ecosystem used figuratively. |
| B2 | Explicit emotion labels (human-elevated): 29 % vs 8 % [T2] | The human habit here is to name the thing directly. In papers: say "the conversion fell by 12 %" rather than "the conversion suffered". | Verbs that give processes feelings or intentions (suffers, struggles, wants, prefers, tries) are replaced by the measured change. |
| B3 | Setting mirrors characters' inner states: 3.58 vs 4.07 [T3/T2] | Do not dress neutral context in evaluative atmosphere ("in an increasingly challenging and uncertain landscape"). | Opening and context sentences contain facts (values, dates, sources), not mood. |
| B4 | Environmental and ecological emphasis: 2.83 vs 3.21 [T2] | Environmental and sustainability statements only with numbers and sources (emissions per tonne, energy per unit, with reference). Quantified environmental indicators are fine; decorative ones are not. | Each environmental claim has a number, a unit and a source or comes from this study's results. |
| B5 | Smell-based imagery: 57 % vs 82 % [T3] | No equivalent in papers. | Only for narrative passages. |
| B6 | Sensory density: 3.66 vs 3.93 [T2] | Cut descriptive adjectives that add no information (detailed, comprehensive, thorough, rich, extensive, intricate). | For each such adjective, ask what number or fact would justify it; if none, delete. |
| B7 | Depth of access to characters' inner lives: 3.67 vs 3.93 [T2] | Do not attribute minds to methods, models or researchers ("the network learns to understand", "researchers have long sought to"). | No mental verbs (understand, know, believe, seek, want) with a model, algorithm or "the field" as subject. |

**C. AI streamlines structure: one track, tidy causes, internal resolution**

| # | Finding (human vs AI) | In a research article | Check |
|---|---|---|---|
| C1 | Continuity of one main causal chain: 3.92 vs 4.20 [T2] | Avoid one tidy causal story for all results. Where several mechanisms contribute, or the cause is unclear, say so. | At least the main explanations name their evidence type (`results-discussion-writing.md` §0) and, where plausible, an alternative explanation. |
| C2 | Resolution driven by the protagonist's own choice: 46 % vs 69 % [T2] | The proposed method is not a hero that resolves everything. Credit conditions, data and prior work; state what it does not solve. | The Results and Conclusion contain at least one explicit statement of what the method does not achieve, or under which conditions it fails. |
| C3 | No subplots at all: 57 % vs 79 % [T2] | Do not cut side analyses, negative results or failed variants just to keep the story clean; place them briefly (one paragraph, a table, or the supplement). | Compare the planned analyses with what is reported: anything run and dropped is either reported or its omission is justified. |
| C4 | Resolution through internal understanding or acceptance: 27 % vs 47 % [T2] | Conclusions end in concrete outcomes, not in "insight", "understanding" or "a deeper appreciation of". | Ban "provides valuable insights", "sheds light on", "deepens our understanding", "paves the way" unless followed by the specific insight. |
| C5 | Central character introduced by external description: 30 % vs 52 % [T2] | Introduce a method or concept by what it does in this problem, not by a generic description of its class. | The first sentence about each method contains its role here ("X predicts … from …"), not only a textbook definition. |
| C6 | Opening grounded in a clearly described place: ord 2.12 vs 2.33 [T2] | Do not open with formulaic scene-setting ("In today's rapidly evolving world …", "In recent years, … has attracted increasing attention"). | The first sentence of the Introduction states a specific fact with a citation (`introduction.md` §3). |
| C7 | Spatial granularity (fine detail of physical space): ord 2.27 vs 2.53 [T3/T2] | Describe the system at the level the method needs; do not add descriptive detail that no equation or result uses. | Every dimension or detail in the system description is used later (in an equation, a parameter table or a result). |
| C8 | Investment in characters before the threat: 2.76 vs 2.99 [T2] | Do not delay the problem with long general background. | The gap is reached within the first third of the Introduction for a standard article, or the literature part is organized toward it (`introduction.md` §6a). |

**D. Humans name their sources; AI alludes (intertextual richness)**

| # | Finding (human vs AI) | In a research article | Check |
|---|---|---|---|
| D1 | Explicit named references to texts and authors: 47 % vs 24 % (about double for humans) [T1] | Name specific studies, datasets, standards, plants, software and their versions. Avoid "a popular model", "state-of-the-art methods", "commercial software". | Every method, dataset, tool and comparison is named and cited; no "well-known", "popular", "standard" without the name. |
| D2 | Balanced mix of explicit and implicit references: 37 % vs 16 % [T1] | Combine specific citations with your own synthesis of them; do not reduce the literature to vague gestures. | The literature part has both cited specific findings and your own comparative statements about them (`literature-review.md`). |

**E. Humans address the reader; AI writes as if no one is watching (reader engagement)**

| # | Finding (human vs AI) | In a research article | Check |
|---|---|---|---|
| E1 | Breaking the fourth wall: ord 0.67 vs 0.39 [T3, inverted] | Not appropriate in a journal article. Do not imitate. | – |
| E2 | Direct address of the reader: ord 0.28 vs 0.07 [T3, inverted] | Address the reader only through ordinary signposting ("Section 4 shows …"); no "you, dear reader". | – |

**F. Humans use time and surprise; AI tells events in order (temporal complexity)**

| # | Finding (human vs AI) | In a research article | Check |
|---|---|---|---|
| F1 | A revelation forces re-reading of earlier scenes: 3.28 vs 2.95 [T2] | When a later result changes the meaning of an earlier one, say so and point back to it. | Later sections refer back explicitly when they revise or qualify an earlier result ("This explains the deviation in Section 4.1"). |
| F2 | Chronological discontinuity: 2.40 vs 2.12 [T2, inverted form] | Papers are not narrated in time order either way. The AI default (a straight first-to-last account) appears in papers as a laboratory diary: "First we …, then we …, next we …". Organize Methods and Results by logic and question, not by the order of work. | No section reads as a sequence of "first, then, next, after that" describing your work history. |
| F3 | Time jumps used to stage delayed disclosure: 1.96 vs 1.68 [T3] | Do not withhold the main result for effect; state it early (`results-discussion-writing.md` §1.4). | The main finding appears in the first paragraph of its subsection. |
| F4 | Flashbacks and flash-forwards (anachrony): 2.58 vs 2.31 [T3] | No equivalent. | – |

**G. Humans range more widely (narrative diversity)**

| # | Finding (human vs AI) | In a research article | Check |
|---|---|---|---|
| G1 | Number of distinct locations: ord 1.34 vs 1.08 [T2] | A claim of generality needs more than one case, condition or dataset. | Any "general", "broadly applicable" or "transferable" claim is backed by results on more than one case, or is scoped to the one tested. |
| G2 | Dialogue-to-narration proportion: 2.95 vs 2.70 [T3] | No equivalent. | – |
| G3 | Subplots that run parallel to the main theme: 42 % vs 21 % [T2] | Integrate secondary analyses with the main argument (sensitivity, robustness, failure cases) instead of omitting them or listing them unconnected. | Each secondary analysis states in one sentence what it adds to the main claim. |
| G4 | Protagonist's choices framed as morally ambivalent: 59 % vs 38 % [T1/T2] | Present the method's trade-offs: accuracy vs cost, gains vs assumptions, where it is better and where it is not. A uniformly positive account is a warning sign. | The paper states at least one cost or disadvantage of the proposed approach with a number (computation time, data needs, error outside the range). |
| G5 | (See B2: humans name emotions explicitly, 29 % vs 8 %.) | | |

### 8.3 Patterns of the AI cluster as a whole

| # | Finding | In a research article | Check |
|---|---|---|---|
| H1 | The five models occupy one tight region of narrative space: mean human–AI centroid distance 6.6 vs AI–AI 4.3 (1.6×); the human source is further from every model (minimum 6.2) than any two models are from each other (maximum 6.0) [T1] | Different models write alike. A draft built from model defaults will look like every other model-built draft. | For each section, list the structural choices made (order, what is foregrounded, what is left out). If each one is the obvious default, change at least the ones the content gives you reason to change. |
| H2 | Human stories are more dispersed (distance to centroid 33.2 vs 27.4, +22 %) and rarer (rarity percentile 0.71 vs 0.49, Cohen's *d* = 0.83); the human version is the rarest of six in 57.8 % of prompts (chance 16.7 %) [T1] | What makes a paper distinctive is its specific content: its system, its numbers, its unexpected results, its disagreements with the literature. | Each paragraph contains at least one element that could not appear in a paper on another system (a value, a name, a condition, a figure reference). |
| H3 | Removing surface artifacts lowered detection only from 95.5 % to 93.9 % [T1] | Editing word choice does not change structure. Running the word-level checks (§§2–5) is necessary but not sufficient. | After word-level editing, review the structure with the A–G checks above. |
| H4 | No single narrative dimension is sufficient or necessary: best single dimension 80.2 %, worst removal −1.2 points; the signals co-occur (linear plots, tight causality, explicit themes, narrow social structure) [T1] | The patterns come together. Fixing one (say, deleting moral endings) while keeping the others leaves the text recognizably generic. | Run all of A–G, not a selection. |

### 8.4 Model fingerprints

The paper also identifies features that mark each source (number of fingerprint features: human 32, Claude 26, GPT 11, Gemini 11, DeepSeek 7, Kimi 3). For a writer working with one of these models, its fingerprint shows which defaults to watch.

| Source | Fingerprint (from the paper) | In a research article | Check |
|---|---|---|---|
| Claude (Sonnet 4.6) | Restraint: the flattest escalation of events (uniqueness 22.4 vs next source), lowest event-type diversity, the most uniform voice; reverent continuation of literary convention (62 % vs 39–56 % for others); favours epilogues, avoids dream sequences; quiet endings | **Flat emphasis:** every result reported with the same weight and the same sentence shape; deference to prior work; a gentle summary at the end of every unit. | The main result is visibly more prominent than secondary ones (first position, own subsection or sentence, numbers); disagreements with earlier studies are stated when the data show them; no closing summary paragraph after each subsection. |
| GPT (5.4) | Gossip and rumour as a plot mechanism (64 % vs 44–55 %); stories framed as distant retrospection; subverts expectations more than other models (41 % vs 27–36 %); ambiguous reconciliations | **Hearsay and retrospection:** "it is often said", "it has been widely reported", "over the past decades, researchers have …" | No claim rests on unnamed reports; no "over the past decades" opening without a cited trend. |
| Gemini (3 Flash) | Tidiest endings and extended denouements; bleakest settings (88 % tagged bleak and oppressive); defaults to external character description; mostly direct speech; ordeal/siege schemas | **Dramatic problem framing and long wind-downs:** "critical", "pressing", "urgent" challenges; conclusions that restate everything. | Problem statements use numbers, not alarm; the Conclusion does not repeat each result section. |
| DeepSeek (V3.2) | Front-loads crucial context that others reveal later; visible narrator; emotions shown by behaviour; backstory evenly interleaved | **Background before the point:** long context before the claim of a paragraph. | The first sentence of each paragraph states its claim; background follows only as needed. |
| Kimi (K2.5) | Fewest fingerprints and lowest attribution F1: the generic centre of the AI distribution; opens in the middle of action; does not label traits | **Generic centre:** prose that could belong to any paper. | Covered by H1 and H2. |
| Human | Introduces characters in dialogue; single focal character; no direct reader address in this subset; back-loaded revelation; crossover genres | Human fingerprints are not rules for papers; journal conventions (main result early, IMRaD order) take precedence. | – |

## 9. Self-check procedure

1. Run `scripts/check_ai_signs.py` on the draft (plain text, Markdown or LaTeX). It flags watch-words, "-ing" analysis tails, "serves as"-type constructions, negative parallelisms, em dashes, chat leftovers and placeholders, with line numbers. Add `--structure` for the discourse-level checks of §8 that can be detected automatically: moralizing or insight-type paragraph endings without evidence, vague and hearsay attribution, anthropomorphic verbs, formulaic and retrospective openings, alarm framing, diary-style sequences, and a count of limitation and trade-off statements.
2. For each flag, ask: is there a specific fact, number or citation behind this? If yes, write that instead. If no, delete.
3. Read each paragraph's first sentence: does it state a specific claim about this study? Read each paragraph's last sentence: does it add evidence, or only a lesson (§8, A1)?
4. Count adjectives of importance (crucial, significant, key, important) per page; each must be justified by data or a citation.
5. Go through the A–G and H checks of §8 for structure: complications reported, trade-offs stated, sources named, main result emphasized, generality scoped.
6. Verify all citations (§6).
7. Read the section aloud; rewrite sentences that sound like a press release or a summary of a summary.

## Sources

Russell, J., Rajendhran, R., Pham, C. M., Iyyer, M., Wieting, J. (2026). StoryScope: Investigating idiosyncrasies in AI fiction. Conference on Language Modeling (COLM 2026). arXiv:2604.03136v6. Code and data: https://github.com/jenna-russell/storyscope. Findings in §8 are reported with the paper's numbers; the research-article rules are this skill's translation.


Adapted and condensed, in our own words and for research articles, from *Wikipedia: Signs of AI writing* (WikiProject AI Cleanup, https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), which documents these patterns with examples and research references. The Wikipedia page is a descriptive field guide for detecting AI text; this file turns the observations into writing guidance.
