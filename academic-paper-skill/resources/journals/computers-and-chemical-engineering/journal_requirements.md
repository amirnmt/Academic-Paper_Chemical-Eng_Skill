# Computers & Chemical Engineering: requirements for authors

Source: Guide for Authors, saved 26 November 2026; https://www.sciencedirect.com/journal/computers-and-chemical-engineering (Guide for authors). Paraphrased; check the original before submission, as journals update their rules.

## Fit and article types
- Scope: computing and systems technology applied to chemical engineering problems. Listed areas include modelling, numerical analysis and simulation; optimization; informatics and intelligent systems; process dynamics, control and monitoring; process safety; plant operations; energy and environmental applications.
- Accepted contributions also include new applications of established methods, comparisons of alternative methods and descriptions of state-of-the-art industrial applications. Software reports must use computing technology in a new way.
- Full-length papers must be complete and authoritative and presented clearly and concisely. No word or page limit is stated for them.
- Short notes: at most 8 pages, double spaced. Letters: about 2 pages. Reviews: contact the editor first.
- Review: single anonymized; editors screen first, then usually at least two reviewers.

## Files and layout
- Source file: Word (.doc/.docx, single column) or LaTeX (.tex; double column allowed). A PDF is not accepted as the source.
- Sections numbered 1, 1.1, 1.1.1; the abstract is not numbered. Cross-reference by section number, not "see the text".
- Appendices A, B, … with equations (A.1), tables Table A.1, figures Fig. A.1.
- Footnotes sparingly, numbered consecutively.
- American or British English, not a mixture.

## Title page
- Concise, informative title; avoid abbreviations and formulas unless widely established.
- Full author names; affiliations with lowercase superscript letters and full postal address including country.
- One corresponding author, with e-mail (published). Only the corresponding author's affiliation decides eligibility for institutional open-access agreements.

## Abstract, keywords, highlights, graphical abstract
- Abstract: at most **250 words**, factual: purpose, basic procedure, main findings (with significance where applicable), principal conclusions; emphasize what is new. Stand-alone; avoid references (if essential, author and year); avoid uncommon abbreviations or define them.
- Keywords: **1–7**, in English; avoid multi-word keywords joined by "and" or "of"; abbreviations only if firmly established.
- Highlights: **required**, **3–5 bullet points**, each **at most 85 characters including spaces**, describing the new results and methods; separate editable file with "highlights" in the file name.
- Graphical abstract: encouraged; at least 1328 pixels wide, landscape, readable at 13 cm width; TIFF, EPS, PDF or MS Office; separate file.

## Structure
- No fixed section list. Numbered sections; theory and calculation sections may extend the background and develop it practically. Recent papers usually follow Introduction (with literature) → process/system description → methodology → case study → results and discussion (often combined) → conclusions; see `section_models.md`.
- Nomenclature not required by the guide; used by about a third of recent papers.

## Units, equations, tables, figures
- SI units; give SI equivalents for any other unit.
- Equations as editable text, not images; simple formulas inline; solidus (X/Y) for small fractions; variables in italics; powers of e as exp; displayed equations numbered consecutively in the order cited.
- Tables as editable text, cited in the text, numbered in order of appearance, with captions, notes below the table body; no vertical rules or shading; do not duplicate results shown elsewhere; use sparingly.
- Figures: cited and numbered in order; each a separate file (Figure_1, Figure_2, …); in LaTeX they may be embedded. Caption = short title plus description; explain every symbol and abbreviation.
  - Vector drawings: EPS or PDF with fonts embedded.
  - Photographs: TIFF/JPG/PNG, at least 300 dpi. Bitmapped line drawings: at least 1000 dpi.
  - Do not combine several unrelated graphs into one file; make colour figures readable for colour-blind readers.
- Generative AI may help with schematics and with data visualizations produced reproducibly from data; disclose it in the caption and in the AI declaration. It must not create or alter images of primary data.

## References (author–year style)
- In the text: (Smith, 2020); (Smith and Jones, 2020); (Smith et al., 2020); or narrative "Smith et al. (2020) showed …". Groups ordered alphabetically then chronologically, or the reverse, consistently.
- Reference list alphabetical, then chronological; 2020a, 2020b for the same authors and year.
- Journal names abbreviated according to ISO 4 / LTWA. Include DOIs. Every reference must exist and be complete; cited ⇔ listed.
- Datasets: add [dataset] before the reference; software and preprints may be cited (mark preprints; cite the published version once it exists).
- Unpublished results and personal communications: preferably in the text only. "In press" means accepted.
- LaTeX: use Elsevier's `elsarticle` class with an author–year bibliography style (for example `elsarticle-harv`). In BibTeX, keep DOIs in every entry.

## Declarations and statements
- Declaration of competing interests (declarations tool, uploaded as .docx).
- Funding statement in the standard form, or the sentence stating that no specific grant was received.
- CRediT author-contribution statement (corresponding author provides it).
- Research data: **Option C**: deposit data in a repository and link it at submission, or explain why data cannot be shared (the statement is published).
- **Declaration of generative AI use** in a separate section before the references, if AI tools were used for writing (not needed for basic grammar, spelling or reference tools). AI tools cannot be authors.
- Acknowledgements in a separate section directly before the references (including help with language or proofreading).
- Authorship changes after submission are rarely accepted and never after acceptance: fix the author list and order before submitting.

## Originality, plagiarism and text reuse (publisher-level policies)

- New submissions to many Elsevier journals are screened automatically with Crossref Similarity Check (iThenticate); editors interpret the report, and no fixed percentage applies. Duplicate submissions to the journal are checked separately (title, abstract, authors).
- A thesis, an abstract or an electronic preprint does not count as prior publication (Elsevier policy on prior publication, 2016).
- Reuse of your own published text follows COPE's text-recycling guidance: possible in Methods with citation; not in Results or Conclusions.
- Details, sources and the pre-check: `references/plagiarism-and-paraphrasing.md` §9, §11.

## Submission and after acceptance
- Checklist: corresponding author with full details; all files (figures, tables, captions, supplementary files); spelling and grammar checked; references complete in both directions; permissions for copyrighted material.
- Optional: free SSRN preprint at submission; co-submission of a data or methods article to Data in Brief or MethodsX (those charge an APC).
- Proof corrections are due within two days.
- Open access: hybrid journal (subscription publication or open access with an article publishing charge; institutional agreements may cover it, based on the corresponding author's affiliation).

## Defaults kept (not specified in the guide)
- Length of full-length papers: no limit stated; recent papers have a median of about 8–9 figures and 5–6 tables.
- Cover letter and suggested reviewers: not specified; prepare a short cover letter (`submission-and-reviewers.md`).
- LaTeX template: Elsevier `elsarticle` (the guide accepts LaTeX source; double column allowed).
