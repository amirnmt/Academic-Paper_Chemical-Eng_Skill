# Methodology and LaTeX mathematics

The Methods section must let an average expert with the same resources reproduce the work. Every result reported later needs a method here, and every method needs a result later. If a method is already published, summarize it and cite the source; describe only what you changed.

## 1. Structure: a menu, not a fixed sequence

Choose the components that apply to your study and journal.

1. **Overview** — restate the purpose of the work; outline the overall approach (experimental, numerical, data-driven, hybrid); give the source of materials and equipment (supplier, model, city, country); give essential background.
2. **Specific, precise details** — quantities, concentrations, temperatures, pressures, flow rates, durations, sequence, conditions, locations, dimensions. Justify non-obvious choices. Show that appropriate care was taken.
3. **Relation to other studies** — what follows an established method (cite it) and what was modified.
4. **Problems encountered** — difficulties, exclusions, and how they were handled. Omit if there were none.

Engineering articles commonly cover (move analysis of five engineering fields):
- Source of data and how it was collected: source, size, selection criteria, collection procedure, background on what is analysed.
- Experimental or computational procedure: main apparatus or software, the process step by step, criteria for success. In chemical engineering, recounting the experimental process is close to obligatory, and some papers state the hypothesis being tested here.
- Data analysis: terminology, how data were classified, analytical instruments or algorithms, modifications to standard procedures.

## 2. Subsections

Use descriptive subheadings and reuse them in Results, in the same order. Example for a modelling paper:
- 2.1 Reactor and catalyst
- 2.2 Kinetic model
- 2.3 Reactor model (balances, assumptions, boundary conditions)
- 2.4 Physical properties and transport correlations
- 2.5 Numerical solution
- 2.6 Validation data and error metrics
- 2.7 Data-driven model (if any)

## 3. Content checklists by study type

**Experimental**
- Equipment: make, model, supplier, accuracy, calibration.
- Materials: purity, supplier, preparation, pretreatment.
- Conditions: ranges, set points, control accuracy, sequence and timing.
- Measurements: instruments, sampling, repetitions, how uncertainty was estimated.
- Safety or ethics statements if the journal requires them.

**Mechanistic model**
- Governing equations (mass, energy, momentum) with all assumptions stated next to them.
- Boundary and initial conditions.
- Kinetics: rate expressions, parameters with units and sources, range of validity.
- Thermodynamics and properties: equation of state, property sources, mixing rules.
- Transport correlations: heat and mass transfer, pressure drop, with their validity ranges.
- Numerical method: discretization (finite volume/difference/element), grid or mesh, time integration, solver, tolerances, convergence and grid-independence checks, software and version, computing time.

**Data-driven or hybrid model**
- Data source, size, time span, preprocessing (interpolation, filtering, outlier handling).
- Inputs, outputs, feature selection.
- Data split and why (time-ordered splits for time series to avoid leakage from the future), scaling fitted on training data only.
- Architecture and hyperparameters, how they were chosen (search space, validation scheme).
- Training: loss, optimizer, epochs, early stopping, random seeds, hardware.
- Baselines for comparison.
- Error metrics and on which data they are computed.

**Statistics and error analysis**
- How data are summarized (mean ± standard deviation, median [interquartile range]).
- Tests used, significance level, software.
- Error metrics: RMSE, MAE, MAPE, R², maximum relative error; define each.
- Uncertainty propagation or sensitivity analysis (local, Sobol), with sample sizes.

## 4. Language that shows care and precision

Use specific verbs instead of "was done" or "was used": calibrated, prepared, pretreated, discretized, integrated, fitted, optimized, validated, averaged, filtered, interpolated, normalized, scaled, sampled, repeated, monitored, controlled, measured, recorded.

Words that show care: carefully, accurately, precisely, consistently, independently, systematically, in triplicate, under identical conditions, to avoid, to ensure, to minimize, to prevent, in order to eliminate.

State precisely:
- sequence and timing ("after reduction at [T] for [t] h, the feed was switched to …");
- frequency ("each condition was repeated three times");
- conditions ("at [p] bar and a gas hourly space velocity of [value] h⁻¹");
- justification ("This correlation was chosen because it was derived for tube-to-particle ratios below 10 [14].").

## 5. Tense and voice

- Past simple for what was done: "The bed was discretized into 200 axial cells."
- Past perfect for events before the main procedure: "after the catalyst had been reduced, …".
- Present simple for equations, the model as a description, and what tables and figures show: "Eq. (3) describes …"; "Table 2 lists the parameters."
- Passive voice suits procedures; first person ("we") is acceptable in most engineering journals for decisions ("We chose …"). Follow the target journal.

## 6. Mathematics in LaTeX

### 6.1 Preamble

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

### 6.2 Writing equations

- Introduce each equation in the sentence before it and punctuate it as part of the sentence (comma or full stop at the end of the equation).
- Define every symbol directly after its first equation ("where …"), with units. Add a nomenclature table when there are many symbols.
- Number equations with `equation`/`align` and refer with `\eqref{}` ("Eq. (3)" or as the journal requires). Never hard-code numbers.
- Number only equations referred to later, unless the journal numbers all.
- Italic for variables; upright for units, labels, descriptive subscripts and standard functions: `T_\mathrm{w}` (wall), `C_i` (index i is italic), `\exp`, `\ln`, `\mathrm{d}` for the differential.
- Bold for vectors and matrices: `\bm{u}`, `\mathbf{A}`.
- Same symbol, same meaning throughout the paper. Do not reuse a symbol for two quantities.
- State assumptions next to the equation they simplify.
- Use `align` for systems and multi-line equations, aligned at `=`; `cases` for piecewise definitions.

### 6.3 Example: a reactor balance

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

### 6.4 Units and numbers with siunitx

- `\SI{523}{\kelvin}`, `\SI{50}{\bar}`, `\SI{2.5e-3}{\metre}`, `\SI{12.3 +- 0.4}{\percent}`.
- Ranges and lists: `\SIrange{473}{553}{\kelvin}`, `\SIlist{1;2;5}{\bar}`.
- Units alone: `\si{\mol\per\kilogram\per\second}`.
- SI units only; a space between number and unit (siunitx does this); no plural units.
- In newer siunitx versions, `\qty{}{}`, `\qtyrange{}{}{}`, `\unit{}` replace `\SI`, `\SIrange`, `\si`.

### 6.5 Chemistry with mhchem

- Formulas: `\ce{CO2}`, `\ce{CH3OH}`, `\ce{Cu/ZnO/Al2O3}`.
- Reactions:

```latex
\begin{align}
  \ce{CO + 2 H2} &\ce{<=> CH3OH} \label{r:co}\\
  \ce{CO2 + 3 H2} &\ce{<=> CH3OH + H2O} \label{r:co2}\\
  \ce{CO2 + H2} &\ce{<=> CO + H2O} \label{r:rwgs}
\end{align}
```

### 6.6 Nomenclature

Group symbols: Latin letters, Greek letters, subscripts, superscripts, abbreviations. Give units for each. Example with `nomencl`:

```latex
\nomenclature{$C_i$}{molar concentration of species $i$, \si{\mol\per\cubic\metre}}
\nomenclature{$\eta_j$}{effectiveness factor of reaction $j$, --}
\printnomenclature
```

Many journals expect a plain table instead; follow the template.

### 6.7 Parameter table (booktabs + siunitx)

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

### 6.8 Common LaTeX mistakes

- Italic units or descriptive subscripts (`T_{wall}` instead of `T_\mathrm{w}`).
- `*` for multiplication; use juxtaposition, `\cdot` or `\times`.
- Manual spacing and hard-coded equation numbers.
- Long text inside math; put explanations in the sentence.
- `\frac` in running text that makes lines tall; use a slash or `\tfrac` there.
- Inconsistent symbols between equations, tables and figures.

## 7. Checklist

- [ ] Every result in the paper has a method here, in the same order and with the same subheadings.
- [ ] A competent reader could reproduce it: all conditions, parameters (with units and sources), and software versions given.
- [ ] Assumptions stated next to the equations; boundary and initial conditions complete.
- [ ] Choices justified; published methods cited, modifications described.
- [ ] Numerical accuracy shown (grid/time-step independence, tolerances); validation data and error metrics defined.
- [ ] For data-driven models: split, leakage prevention, scaling, hyperparameters, seeds, baselines.
- [ ] All symbols defined with units; nomenclature consistent; SI units.
- [ ] Past tense for procedures, present for equations and figure/table descriptions.
