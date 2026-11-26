# Sources

The guidance in this skill is distilled, in our own words, from the following works. Except for Lövei (2021), whose CC BY 4.0 text is included in `resources/open/` (see `resources/open/NOTICE.md`), they are not included in this repository; obtain them from their publishers or libraries. Several are open access. Users can add their own converted copies to `resources/guides/` and search them with `scripts/search_resources.py`.

**Writing guides**
- Ecarnot, F., Seronde, M.-F., Chopard, R., Schiele, F., & Meneveau, N. (2015). Writing a scientific article: A step-by-step guide for beginners. *European Geriatric Medicine*, 6, 573–579. https://doi.org/10.1016/j.eurger.2015.08.005
- Lövei, G. L. (2021). *Writing and Publishing Scientific Papers: A Primer for the Non-English Speaker*. Open Book Publishers. https://doi.org/10.11647/OBP.0235 (open access, CC BY 4.0)
- Glasman-Deal, H. (2010). *Science Research Writing for Non-Native Speakers of English*. Imperial College Press.
- Gastel, B., & Day, R. A. (2022). *How to Write and Publish a Scientific Paper* (9th ed.). Greenwood.
- Morley, J. (2014). *Academic Phrasebank*. University of Manchester. https://www.phrasebank.manchester.ac.uk/
- University of Hohenheim, Faculty of Agricultural Sciences. *Academic Writing: Practical Guidance and Tips* (Academic Writing Aid Series).
- Chair in E-Business. *Guidelines for Academic Paper Writing* (formatting, captions, formulas, citation).

**Vocabulary and style resources**
- Coxhead, A. (2000). A new academic word list. *TESOL Quarterly*, 34(2), 213–238. https://doi.org/10.2307/3587951. Online sublists: Oxford Learner's Dictionaries, *The Academic Word List* (American English), https://www.oxfordlearnersdictionaries.com/wordlist/american_english/academic/sublist01/
- WikiProject AI Cleanup. *Wikipedia: Signs of AI writing*. https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing (CC BY-SA 4.0; observations condensed and rewritten in our own words for research articles in `avoid-ai-signs.md`)
- Lu, C., Lu, C., Lange, R. T., Yamada, Y., Hu, S., Foerster, J., Ha, D., Clune, J. (2026). Towards end-to-end automation of AI research. *Nature* 651, 914–919 (failure modes summarized and adapted in `research-integrity.md` §2).
- Wu, C.-I. (2026). *academic-research-skills* (CC BY-NC 4.0). https://github.com/imbad0202/academic-research-skills (ideas only, written independently in our own words: failure-mode checklist, claim–source checking, protected qualifiers in the abstract, acronym scopes, section-template pattern; no text or code copied, because its non-commercial licence is not compatible with this skill's CC BY 4.0).
- Song, Y., Song, Y., Pfister, T., Yoon, J. (2026). PaperOrchestra: A multi-agent framework for automated AI research paper writing. arXiv:2604.05018. https://github.com/google-research/paper-orchestra (Apache 2.0; ideas adapted in our own words: results log as single source of truth, inventory of external elements to cite, two-level literature planning with method groups, comparison and concurrent-work rules, literature-review rubric with caps).
- Russell, J., Rajendhran, R., Pham, C. M., Iyyer, M., Wieting, J. (2026). *StoryScope: Investigating idiosyncrasies in AI fiction*. COLM 2026. arXiv:2604.03136v6. https://arxiv.org/abs/2604.03136 (numbers from Tables 16–17 and §§4–5 reported in `avoid-ai-signs.md` §8; the translation of each pattern into a rule for research articles is ours)

**Own analyses used in the skill**
- Section structure, Introduction moves and Results-and-discussion patterns of 20 research articles in *Computers & Chemical Engineering* (2006–2026) and section structure of 90 papers on reactor modelling and surrogate models; analysed with `scripts/build_section_phrases.py` and by reading. The papers themselves are not included.
- Abstracts and Introductions (up to the first methods section) of the same 20 *Computers & Chemical Engineering* articles: sentence-by-sentence move coding and automatic citation counts per sentence, paragraph and part of the Introduction (layout-aware PDF extraction, spot-checked); results in `resources/journals/computers-and-chemical-engineering/section_models.md` §2–3 and `citation_benchmarks.json`, and in `references/citation-practice.md`.
- Methodology parts of the same 20 articles (end of the Introduction to the first results section): structure, equation counts and contexts, citations, voice and tense per sentence, reproducibility items, and reading of assumptions, model adoption, parameters, numerics, data-driven and hybrid components; results in `section_models.md` §4, `citation_benchmarks.json` → `methods` and `references/methodology-writing.md`.
- Results and Discussion parts of the same 20 articles (first results section to the Conclusion), with page numbers: structure, subsection openings, sentence coding (numbers, explanation, comparison, hedging, limitation, implication, figure/table/equation references, citations, voice and tense), and reading of validation, benchmarking, variability, computational performance, physical interpretation, literature comparison and limitations; results in `section_models.md` §5 (with the DOIs of all papers), `citation_benchmarks.json` → `results_discussion` and `references/results-discussion-writing.md`.

**Tools**
- Microsoft MarkItDown, https://github.com/microsoft/markitdown (used to convert the guides to Markdown); PyMuPDF and pypdf as alternatives in `scripts/convert_to_markdown.py`.
- OpenAlex, https://openalex.org, and Crossref, https://www.crossref.org (reference checks in `scripts/check_citations.py`).

**Genre studies of research articles**
- Lin, L., & Evans, S. (2012). Structural patterns in empirical research articles: A cross-disciplinary study. *English for Specific Purposes*, 31, 150–160. https://doi.org/10.1016/j.esp.2011.10.002
- Maswana, S., Kanamaru, T., & Tajino, A. (2015). Move analysis of research articles across five engineering fields: What they share and what they do not. *Ampersand*, 2, 1–11. https://doi.org/10.1016/j.amper.2014.12.002
- Khaw, L. L. (2017). A problem-solution based framework for writing the introductions of research articles in electronic and communication engineering: Pedagogical implications. *2017 IEEE Global Engineering Education Conference (EDUCON)*. https://doi.org/10.1109/EDUCON.2017.7942834
- Jin, B. (2018). A multidimensional analysis of research article discussion sections in the field of chemical engineering. *IEEE Transactions on Professional Communication*, 61(3), 242–256. https://doi.org/10.1109/TPC.2018.2817002
