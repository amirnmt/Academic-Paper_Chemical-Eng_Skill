# Figures and tables

Figures and tables usually carry the main results. Design them so a reader can understand them on their own, and integrate each into the text.

## 1. Text, table or figure?

- One or two values, or a result that fits in a sentence: text.
- Many precise values, repetitive data, parameters, comparisons across several conditions: table.
- Trends, relationships, profiles, distributions, comparisons of shapes: figure.
- If the numbers show no pronounced trend, a table is usually better than a graph.
- Never present the same data in more than one form.
- Check the journal's limit on the number of figures and tables; supplementary material can hold the rest.

## 2. Figure principles: economy, integrity, clarity

**Economy**
- As simple as possible; every element must carry information.
- No 3D effects, shadows, background shading, decorative images or unnecessary gridlines.
- Maximize the data-to-ink ratio: data stand out, everything else recedes.
- Fit the axis range to the data; do not extend axes far beyond the data (if values run from 0 to 78, end the axis at 80), and do not leave large empty regions.

**Integrity**
- Every axis has a label with quantity and unit, even when it seems obvious: "Temperature, T (K)" or "T / K" (follow the journal).
- Do not add pseudo-dimensions (3D bars for 2D data); data dimension = figure dimension.
- Compared panels use identical axis ranges and scales.
- Show uncertainty where it exists (error bars, bands) and state what it represents (standard deviation, standard error, confidence interval, min–max).
- Do not truncate axes in a way that exaggerates differences (bar charts start at zero).

**Clarity**
- Ticks point outward; tick labels at round numbers (0, 20, 40, 60, 80 rather than 0, 17, 34 …).
- Font size readable at final printed width (about 8–10 pt at one column, 8–9 cm wide, or two columns, 17–18 cm).
- Consistent colours, markers and line styles across all figures (the same correlation always has the same colour).
- Colourblind-safe palette; distinguishable in greyscale (vary markers and line styles as well as colour).
- Experimental data as markers, model results as lines.
- Legends inside the plot area when space allows, or direct labels on the lines.
- Panels labelled (a), (b), (c) and referenced in the caption and text.

## 3. Common engineering chart types

| Purpose | Chart |
|---|---|
| Profile along a reactor or column | line plot vs axial position; measured points as markers |
| Model validation | parity plot (predicted vs measured, 1:1 line, ±10 % or ±20 % bands) |
| Model error distribution | residual plot or histogram |
| Time series and forecasts | line plot vs time; training/test boundary marked; prediction intervals as bands |
| Parameter effect | family of curves, one per parameter value |
| Sensitivity analysis | horizontal bar chart of sensitivity indices (e.g. first-order and total Sobol indices) |
| Comparison of methods/correlations | grouped bar chart of error metrics or a table |
| Two-dimensional fields | contour or colour map with a perceptually uniform colour scale and a labelled colour bar |

## 4. Producing figures

- Generate every figure from a script that the author can rerun when data change (Python/matplotlib or similar); keep data and script together.
- Export vector formats (PDF, EPS or SVG) for line art; high-resolution raster (≥ 300–600 dpi) only for images.
- Set the figure size to the final column width in the script, not by scaling afterwards.
- Use the same style settings for all figures.

Minimal matplotlib style:

```python
import matplotlib.pyplot as plt
plt.rcParams.update({
    "figure.figsize": (3.5, 2.6),   # inches, one journal column
    "font.size": 8, "axes.labelsize": 8, "legend.fontsize": 7,
    "xtick.direction": "out", "ytick.direction": "out",
    "lines.linewidth": 1.2, "lines.markersize": 4,
    "savefig.bbox": "tight", "savefig.dpi": 600,
})
fig, ax = plt.subplots()
ax.plot(z_model, T_model, "-", label="Model")
ax.plot(z_meas, T_meas, "o", mfc="none", label="Measured")
ax.set_xlabel("Axial position, $z$ (m)")
ax.set_ylabel("Temperature, $T$ (K)")
ax.legend(frameon=False)
fig.savefig("fig_temperature_profile.pdf")
```

## 5. Figure captions

- Captions go below figures.
- Start with a short title-like statement, then the necessary details: conditions, symbols, what error bars mean, data sources.
- Self-explanatory: a reader who sees only the figure and caption understands it.
- Do not interpret in the caption; interpretation belongs in the text.
- Example: "Figure 4. Axial temperature profiles at the tube centreline: measurements (symbols) and predictions with five wall heat-transfer correlations (lines). Conditions: p = [value] bar, T_c = [value] K. Error bars show ± one standard deviation of three repeated runs."

## 6. Tables

- Caption (title) above the table: concise, identifies the content without the text. Name conditions instead of "Group 1/Group 2".
- Three horizontal rules (top, below header, bottom); no vertical rules. In LaTeX: `booktabs` (`\toprule`, `\midrule`, `\bottomrule`).
- Units in column headers or a unit column; avoid exponents in headers (×10³ is ambiguous; give the values in suitable units instead).
- Align numbers on the decimal point (siunitx `S` columns); consistent significant figures in a column.
- Arrange like elements to read down columns.
- Remove columns that are constant (state the value once in a note or in Methods) and tables that mostly contain zeros or a single message.
- Footnotes for abbreviations, sources and notes, marked with letters or symbols.
- Analogous tables use the same layout.

## 7. Numbering and placement

- Number figures and tables separately, consecutively, in the order of first citation in the text (Figure 1, 2 …; Table 1, 2 …).
- Cite each in the text before it appears; place it after its first mention (or as the journal requires).
- Refer to them consistently ("Fig. 3" or "Figure 3", as the journal prefers).

## 7a. Referring to figures and tables in the text

- Make the finding the subject and cite the figure in brackets: "The hot spot moved downstream as the coolant temperature decreased (Fig. 5)." Avoid "It is clearly shown in Fig. 5 that …".
- When the figure is the subject, use a precise verb: shows, compares, summarizes, plots, illustrates, lists.
- Do not repeat in words what the figure shows; add what the reader cannot see at once: the main trend, its size, the exception, and its meaning.
- Each figure and table must be discussed in the text; a figure that is never discussed should be removed or moved to supplementary material.
- Figures and tables can also present methods: flowcharts of the procedure or workflow, diagrams of the apparatus or model domain, tables of operating conditions and parameters.

## 7b. What Computers & Chemical Engineering papers do [J-obs]

From all 181 figure and 138 table captions and every in-text reference in 20 papers (details: `resources/journals/computers-and-chemical-engineering/section_models.md` §8):
- **How many:** median 8.5 figures and 5.5 tables per paper, about 0.9 per page; roughly half of the figures in two-column papers are full width.
- **Which figures:** a scheme of the framework or process early (Fig. 1 or 2) in nearly every paper; then comparisons with data or baselines (28 % of figures), profiles and time series (14 %), error and uncertainty distributions (13 %), sensitivity or importance (12 %), optima and Pareto fronts (10 %).
- **Which tables:** parameters, properties and input data (46 %), results and comparisons (39 %), method settings and reaction mechanisms (9 %); sources of literature values in the caption or a footnote.
- **Captions:** figures median 14 words (a third are several sentences: title phrase, what is plotted, conditions with values, meaning of panels and symbols); tables median 10 words, a noun phrase, explanations in footnotes.
- **In the text:** always "Fig. 3" in running text; "Table 2". Most references sit inside the sentence (85 % of figure references are not in brackets): "Fig. 3 shows …" (the most common opener), "presents", "illustrates", "compares"; "as shown in Fig. 3". The general advice in §7a (finding first, figure in brackets) is equally accepted and usually shorter; use it for results, and "Fig. X shows …" when introducing a figure that the reader must study.
- **Order:** the first mention comes before or on the page of the figure in 93 % of cases.

## 8. Common errors

- Missing units or axis labels; units in different systems.
- Too many curves on one plot; unreadable small fonts after scaling.
- Different colours for the same item in different figures.
- Data repeated in a figure and a table.
- Captions that interpret instead of describe.
- Graphs for data without a trend; tables for data with a strong trend.

## 9. Checklist

- [ ] Right form chosen (text/table/figure); nothing duplicated.
- [ ] Axes labelled with quantity and unit; readable at final size.
- [ ] Consistent style, colours and markers across figures; colourblind-safe.
- [ ] Uncertainty shown and explained.
- [ ] Captions below figures, above tables; self-explanatory, descriptive not interpretive.
- [ ] Tables with three rules, units in headers, aligned decimals.
- [ ] Numbered in order of citation; each discussed in the text.
- [ ] Figures generated by rerunnable scripts; vector format.
