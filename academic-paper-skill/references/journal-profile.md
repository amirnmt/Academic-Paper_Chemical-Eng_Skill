# Journal profiles: the target journal's rules override the defaults

Every journal has its own rules for length, abstract, highlights, reference style, figures and declarations, and its own habits for structuring papers. The skill therefore works with a **journal profile**: one folder per journal that records those rules and habits. When no profile exists, the skill uses the **default profile** in §4 and says so.

## 1. Workflow

1. **At intake, ask for the target journal and its Guide for Authors** (a PDF or Word file, a saved web page, or a link). Also ask for 10–20 recent research articles from the journal, ideally close to the user's topic (optional but strongly recommended).
2. **If a profile for that journal already exists** (`resources/journals/<journal>/journal_requirements.md`), read it. Ask whether the guide has changed since the date recorded in the profile; if the user sends a newer guide, rebuild the profile.
3. **If the user sends a guide, build the profile:**
   ```bash
   python scripts/journal_profile.py init "Journal Name" --guide path/to/guide.pdf [--papers path/to/sample_papers]
   ```
   This creates `resources/journals/<journal-slug>/` with
   - `guide.md`: the converted guide (kept local, not committed);
   - `requirements_draft.md`: the guide's lines for each field of the template in §3, with line numbers;
   - with `--papers`: `papers/` (converted sample papers, kept local) and `section_phrases.md`.
   If the guide is a link, open it, save its text to a file, and pass that file. If nothing can be converted, ask the user for the text.
4. **Write `journal_requirements.md`** from the draft and the guide, using the template in §3: every field filled, paraphrased, with the guide's date and the source line numbers for the hard limits. Where the guide is silent, write "not specified" and keep the default from §4, marked "(default)".
5. **If sample papers were given, write `section_models.md`**: the journal's typical section order, the moves of the Introduction and of the (combined) Results and discussion, abstract and conclusion patterns, with counts. Use `introduction.md` §5a and `results-and-discussion-combined.md` as the frame; see the example profile for *Computers & Chemical Engineering* in `resources/journals/`.
6. **Check:** `python scripts/journal_profile.py check "Journal Name"` reports empty fields and leftover TODOs.
7. **From then on, the profile overrides the defaults** everywhere: outline, section names, abstract and highlight limits, reference style (and the LaTeX bibliography style), figure formats, required statements, final checklist.

Several profiles can exist side by side (`python scripts/journal_profile.py list`). The active one is the journal the user names for the current paper; if several exist and none is named, ask.

## 2. Reading a Guide for Authors

- Guides mix rules ("must", "required", "do not exceed") with advice ("we encourage", "consider"). Record rules as rules and advice as advice.
- Hard numbers to capture exactly: word or page limits (per article type), abstract length, number and length of highlights, number of keywords, figure resolution and size, file formats, maximum number of figures, tables or references, character limits for titles.
- The reference style is often given only by example: copy the pattern (author–year or numbered; list order; journal abbreviations; DOI), and choose the matching LaTeX style (for Elsevier `elsarticle-num` or `elsarticle-harv`; for ACS `achemso`; for Springer Nature `sn-jnl` with the matching option; otherwise the journal's template).
- Statements now required by most publishers: competing interests, funding, author contributions (often CRediT), data availability, use of generative AI, and acknowledgements. Record where each goes (title page, end matter, submission system).
- Note the publisher-wide policies the guide links to (ethics, AI, data), but summarize only what the author must do.
- Record the date the guide was saved. Journals change their guides.

## 3. Template for `journal_requirements.md`

```markdown
# <Journal>: requirements for authors
Source: Guide for Authors, saved <date>; <URL>. Paraphrased; check the original before submission.

## Fit and article types
- Scope (one or two lines), article types and their limits (words, pages, figures, references):
- Review model (single/double anonymized), first screening:

## Files and layout
- Accepted source files; template or LaTeX class; columns; line numbers; page size:
- Section numbering; cross-referencing; appendices:
- Language variety:

## Title page
- Title rules; author names and affiliations; corresponding author; other items:

## Abstract, keywords, highlights, graphical abstract
- Abstract: length, structured or not, what it must contain, citations allowed?:
- Keywords: number and rules:
- Highlights / key points: required?, number, character limit, file:
- Graphical abstract / TOC graphic: required?, size, format:

## Structure
- Required or usual sections and their order; Nomenclature; theory/calculation sections:

## Units, equations, tables, figures
- Units; equation format and numbering:
- Tables: format, captions, notes, rules:
- Figures: file types, resolution, size, one file per figure?, captions, colour:
- Generative AI in figures:

## References
- In-text style (with an example):
- Reference list order and format (with an example); journal abbreviations; DOIs:
- Data, software and preprint references; unpublished work; "in press":
- LaTeX bibliography style:

## Declarations and statements
- Competing interests:
- Funding:
- Author contributions:
- Data availability (policy level and wording):
- Generative AI use (where and wording):
- Acknowledgements; ethics; other:

## Submission and after acceptance
- Cover letter; suggested reviewers; checklist items; preprints; proofs; open-access options and costs:

## Defaults kept (not specified in the guide)
- <field>: <default from journal-profile.md §4>
```

## 4. Default profile (used only when no guide is available)

Typical of engineering journals from the large publishers. Replace with the journal's rules as soon as the guide is available, and tell the user which defaults were used.

| Field | Default |
|---|---|
| Article type | Full-length research article; no length limit assumed; aim for the length of recent papers in the field |
| Source file | LaTeX, `elsarticle` class (`\documentclass[preprint,12pt]{elsarticle}`), single column; Word only if the user prefers it |
| Sections | Numbered: 1 Introduction (with the literature review unless the field uses a separate one), 2 Methods / Model / Methodology (with process or data description if needed), 3 Results and discussion (or separate Results and Discussion), 4 Conclusions; Nomenclature if many symbols; appendices A, B |
| Title | Concise and specific; no abbreviations or formulas unless widely known |
| Abstract | One unstructured paragraph, at most 250 words, no citations, abbreviations defined |
| Keywords | 4–6, specific, no repetition of title words where avoidable |
| Highlights | Prepared anyway: 3–5 bullets, at most 85 characters each (easy to delete if not required) |
| Graphical abstract | Optional; prepare if time allows |
| Units and equations | SI units; equations as editable text, numbered consecutively; variables in italics |
| Tables | Editable, numbered, cited, caption with the table, no vertical rules (booktabs) |
| Figures | Vector PDF (or 300 dpi raster, 1000 dpi line art), one file per figure, readable at final width, colour-blind-safe, captions explain all symbols |
| References | Numbered in order of first citation, e.g. [1], [2–4]; list in citation order; ISO 4 journal abbreviations; DOI for every item; LaTeX `elsarticle-num` |
| Statements | CRediT author contributions; declaration of competing interests; funding; data availability; declaration of generative-AI use (before the references); acknowledgements |
| English | One variety (British or American), consistent |
| Submission extras | Cover letter; 3–5 suggested reviewers without conflicts of interest |

## 5. Building the profile from sample papers

When sample papers are available, they show what the guide does not: how long Introductions are, whether the literature review is a separate section, whether Results and Discussion are combined, how many figures are usual, how much the papers cite in the discussion, what the contributions paragraph looks like.

- Convert and analyse: `journal_profile.py init … --papers <dir>` (or `convert_to_markdown.py` and `build_section_phrases.py` separately).
- List the top-level headings of every paper and count the section patterns.
- Read the Introductions and the Results-and-discussion sections of the 6–10 papers closest to the user's topic; record the moves and their order.
- Write `section_models.md`: architecture table with counts; abstract, Introduction, Methods, Results-and-discussion and Conclusion models; typical wording paraphrased; lengths; anything unusual about the journal.
- Paraphrase everything; identify papers by their DOI or PII, not by copying their sentences.
