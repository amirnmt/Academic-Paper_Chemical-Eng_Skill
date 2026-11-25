# The writing process: from notes to a finished draft

Experienced writers plan extensively, write in a set order, revise in rounds, and build their references as they go. This file covers how to organize the work; the section files cover what to write.

## 1. Before writing

- **Choose the target journal first.** Its scope, readership, article types, length limits, abstract type, reference style and template shape the paper. Read several recent papers in it; note their structure (IMRD or ILM[RD]C), the length and detail of each section, and how paragraphs are built.
- **Know the audience.** Decide which terms and procedures need definition and which can be assumed known. Write for researchers in neighbouring fields, not only for the few working on exactly your problem.
- **Have a provisional title and an outline** with one-line purposes for each paragraph. Without a plan you will write in several directions at once.
- **Set up a reference manager** (Zotero, EndNote, JabRef/BibTeX) before you start.
- **Build a phrase list for your field.** For each section, collect words and phrases that recur in 15–30 good papers in your target journal (`scripts/build_section_phrases.py` extracts them from converted papers). Consult it while writing.

## 2. Order of writing

The writing order differs from the order of the paper:
1. **Methods** first, ideally while the work is still in progress (details are fresh; equipment and co-authors are available).
2. **Results** together with the figures and tables, which should be tightly integrated.
3. **Literature review** and **Introduction** (the Introduction can be drafted early, while the context is fresh, and finalized later).
4. **Discussion**, after the Results are complete.
5. **Conclusion**.
6. **Abstract**, then **title** (provisional → draft → final), **keywords**, **highlights**.
7. Acknowledgements, declarations, cover letter.

Start writing early. Writing reveals inconsistencies in the results and gaps in the analysis while there is still time to fix them.

## 3. Write in English

Draft directly in English rather than translating from your native language. Translation produces unnatural English and long, foreign sentence structures; improving an imperfect English draft is easier. Keep laboratory notebooks and notes in English if possible.

## 4. Drafting without blocking

- Do not try to write the final version at the first sitting. Get the content down; polish later.
- If you cannot start: write freely for a few minutes about the section without stopping or correcting, then organize what you wrote.
- Start with easy parts (methods, figure captions, acknowledgements, keywords) to get going.
- If a passage does not progress, leave it and return later.
- Keep a notebook (or a folder per section) for ideas that come while you are not writing; many good ideas appear away from the desk.
- Write regularly: a fixed daily slot produces more text than occasional long sessions.
- While drafting, do not polish the English; express the ideas first.

## 5. References while writing

- Insert each citation the moment you write the claim, with the full record in the reference manager. Adding references "later" is slow and error-prone.
- Read the original source before citing it; never copy a citation from another paper without checking it.
- Keep complete information for every reference (all authors, title, journal, volume, pages, DOI), even if the target journal uses a short style: you may need it for another journal later.
- Paraphrase in your own words; quote only when the exact wording matters, with quotation marks and source. Reusing your own published text without citation is self-plagiarism.

## 6. Revising

Writing is recursive: draft, redraft, then edit. Revise in rounds, from large to small:
1. **Structure and argument:** does each section do its job? Does the Discussion answer the Introduction's questions? Is the gap closed?
2. **Paragraphs:** one idea each; topic sentences tell the argument when read alone.
3. **Sentences and words:** clarity, concision, terminology, tense.
4. **Final pass from beginning to end:** consistency of numbers, terms, symbols, units, references.

Techniques:
- **Stand back:** leave the draft for a few days, then read it as a reader would, checking whether each step of the argument leads to the next.
- **Read aloud:** sentences that sound wrong usually are.
- **Use checklists** (`checklists.md`) and the self-review roles (`self-review.md`).
- **Ask for feedback:** a colleague who has not seen the work, ideally from your field, and fluent in English. Ask specifically whether they could repeat the methods.
- **Talk about the writing** with co-authors; explaining the argument aloud often shows where it is weak.

## 7. Co-authors and timing

- Agree on authorship and author order early; everyone listed must have contributed substantially and approve the final version.
- Ask co-authors to write or check their parts (especially methods they carried out) while the work is fresh.
- Keep earlier drafts: a section cut on one reviewer's advice may be requested by another.
- Meet journal deadlines; tell the editor early if you need more time.

## 8. Using an AI assistant responsibly

- The authors are responsible for every statement, number and citation.
- Verify every citation against the source and every number against the data (`scripts/check_citations.py`; `evidence-base.md`).
- Rewrite generic, inflated or AI-typical prose (`avoid-ai-signs.md`; `scripts/check_ai_signs.py`).
- Disclose AI assistance as the target journal requires.
