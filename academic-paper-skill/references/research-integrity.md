# Research integrity checks for AI-assisted papers

Use this file before a section leaves the drafting stage and again before submission. It catches failures that look like competent work: a number no run produced, a method described as it should have been rather than as it was, a reference that does not say what the sentence claims. Word-level and structure-level checks (`avoid-ai-signs.md`) do not find these; only comparison with the records does.

Levels: [Rule] = integrity requirement of this skill (always applies); [G] = general good practice. See `journal-profile.md` §0.

---

## 1. One results log as the single source of truth [Rule]

Keep every number that may appear in the paper in one file, `results_log.md` (template: `resources/templates/results_log.md`), next to the script, notebook or run that produced it. The draft is written from the log, never from memory or from an earlier draft.

- Each entry: the quantity, value, unit, conditions (case, operating point, data split), the run or file it came from, and the date.
- When a run is repeated or corrected, update the log first, then every place in the draft that uses the value.
- Values from the literature go in the log too, with the reference and the page, table or figure they come from.
- `python scripts/check_numbers.py draft.tex --log results_log.md` lists every number in the draft that is not in the log (allowing for rounding), and numbers that look suspicious (§2, F3).

If a number in the draft is not in the log, it is either added to the log with its source or removed from the draft. There is no third option.

---

## 2. Seven failure modes to rule out [Rule]

Lu et al. (2026, *Nature* 651, 914–919) described these failures in a fully automated research system; the list was adapted as a checklist by the academic-research-skills project (Wu, 2026). They apply equally when a human works with an AI assistant. The checks below are this skill's version for process modelling, simulation and machine learning.

| # | Failure | What it looks like in a modelling or ML paper | Check |
|---|---|---|---|
| F1 | A code error produces plausible numbers | A wrong unit, sign, index or flag gives a temperature profile or an R² that "looks fine" | Each main result has been reproduced from a clean run; mass and energy balances close; limiting cases (zero reaction rate, adiabatic, no flow) give the known answer; the solver finished without warnings |
| F2 | Wrong or unsupported citation | A reference that does not exist, has wrong details, or does not contain the claim | `check_citations.py` for existence and details; §3 for whether the source supports the claim |
| F3 | Reported result that no run produced | A percentage improvement, error or optimum that cannot be found in any saved output | Every number traces to `results_log.md` (§1). Suspicious signs: exactly round values (0.50, 2.0×), identical uncertainties in every condition, zero variance across repeats, a table whose totals do not add up |
| F4 | Good score for the wrong reason | A surrogate that is accurate because test points lie between training points, a model that fits the plant data because the inputs leak the output, a SHAP ranking that reflects correlated inputs | Test data truly separated (time-wise for dynamic data, by operating region for extrapolation claims); a baseline strong enough that beating it needs the proposed idea; an ablation that removes the claimed mechanism, not an incidental setting |
| F5 | An error reported as a discovery | An "unexpected" hot spot, oscillation or sensitivity that comes from a discretization, tolerance or implementation problem | Before an unexpected result is written as a finding: refine the grid and time step, tighten tolerances, check against an independent implementation or limiting case. Only what survives is a finding |
| F6 | Methods describe what should have been done | The Methods section lists the solver, settings, data split or hyperparameters a reasonable study would use, not those actually used | Compare every setting in Methods with the code or configuration file that produced the results; quote values from the files, not from memory |
| F7 | An early choice locks in the wrong question | The study is well executed but the objective, the model structure or the data range chosen at the start cannot answer what the paper claims | Re-read the objective against the final results: does the evidence answer this question, at this scope? If not, narrow the claim or the objective, do not stretch the results |

Record for each mode: "ruled out by …" or "suspected: …". A suspected mode is resolved before submission, or stated as a limitation.

Two further checks, from published C&CE practice (instruction study, v2.11):
- **Anomalous data before anomalous model** (the reverse of F5): before attributing a large error to the model, check the data point. …4321 sets apart a mixture whose measured viscosity rises on dilution with a lighter solvent, calls it physically paradoxical, and reports it separately from the model error. Say why the point is suspect; never drop it silently.
- **A passed test is not a proof of structure** (related to F4): …431X shows an incorrect rate term that passes both the χ² adequacy test and the t-tests. A high R², a passed adequacy test or a small validation error shows agreement with the data used, not physical correctness. Say which property a test establishes and which it does not.

---

## 3. Does the source support the sentence? [Rule]

A reference can be real and correctly described, yet say something different from the sentence that cites it. For every sentence that cites:

1. Open the cited paper (the Markdown conversions in the repository make this quick) and find the passage, table or figure that supports the statement. Note its location (page, section, table) in the claim–evidence map (`evidence-base.md`).
2. Classify: **supported** (the source states or shows it), **partly supported** (the source shows it for other conditions, or less strongly), **not supported**.
3. Partly supported: narrow the sentence to what the source shows ("for packed beds of spheres", "at laboratory scale"). Not supported: find a source that does support it, or delete the claim.
4. Check the direction and strength: a source that "suggests" cannot be cited for "has been demonstrated"; a source that reports a correlation cannot be cited for a cause.

Common failures: citing a review for a number that appears only in a paper it reviews (cite the original, or both); citing a paper's abstract claim that its own results qualify; citing a paper for a value from a different system.

---

## 4. Comparison claims [Rule]

- **Do not claim to outperform a cited method unless your own results compare against it** on the same case, data and metric. Otherwise describe it as related, complementary or differently scoped work.
- **Numbers from other papers are not a benchmark unless the conditions match.** Comparing your error with an error reported elsewhere requires the same quantity, metric definition, data range and test design; state any differences next to the comparison.
- **Concurrent work.** Papers published after you fixed your methods and results (or after a cutoff you state) are concurrent work: cite and discuss them, but do not present them as baselines you have beaten or as prior work you have improved on.
- **"First" and "novel" claims** require a search that would have found the earlier work; state the scope ("to our knowledge, no transient model of an industrial EO reactor has been …") and cite the closest studies.

---

## 5. Hedges that must survive shortening [Rule]

When the Abstract, Highlights, Conclusion or the title compress the paper, the qualifications that limit a claim must stay. Dropping them turns a bounded result into a general one.

Protected qualifiers:
- **Scope:** "for the tested operating range", "for this reactor", "under steady operation", "on the plant data of [ref]", "in simulation".
- **Strength:** "suggests", "is consistent with", "indicates" (do not upgrade to "shows", "proves", "demonstrates").
- **Status:** "preliminary", "for a single case", "without experimental validation".
- **Conditions of a number:** the case, the metric and the data set a value refers to.

Check: for every claim in the Abstract, Highlights and Conclusion, find the corresponding sentence in the body and compare scope and strength. The short version may be shorter, not stronger.

---

## 6. Revision and response to reviewers [Rule]

- State limitations openly; never hide one to make a revision easier.
- If a reviewer asks for an analysis you have not done, either do it and add it to the log, or explain in the response why it is outside the scope; never write the text as if it had been done.
- Every number added during revision enters `results_log.md` first (§1).
- **Earlier versions of the same work** (conference paper, preprint, thesis chapter): state what is reused, what was corrected and against which primary source, and whether the earlier conclusions still hold. If a correction changes an earlier conclusion, say so in the paper (…4424 does this for its own conference abstract). Text reuse rules are in `plagiarism-and-paraphrasing.md` §9.

---

## 7. Checklist before submission

- [ ] Every number in the manuscript is in `results_log.md` with its source; `check_numbers.py` reports no untraced values.
- [ ] F1–F7 each marked "ruled out by …" or resolved.
- [ ] Every citation checked for existence (`check_citations.py`) and for support (§3), with the location noted.
- [ ] No copied or closely paraphrased wording; `check_overlap.py` clean (`plagiarism-and-paraphrasing.md`).
- [ ] No "outperforms", "better than" or "state of the art" against a method not compared in this work.
- [ ] Abstract, Highlights and Conclusion keep the body's scope and strength.
- [ ] Methods settings match the code and configuration files.
- [ ] AI assistance disclosed as the journal requires.

## Sources

- Lu, C., Lu, C., Lange, R. T., Yamada, Y., Hu, S., Foerster, J., Ha, D., Clune, J. (2026). Towards end-to-end automation of AI research. *Nature* 651, 914–919 (failure modes described in its Limitations; arXiv version: arXiv:2606.15497).
- Wu, C.-I. (2026). *academic-research-skills* (CC BY-NC 4.0). https://github.com/imbad0202/academic-research-skills (ideas for the failure-mode checklist, claim–source checking and protected hedges; this file is written independently in our own words).
- Song, Y., Song, Y., Pfister, T., Yoon, J. (2026). PaperOrchestra: A multi-agent framework for automated AI research paper writing. arXiv:2604.05018. https://github.com/google-research/paper-orchestra (Apache 2.0; ideas for the single results log, comparison-claim and concurrent-work rules).
