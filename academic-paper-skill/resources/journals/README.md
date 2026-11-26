# journals/: one profile folder per target journal

A journal profile records the rules of one journal (from its Guide for Authors) and, if sample papers are available, how its papers are usually structured. The skill reads the profile of the journal you are writing for, and the profile overrides the skill's default profile (`references/journal-profile.md` §4).

```
journals/
└── <journal-slug>/
    ├── journal_requirements.md   rules from the Guide for Authors (template in references/journal-profile.md §3)
    ├── section_models.md         how the journal's papers are built (optional, from sample papers)
    ├── section_phrases.md        openers and phrases per section (optional, from sample papers)
    ├── guide.md                  converted Guide for Authors        (local only, git-ignored)
    ├── requirements_draft.md     guide lines sorted by field         (local only, git-ignored)
    └── papers/                   converted sample papers             (local only, git-ignored)
```

Create a profile:

```bash
python scripts/journal_profile.py init "Journal Name" --guide guide.pdf --papers sample_papers/
python scripts/journal_profile.py check "Journal Name"
python scripts/journal_profile.py list
```

Then ask Claude to write `journal_requirements.md` (and `section_models.md` if you gave sample papers) from the draft. To write for another journal later, create another profile; the old one stays.

`computers-and-chemical-engineering/` is an example profile (guide saved November 2026; check the current guide before submitting).
