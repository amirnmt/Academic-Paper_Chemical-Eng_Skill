# Resources: full texts the skill can search

The files in `references/` are short, structured summaries. This folder holds full texts that the skill searches when a summary is not enough, for example "how do the guides suggest ending an Introduction?" or "which phrases do papers in my target journal use to introduce a validation?".

| Folder | Content | In the public repository? |
|---|---|---|
| `open/` | Openly licensed writing guides, converted to Markdown | Yes (see `open/NOTICE.md`) |
| `guides/` | Your own converted writing guides and books | No: kept on your computer only |
| `journal-papers/` | Your own converted papers, ideally recent papers from the target journal | No: kept on your computer only |

`.gitignore` keeps everything in `guides/` and `journal-papers/` out of the repository except their README files. Most writing guides and all journal papers are copyrighted; keep them for your own use and do not publish or share them.

## 1. Add your own material

Convert PDFs to Markdown and put them in the right folder:

```bash
pip install 'markitdown[pdf]'
python scripts/convert_to_markdown.py path/to/guide_pdfs resources/guides
python scripts/convert_to_markdown.py path/to/journal_paper_pdfs resources/journal-papers
```

The converter keeps the text but damages equations, tables and multi-column layouts. Always check numbers, equations and quotations against the original PDF.

Good sources for `guides/`: writing guides and books you own or have access to through your library; open-access genre studies of research articles (for example Maswana et al. 2015 in *Ampersand*, CC BY-NC-ND). Good sources for `journal-papers/`: 15–30 recent research articles from the target journal, on topics close to yours.

## 2. Search the texts

```bash
python scripts/search_resources.py "topic sentence"
python scripts/search_resources.py "first sentence" introduction --context 4
python scripts/search_resources.py hedging --dir resources/guides --max 5
python scripts/search_resources.py --list          # files and sizes
python scripts/search_resources.py --headings      # section headings of each file
```

Several terms must all occur within the context window (default ±3 lines). Quoted terms are matched as phrases; matching ignores case. The output gives file, line number and the nearest heading, so a passage can be checked in the original.

Use what you find as guidance, in your own words. Do not copy passages from the guides into a paper.

## 3. Build a phrase list from the target journal

```bash
python scripts/build_section_phrases.py resources/journal-papers --out section_phrases.md
```

The script splits each paper into Abstract, Introduction, Literature review, Methods, Results, Discussion and Conclusion by its headings, then lists for each section:
- the most common sentence openers (first words of sentences), and
- recurring 3–6-word phrases used by several different papers.

Phrases shared by many papers are the conventional language of the journal and field, which is what reviewers expect to read. Phrases from a single paper are not listed, so the output is a list of shared conventions, not of anyone's sentences. Papers whose headings could not be recognized are reported at the end of the file.

## 4. How the skill uses this folder

- It reads the summaries in `references/` first.
- When a question needs more detail or the user asks what a guide says, it runs `search_resources.py` and reports what it found, with file and line, in its own words.
- When `journal-papers/` contains papers, it runs `build_section_phrases.py` and prefers the journal's own conventions over the general phrase bank.
- A journal profile kept in `journal-papers/` (for example `<JOURNAL>_journal_requirements.md` summarizing the Guide for Authors, `<JOURNAL>_section_models.md` with the section structure of the journal's papers, and the phrase list) is read at the start and overrides the general defaults.
