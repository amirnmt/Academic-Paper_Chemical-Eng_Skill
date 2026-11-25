# Evidence base: from a folder of papers to verified citations

Read this before writing any section that cites literature. The paper can only be as good as the notes behind it.

## 1. Fill the gaps in the repository

A personal repository is rarely complete. Before writing, check it against a structured search.

- Search several databases (for example Scopus, Web of Science, Google Scholar, OpenAlex). Their coverage never fully overlaps.
- Several small searches that narrow step by step work better than one "perfect" search string. Start with the core concept, then add one restriction at a time.
- Use Boolean operators: `AND` narrows, `OR` widens with synonyms, `NOT` excludes, quotation marks keep a phrase together, `*` truncates. Example: `("fixed bed" OR "packed bed") AND reactor AND ("radial heat transfer" OR "effective conductivity") NOT membrane`.
- Follow citations backwards (the reference lists of the closest papers) and forwards (papers that cite them). The closest two or three papers are the best starting points.
- Draw a mind map of the topic before reading in depth: branches for the themes, with their expected share of the paper. It shows where reading effort should go and keeps the review proportional.
- Obtain papers through the library, interlibrary loan, institutional repositories, the authors' pages, or by writing to the corresponding author.
- Record the search strings, databases and dates. Some journals and reviewers ask for them.

## 2. Read papers, not abstracts

- An abstract is already the authors' interpretation, compressed. Read the paper itself before citing it for anything more than its main claim.
- Efficient order for a first pass: title → abstract → figures and tables with captions → conclusions → the parts of the Methods you need. Read the full text of the 10–20 papers closest to yours.
- Write the note in your own words immediately, with page, table or figure numbers. Notes in your own words protect you from accidental copying later.
- Never cite a paper you have not seen. Errors and distorted claims spread when authors copy citations from other papers. If the original is truly unobtainable, cite it as "[original], as cited in [secondary]" and follow the journal's rule for secondary citation.

## 3. Inventory the repository

For every paper, record one entry in `lit_notes.md`:

```markdown
### [key] FirstAuthor Year — short title
- Citation: Authors (Year). Title. Journal, Vol(Issue), pages. DOI
- Type: original research | review | book chapter | thesis | standard/report
- System: process/material/reactor/data studied (e.g. Cu/ZnO/Al2O3 catalyst, multitubular fixed bed)
- Method: experimental | 1D/2D model | CFD | data-driven/ML | hybrid; key assumptions
- Key result (with numbers): ...
- Limitation (stated by authors or evident): ...
- Relevance to our paper: background | method we follow | direct comparison | validation data | contrasting result
- Themes: T1, T3
- Where in our paper: Intro | Lit review §2.3 | Methods §3.2 | Discussion
```

Rules:
- Record numbers with units and conditions; a result without conditions is useless for comparison.
- Note the page, table or figure for every number you may quote later.
- Mark review papers. They summarize a field quickly, but cite the original study for any specific finding.
- Keep `refs.bib` in step with `lit_notes.md`: one stable BibTeX key per paper (`FirstauthorYearKeyword`, e.g. `Smith2011Kinetics`).
- A reference manager (Zotero, Mendeley, EndNote, JabRef) helps keep the library and exports BibTeX, but its records are often incomplete or wrong. Check them.

## 4. Convert and check

- Convert PDFs to Markdown (for example with MarkItDown) for fast reading and searching.
- Conversion damages equations, tables, Greek letters, subscripts and multi-column layouts. Before quoting any number, equation, kinetic parameter or table value, check it against the original PDF.
- Never copy text into the paper from a conversion. Paraphrase from your notes.
- Converted papers from the repository can also be mined for the phrasing of the target journal (`scripts/build_section_phrases.py`; see `resources/README.md`).

## 5. Theme map (broad → narrow)

Group the papers into 4–8 themes that lead the reader from the field to your gap. Example for a fixed-bed reactor modelling paper:

| Theme | Content | Typical citations |
|---|---|---|
| T1 Process and importance | product use, production routes, economics, safety | 4–8 |
| T2 Catalyst and kinetics | catalyst types, rate expressions, selectivity | 10–15 |
| T3 Reactor modelling | pseudo-homogeneous vs heterogeneous, 1D vs 2D, steady vs transient | 12–20 |
| T4 Heat transfer in packed beds | wall and effective radial conductivity correlations, low tube-to-particle ratios | 8–12 |
| T5 Data-driven and hybrid models | ML surrogates, physics-informed approaches | 10–15 |
| T6 Validation data | pilot and industrial datasets, benchmarking practice | 4–8 |

The totals show how a target of 70+ citations is reached honestly: by covering each theme properly, not by citing many papers for one statement.

## 6. Comparison matrix of the closest studies

Build a table of the 10–20 studies closest to yours. It feeds the literature review, the gap statement and the Discussion.

| Key | System | Model / method | Dimensions & regime | Heat-transfer correlation | Validation data | Metric | Main result | Limitation |
|---|---|---|---|---|---|---|---|---|

Read the matrix by column. A gap usually appears as a column where most cells are empty or the same (for example, "no study compares predicted radial profiles with measurements at low tube-to-particle ratios").

## 7. What to cite, and with what weight

Weight of sources, from strongest to weakest:
1. Peer-reviewed original research papers.
2. Peer-reviewed reviews and scholarly books (cite books with chapter and pages).
3. Standards, theses, technical reports, conference abstracts.
4. Websites, yearbooks, personal communication.

Rules:
- Cite only papers in the repository or papers verified by DOI. Title, authors and year must match the source.
- Every cited claim must say what the source actually says, at the same strength. Do not upgrade "may" into "does".
- If unsure, write `[CHECK: key — what to verify]` instead of citing.
- Keep a citation map in the notes: claim → key → page/table/figure.
- Cite the original source of any named model, correlation, kinetic scheme, equation of state, dataset or criterion (e.g. Peng–Robinson, Ergun, a specific rate law).
- Common knowledge needs no citation; anything specific, numerical, recent or contestable does.
- A reference list is a selection, not an inventory of everything read. Cite what the argument needs.
- Avoid unpublished data, manuscripts in preparation and personal communication. If unavoidable, follow the journal's rule (often in the text only, with the person's full name and affiliation, and a written record kept by you).
- "In press" means accepted. A submitted paper is not "in press".
- Preprints: allowed by many journals, but cite the published version once it exists.
- Self-citation: cite your earlier work where you would cite it if someone else had written it, and not otherwise.
- Insert the citation the moment the sentence is written. Adding references "later" is the main source of wrong citations.

## 8. Citation forms and placement

- Information-prominent (non-integral): the finding is the subject, the citation is in brackets. "Silver catalysts promoted with Cs and Re reach higher selectivity [12,15]." Use for most statements.
- Author-prominent (integral): the researcher is the subject. "Smith et al. [12] showed that …". Use when the specific study, its method, or a disagreement between authors matters.
- Put names or dates into the sentence when they carry information ("first proposed in 1952 [8]").
- Place each citation next to the part of the sentence it supports. Citations collected at the end of a long sentence imply that every source supports every part.
- Group citations for a shared point ([3–7]); split them when studies differ in method or result. Order grouped citations as the journal requires (numerically, chronologically or alphabetically).
- Say what a cited study found. A citation with only praise ("the elegant work of [n]") tells the reader nothing.
- Criticize work, not people: "did not consider" or "was limited to", never "ignored" or "failed to notice".

## 9. Copying, paraphrasing and quoting

- Write in your own words. Short technical phrases ("effective radial thermal conductivity") are shared vocabulary; whole sentences are not.
- Quote word for word only when the wording itself matters, in quotation marks with the citation. Quotations are rare in engineering papers.
- Reusing your own published sentences without citation is self-plagiarism. Most journals run similarity checks.
- Figures or tables taken from other papers need permission from the copyright holder unless the source licence allows reuse; redrawn figures still need the source cited ("adapted from [n]").

## 10. Verification before submission

Run `scripts/check_citations.py refs.bib --tex <files>`: it resolves each DOI in OpenAlex and Crossref, compares title, first author and year, flags retracted papers, suggests DOIs for entries without one, and lists duplicates, missing fields, cited keys missing from the .bib file and uncited entries. Then check by hand what no script can:

- That each source supports the sentence that cites it, at the same strength.
- That journal, volume and pages agree with the publisher's page. The reference list typically contains more errors than any other part of a manuscript.
- That the same paper does not appear twice (two keys, or a preprint and its published version).
- That every in-text citation has a reference entry and every entry is cited.
- List any remaining `[CHECK]` items for the author, and the repository papers that were not used.
- Report themes where the repository is thin rather than padding them.
