# Academic Paper Skill (STEM)

A [Claude skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) for writing STEM and engineering journal articles, from a repository of reference papers and your own results.

It guides Claude through the whole article:

- **Evidence base** — turn a folder of papers into notes, a `refs.bib`, and a comparison matrix; cite only verified sources.
- **Introduction** — funnel from the broad field to the research gap, including a problem → solution → evaluation model for engineering papers.
- **Literature review** — thematic, synthesized and critical, not a list of summaries.
- **Methodology** — reproducible detail, LaTeX equations, units with `siunitx`, nomenclature.
- **Results** — report trends with numbers, compare with validation data, no interpretation.
- **Figures and tables** — clear axes, consistent styling, `booktabs` tables.
- **Discussion and conclusion** — interpret, compare with literature, state limitations, calibrated hedging.
- **Abstract, title, keywords, academic style, phrase bank, references.**

The rules are distilled from established writing guides and genre studies of engineering research articles (listed at the end of `SKILL.md`). Those sources are not included here.

## Install

**Claude apps (claude.ai / desktop):** download `academic-paper-skill/SKILL.md`, zip the `academic-paper-skill` folder, and upload it under *Settings → Capabilities → Skills*.

**Claude Code:**

```bash
git clone https://github.com/amirnmt/academic-paper-skill.git
mkdir -p ~/.claude/skills
cp -R academic-paper-skill/academic-paper-skill ~/.claude/skills/
```

Then ask Claude, for example: *"Use the academic-paper-skill to draft the introduction of my paper from the papers in this folder."*

## Author

Amir Nematollahi

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You may share and adapt this skill with attribution.
