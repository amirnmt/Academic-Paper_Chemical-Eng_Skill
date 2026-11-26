# Methodology and LaTeX mathematics

The Methods section (also called Materials and Methods, Experimental, Procedure, Simulation, Model, or Methodology) must let a competent reader **repeat** the work and **judge** whether the methods were appropriate and how far the results can be generalized. Many readers skip it; reviewers read it closely. If a reviewer doubts that the work can be repeated, the paper is rejected however good the results are.

Its message is: **this is exactly what we did, we did it carefully, and we had good reasons for doing it this way.**

Every result reported later needs a method here, and every method needs a result later. If a method is already published, summarize it and cite the original source; describe only what you changed.

Use with `methodology-writing.md` (pattern-by-pattern guide for modelling, simulation, optimization and data-driven methodologies: architecture, physical foundations, assumptions, equations in the narrative, numerics, algorithms, ML and hybrid models, parameter origin, verification and validation, reproducibility checklist, journal benchmarks), `paragraphs-and-sentences.md`, `vocabulary-by-section.md` §4 and `phrasebank.md` (Methods).

## 1. Write it first

Write the Methods first, ideally while the work is still in progress: details are fresh, equipment and co-authors are available, and routine steps that you no longer notice are easier to record. A common fault is missing detail, not because anything is hidden, but because repeated routine steps are forgotten.

## 2. How to start, what to include, how to end

**First sentence:** an overview of the approach or design, or the source of the materials or data.
- "The study combined pilot-plant measurements with a two-dimensional reactor model."
- "Temperature profiles were measured in a single-tube pilot reactor and compared with predictions of five model variants."
- "Plant data covering [n] days of operation were taken from [source]."

Do not start with a detailed step and no overview, and do not write in the imperative style of a recipe ("Heat the reactor to 250 °C").

**Middle:** the components in §3, ordered as in §4.

**Last part:** usually the data analysis, statistics and error metrics; or validation of the model; or a statement of the software and computing resources.

## 3. Components (a menu; select what applies)

1. **Overview and purpose:** restate the purpose of the work; outline the approach (experimental, numerical, data-driven, hybrid); give essential background.
2. **Source of materials, data and equipment:** supplier, grade/purity, model, city and country where the quality matters; generic or chemical names rather than trade names (use a trade name with manufacturer only when products differ in a way that matters).
3. **Specific and precise details:** quantities, concentrations, temperatures, pressures, flow rates, durations, sequence, frequency, locations, dimensions, conditions. Answer "how?" and "how much?" for every step.
4. **Justification of choices:** why this method, correlation, solver, parameter value or data split.
5. **Evidence that care was taken:** calibration, repeats, checks, controls, convergence and independence tests.
6. **Relation to other studies:** which parts follow an established method (cite it, name it) and which are modified (state the modification).
7. **Problems encountered:** missing samples, failed runs, excluded data, numerical difficulties, and how they were handled. Reporting them increases credibility.
8. **Data analysis:** processing steps, error metrics, uncertainty estimation, statistical tests and their assumptions, software with version.

Engineering articles typically contain three groups of moves here: identifying the data source and how it was collected (source, size, selection criteria, procedure); describing the experimental or computational procedure (apparatus, process, criteria for success); and describing the data analysis (terms, classification, instruments or algorithms, modifications). In chemical engineering, recounting the experimental or computational procedure step by step is close to obligatory, and some papers state the hypothesis being tested here.

## 4. Order and subheadings

- Order chronologically, but group related items: all sites/units, then materials, then procedures experiment by experiment, then analysis. An analysis method performed late in the project is still described with the other analysis methods.
- Begin with an overview of the design when the study has several parts.
- Use descriptive subheadings and reuse them in Results, in the same order. Example for a modelling paper:
  - 2.1 Reactor and catalyst
  - 2.2 Kinetic model
  - 2.3 Reactor model (balances, assumptions, boundary conditions)
  - 2.4 Physical properties and transport correlations
  - 2.5 Numerical solution
  - 2.6 Validation data and error metrics
  - 2.7 Data-driven model (if any)
- Tables and figures help: tables of operating conditions, parameters or materials; flowcharts of the procedure or workflow; diagrams of the apparatus or reactor; schematics of the model domain.

## 5. Content checklists by study type

**Experimental**
- Equipment: make, model, supplier, accuracy, calibration.
- Materials: purity, supplier, preparation, pretreatment.
- Conditions: ranges, set points, control accuracy, sequence and timing.
- Measurements: instruments, sampling locations and frequency, repetitions, uncertainty estimation.
- Safety or ethics statements if the journal requires them.

**Mechanistic model**
- Governing equations (mass, energy, momentum) with all assumptions stated next to them.
- Boundary and initial conditions.
- Kinetics: rate expressions, parameters with units and sources, range of validity.
- Thermodynamics and properties: equation of state, property sources, mixing rules.
- Transport correlations: heat and mass transfer, pressure drop, with validity ranges.
- Numerical method: discretization (finite volume/difference/element), grid, time integration, solver, tolerances, convergence and grid-independence checks, software and version, computing time.

**Data-driven or hybrid model**
- Data source, size, time span, preprocessing (interpolation, digitization, filtering, outlier handling); state clearly which data were measured and which were interpolated or digitized from figures.
- Inputs, outputs, feature selection.
- Data split and why (time-ordered splits for time series to avoid leakage from the future); scaling fitted on training data only.
- Architecture and hyperparameters, and how they were chosen (search space, validation scheme).
- Training: loss, optimizer, epochs, early stopping, random seeds, hardware.
- Baselines for comparison.
- Error metrics and on which data they are computed.

**Statistics and error analysis**
- How data are summarized (mean ± standard deviation; median [interquartile range]).
- Which test for which variable, significance level, how test assumptions were checked, software with version. Standard methods need only a name and citation; describe only unusual ones (avoid explaining textbook statistics).
- Error metrics: RMSE, MAE, MAPE, R², maximum relative error; define each.
- Uncertainty propagation or sensitivity analysis (local, Sobol), with sample sizes.

## 6. Tense and voice: making your own contribution visible

- In computational papers the model and the framework are usually described in the **present** ("The model consists of …", "The framework proceeds in three stages"), and the past is kept for what was actually carried out (data collection, runs, fitting); in 20 *Computers & Chemical Engineering* Methodology sections, present-tense markers appeared in about 55 % of sentences and past-tense markers in about 4 % [J-obs]. Either convention is correct; keep it consistent within a subsection.
- **Past simple** for what you did: "The bed was discretized into 200 axial cells."
- **Present simple** for standard procedures, how standard equipment works, equations, and what tables and figures show: "In this reactor type, heat is removed by boiling water"; "Eq. (3) describes …"; "Table 2 lists …".
- The switch between them tells the reader what is standard and what you did. If a description of a standard procedure in the present suddenly changes to the past ("The pulses were then split …"), readers understand that this step was yours.
- **Past perfect** for events before the main procedure: "after the catalyst had been reduced, …".
- The agentless passive is standard ("The samples were collected …"). Many journals accept "we" for decisions ("We chose …") and it is clearer when the actor matters.
- **Separate your work from others'.** An agentless passive can describe your procedure or a cited one, so mark the difference:
  - yours: "In this study, …", "In our experiments, …", "here", "in the present model", or a dummy subject ("This experiment …");
  - others': "In [12], …", "Smith et al. [12] used …", "in their model".
- Avoid dangling modifiers: "Using a thermocouple, the bed temperature was measured" says that the temperature used the thermocouple; write "The bed temperature was measured with a thermocouple". Avoid stating an action without a plausible agent: "To determine its activity, the catalyst was …" (the catalyst did not determine anything).

## 7. Language for each component

**Overview and source**
- "Syngas of composition [x] was supplied by [company, city, country] and used as received."
- "The kinetic parameters were taken from [n]."
- "Operating data for [n] days were digitized from Fig. 4 of [n] using [software]."

**Specific details**
- Use precise verbs (calibrated, discretized, normalized, interpolated, fitted, validated …) instead of "done" or "used".
- Give quantities with units and conditions: "The catalyst (2.5 kg, particle diameter 6 mm) was diluted 1:1 with inert alumina spheres."
- State frequency: "Temperatures were recorded every 10 s at 12 axial positions."
- State sequence and timing precisely: "After reduction at 513 K for 12 h, the feed was switched to syngas."

**Equipment and geometry**
- Use exact spatial language: upstream/downstream of, at the centreline, near the wall, at axial positions of …, mounted on, aligned with, embedded in, equally spaced.
- Precise proximity: "directly above", "flush with", "in contact with".

**Justification**
- "This correlation was chosen because it was derived for tube-to-particle ratios below 10 [14]."
- "A time-ordered split was used to avoid leakage of future information into the training set."
- "For simplicity, the gas properties were evaluated at the mean bed temperature; Section 4.3 examines the effect of this assumption."
- "By solving the cells sequentially, the computing time was reduced from [x] to [y] min."

**Showing care**
- "Each experiment was repeated three times."
- "Grid independence was confirmed by halving the cell size, which changed the hot-spot temperature by less than 0.1 K."
- "The thermocouples were calibrated against a reference thermometer to within ±0.5 K."

**Relating to other studies**
- Same: "The catalyst was reduced as described in [8]." (name the step even when citing)
- Similar: "The model is based on that of [10], with the following modifications: …"
- Different: "Unlike [10], the energy balance includes axial conduction."

**Problems**
- "Data for days 0–30 were excluded because the plant was operating in start-up mode."
- "One thermocouple failed after day 40; its readings were replaced by interpolation between neighbouring positions."
- "Future work will (your plan) / should (suggestion to others) …"

## 8. Common mistakes

- Results reported in Methods (or methods first described in Results).
- Missing quantities, temperatures, durations, or the starting material (a colleague test catches these: ask a colleague whether they could repeat the work).
- "As described previously [8]" without naming the method or giving the reader enough to follow.
- Statistics described at textbook length; or the test named without its assumptions.
- Trade names instead of generic names, without manufacturer.
- Units not SI; "weight" when mass is meant.
- Future tense copied from a proposal ("Samples will be collected").
- Data that were interpolated, digitized or reconstructed presented as if measured.

## 9. Mathematics in LaTeX

### 9.1 Preamble

```latex
\usepackage{amsmath,amssymb}   % equations, align, symbols
\usepackage{bm}                % bold math symbols for vectors and matrices
\usepackage{siunitx}           % numbers and units
\usepackage[version=4]{mhchem} % chemical formulas and reactions
\usepackage{booktabs}          % tables
\usepackage{nomencl}           % nomenclature list (if the journal does not provide one)
\makenomenclature
\sisetup{per-mode=symbol, separate-uncertainty=true}
```

Use the journal's template (for Elsevier, `elsarticle`) and check which packages it allows.

### 9.2 Writing equations

- Introduce each equation in the sentence before it and punctuate it as part of the sentence (comma or full stop at the end of the equation).
- Define every symbol directly after its first equation ("where …"), with units. Add a nomenclature table when there are many symbols.
- Number equations with `equation`/`align` and refer with `\eqref{}` ("Eq. (3)" or as the journal requires). Never hard-code numbers.
- Number only equations referred to later, unless the journal numbers all.
- Italic for variables; upright for units, labels, descriptive subscripts and standard functions: `T_\mathrm{w}` (wall), `C_i` (index i is italic), `\exp`, `\ln`, `\mathrm{d}` for the differential.
- Bold for vectors and matrices: `\bm{u}`, `\mathbf{A}`.
- Same symbol, same meaning throughout the paper. Do not reuse a symbol for two quantities.
- State assumptions next to the equation they simplify.
- Use `align` for systems and multi-line equations, aligned at `=`; `cases` for piecewise definitions.

### 9.3 Example: a reactor balance

```latex
Assuming plug flow and negligible axial dispersion, the steady-state mass
balance for species $i$ reads
\begin{equation}
  \frac{\mathrm{d}(u_\mathrm{s} C_i)}{\mathrm{d}z}
  = \rho_\mathrm{b} \sum_{j=1}^{N_\mathrm{r}} \nu_{ij}\, \eta_j\, r_j ,
  \label{eq:mass}
\end{equation}
and the energy balance
\begin{equation}
  u_\mathrm{s} \rho_\mathrm{g} c_{p,\mathrm{g}} \frac{\mathrm{d}T}{\mathrm{d}z}
  = \rho_\mathrm{b} \sum_{j=1}^{N_\mathrm{r}} (-\Delta_\mathrm{r} H_j)\, \eta_j\, r_j
  - \frac{4 U}{d_\mathrm{t}} \left( T - T_\mathrm{c} \right) ,
  \label{eq:energy}
\end{equation}
where $u_\mathrm{s}$ is the superficial velocity (\si{\metre\per\second}),
$C_i$ the molar concentration (\si{\mol\per\cubic\metre}),
$\rho_\mathrm{b}$ the bulk density of the catalyst bed (\si{\kilogram\per\cubic\metre}),
$\nu_{ij}$ the stoichiometric coefficient, $\eta_j$ the effectiveness factor,
$r_j$ the rate of reaction $j$ (\si{\mol\per\kilogram\per\second}),
$U$ the overall heat-transfer coefficient (\si{\watt\per\square\metre\per\kelvin}),
$d_\mathrm{t}$ the tube diameter (\si{\metre}) and $T_\mathrm{c}$ the coolant
temperature (\si{\kelvin}).
```

### 9.4 Units and numbers with siunitx

- `\SI{523}{\kelvin}`, `\SI{50}{\bar}`, `\SI{2.5e-3}{\metre}`, `\SI{12.3 +- 0.4}{\percent}`.
- Ranges and lists: `\SIrange{473}{553}{\kelvin}`, `\SIlist{1;2;5}{\bar}`.
- Units alone: `\si{\mol\per\kilogram\per\second}`.
- SI units only; a space between number and unit (siunitx does this); no plural units.
- In newer siunitx versions, `\qty{}{}`, `\qtyrange{}{}{}`, `\unit{}` replace `\SI`, `\SIrange`, `\si`.

### 9.5 Chemistry with mhchem

- Formulas: `\ce{CO2}`, `\ce{CH3OH}`, `\ce{Cu/ZnO/Al2O3}`.
- Reactions:

```latex
\begin{align}
  \ce{CO + 2 H2} &\ce{<=> CH3OH} \label{r:co}\\
  \ce{CO2 + 3 H2} &\ce{<=> CH3OH + H2O} \label{r:co2}\\
  \ce{CO2 + H2} &\ce{<=> CO + H2O} \label{r:rwgs}
\end{align}
```

### 9.6 Nomenclature

Group symbols: Latin letters, Greek letters, subscripts, superscripts, abbreviations. Give units for each. Example with `nomencl`:

```latex
\nomenclature{$C_i$}{molar concentration of species $i$, \si{\mol\per\cubic\metre}}
\nomenclature{$\eta_j$}{effectiveness factor of reaction $j$, --}
\printnomenclature
```

Many journals expect a plain table instead; follow the template.

### 9.7 Parameter table (booktabs + siunitx)

```latex
\begin{table}[t]
  \centering
  \caption{Reactor and operating parameters.}
  \label{tab:params}
  \begin{tabular}{l S[table-format=3.2] l}
    \toprule
    Parameter & {Value} & {Unit} \\
    \midrule
    Tube inner diameter, $d_\mathrm{t}$ & 38.10 & \si{\milli\metre} \\
    Bed length, $L$                     & 7.02  & \si{\metre} \\
    Coolant temperature, $T_\mathrm{c}$ & 523.15 & \si{\kelvin} \\
    \bottomrule
  \end{tabular}
\end{table}
```

(Values are placeholders.) Caption above the table; three horizontal rules; no vertical rules; units in their own column or in the header.

### 9.8 Common LaTeX mistakes

- Italic units or descriptive subscripts (`T_{wall}` instead of `T_\mathrm{w}`).
- `*` for multiplication; use juxtaposition, `\cdot` or `\times`.
- Manual spacing and hard-coded equation numbers.
- Long text inside math; put explanations in the sentence.
- `\frac` in running text that makes lines tall; use a slash or `\tfrac` there.
- Inconsistent symbols between equations, tables and figures.

## 10. Checklist

- [ ] Starts with an overview of the approach or the source of materials/data.
- [ ] A competent reader could repeat it: all conditions, quantities, parameters (with units and sources), software versions given.
- [ ] Assumptions stated next to the equations; boundary and initial conditions complete.
- [ ] Every choice justified; published methods named and cited; modifications described.
- [ ] Care shown: calibration, repeats, grid/time-step independence, tolerances.
- [ ] Problems, exclusions and missing data reported with how they were handled.
- [ ] Validation data and error metrics defined; for data-driven models: split, leakage prevention, scaling, hyperparameters, seeds, baselines.
- [ ] Every result in the paper has a method here, in the same order and under the same subheadings.
- [ ] Your own steps clearly distinguished from standard or cited procedures (tense and marker phrases).
- [ ] All symbols defined with units; nomenclature consistent; SI units.
- [ ] Past tense for what was done, present for equations and figure/table descriptions; no dangling modifiers.
