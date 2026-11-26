# Results log

The single source of truth for every number in the manuscript (`references/research-integrity.md` §1). Write the draft from this file. Update it first when a run changes.

`python scripts/check_numbers.py draft.tex --log results_log.md` compares the draft against the tables below. Put each value in its own table cell; units and conditions in their own columns.

Project: …
Last updated: YYYY-MM-DD

## 1. Own results

| ID | Quantity | Value | Unit | Conditions (case, operating point, data split) | Source (script / run / file) | Date |
|---|---|---|---|---|---|---|
| R1 | Outlet temperature, model vs plant, MAE | … | K | steady state, case A, plant data of [ref] | `runs/steady_caseA/summary.csv` | |
| R2 | Surrogate test R² (outlet EO mole fraction) | … | – | time-wise split, last 20 % held out | `ml/eval_lstm.ipynb`, cell 14 | |
| R3 | Optimal inlet temperature | … | K | objective …, constraints … | `opt/run_03.log` | |

## 2. Values taken from the literature

| ID | Quantity | Value | Unit | Conditions | Reference and location (page, table, figure) |
|---|---|---|---|---|---|
| L1 | Plant outlet temperature | … | K | industrial reactor | Rahimpour et al. (2011), Table … |
| L2 | Reported error of the comparison model | … | % | … | [ref], Table … |

## 3. Model parameters and settings (match the Methods section)

| ID | Symbol | Description | Value | Unit | Origin (literature / measured / calibrated / assumed) | Source |
|---|---|---|---|---|---|---|
| P1 | | | | | | |

## 4. Failure-mode record (research-integrity.md §2)

| Mode | Status | How ruled out / what was done |
|---|---|---|
| F1 code error | | |
| F2 citations | | |
| F3 untraced results | | |
| F4 right score, wrong reason | | |
| F5 error reported as finding | | |
| F6 Methods ≠ what was run | | |
| F7 question locked in early | | |
