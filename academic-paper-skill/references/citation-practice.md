# Citation practice: every literature-based claim is supported

How to decide which sentences need a citation, how many sources to cite, where the citation goes, and how to write an Introduction from the papers the user provides. Read this before drafting the Introduction or a literature review, and before revising either. Use it with `evidence-base.md` (finding, reading and verifying sources) and `introduction.md` / `literature-review.md` (structure).

Levels used in this file (see `journal-profile.md` §0): **[Rule]** standing rule of this skill; **[G]** general scientific writing; **[D]** chemical and process engineering; **[J-obs]** observed in a journal's published papers (here *Computers & Chemical Engineering*, 20 research articles; numbers are conventions, not requirements).

## 1. The rule [Rule]

The skill's author set this rule for all writing done with the skill:

> When writing the Introduction of a scientific article, virtually every sentence containing a scientific statement, factual assertion, or literature-based claim requires one or more citations. We must not make unsupported scientific claims. Every literature-based statement must be supported by one or more credible academic sources. … When I specify the directories containing the scientific literature for our own article, you must develop the introductory sections comprehensively using those sources. You must not independently generate unsupported scientific claims, assumptions, or conclusions. Exceptions include statements describing our own research, methodology, objectives, original contributions, and findings. … This does not mean copying sentences directly from other publications. … Prioritize the scientific relevance, accuracy, and suitability of each reference rather than increasing the number of citations artificially. The fundamental principle is that no scientific claim should remain unsupported by appropriate evidence.

In practice:
1. **A sentence that states something about the world or about other work carries a citation**, in the Introduction, the literature review and wherever else such a statement appears (Methods for method origins, Discussion for comparisons).
2. **The source must support that sentence**, at the same strength and for the same conditions. Find the source first, then write the sentence from it. Never write the sentence and look for a source afterwards.
3. **The sentence is written in your own words.** Paraphrase the finding; do not copy or lightly edit the source's sentences (§10).
4. **No source, no claim.** If the user's papers do not support a statement, either leave the statement out or mark it `[CITATION NEEDED: what must be shown]` and report it. Do not fill the gap from memory, and never invent or guess a reference.
5. **Relevance over count.** Cite the sources that best support the claim; do not add weak or loosely related sources to raise the count (§5).

This rule is stricter than what many published papers do. In the 20 *Computers & Chemical Engineering* papers analysed, about half of the background and literature sentences carry no citation, and roughly two thirds of those uncited sentences are factual statements that a reviewer could ask to see supported (§6). Follow the rule, not that average.

## 2. Which sentences need a citation

| Kind of sentence | Citation? | What to cite |
|---|---|---|
| Fact about a process, product, material or market (production volume, uses, hazards, properties, energy use, emissions, regulation) | Yes | Primary data source, handbook, review or official report; for numbers, the source of that number |
| Definition of a technical term, method or model | Yes | The original paper, a standard textbook or a review |
| Statement that research has addressed something ("Several studies have modelled …") | Yes | The studies meant (a representative set) or a review |
| What a specific study did or found | Yes | That study |
| Strength or limitation of earlier work ("these models neglect …") | Yes | The works being evaluated, in that sentence or unambiguously in the one before |
| A gap ("few studies have …", "no model has yet …") | Yes, where possible | The few studies or the closest ones; "no study" claims rest on a stated search and are hedged ("to our knowledge") |
| Origin of a named model, correlation, kinetic scheme, equation of state, algorithm, dataset, software or criterion | Yes | The original source (plus the version or edition used) |
| A number, equation or figure taken from elsewhere | Yes | The exact source, with table or page if useful |
| An inference you draw from facts cited in the same paragraph ("Hence, the hot-spot temperature is sensitive to …") | No new citation, if the premises are cited | Write it visibly as an inference (therefore, hence, this implies) |
| A topic sentence that only announces a group of studies, whose members are cited in the next sentences | Optional | Better: cite a review in it |
| Your own objective, approach, methods, contributions, findings, scope and the paper outline | No | Cite only the methods or data you take from others |

**In chemical and process engineering papers [D]**, the claims that most often need a source, and the usual kind of source:
- production capacity, market, energy use, emissions of a process or product: statistics of agencies or industry associations, technical encyclopedias, recent reviews; give the year of the number;
- hazards and properties of chemicals (flammability limits, toxicity, decomposition): handbooks, safety data and the primary measurements;
- process descriptions (catalyst, reactor type, operating window): technical encyclopedias, reviews, the papers that describe the plant;
- kinetic models, correlations (heat and mass transfer, pressure drop), equations of state, property methods: the original papers, plus the paper whose parameter values you use;
- benchmark processes and datasets (for example a standard simulated plant used for monitoring and control studies): the paper that defined them and the version used;
- plant or pilot data taken from earlier papers: the paper that reported them, with table or figure.

Common knowledge is a narrow exemption: a fact found in every undergraduate textbook of the field ("the reaction is exothermic") may stand without a source; anything specific, numerical, recent, industrial or contestable may not. When unsure, cite.

## 3. Writing from the user's literature directories [Rule]

When the user names directories with the papers for the article, write the Introduction and literature review from those papers.

1. **Inventory.** Convert the PDFs (`scripts/convert_to_markdown.py`) and list every paper with key, topic and what it can support (`evidence-base.md` §3). Read the papers themselves, not only the abstracts.
2. **Plan the argument as claims.** For each planned paragraph, list the claims it must make (importance → background → approach families → their limits → gap → present work).
3. **Build a claim–evidence map** before drafting:

   | Claim (planned sentence, in note form) | Source key(s) | Where in the source (page, table, figure) | What the source actually says (paraphrased) | Strength (shows / suggests / assumes) |
   |---|---|---|---|---|

   Use `python scripts/search_resources.py "term" --dir <papers>` to find which papers discuss a point.
4. **Draft sentence by sentence from the map.** Each sentence carries the citations of its row; adjust the verb to the strength column.
5. **Mark what is missing.** A claim with no row in the map is either dropped or written as `[CITATION NEEDED: …]`. Collect these and tell the user which themes are thin; offer to search for further papers (`evidence-base.md` §1) and add only papers the user accepts and that are verified by DOI.
6. **Audit** (§9) before handing the draft over.

## 4. Where the citation goes [G]

- **After the claim it supports.** For a sentence with one claim, at the end of the sentence. In the analysed papers, 69 % of cited sentences end with the citation.
- **After each clause** when a sentence makes several claims from different sources (31 % of cited sentences carry a citation in mid-sentence): "Smaller catalyst particles reduce internal diffusion limitations [4], whereas larger ones lower the pressure drop [7]." A citation at the end of a long sentence implies that every source supports every part.
- **After each item of an enumeration** when the items come from different sources: "… including empirical correlations [3,4], molecular simulation [5] and machine-learning models [6–8]."
- **Information-prominent** (citation in brackets) for most statements; **author-prominent** ("Lee et al. (2021) showed …", "Lee et al. [9] showed …") when the specific study, its method or a disagreement matters (§7).
- Do not cite in the first sentence of the abstract or in figure captions unless the figure is taken from a source; never cite in highlights.

## 5. How many sources per claim [G, J-obs]

| Claim | Sources | Note |
|---|---|---|
| A specific finding, number or method | 1 | The original study |
| A general statement about a process or method | 2–3 | Strong, recent sources; a review plus one or two original papers |
| "Widely used", "extensively studied", "several approaches" | 3–5 | Representative, not exhaustive; or one review |
| Taxonomy of approaches | 1–3 per category | A citation group after each category |
| More than about 6 | Avoid | Split the claim, cite a review, or keep the most relevant |

Observed in *Computers & Chemical Engineering* [J-obs]: a cited sentence carries a median of 1.8 citations; 52 % of cited sentences cite one source, 27 % two, 9 % three and 12 % four or more; the most heavily cited sentence of a paper typically has 3–8 sources. About half of the cited sentences cite more than one source.

## 6. Density across the Introduction [J-obs, Rule]

Citation density falls as the Introduction moves from the world to the paper. Per-paper medians from the 20 papers (pooled values in brackets):

| Part | Share of sentences cited | Citations per sentence | Target under the rule |
|---|---|---|---|
| Opening (importance, background) | 0.54 (0.53) | 0.86 (1.11) | Every factual sentence cited: about 0.8–1.0 |
| Literature (approach families, studies, limits) | 0.44 (0.50) | 0.80 (0.98) | Every sentence about other work cited: about 0.8–1.0; uncited sentences only for inferences and signposts |
| Gap | 0.38 (0.41) | 0.38 (0.62) | Cite the closest or the few existing studies in the gap paragraph |
| Present work, contributions | 0.04 (0.13) | 0.10 (0.23) | Only method or data origins |
| Roadmap | 0 | 0 | None |

Whole Introduction, per paper (median, interquartile range): 55 sentences (38–73), 9 paragraphs (7–13), 1,364 words (1,037–1,704); 40 citation instances (27–54) to 36 unique references (25–43); 38 % of sentences cited (26–47 %); 0.69 citations per sentence (0.43–1.00); 2.6 citations per 100 words (2.0–3.6). The papers with the most thoroughly supported Introductions cite 53–62 % of all their sentences; because the present-work and roadmap parts are almost never cited, an Introduction that follows the rule will reach roughly 0.55–0.70 overall. The first sentence was cited in only 6 of 20 papers; under the rule, cite it.

Use these numbers as a check, not as a target to reach by padding. A low share of cited sentences in the opening or literature part means unsupported claims; a high number of citations per cited sentence may mean citation dumps.

## 7. Synthesis: one sentence, several sources [G]

Synthesis sentences combine sources around a point of yours. Patterns, from the most to the least compact:

- **Shared finding:** a claim, then the group: "Two-dimensional models resolve the radial temperature profile that controls the hot spot [8–11]."
- **Taxonomy:** categories, each with its own citation group: "Wall heat transfer has been described by lumped coefficients [3,4], by two-parameter models that separate bed and wall resistances [5,6] and by resolved particle-scale simulations [7–9]."
- **Contrast:** "Most studies report an increase in … with … [12–14], whereas [15] observed a decrease under …"
- **Range:** "Reported coefficients range from A to B for … [9–14]."
- **Lineage:** "Early models assumed … [2]; later work added … [5,6]; recent studies … [9]."
- **Chain of studies (author-prominent):** one study per clause with what it did: "Lee et al. (2019) fitted …, Kim and Park (2021) extended … to …, and Müller et al. (2023) validated … against pilot data." Useful when the methods differ in ways that matter; tiring if longer than three or four studies.
- **Group then exemplify:** a claim with a group citation, then one or two sentences on the most relevant study.

Close a group with an evaluation in your voice, attributed to the works evaluated: "These models, however, rely on correlations fitted at large tube-to-particle ratios [12,13]."

## 8. Verbs and tenses for cited work [G]

- **Specific study, what it did:** past simple (proposed, developed, used, formulated, applied, measured, compared). **What it found:** past simple (showed, found, reported, observed, indicated, demonstrated).
- **A line of research continuing to now:** present perfect ("have been proposed", "has received attention"). In the analysed papers about one sentence in eight in the background and literature parts uses it.
- **Accepted knowledge:** present simple, with the citation ("Silver is the industrial catalyst for … [3].").
- Match the verb to the source's certainty: "suggested" for a cautious source, "showed" for a demonstrated result; "claimed" or "assumed" only when you mean to distance yourself.
- Author-prominent citations are a choice of emphasis: in the analysed papers narrative citations were under 5 % of the citations in most papers (18 % pooled), but a few papers write almost the whole literature part as a chain of named studies. Choose one dominant mode and use the other where it adds meaning.

## 9. Audit before handing over

1. Run `python scripts/citation_density.py audit <draft.tex|.md> --benchmarks resources/journals/<journal>/citation_benchmarks.json`. It prints the density metrics next to the journal's range, the density in each part of the Introduction, the **uncited sentences in the background, literature and gap parts**, and sentences with six or more citations.
2. For each listed uncited sentence: add the supporting source, rewrite it as an explicit inference from sources cited in the same paragraph, turn it into a statement about your own work if that is what it is, or delete it.
3. For each heavily cited sentence: check that every source supports the whole sentence; otherwise split the claim.
4. Check by hand that each citation supports its sentence at the same strength (`evidence-base.md` §10), then run `scripts/check_citations.py` on the bibliography.
5. Report the remaining `[CITATION NEEDED]` and `[CHECK]` items to the user.

## 10. Paraphrase, do not copy [G]

- Take the finding, not the sentence: read the passage, close it, write what it showed in your own structure, then check the numbers against the source.
- Do not reproduce another paper's sequence of sentences or arguments with small changes; similarity checks find it and reviewers recognize it.
- Technical terms and names of methods are shared vocabulary and can be reused.
- Quote word for word only when the wording itself matters (a definition, a contested claim), in quotation marks with the source and page.

## 11. Other points

- **Recency** [J-obs]: in the analysed papers the median cited reference was 4 years older than the citing paper; 58 % of citations were at most 5 years old and 77 % at most 10. Combine foundational sources with recent ones; a literature part with no source from the last three years looks out of date.
- **Own earlier work:** cite it where it is relevant, as you would cite anyone else ("In our previous work (Lee et al., 2024), …"); state what is new relative to it. A paper that continues an earlier one ("Part 2") may refer to Part 1 for the full literature review, but still cites the sources of its own claims.
- **Abstract:** no citations [G, J-obs: 3 of 20 abstracts had one, always to the earlier study the paper builds on].
- **Reviews and secondary citations:** cite a review for a broad statement; cite the original for a specific finding. Never cite a paper only because another paper cites it; if unavoidable, write "(original, cited in source)".
