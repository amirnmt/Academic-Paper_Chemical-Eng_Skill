# Technical terms — process systems engineering and reactor modelling

Terms that recur in modelling, optimization and data-driven papers in chemical and process engineering (collected from 21 *Computers & Chemical Engineering* papers), with short definitions in our own words and the term each is often confused with. Use one term for one thing throughout a paper (`paragraphs-and-sentences.md`, consistency), define the term at first use when the reader may not know it, and check definitions against a textbook of your field when precision matters. General academic words are in `academic-vocabulary.md` and `vocabulary-by-section.md`.

## Reactors, kinetics and catalysis
| Term | Use it for | Do not confuse with |
|---|---|---|
| multitubular (shell-and-tube) packed-bed reactor | catalyst in many parallel tubes, coolant on the shell side | "fixed-bed" (general term; fine as a synonym, but pick one and keep it) |
| hot spot | local temperature maximum along the bed | outlet temperature |
| thermal runaway | self-accelerating temperature rise once heat generation exceeds removal | "hot spot" (a hot spot can be stable) |
| parametric sensitivity | large change of the output (often the hot spot) for a small change of an input | sensitivity analysis (the method) |
| selectivity / conversion / yield | product formed per reactant converted · reactant converted per reactant fed · product formed per reactant fed | use one definition and state the basis (molar, carbon) |
| ballast gas / diluent | inert or nearly inert gas (methane, nitrogen) that widens the flammability margin | inert (methane is not inert in combustion) |
| Langmuir–Hinshelwood kinetics | surface-reaction rate law with adsorption terms | power-law kinetics |
| reparameterisation (reference temperature) | Arrhenius written around T_ref to reduce the correlation between k0 and E | |
| auto-ignition / auto-decomposition temperature | temperature at which the mixture ignites, or EO decomposes, without an external source | flash point |
| MAWP | maximum allowable working pressure of the vessel | design pressure, operating pressure |

## Models, estimation and validation
| Term | Use it for | Note |
|---|---|---|
| verification | the equations are solved correctly (mesh, tolerance, code checks) | not validation |
| validation | the model represents the real system (comparison with independent data) | state the data and the metric |
| calibration (adjustable) parameter | a parameter estimated from data because its literature value is not transferable | name it as such |
| estimability / identifiability | whether parameters can be estimated from the available data (practical) or from perfect data (structural) | not "sensitivity" |
| orthogonalization-based estimability ranking | ranks parameters by sensitivity not explained by those already ranked | |
| surrogate (metamodel) | fast approximation of a rigorous model, trained on samples of it | "reduced-order model" (derived from the equations) |
| infill / adaptive sampling | adding samples where the surrogate is uncertain or near the optimum | |
| hybrid (grey-box) model | mechanistic and data-driven parts combined (serial or parallel) | |
| held-out / test set | data never used for training or selection | validation set (used for selection) |
| data leakage | information from test data or the future reaching training | |
| ablation | removing one component to measure its contribution | |
| persistence baseline | forecast equal to the last observed value | |
| Sobol indices (first-order, total) | variance-based global sensitivity | local (derivative-based) sensitivity |
| SHAP value | additive attribution of one prediction to the inputs | a causal effect (it is not) |

## Optimisation, design and scheduling
superstructure · MILP / MINLP / GDP (and convex-hull reformulation) · relative optimality gap · ε-constraint method and Pareto front · rolling horizon · fix-and-relax · proactive vs reactive scheduling · integrated scheduling and control.

## Economics, energy and environment
ROI vs NPV (state the definition used) · FCI, WCI, TCI · six-tenths rule (a scaling approximation) · CEPCI · levelized cost · grand composite curve and ΔTmin · energy targets vs heat-exchanger network · functional unit (LCA) · emission factor · CO2-equivalent.

## Safety and operation
operating window / operating zones · security-sensitive variable · one-factor-at-a-time disturbance study · relief device sizing · exposure limits (NIOSH REL, ACGIH TLV, AIHA ERPG: name which one is used).
