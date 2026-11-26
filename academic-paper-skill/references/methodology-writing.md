# Writing the Methodology of a modelling, simulation, optimization or data-driven paper

A pattern-by-pattern guide to how the Methodology is organized, how models, assumptions, equations, numerics, algorithms, data-driven components, parameters and validation are described, and how each choice is justified and cited. It complements `methods-latex.md` (what a Methods section must contain, study-type checklists, LaTeX mathematics) and is written for computational chemical and process engineering papers; most patterns apply to any quantitative field.

Levels (see `journal-profile.md` §0): **[G]** general academic writing · **[M]** general scientific methodology · **[D]** chemical and process engineering · **[PB]** physics-based modelling · **[NUM]** numerical and computational modelling · **[ML]** machine learning and hybrid modelling · **[J-obs]** observed in the Methodology of 20 *Computers & Chemical Engineering* research articles (convention, not rule; numbers in §17 and in the journal profile) · **[J-req]** stated in a journal's Guide for Authors · **[Rule]** standing rule of this skill.

Each pattern gives: **Purpose** · **Form** (grammar and structure) · **Templates** · **Example** (illustrative, with the skill's running example of a fixed-bed methanol reactor; values are placeholders) · **Cite** (what needs a source) · **Mistakes** · **Applies to**.

The guiding rule [Rule]: the Methodology says what was done, how, why each decision was made, which foundations support it, and enough for another researcher to reproduce it. No parameter, equation, correlation, dataset or assumption appears without a traceable origin or a stated justification; nothing is invented.

---

## 1. Architecture of the Methodology

### 1.1 Four structures, chosen by the type of research [J-obs, M]

| Structure | Order | Fits | Seen in |
|---|---|---|---|
| **System → model → solution** | system or process description (plant, reactor, data) → physical model (balances, kinetics, properties) → numerical solution → validation and metrics | First-principles and process-simulation papers | industrial reactor, EO plant simulation, process-route comparison, eco-industrial park, refrigeration cost papers |
| **Overview → modules in order** | workflow figure or list of stages → one subsection per stage, in execution order → evaluation metrics | Frameworks, ML pipelines, hybrid workflows | kinetic-model discovery, furnace attention model, fault diagnosis, data-augmented MPC, cell sorting, robustness protocol |
| **Problem statement → formulation → solution strategy** | sets, parameters and variables → objective → constraints by category → reformulation or decomposition → solution algorithm | Optimization, scheduling, supply-chain papers | superstructure MILP, scheduling under disruptions, energy-system scheduling, palm-oil and SAF supply chains |
| **Problem statement → preliminaries → results with proofs** | system and assumptions → definitions and lemmas → theorems and proofs → remarks | Control-theory papers | fault-tolerant control paper |

Most papers [J-obs] open the Methodology with a description of the system or problem (about 12 of 20) or with an overview of the framework, often with a workflow figure (about 9 of 20; some do both). Hybrid papers combine the first two: a physical model that generates or constrains data, followed by the data-driven modules.

Choose by asking what the reader must hold in mind first: the physical system (start with it), the workflow (start with the overview), or the decision problem (start with the problem statement).

### 1.2 The opening paragraph [G, J-obs]

- **Purpose:** tell the reader what the Methodology contains and in what order, so that each subsection has a place.
- **Form:** one or two sentences; present tense; "This section …", "The framework consists of …", "The proposed method is applied in two steps"; optionally a pointer to the workflow figure.
- **Templates:**
  - "This section describes [the system], [the model] and [the solution procedure]; Section 2.4 defines the metrics used to evaluate it."
  - "The [framework] consists of [n] stages, shown in Fig. 1: (i) …, (ii) … and (iii) …. Each stage is described in one of the following subsections."
  - "The approach combines [A], which [role], with [B], which [role]."
- **Example:** "The methodology has three parts (Fig. 1): a two-dimensional reactor model (Section 2.2), its numerical solution (Section 2.3) and the comparison with pilot-plant temperature profiles (Section 2.4)."
- **Cite:** nothing, unless the framework as a whole is taken from earlier work.
- **Mistakes:** starting with an equation; starting with a detail of step 3; repeating the Introduction's motivation at length.
- **Applies to:** all.

### 1.3 Moving between subsections [G, J-obs]

Subsections are linked in four ways: a forward map in the opening ("as described in the following subsections"); a backward link in the first sentence of a subsection ("Following model calibration, each retained model …", "Based on the predicted curves of Section 2.1, …"); the step number of the workflow figure ("Step 3 in Fig. 1"); or a sentence that states the input the subsection receives and the output it passes on ("The resulting profiles are the input to the optimization in Section 2.5").

- **Templates:** "Having defined …, we now …"; "The [output] obtained in Section 2.2 is used here to …"; "This stage receives … and returns …"; "The second step of the framework is to …".
- **Mistakes:** subsections that read as independent notes; a variable defined in one subsection and renamed in the next.

### 1.4 What goes into the main text, the appendix and the supplementary material [G, J-obs]

| Main text | Appendix | Supplementary material |
|---|---|---|
| Governing equations, the closures that matter for the results, assumptions, the solution strategy, data sources and splits, architectures, metrics | Long derivations, proofs, full sets of correlations, parameter and nomenclature tables, algorithm listings, implementation and verification details | Process-block details, full datasets or networks, extra equations of a component, extended tables, code |

In the analysed papers, 12 of 20 Methodology parts refer the reader to an appendix or supplementary file, typically for full parameter tables, per-component equations, algorithm listings, and implementation or verification details. Rule of thumb: a reader must be able to follow the argument and judge the method from the main text alone; reproduction may require the appendix.

- **Templates:** "The values of all parameters, with units and sources, are listed in Appendix A."; "The full equations of each block are given in Section S2 of the Supplementary Material."; "Implementation details and the verification of the code are reported in Appendix C."
- **[J-req, e.g. C&CE]:** appendices lettered A, B …; equations in appendices numbered (A.1), (A.2); supplementary files cited in the text, each with a caption.

---

## 2. Describing the system, process or problem

- **Purpose:** define what is modelled: boundaries, units, streams, operating range, and (for industrial cases) where the data come from.
- **Form:** present tense for the system ("The reactor consists of …"); past tense for what was done to it or collected from it ("Data were recorded over …"). A schematic is introduced in the first or second sentence.
- **Templates:**
  - "The system considered is a [type] with [main units], shown schematically in Fig. 2."
  - "[Feed] enters …, passes through … and leaves …; [stream] is recycled to …"
  - "The plant operates at [range of T, P, flows]; Table 1 lists the nominal conditions and their sources."
  - "The problem can be stated as follows. Given (i) …, (ii) …, determine … so as to minimize …"
- **Example:** "The pilot reactor is a single tube of 2.5 m length and 0.04 m internal diameter, filled with Cu/ZnO/Al2O3 pellets and cooled by boiling water on the shell side (Fig. 2)."
- **Cite:** the source of the process description (plant documentation, an earlier paper that described the plant, encyclopedias for standard process routes) and of every operating value not measured by the authors.
- **Mistakes:** values without origin; a schematic that uses different names from the equations; industrial details that are confidential stated without saying they were anonymized or normalized.
- **Applies to:** [D], all application papers.

---

## 3. Physical foundations before the equations [PB, D]

### 3.1 Introduce the phenomena in words first

The analysed physics-based papers describe the physical picture in prose before writing a balance: what phases exist, where reaction occurs, which transport steps connect them, what is fast and what is slow. The equations then formalize that picture, and the lead-in sentence of each balance names the conditions it rests on ("Considering the assumptions above and the reaction mechanism, the mass balance of species *i* in the emulsion phase is …").

Order for a reactor model [PB, D]:
1. Phases and domains (gas, solid; bulk and pellet; bubble and emulsion) and the scales resolved (reactor, particle, pore).
2. Reactions and kinetic scheme (with the source of the rate expressions).
3. Transport between phases and domains (interphase mass and heat transfer, intraparticle diffusion, wall heat transfer).
4. Conservation equations: mass (species), energy (each phase), momentum (pressure drop), each with its assumptions.
5. Closures: rate laws, equilibrium, thermodynamic and transport properties, correlations.
6. Initial and boundary conditions; for transient models, the initial state and the disturbances.
7. Catalyst behaviour: activity, deactivation, its time scale relative to the simulated horizon.
8. Coupling between scales (what each scale receives from and returns to the other).

- **Templates:**
  - "The bed is described as [pseudo-homogeneous / heterogeneous], with [n] phases: …"
  - "Reaction takes place only in …; mass and heat are exchanged with … through …"
  - "At the particle scale, species diffuse through the pores while reacting; the resulting effectiveness factor links the pellet model to the reactor model."
  - "Catalyst deactivation is slow compared with the simulated horizon of [time] and is therefore represented by a constant activity factor (Section 2.6)."
- **Cite:** the phenomena descriptions when they are not textbook knowledge; every kinetic scheme, correlation and property method.
- **Mistakes:** balances written before the reader knows the phases; a scale introduced in the equations but never in the text.

### 3.2 Conservation equations [PB]

| Balance | State in words | Typical lead-in |
|---|---|---|
| Species mass | accumulation, convection, dispersion, reaction (and interphase transfer) | "The mass balance of species *i* in the gas phase reads" |
| Energy | accumulation, convection, conduction, heat of reaction, heat exchange with the wall or the other phase | "The energy balance of the solid phase accounts for …" |
| Momentum | pressure drop correlation, usually with its validity range | "The pressure drop is described by the [named] equation (ref)" |
| Population or moments | distribution of size or chain length, and the closure used | "To reduce the number of equations, the method of moments is applied" |

Explain each term the first time, or state which terms were dropped and why ("Axial dispersion is neglected because the Péclet number exceeds …").

### 3.3 Adopted, modified and new elements [PB, M, Rule]

State the origin of each part of the model at the place where it appears:
- **adopted:** "The kinetic model of [ref] is used without modification (Table 2)."
- **adapted:** "The formulation is adapted from [refs]; two terms are added to account for …"
- **extended:** "The model of [ref] is extended to the transient case by adding accumulation terms to Eqs. (3) and (5)."
- **combined:** "The reactor model follows [ref], and the pellet model follows [ref]; they are coupled through …"
- **new:** "The coupling scheme of Section 2.5 is introduced in this work."
- **chosen among alternatives:** "The constant-coefficient formulation of [ref] is used instead of the more detailed variant proposed in the same work, because it predicted the measured temperatures better (Section 4.1)."

Mistakes: an adopted model presented as if new; a modification hidden in an equation without comment; "based on [ref]" when large parts were changed.

---

## 4. Assumptions and simplifications [PB, M]

### 4.1 Where to state them

Two placements, both common [J-obs]: a **list at the start of the model** (bullets or (i)–(iv), often with the source the assumption set comes from), and **assumptions inside each subsection, next to the equation they simplify**. Use the list for model-wide assumptions and the inline form for local ones. In the analysed papers, 17 of 20 Methodology parts state assumptions; 14 % of these sentences carry a citation, mostly when the assumption set is inherited from an earlier model.

### 4.2 Form of an assumption sentence

- **Statement:** passive or "is considered/assumed/taken as": "The gas phase is assumed to be ideal." / "Heat losses to the surroundings are neglected."
- **Justification**, one of:
  - order-of-magnitude or dimensionless argument: "because the Biot number is below 0.1";
  - evidence from data or documentation: "since all feed streams are filtered and impurity levels are below …";
  - previous studies: "as is common for … (refs)" or "as shown by …";
  - purpose of the study: "to isolate the effect of …";
  - comparison of alternatives: "the simpler formulation predicted the plant data better".
- **Validity range:** "This holds for … ; outside this range, …"
- **Consequence:** "This may overestimate …", "This assumption is examined in Section 4.3."
- **Origin:** "adopted from [ref]" vs "introduced here".

- **Templates:**
  - "The model is based on the following assumptions (ref): (i) …; (ii) …; (iii) …"
  - "[Phenomenon] is neglected, since [argument with number]."
  - "For simplicity, … is taken as …; the effect of this choice is examined in Section …"
  - "These assumptions isolate the influence of …, but may lead to an [optimistic / conservative] estimate of …"
  - "Several simplifications are introduced to keep the problem tractable while preserving …"
  - "Assumptions inherited from [ref] that still affect the results are listed in Table …"
- **Example:** "Intraparticle temperature gradients are neglected, because the estimated Prater number is below 0.05 under all operating conditions (Appendix B); concentration gradients inside the pellet are retained."
- **Cite:** the source of an inherited assumption set; the evidence behind a justification that is not your own calculation.
- **Mistakes:** "It is assumed that … " with no reason; assumptions scattered so that the reader cannot find them; an assumption stated in Methods and contradicted by a result; an assumption whose consequence for the results is never discussed.
- **Applies to:** [PB], [D], optimization (modelling simplifications), [ML] (data and stationarity assumptions).

---

## 5. Equations in the narrative [G, PB, NUM]

### 5.1 The sentence before the equation

The equation is part of the sentence. Over all 341 equation blocks in the 20 analysed papers, about half of the lead-in sentences run straight into the display without punctuation, about a fifth end with a colon and a fifth with a full stop after a complete sentence; reading the equation pages of 13 papers shows that each paper keeps mainly one style (`resources/journals/computers-and-chemical-engineering/section_models.md` §9). Lead-in verbs, by the number of papers using them [J-obs]: *defined as* (11), *obtained as/by* (10), *calculated as/by* (9), *as follows* (8), *expressed as* (7), *computed as*, *given by* (6 each), *formulated as* (5).

| Function | Templates |
|---|---|
| Introduce a governing equation | "The mass balance of species *i* reads"; "The energy balance of the solid phase is written as"; "… is described by" |
| Introduce a definition | "The effectiveness factor is defined as"; "Let *x* denote …, then" |
| Introduce a calculation | "The heat-transfer coefficient is calculated from the correlation of [ref]:"; "… is obtained by integrating Eq. (4) over …" |
| Introduce an objective or constraint | "The net present value is maximized:"; "subject to the energy balance (6) and the bounds" |
| Introduce an adopted equation | "Following [ref], the rate of reaction *j* is expressed as" |
| Introduce a modified equation | "Compared with [ref], Eq. (7) contains an additional term for …" |

Punctuate displayed equations as part of the sentence (comma or full stop after the equation) if the journal's style does; be consistent. In C&CE about 5 of 13 papers read punctuate their equations and the others do not [J-obs]; either is accepted.

**Other conventions observed in C&CE** [J-obs]: equations numbered (1), (2) through the paper and (A.1) in appendices, referred to as "Eq. (5)" and "Eqs. (1)–(2)"; the source of an adopted equation cited in the lead-in; long equations broken before an operator; the domain of each optimization constraint after it (∀*i* ∈ *I*); vectors and matrices bold; units in the where-clause, nomenclature or parameter table, not in the equation; a nomenclature list in 6 of 20 papers, mostly model-heavy ones; pseudocode as a numbered "Algorithm" box. Median 18 numbered equations per paper (0–80).

### 5.2 The sentence after the equation: defining symbols and explaining terms

- **"where" clause:** "…, where *u* is the superficial velocity, *D*ax the axial dispersion coefficient and *r*i the rate of formation of species *i*." Used in 14 of 20 papers; *denotes* and *represents* in 10 and 16. Define each new symbol once, with units in the nomenclature or in brackets.
- **Term-by-term meaning:** "The first term on the right-hand side represents convection, the second axial dispersion, and the third the reaction source."
- **Physical interpretation:** "Eq. (5) states that the heat released by reaction is removed by convection and through the wall; at the hot spot the two balance."
- **Purpose:** "This expression is used to …", "Eq. (9) ensures that …".
- **Range or condition:** "valid for Re > …", "for *i* = 1, …, *N*".

### 5.3 Linking equations

| Operation | Templates |
|---|---|
| Refer back | "Using Eq. (3)", "From Eqs. (3)–(5)", "the balance in Eq. (6)" (12 of 20 papers; one paper refers to equations 41 times) |
| Substitute | "Substituting Eq. (4) into Eq. (2) gives"; "Inserting the rate expression (7) into the balance (3) yields" |
| Combine | "Combining Eqs. (1) and (4), the integral error over one period is obtained as" |
| Simplify | "For steady state, the accumulation term vanishes and Eq. (2) reduces to"; "Neglecting …, the expression simplifies to" |
| Couple | "Eqs. (2)–(6) form a coupled system of differential-algebraic equations in the unknowns …"; "The pellet and reactor models are coupled through the surface concentrations, which enter Eq. (8) as boundary values." |
| Reformulate | "To obtain a tractable problem, the bilevel model is reformulated as a single-level problem by replacing … with its KKT conditions (ref)." |

### 5.4 Closures and correlations

- **Form:** name the correlation, its source, its validity range, and why it was chosen: "The wall heat-transfer coefficient is calculated with the correlation of [ref] (Eq. 12), which was derived for tube-to-particle diameter ratios between 3 and 12 and therefore covers the present ratio of [value]."
- **Cite:** always the original source; for property methods also the software implementation used.
- **Mistakes:** an unnamed correlation; a correlation used outside its range without comment.

### 5.5 Initial and boundary conditions

- **Form:** right after the equations they close, with the physical meaning: "At the inlet (*z* = 0) the composition and temperature equal the feed values (Danckwerts conditions); at the outlet (*z* = *L*) the axial gradients vanish. Symmetry at the axis and heat exchange with the coolant at the wall close the radial problem."
- For transient models: the initial state and how it was obtained ("The steady state at nominal conditions serves as the initial state for the dynamic simulations.").
- **Mistakes:** conditions missing for one of the variables; an initial state that is not reproducible.

### 5.6 Notation and numbering

- One symbol per quantity throughout; the same symbol in figures, tables and text; nomenclature list for model-heavy papers (about a third of the analysed papers had one).
- Number displayed equations consecutively in the order they are cited [J-req, C&CE]; refer to them by number ("Eq. (5)"), not "the equation above".
- Present simple formulas in line; display the rest [J-req, C&CE].
- Variables italic; units and descriptive subscripts upright; exp for powers of e [J-req, C&CE]. LaTeX: `methods-latex.md` §9.

### 5.7 Established, modified and new equations

Mark the status of every displayed equation that is not textbook material: "(ref)" in the lead-in for adopted ones; a sentence naming the change for modified ones; "we propose" or "introduced here" for new ones, followed by its derivation (main text if short, appendix if long).

---

## 6. Numerical methods and implementation [NUM]

### 6.1 What to report

| Item | Form |
|---|---|
| Problem class | "The model is a system of [n] DAEs of index 1" / "a nonconvex MINLP with … binary variables" |
| Discretization | "The radial and axial coordinates are discretized by orthogonal collocation with … points / finite volumes with … cells"; "method of lines" |
| Time integration | "The resulting ODE system is integrated with a variable-order BDF method (solver, software, version)" |
| Nonlinear or optimization solver | name, version, options that matter |
| Tolerances and criteria | "relative and absolute tolerances of 10⁻⁶ and 10⁻⁸"; "optimality gap of 0.1 %"; "convergence when the change in … falls below …" |
| Solution strategy | sequential or simultaneous; iterative coupling; initialization; warm starts |
| Independence checks | grid or collocation-point and time-step independence, with the criterion and the result |
| Implementation | language, software, libraries, versions; hardware when run time is reported |
| Cost | run time per simulation or per optimization, and on what hardware |

The analysed C&CE papers [J-obs] report software in 11 of 20 Methodology parts, but versions in only 3, solvers in 6, tolerances or stopping criteria in 5, discretization in 9 and hardware or run time in about 9 (some only in the Results). No paper in the sample solved a PDE reactor model, so no grid-independence study was observed. **For a transient multiscale reactor model, report more numerical detail than this average** [G, NUM]: reviewers of reactor-modelling papers expect discretization, solver, tolerances and an independence check.

### 6.2 Justifying the numerical choice

- **Templates:**
  - "A stiff integrator is required because the time constants of the pellet and the reactor differ by about [n] orders of magnitude."
  - "Orthogonal collocation was chosen because it gives accurate radial profiles with few points [ref]."
  - "A decomposition approach is used because the full MINLP could not be solved within [time] with [solver]."
  - "The approach of [ref] was tested first and performed poorly because …; the method below was therefore used."
- **Cite:** the numerical method when it is named and not textbook-standard; the software and solver.
- **Mistakes:** "solved numerically" with no method; tolerances absent; a check stated without its result ("grid independence was verified").

### 6.3 Code and reproducibility

Give enough to rebuild the computation without reproducing the code: equations, discretization, solver and settings, initialization, data, and where the code or data are deposited (or why they cannot be shared). Long listings belong in a repository or an appendix.

---

## 7. Algorithms and workflows [NUM, M]

- **Purpose:** show the sequence of computations, the information passed between modules, the loops and the stopping rule.
- **Forms used** [J-obs]: a workflow figure whose steps are referred to in the text (about 8 papers); numbered algorithm boxes or step lists (4 papers; one in an appendix); prose with "first … then … finally".
- **What each step states:** input, operation, output, and the condition to continue or stop.
- **Templates:**
  - "The procedure starts with an initialization step in which …"
  - "At iteration *k*, … is solved for … with … fixed; the solution is passed to …"
  - "Steps 3–5 are repeated until [criterion], or until [budget] is exhausted."
  - "If no candidate satisfies …, the procedure returns to Step 2 and …"
  - "The algorithm terminates when any of the following criteria is met: (i) …; (ii) …"
  - "Algorithm 1 summarizes the complete sequence."
- **Originality:** say which steps are new: "Steps 1–3 follow [ref]; the refinement in Step 4 is introduced here."
- **Mistakes:** a loop without a stopping criterion; a figure whose step numbers do not match the text; pseudocode that defines symbols not used in the equations.

---

## 8. Data-driven, machine-learning and hybrid components [ML]

### 8.1 Data

- **Source and acquisition:** who produced the data, when, how, how much. "Operating data were recorded in the plant between [dates] at [interval]"; "The dataset was curated by [ref]; only the publicly available subset of [n] entries is used."
- **Reconstruction and synthetic data:** state clearly what was measured, digitized, interpolated, simulated or generated [Rule]: "Profiles were digitized from Fig. 4 of [ref] (uncertainty ±…)"; "A first-principles model serves as a virtual plant to generate [n] trajectories."
- **Cleaning and preprocessing:** synchronization, aggregation, outlier treatment, interpolation, filtering, scaling, each with its parameters and the data it was fitted on.
- **Features:** inputs and outputs in a table; engineered features with their physical motivation.

### 8.2 Splits and leakage

- Training, validation and test sets with sizes and the rule used (random, grouped, time-ordered); why that rule fits the use.
- Leakage control: "Scaling parameters are computed on the training set only"; "The test period lies after all training data"; "The held-out data are used once, after all choices were fixed"; "Windows from the same trajectory are kept in the same set." In the analysed papers, 6 of 20 address leakage explicitly; under the rule of this skill, every data-driven method states how it was prevented.

### 8.3 Model, training and selection

- Architecture (layers, units, activation; trees and depth; kernel), with a figure if non-standard.
- Loss function and optimizer; training length and stopping rule; hyperparameters and how they were chosen (search space, validation scheme); random seeds and repetitions (4 of 20 papers report seeds; several repeat training or report several seeds).
- Baselines defined in the Methodology, with what each isolates ("a context-only model gives the floor; an aggregated model shows the value of the individual features").
- **Templates:** "The network has [n] hidden layers of [m] units with [activation]; it is trained with [optimizer] at a learning rate of [value] for [n] epochs, minimizing [loss]."; "Hyperparameters were selected by [search] on the validation set over the ranges in Table 3."; "Each model is trained with five random seeds; results are reported as mean and range."

### 8.4 Hybrid models

Explain the division of labour: which quantities the physical part computes, which the data-driven part learns, how the two exchange information, and what physical structure the hybrid enforces.
- **Templates:**
  - "The data-driven part predicts [quantity] at the reference state, while the parameters of [physical relation] are learned jointly and extrapolate it to other [temperatures / conditions]."
  - "The first-principles model provides [states]; the network corrects [residual] / replaces [closure]."
  - "Physics enters as [constraint / structural prior / library of candidate terms], so that …"
  - "The surrogate is trained on [n] simulations of the first-principles model sampled by [design] over [ranges]."
- **Cite:** the established architecture or algorithm (the network type, the training algorithm, the sampling design); state what is new.
- **Mistakes:** an architecture described only by a name; hyperparameters "tuned" without a procedure; a test set used for model selection; a hybrid whose physical and learned parts are not distinguishable in the text.

---

## 9. Parameters, data and their origin [M, Rule]

Every value has a traceable origin. Distinguish six origins and say which one applies:

| Origin | Wording |
|---|---|
| Literature | "taken from [ref]", "as reported by [ref]" |
| Own measurement | "measured with [instrument], uncertainty ±…" |
| Industrial source | "provided by the plant operator", "from the plant documentation"; anonymized or normalized if confidential |
| Calculated from an established relation | "calculated from Eq. (12) with properties from [source]" |
| Estimated or calibrated in this work | "estimated by minimizing … against [data] (Section 2.6)" |
| Assumed or selected by the authors | "set to [value] because …", "chosen as a representative value within the range [a–b] reported by [refs]" |

- **Parameter table:** symbol, description, value, unit, origin (reference, measured, calibrated, assumed). Put it in the main text if short, in an appendix if long; refer to it where the parameters are first used.
- **Honesty about provenance** [J-obs]: some papers state that data from different years were combined, which values are inherited and still matter, and which were calibrated with a proxy. Do the same.
- **Mistakes:** a tolerance, weight or penalty "considered" without reason; values from a figure presented as if from a table; a parameter estimated and validated on the same data.

---

## 10. Verification, validation and evaluation [M, PB, ML]

### 10.1 Verification vs validation

- **Verification:** the equations are solved correctly (code checks, mass and energy closure, comparison with an analytical solution or a published simulation, independence of grid and time step).
- **Validation:** the model represents reality for the intended use (comparison with experimental, pilot or plant data not used for fitting).
- Say which is which; describe both procedures in the Methodology and their outcomes in the Results [G]. In the analysed papers only a few name verification explicitly (for example a subsection on computation and verification, or an appendix on implementation and verification).

### 10.2 Metrics and criteria

- Define each metric with its formula and say what it measures and why it fits ("RMSE weights large deviations; MAE is less sensitive to them"); say on which data it is computed. 12 of 20 papers define metrics in the Methodology; some give them a section of their own.
- Statistical tests: name, assumption, significance level ("a χ² test at α = 0.05 on the weighted residuals").
- Uncertainty and sensitivity: method (local, Sobol, bootstrap, Monte Carlo, profile likelihood), sample sizes, ranges; identifiability or estimability analysis before parameter estimation.
- **Templates:** "Model accuracy is quantified by …, defined as … (Eq. 20)."; "Validation uses [data] from [period/campaign], which was not used for calibration."; "Parameter uncertainty is expressed as 95 % confidence intervals computed from …"; "Global sensitivity is quantified by first-order and total Sobol indices estimated from [n] samples."
- **Mistakes:** a metric used in the Results but never defined; validation on training data; "good agreement" criteria not stated in advance.

---

## 11. Citations in the Methodology [Rule, J-obs]

Every externally sourced equation, model, correlation, parameter, dataset, method, algorithm, software or methodological claim is cited; the authors' own implementation, procedures, derivations and decisions need no external citation but must be traceable to equations, evidence or validation. Full rules: `citation-practice.md` §12.

**Inventory before drafting** (idea adapted from the outline stage of PaperOrchestra, Song et al., 2026). List every external element the study uses and attach a citation to each before writing the Methodology. In a chemical-engineering modelling paper the list usually includes:
- reaction network and kinetic model (rate expressions and their parameters);
- transport correlations: pressure drop (e.g. Ergun), heat- and mass-transfer coefficients, effective conductivity and dispersion, wall heat transfer;
- physical and thermodynamic property data or methods (equations of state, mixing rules, property databases);
- reactor, plant or experimental data used for validation or training, with the source and the table or figure;
- numerical methods: discretization scheme, ODE/DAE/PDE solver, optimization algorithm, sampling design;
- sensitivity and explanation methods (Sobol indices and the estimator used, SHAP and the explainer variant);
- machine-learning architectures, training algorithms and optimizers, metrics if not standard;
- software and packages with versions (simulator, Python libraries, solvers).

Where the exact source of an element is not known, find it before writing; never write a citation from memory. Observed in C&CE: about 10 % of Methodology sentences carry a citation (median 9 unique references per Methodology), mostly for facts and justifications, parameter and property values, adopted models, datasets and named methods.

---

## 12. Figures, tables and nomenclature [G, J-obs]

- **Figures typical of the Methodology:** process flow diagram or reactor schematic (system), computational domain or discretization sketch (numerics), workflow or flowchart (framework), network architecture (ML). Median two figures and one table are first referred to in the Methodology [J-obs].
- **Introduce and use them:** "as shown in Fig. 2" (15 of 20 papers), "Fig. 1 shows / illustrates …" (12); say what to look at in the figure, not only that it exists.
- **Tables:** operating conditions, parameters with origin, data sets with sizes and splits, hyperparameters, model inputs and outputs.
- **Consistency:** one name per quantity across equations, nomenclature, figures and text; units SI [J-req]; dimensionless groups defined once.

---

## 13. Language of the Methodology [G, J-obs]

- **Tense** [J-obs]: computational Methodology sections are written mainly in the **present** (what the model is, what the framework does: about 55 % of sentences contain present-tense markers against 3–4 % with past markers), with the **past** used for what was actually carried out on data (collection, processing, runs: up to 40 % in data-heavy papers). This differs from experimental papers, where the procedure is in the past [G]; choose by content and be consistent within a subsection.
- **Voice** [J-obs]: passive in about half of the sentences (median 46 %); "we" is rare (median under 1 % of sentences, up to about 30 % in a few papers) and is used for decisions and new proposals ("we propose", "we freeze"). Imperatives ("Write the plant as …") appear in one paper and are unusual.
- **Sentence length:** median 21 words, shorter than in the Introduction (27); equations take the load of precision.
- **Frequent expressions:** *based on* (18 of 20 papers), *represents* (16), *as shown in Fig.* (15), *where … is/are* (14), *yields* (12), *in this work/study* (12), *defined as* (11), *obtained as/by* (10), *denotes* (10), *calculated as* (9), *for details see / is provided in* (9). Do not decorate these with adverbs; they are working phrases.
- **Remarks and definitions** (theory papers): "Remark 1:", "Definition 1", "Lemma 1" with proofs, to keep the main argument clean.

---

## 14. Avoiding repetition without losing completeness [G]

- Define each symbol once; refer to the nomenclature afterwards.
- Describe a standard method by name and citation; describe only what you changed.
- Put long lists of correlations or parameters in a table or appendix and refer to it once in each place of use.
- Use one sentence pattern for parallel items (balances of each phase; constraints of each category) so that differences stand out.
- Do not restate the Introduction's motivation; one clause of purpose per subsection is enough.

---

## 15. Reproducibility checklist [M, NUM, ML]

Check each item; state it in the Methodology, an appendix or a repository.

- [ ] System, boundaries and operating range defined; schematic provided.
- [ ] All governing equations, closures and correlations, with sources and validity ranges.
- [ ] Assumptions listed, justified, with validity and consequences; adopted vs introduced marked.
- [ ] Initial and boundary conditions for every variable; initial state of transient runs.
- [ ] Every parameter with value, unit and origin (literature, measured, industrial, calculated, estimated, assumed).
- [ ] Discretization, integrator or solver, version, tolerances, solution strategy, initialization.
- [ ] Grid or collocation-point and time-step independence, with criterion and result.
- [ ] Data: source, period, size, sampling, measured vs reconstructed vs simulated; preprocessing with parameters.
- [ ] Splits with sizes and rule; leakage prevention stated.
- [ ] Model architecture, loss, optimizer, training length, stopping rule, hyperparameter search, seeds and repetitions.
- [ ] Baselines and what they isolate.
- [ ] Metrics defined with formulas and the data they are computed on; statistical tests and levels.
- [ ] Verification and validation procedures, with independent validation data.
- [ ] Sensitivity and uncertainty methods with sample sizes.
- [ ] Software, libraries and versions; hardware and run times where they are reported.
- [ ] Code and data availability (repository, or the reason they cannot be shared) [J-req where the journal has a data policy].
- [ ] Supplementary files cited in the text and captioned.

Frequently missing in the analysed papers [J-obs]: software versions, solver tolerances, random seeds, verification, and independence checks.

---

## 16. Common mistakes in the Methodology

- Results or their interpretation in the Methodology; or methods first described in the Results.
- Equations dropped into the text without a lead-in or without defining their symbols.
- "Solved numerically", "trained a neural network", "standard parameters" without specifics.
- A parameter, tolerance or penalty value without origin or reason.
- An assumption without justification, validity range or consequence.
- Adopted elements not cited, or new elements not marked as new.
- Inconsistent symbols between equations, figures and the nomenclature.
- Validation data that were also used for calibration or model selection.

---

## 17. Benchmarks from *Computers & Chemical Engineering* [J-obs]

Methodology part (from the end of the Introduction to the first results section) of 20 research articles; medians with interquartile range. Use as orientation, not as targets.

| Measure | Median (IQR; range) |
|---|---|
| Words | 2,676 (2,118–3,714; 555–6,619) |
| Sentences | 123 (99–210) |
| Words per sentence | 20.9 (19.8–22.7) |
| Top-level sections in the methodology part | 1 (1–2; up to 8) |
| Subsections | 4 (3–8; 0–16) |
| Numbered equations | 15.5 (4–22; 0–75) |
| Equations per 1,000 words | 5.5 (2.8–7.3) |
| References to equations by number ("Eq. (n)") | 1 (0–5; up to 41); used in 12 papers |
| Figures / tables first referred to in the methodology | 2 (2–3) / 1 (0–2) |
| Citation instances / unique references | 15.5 (7–24) / 9 (6–15) |
| Share of sentences with a citation | 0.10 (0.03–0.14; 0.01–0.28) |
| Citations per sentence | 0.13 (0.05–0.21) |
| Sentences with a passive verb | 0.46 (0.42–0.57) |
| Sentences with present / past markers | 0.56 / 0.04 |

By type of methodology (medians): first-principles and process simulation (5 papers): about 1,100 words, 21 % of sentences cited; optimization and control (6): about 4,100 words, 22 equations, 7 % cited; data-driven (6): about 3,200 words, 9 equations, 3 % cited; hybrid (3): about 2,700 words, 17 equations, 11 % cited. Citation share by subsection type (pooled): system and case description 14 %, data-driven components 10 %, physical model 8 %, evaluation 7 %, numerics and solution 6 %.
