# Evidence base: from a folder of papers to verified citations

Read this before writing any section that cites literature. The paper can only be as good as the notes behind it.

## 1. Inventory the repository

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

## 2. Convert and check

- Convert PDFs to Markdown (for example with MarkItDown) for fast reading and searching.
- Conversion damages equations, tables, Greek letters, subscripts and multi-column layouts. Before quoting any number, equation, kinetic parameter or table value, check it against the original PDF.
- Never copy text into the paper from a conversion. Paraphrase from your notes.

## 3. Theme map (broad → narrow)

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

## 4. Comparison matrix of the closest studies

Build a table of the 10–20 studies closest to yours. It feeds the literature review, the gap statement and the Discussion.

| Key | System | Model / method | Dimensions & regime | Heat-transfer correlation | Validation data | Metric | Main result | Limitation |
|---|---|---|---|---|---|---|---|---|

Read the matrix by column. A gap usually appears as a column where most cells are empty or the same (for example, "no study compares predicted radial profiles with measurements at low tube-to-particle ratios").

## 5. Citation rules

- Cite only papers in the repository or papers verified by DOI. Title, authors and year must match the source.
- Every cited claim must say what the source actually says, at the same strength. Do not upgrade "may" into "does".
- If unsure, write `[CHECK: key — what to verify]` instead of citing.
- Keep a citation map in the notes: claim → key → page/table/figure.
- Cite the original source of any named model, correlation, kinetic scheme, equation of state, dataset or criterion (e.g. Peng–Robinson, Ergun, a specific rate law).
- Common knowledge needs no citation; anything specific, numerical, recent or contestable does.
- Prefer peer-reviewed journal papers. Cite books with chapter and pages. Avoid websites, personal communication and unpublished data; if unavoidable, follow the journal's rule for them.
- Insert the citation the moment the sentence is written. Adding references "later" is the main source of wrong citations.

## 6. Citation forms

- Information-prominent (non-integral): the finding is the subject, the citation is in brackets. "Silver catalysts promoted with Cs and Re reach higher selectivity [12,15]." Use for most statements.
- Author-prominent (integral): the researcher is the subject. "Smith et al. [12] showed that …". Use when the specific study, its method, or a disagreement between authors matters.
- Group citations for a shared point ([3–7]); split them when studies differ in method or result.
- Avoid long strings of citations without comment; say what the group of studies shows.

## 7. Verification before submission

Run `scripts/check_citations.py refs.bib --tex <files>`: it resolves each DOI in OpenAlex and Crossref, compares title, first author and year, flags retracted papers, suggests DOIs for entries without one, and lists duplicates, missing fields, cited keys missing from the .bib file and uncited entries. Then check by hand what no script can: that each source supports the sentence that cites it.


- Resolve every DOI (OpenAlex, Crossref or the publisher site) and compare title, authors, year, journal, volume, pages.
- Check that every in-text citation has a reference entry and every entry is cited.
- Search for duplicates (the same paper under two keys, preprint and published version).
- List any remaining `[CHECK]` items for the author, and the repository papers that were not used.
- Report themes where the repository is thin rather than padding them.
