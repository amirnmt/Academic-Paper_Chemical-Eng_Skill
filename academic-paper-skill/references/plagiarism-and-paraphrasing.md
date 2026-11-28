# Plagiarism, paraphrasing and text reuse

Read this file before writing any sentence that reports other work, before reusing text from your own thesis or papers, and before submission. Run `scripts/check_overlap.py` on every section that cites literature (§11).

Levels: [Rule] = integrity requirement of this skill; [G] = general good practice from the guides; [J-req] = publisher or journal requirement. Sources at the end; everything here is paraphrased.

---

## 1. What counts as plagiarism in a research paper

Plagiarism is presenting another person's work as your own without adequate credit. The work can be **words, ideas, methods, processes, results, data, figures or equations**, published or unpublished, in print or online (Oxford; Gastel and Day 2022, after the US National Institutes of Health; William 2024).

Three points matter for an engineering article:
- **Intent does not decide it.** Copying without noting the source, or not knowing the conventions, is still plagiarism (Oxford). Most cases in student and early-career writing are unintentional (William 2024, citing Pecorari 2003).
- **A citation alone does not make copied wording acceptable.** Copied or closely paraphrased wording with a reference still claims the wording as yours (Oxford; Hohenheim).
- **Paraphrased ideas still need the source.** Your own words do not make someone else's idea, method or result yours (Hohenheim; Oxford).

Consequences in publishing: rejection, retraction after publication, and editors declining later submissions from the same authors (Lövei 2021). Plagiarism found in one part of a manuscript taints the whole of it.

---

## 2. The forms, with what they look like in a modelling paper [Rule]

| Form | What it is | In an EO reactor or process-modelling paper | Fix |
|---|---|---|---|
| Verbatim copying | Words, phrases or sentences taken unchanged, without quotation marks | A sentence on EO hazards or on the silver catalyst copied from a review | Paraphrase and cite; quote only if the wording itself matters (§7) |
| Close paraphrase (patchwriting, mosaic plagiarism) | The source's sentence kept with some words swapped, reordered or the voice changed | A kinetic-model description with "rate" → "velocity" and active → passive | Rewrite from notes with your own structure (§5) and cite |
| Uncited paraphrase (idea plagiarism) | An idea, method, result or argument in your own words without the source | A heat-transfer correlation or a model-reduction idea described without its origin | Cite the original source of the idea |
| Ambiguous attribution | A paragraph built from one source with a single citation at the end, so the reader cannot tell what came from where | Three sentences on reactor runaway, one citation after the last | Cite each claim, or introduce the source at the start ("According to X …") and keep to it (§8) |
| Inaccurate or secondary citation | A reference attached to a claim it does not back up, or a paper known only through another paper but cited as if read | Citing an original 1970s kinetics paper known only from a review's reference list | Cite only what you read; otherwise "as reported by [review]" (§8; `research-integrity.md` §3) |
| Text recycling (self-plagiarism) | Reusing your own earlier text without saying so | Paragraphs from the Bachelor thesis or an earlier paper | Acceptable only in limited places and with citation (§9) |
| Duplicate or redundant publication | Publishing the same results again, or slicing one study into several papers without cross-reference | The same surrogate results in two journals | Never; disclose related submissions to the editor |
| Figures, tables, equations, data | Reproduced or adapted without source or permission | A reactor schematic or a kinetic table taken from a paper | Cite; "adapted from"; permission for copyrighted figures (§10) |
| Translation plagiarism | Text translated from another language without credit | A paragraph from a Persian or German source rendered in English | Treat a translation as a quotation or paraphrase: cite it |
| Unacknowledged assistance | Substantive help with content not acknowledged; text written by others, including AI tools, presented as your own | Undisclosed AI-generated paragraphs; a colleague's analysis | Acknowledge assistance; declare AI use as the journal requires (§12) |

Not plagiarism:
- **Common knowledge**, general or field-specific, needs no citation (Hohenheim). Examples: ethylene oxide is produced by partial oxidation of ethylene over silver; the Arrhenius form of a rate constant. If you are not sure your readers share it, cite it (Oxford; Hohenheim). The citation rule of this skill (`citation-practice.md` §1–§2) is stricter than general advice: any specific fact, number or interpretation gets a source.
- **Your own ideas, results, tables and figures** from this study (Hohenheim).
- **Shared technical vocabulary**: method names, quantities and standard phrases ("effective radial thermal conductivity", "pseudo-homogeneous model", "mean absolute error") can be reused; they are not paraphrased away (Hohenheim; Bolton).

---

## 3. The standard: what makes a paraphrase acceptable [Rule]

The guides do not set the bar at the same height.
- The Bolton tutorial demonstrates paraphrasing with one sentence changed by a single synonym and a switch to the passive voice. Hohenheim lists synonyms, word order, sentence structure and voice as quick tips.
- Oxford, by contrast, rejects a synonym-swapped rewrite that follows the source's structure, even when cited. Hohenheim's own checklist says that changing a few words does not make the text yours.
- Similarity software (§11) matches runs of words, so it finds lightly edited sentences.

For a journal article, use the stricter standard: **a paraphrase is acceptable only when both the wording and the sentence structure are your own, the meaning is unchanged, and the source is cited.** The mechanical techniques in §6 are tools for writing your own sentence, not a paraphrase on their own. Most good paraphrases in research papers also do something the source did not: compress, combine with other sources, or connect the point to your argument.

**Summary versus paraphrase.** A paraphrase restates one passage at about its length; a summary condenses an argument or a whole paper. Research papers mostly summarize: one sentence on what a study did and found, then on to the comparison (`literature-review.md`). Oxford recommends a brief summary of the author's argument in your own words as the safer alternative to close paraphrase.

---

## 4. A workflow that prevents plagiarism [G, Rule]

1. **Notes in your own words, with the source attached.** Record author, year, page, table or figure with every note (William 2024; Gastel and Day 2022). Note keywords and numbers, not sentences (Hohenheim; Bolton). Mark any phrase you copy into notes with quotation marks so it cannot slip into the draft unmarked.
2. **Write the claim–evidence map** (`citation-practice.md` §3): each planned claim with its source location and what the source shows, paraphrased.
3. **Draft without looking at the source.** Write the paragraph from the map, then open the source to check accuracy (Gastel and Day 2022).
4. **Check each sentence against the source** (§5 step 5) and run `check_overlap.py` (§11).
5. **Never paste converted PDF text into the manuscript**, not even as a placeholder (`evidence-base.md` §4).
6. **Writing in a second language:** patchwriting is a known stage of learning to write in another language (Pecorari 2003, as cited by William 2024), so check your own drafts for it deliberately. A useful habit is to keep notes as keywords, numbers and short phrases (in English or Persian), and to write the English sentence from the notes, not from the source sentence. A sentence-by-sentence translation of a source is still a close paraphrase of it.

---

## 5. How to paraphrase, step by step [G]

Combined from Bolton (six steps), Hohenheim (tips and checklist) and Gastel and Day (drafting away from the source).

1. **Read until you understand.** You cannot restate what you have not understood; a paraphrase shows the reader how well you read the source (Bolton; Hohenheim).
2. **Mark what must not change**: technical terms, names, numbers, units, formulas and conditions (Bolton step 2). In chemical engineering this list is long: *selectivity*, *conversion* and *yield* are not synonyms; *superficial velocity* is not *flow rate*; numbers keep their precision.
3. **Decide what you need.** Usually one finding, with its conditions, not the whole passage. Decide where it goes in your argument.
4. **Write from your notes**, in your own structure, with the subject that suits your paragraph (often the variable or the comparison, not the source's subject).
5. **Compare with the original** (Bolton step 4; Hohenheim checklist):
   - Did the structure change, not only words?
   - Are there runs of the source's wording? Put any that must stay in quotation marks, or rewrite.
   - Are the technical terms and numbers retained exactly?
   - Is the meaning the same, including scope and strength ("suggests" stays "suggests"; conditions stay attached)?
6. **Cite it**, at the claim it supports (§8).

---

## 6. Techniques for writing your own sentence [G]

Use them together, and only after step 4 above. One alone (a synonym, a voice change) produces patchwriting.

| Technique | Source idea | Your sentence |
|---|---|---|
| Change the starting point (subject) | The study as subject: "They found that selectivity falls as …" | The variable as subject: "Selectivity fell from … to … as the hot-spot temperature rose …" |
| Verb ↔ noun (nominalization) | "Conversion increases when the inlet temperature is raised" | "An increase in inlet temperature raises conversion …" |
| Split or merge sentences | One long sentence with three findings | Two sentences grouped by your argument, or one finding merged with a second source |
| Change the order to fit your argument | Source: mechanism, then consequence | You: consequence (what matters for your reactor), then the mechanism |
| Combine sources (synthesis) | Two studies, two sentences | "Both [a] and [b] report … , although [b] observed it only above …" |
| Make time and comparison explicit | "ten years ago", "more rapidly" | "since 2015", "about twice as fast" (Bolton: time words, comparatives) |
| Change the linking logic | "Because of A, B" | "B; this follows from A" (Bolton: conjunctions, adverbials) |
| Synonyms, carefully | General words only | "develop" → "improve" is fine; technical terms never change (Bolton warns that a thesaurus can destroy meaning) |
| Active ↔ passive | Use only together with other changes | A voice switch alone keeps the source's structure |

---

## 6a. Worked examples from reactor modelling [Rule]

The source passages below are **invented for illustration** (not taken from any paper), written in the style of a modelling article. The verdicts follow the standard of §3.

**Example 1: a finding from the literature**

*Source (invented, "Smith et al. [12]", p. 5):* "In the industrial reactor, the selectivity to ethylene oxide decreased from 82 % to 76 % as the hot-spot temperature increased from 245 °C to 262 °C, because the complete combustion of ethylene accelerates more strongly with temperature than its partial oxidation."

| Attempt | Text | Verdict |
|---|---|---|
| 1. Copied with citation | In the industrial reactor, the selectivity to ethylene oxide decreased from 82 % to 76 % as the hot-spot temperature increased from 245 °C to 262 °C … [12]. | **Plagiarism.** The source's sentence without quotation marks; the citation does not make the wording yours |
| 2. Synonyms | In the commercial reactor, the EO selectivity dropped from 82 % to 76 % when the hot-spot temperature rose from 245 °C to 262 °C, since total ethylene combustion speeds up more strongly with temperature than partial oxidation [12]. | **Close paraphrase (patchwriting).** Same structure, clause order and logic; long matching runs; a similarity check flags it |
| 3. Voice switch plus synonyms (the light technique of some tutorials) | A drop in EO selectivity from 82 % to 76 % was observed by Smith et al. [12] when the hot-spot temperature was raised from 245 °C to 262 °C, which was attributed to the faster acceleration of complete combustion … | **Still close paraphrase.** The structure is the source's, turned round |
| 4. Acceptable paraphrase | Smith et al. [12] attributed a loss of about six points in EO selectivity (82 % to 76 %) over a 17 K rise in hot-spot temperature to the higher activation energy of complete combustion compared with epoxidation. | **Acceptable.** Own structure (the attribution leads, the cause is expressed through activation energies), numbers and terms exact, cited |
| 5. Better: integrated into your argument | The hot spot limits selectivity: in an industrial EO reactor, selectivity fell by about six points between hot-spot temperatures of 245 °C and 262 °C [12], consistent with the higher activation energy of total combustion [12,15]. Our model reproduces this trend (Section 4.2) … | **Best.** Summarized, combined with a second source and with your own result; your voice is clear |

Check for attempt 4: the paraphrase must not overstate the source. If the source only "attributed" the drop to combustion kinetics, do not write that it "was caused by" it.

**Example 2: a method description**

*Source (invented, "Lee and Park [8]"):* "The pressure drop along the catalyst bed was calculated with the Ergun equation, using a bed porosity of 0.42 and an equivalent particle diameter of 7.5 mm."

- *Acceptable when you used the same method:* "Pressure drop was computed from the Ergun equation [5] with a bed voidage of 0.42 and an equivalent particle diameter of 7.5 mm, taken from [8]."
- Why it is acceptable although it is close: the Ergun equation, bed porosity and equivalent particle diameter are shared vocabulary; method descriptions have few possible wordings (COPE; Gastel and Day 2022). What matters is that the origin of the equation [5] and of the parameter values [8] is cited (`methodology-writing.md` §11).

**Example 3: your own earlier text (Bachelor thesis)**

*Thesis sentence (illustration):* "An artificial neural network with two hidden layers was trained on 2,000 DWSIM simulations to predict the outlet temperature of the fixed-bed reactor."

- In a new article's **Methods**, if the article uses the same surrogate: rewrite to fit the new context and cite the thesis if it is publicly available (§9).
- In the **Results** or **Conclusions**: do not reuse thesis sentences; the article states its own new results.

---

## 7. Quoting [G]

- Quote only when the exact wording matters: a definition you adopt, a disputed claim, a statement whose wording is the point. Verbatim quotation is unusual in primary research papers in engineering (Lövei 2021; Gastel and Day 2022).
- Mark it with quotation marks (or as an indented block for long quotations) and cite it with the page (Hohenheim; Oxford). Use the citation style of the journal; for numbered styles, add the page in the citation if the style allows ("[12, p. 4]").
- Keep quotations short. Lövei (2021) notes that about three sentences is the usual maximum without asking the copyright holder's permission, and that primary papers rarely quote even that much.
- Quoted and unquoted material from one source must not be mixed so that the reader cannot tell which is which (Oxford).

---

## 8. Where the citation goes [Rule]

- **Cite each claim**, not each paragraph. A citation only at the end of a paragraph can be read as covering only the last sentence (Hohenheim).
- **When several consecutive sentences come from one source**, introduce the source at the start ("Rahimpour et al. [7] measured …; they found …; their data also show …") and keep the sentences visibly theirs; then mark clearly where your own evaluation begins ("These data, however, do not …") (Hohenheim; Oxford).
- **Secondary sources:** if you know an original only through another paper, say so ("… [3], as reported by [9]") and cite what you read (Oxford). Better, obtain and read the original.
- **Your evaluation versus the source's claim** must be distinguishable at every point (Oxford). When you build on one study's argument heavily, say so in the text and explain how your view differs (Oxford).

---

## 9. Reusing your own text: theses, earlier papers, preprints [J-req, G]

**What publishers and COPE say**
- Elsevier does not treat an academic thesis, an abstract or an electronic preprint as prior publication. A journal paper based on your thesis is therefore possible (Elsevier 2016).
- COPE's text-recycling guidance (developed with BioMed Central) judges reuse of your own text by where it occurs and how much:
  - **Methods:** limited ways exist to describe a method, so reusing wording is often acceptable when the earlier source is cited and the reuse is transparent.
  - **Introduction:** some reuse can be acceptable.
  - **Discussion:** limited reuse only.
  - **Results:** reuse there usually amounts to duplicate publication and is nearly always unacceptable.
  - **Conclusions:** reuse is seldom acceptable, because they should state what is new.
- Gastel and Day (2022) also note that papers from one long project can legitimately describe shared methods in similar words.

**Rules for this skill [Rule]**
- **Results, discussion and conclusions** are written new for the article.
- **Methods:** you may reuse a description of a method you published before only with a citation to that publication (or a statement that the method is described in detail in [x]). Shorten it to what the reader needs.
- **Introduction and literature review:** rewrite. Your thesis literature review will be outdated and organized for a different purpose anyway.
- **Theses:** a thesis is not prior publication, but reusing its wording raises the similarity score if the thesis is online. Rewrite, cite the thesis where the article builds on it, and check what your university requires.
- **Figures from your own published papers** belong to the publisher if you transferred copyright: follow the permission rules in §10.
- **Disclose to the editor** any related manuscript under review or in press.

---

## 10. Equations, figures, tables and data [Rule]

- **Equations:** a standard equation from a textbook or a well-known correlation (Ergun, Arrhenius) is cited to its original or a standard reference; an equation taken or adapted from a specific paper is cited to that paper ("adapted from [x]") with what you changed. Similarity software cannot check equations (Elsevier); reviewers do.
- **Figures:** a figure reproduced from a copyrighted publication needs permission unless its licence allows reuse (e.g. CC BY); a redrawn or adapted figure still cites its source ("adapted from [x]") (`evidence-base.md` §9). Similarity software cannot check figures either.
- **Tables of literature values:** cite the source in the caption or in a footnote per column (`section_models.md` §8 of the C&CE profile).
- **Data from other studies** (e.g. plant data of Rahimpour et al.): cite the source with the table or figure the values come from, and state any processing you did.

---

## 11. The journal's similarity check and your own pre-check [J-req, G]

**What the journal does**
- Elsevier screens new submissions to many of its journals automatically with Crossref Similarity Check, which runs on iThenticate (the system behind Turnitin) (Elsevier).
- The comparison database holds full texts contributed by more than 200 publishers, over 50 million articles. It is not complete: material from non-participating publishers and older print-only work can be missing (Elsevier).
- Editors also run a separate duplicate-submission check against the journal's own submissions (title, abstract, authors) (Elsevier).
- **The score is not a verdict** (Elsevier). Cited reuse, the reference list and methods text all add to it, and editors interpret the report. A score concentrated on one source is read differently from the same score spread thinly over many: 30 % from one paper differs from 1 % each from 30.
- There is no published threshold. Concentrated overlap with a single source, overlap in the Results or Conclusions, and long unquoted runs are what draws attention.

**What you do before submission**
- Pre-screen your own manuscript (Gastel and Day 2022). Institutional Turnitin access, where available, compares against a wide database. Free online checkers vary in quality, and many store what you upload: do not upload unpublished manuscripts to services that keep them.
- Run `python scripts/check_overlap.py <draft> --sources <folder of converted papers and your thesis>`. It lists every passage that shares a run of at least 8 words (adjustable) with one of your sources, with source file and line. It also reports the share of the draft covered by each source. It checks only against the files you give it, typically the papers you cite and your own earlier texts: the most likely places for accidental overlap.
- For each flagged passage: if it is shared technical vocabulary or a standard method phrase, leave it; if it is the source's wording, quote it or rewrite it (§5); if it is your own earlier text, apply §9.

---

## 12. AI tools [J-req, Rule]

- *Computers & Chemical Engineering* requires a declaration of generative-AI use in writing, placed before the references; AI tools cannot be authors (`journal_requirements.md`).
- **Do not use "paraphrasing" tools to disguise source text.** Automated rewording typically changes words and keeps structure: exactly the close paraphrase of §2. The result is still plagiarism even if the similarity score drops.
- AI drafting tools can reproduce wording from their training data, misattribute ideas, or invent references. Every sentence that reports other work must be traced to a source you have read (`research-integrity.md` §3; `citation-practice.md` §1). Run `check_overlap.py` on AI-assisted text as on any other.
- Substantive help (content, analysis, interpretation) is acknowledged; routine language editing is not (Oxford's distinction for human help; apply the journal's rules for AI).

---

## 13. Checklist [Rule]

- [ ] Every idea, method, result, number, equation, figure and dataset from others is cited at the claim it supports.
- [ ] No sentence keeps a source's structure with words swapped; every paraphrase was written from notes and compared with the source (§5).
- [ ] Technical terms, numbers, units and conditions are exactly as in the source; the strength of each claim is unchanged.
- [ ] Quotations are rare, marked, and cited with the page.
- [ ] Multi-sentence summaries of one source are framed so the reader knows where the source ends and your evaluation begins.
- [ ] No secondary citation presented as a primary one.
- [ ] Own earlier text: Results, Discussion and Conclusions new; any reused methods text cited; thesis text rewritten; related submissions disclosed.
- [ ] Figures and tables from others cited, permissions obtained where needed.
- [ ] `check_overlap.py` run on the full manuscript against all cited papers available and your own earlier texts; every flagged run resolved.
- [ ] AI use declared as the journal requires; no automated paraphrasing of sources.

---

## Sources

- University of Oxford. *Plagiarism*. Academic guidance, Study skills. https://www.ox.ac.uk/students/academic/guidance/skills/plagiarism (consulted 28 November 2026): definition, eight forms, worked examples of poor and acceptable rewriting, citation of secondary sources, acknowledgement of assistance.
- William, F. K. A. (2024). What is plagiarism in academic writing and how to avoid it: guiding novice researchers. *International Journal of Research Publications* 144(1), 283–286. https://doi.org/10.47119/IJRP1001441320246161: definition, five types, prevention strategies. Its tool recommendations (consumer checkers) are less relevant to journal submission than the publisher's iThenticate screening (§11).
- University of Bolton (2023). *Paraphrasing*. LEAP Online, Academic Writing (Level 2): six-step method and techniques (synonyms, structure, voice, time, comparatives, linking words). Its demonstration paraphrase is lighter than the journal standard used here (§3).
- University of Hohenheim, Faculty of Agricultural Sciences. *Academic Writing Aid Series*, chapter on referencing: how to avoid plagiarism, how to paraphrase, how to quote (pp. 71–77 of the compiled file).
- Gastel, B., Day, R. A. (2022). *How to Write and Publish a Scientific Paper*, 9th ed., Ethics in scientific publishing (pp. 29–31).
- Lövei, G. L. (2021). *Writing and Publishing Scientific Papers*. Open Book Publishers. https://doi.org/10.11647/OBP.0235 (citing, paraphrasing, plagiarism and self-plagiarism, pp. 131–132 of the book).
- Pecorari, D. (2003). Good and original: plagiarism and patchwriting in academic second-language writing. *Journal of Second Language Writing* 12, 317–345 (as cited by William 2024).
- COPE (Committee on Publication Ethics) and BioMed Central. *Text recycling guidelines for editors*. https://publicationethics.org (where reuse of one's own text may be acceptable, by section).
- Elsevier. *Plagiarism detection* (for editors). https://www.elsevier.com/editor/perk/plagiarism-complaints/plagiarism-detection (Crossref Similarity Check, interpretation of the score).
- Elsevier (2016). *Clarification of our policy on prior publication*. https://www.elsevier.com/connect/clarification-of-our-policy-on-prior-publication (theses, abstracts and preprints are not prior publication).
