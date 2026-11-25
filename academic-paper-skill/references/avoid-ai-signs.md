# Avoiding the signs of AI-generated writing

AI-generated text drifts toward the generic: it smooths specific facts into statements that could fit any topic, inflates importance, and repeats a small set of words and sentence patterns. In a research article these habits are not only recognizable, they are bad writing: they replace evidence with emphasis and precision with vagueness.

The goal of this file is precise, specific writing. It is not a way to hide AI use. Disclose AI assistance as the target journal requires, and make sure every claim, number and citation has been checked by the authors.

Read this file before drafting, and run the check in §8 on every draft section.

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

## 8. Self-check procedure

1. Run `scripts/check_ai_signs.py` on the draft (plain text, Markdown or LaTeX). It flags watch-words, "-ing" analysis tails, "serves as"-type constructions, negative parallelisms, em dashes, chat leftovers and placeholders, with line numbers.
2. For each flag, ask: is there a specific fact, number or citation behind this? If yes, write that instead. If no, delete.
3. Read each paragraph's first sentence: does it state a specific claim about this study?
4. Count adjectives of importance (crucial, significant, key, important) per page; each must be justified by data or a citation.
5. Verify all citations (§6).
6. Read the section aloud; rewrite sentences that sound like a press release or a summary of a summary.

## Source

Adapted and condensed, in our own words and for research articles, from *Wikipedia: Signs of AI writing* (WikiProject AI Cleanup, https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), which documents these patterns with examples and research references. The Wikipedia page is a descriptive field guide for detecting AI text; this file turns the observations into writing guidance.
