# Resources: journal profiles and full texts the skill can search

The files in `references/` are short, structured summaries. This folder holds what is specific to you and your target journal, and full texts the skill searches when a summary is not enough.

| Folder | Content | In the public repository? |
|---|---|---|
| `journals/<journal>/` | One **journal profile** per target journal: requirements from its Guide for Authors, and (optional) section models and phrases from its papers | The profile files yes; the converted guide and papers no |
| `open/` | Openly licensed writing guides, converted to Markdown | Yes (see `open/NOTICE.md`) |
| `guides/` | Your own converted writing guides and books | No: kept on your computer only |
| `field-papers/` | Your own converted papers from your research field (e.g. your reference repository) | No: kept on your computer only |

`.gitignore` keeps `guides/`, `field-papers/` and each profile's `guide.md`, `requirements_draft.md` and `papers/` out of the repository. Writing guides and journal papers are usually copyrighted; keep them for your own use and do not publish or share them.

## 1. Start with the target journal

Send the skill the journal's Guide for Authors (and, if you can, 10–20 recent papers from the journal). The skill then builds a profile:

```bash
python scripts/journal_profile.py init "Journal Name" --guide guide.pdf --papers sample_papers/
python scripts/journal_profile.py check "Journal Name"
python scripts/journal_profile.py list
```

`init` converts the guide, sorts its lines by requirement field into `requirements_draft.md`, converts the papers and builds their phrase list. Claude then writes `journal_requirements.md` (template in `references/journal-profile.md` §3) and, from the papers, `section_models.md`. Without a guide, the skill uses the default profile (`references/journal-profile.md` §4) and tells you so. To write for another journal later, build another profile; the old one stays. `journals/computers-and-chemical-engineering/` is an example.

## 2. Add your own material

Convert PDFs to Markdown and put them in the right folder:

```bash
pip install pymupdf            # or: pip install 'markitdown[pdf]', or pypdf
python scripts/convert_to_markdown.py path/to/guide_pdfs resources/guides
python scripts/convert_to_markdown.py path/to/field_paper_pdfs resources/field-papers
```

The converter keeps the text but damages equations, tables and some layouts. Always check numbers, equations and quotations against the original PDF.

Good sources for `guides/`: writing guides and books you own or have access to through your library; open-access genre studies of research articles (for example Maswana et al. 2015 in *Ampersand*, CC BY-NC-ND).

## 3. Search the texts

```bash
python scripts/search_resources.py "topic sentence"
python scripts/search_resources.py "first sentence" introduction --context 4
python scripts/search_resources.py hedging --dir resources/guides --max 5
python scripts/search_resources.py "it can be seen" --dir resources/journals/<journal>/papers
python scripts/search_resources.py --list          # files and sizes
python scripts/search_resources.py --headings      # section headings of each file
```

Several terms must all occur within the context window (default ±3 lines). Quoted terms are matched as phrases; matching ignores case. The output gives file, line number and the nearest heading, so a passage can be checked in the original.

Use what you find as guidance, in your own words. Do not copy passages from the guides or papers into a paper.

## 4. Build a phrase list

```bash
python scripts/build_section_phrases.py resources/field-papers --out resources/field-papers/section_phrases_field.md
```

(`journal_profile.py init --papers` does this automatically for a journal's sample papers.) The script splits each paper into Abstract, Introduction, Literature review, Methods, Results, Results and Discussion, Discussion and Conclusion by its headings, then lists for each section how it begins, the most common sentence openers, phrases typical of the section, common phrases and recurring terms, counted by the number of papers that use them. Phrases from a single paper are not listed, so the output is a list of shared conventions, not of anyone's sentences. Papers whose headings could not be recognized are reported at the end of the file.

## 5. How the skill uses this folder

- At intake it asks for the target journal's guide and reads or builds that journal's profile; the profile overrides the skill's defaults.
- It reads the summaries in `references/` first. When a question needs more detail or the user asks what a guide says, it runs `search_resources.py` and reports what it found, with file and line, in its own words.
- While drafting it uses the journal's `section_phrases.md` first, the field's phrase list second and the general phrase bank third.
