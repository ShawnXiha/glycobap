# Journal Submission Guide: GlycoSMILES2BAP

## Target Journal: Bioinformatics (Oxford)

### Journal Information

| Metric | Value |
|--------|-------|
| **Impact Factor** | 5.4-5.8 (2024) |
| **Quartile** | Q1 |
| **Publisher** | Oxford University Press |
| **APC** | ~$3,799 USD |
| **Review Time** | 60-90 days to first decision |
| **Acceptance Rate** | 40-50% |

### Why Bioinformatics?

1. **Scope fit**: Premier journal for computational biology methods
2. **Tool papers welcome**: "Application Notes" section for software tools
3. **Community reach**: High visibility in bioinformatics community
4. **Reproducibility focus**: Strong emphasis on code availability
5. **LaTeX support**: Official OUP templates available

---

## Submission Requirements

### Manuscript Format

- **Format**: LaTeX (preferred) or Word
- **Template**: OUP General Template (bioinfo.cls)
- **Bibliography**: author-date style
- **Word limit**: ~3,000 words for Application Notes

### Required Sections

1. **Abstract**: Structured (Background, Results, Conclusions)
2. **Introduction**: Problem statement and significance
3. **Methods**: Detailed methodology
4. **Results**: Validation and benchmarks
5. **Discussion**: Limitations and impact
6. **References**: BibTeX format

### Supplementary Materials

- [ ] Benchmark dataset (JSON)
- [ ] Source code (GitHub)
- [ ] Test cases and validation scripts
- [ ] Extended methods
- [ ] Figure files (PDF/PNG, 300 dpi minimum)

---

## File Preparation Checklist

### Main Manuscript
- [x] `manuscript.tex` - Main LaTeX file
- [x] `references.bib` - Bibliography
- [ ] `figures/` - Figure files
- [ ] `tables/` - Table files

### Supplementary Materials
- [x] `supplementary_methods.tex`
- [x] `benchmark_dataset.json`
- [ ] `validation_results.xlsx`
- [ ] `README.md` for GitHub

### Code Availability
- [ ] GitHub repository created
- [ ] README with installation instructions
- [ ] Example usage scripts
- [ ] Test cases included
- [ ] License file (MIT)

---

## LaTeX Compilation Instructions

### Requirements
- TeXLive 2020+ or MiKTeX
- BibTeX/Biber for bibliography
- pdfLaTeX (recommended) or XeLaTeX

### Compile Steps
```bash
cd bioinformatics_template
pdflatex manuscript.tex
bibtex manuscript
pdflatex manuscript.tex
pdflatex manuscript.tex
```

### Using Overleaf
1. Upload all files to new Overleaf project
2. Set `manuscript.tex` as main document
3. Compile with pdfLaTeX

---

## Figure Requirements

| Figure | Format | Resolution | Size |
|--------|--------|------------|------|
| Fig 1: Pipeline | PDF/PNG | 300 dpi | Single column |
| Fig 2: Accuracy | PDF/PNG | 300 dpi | Single column |
| Fig 3: Time | PDF/PNG | 300 dpi | Single column |
| Fig 4: Case studies | PDF/PNG | 300 dpi | Double column |

### Figure Guidelines
- Vector format preferred (PDF, EPS)
- Sans-serif fonts (Arial, Helvetica)
- Minimum 8pt font size
- Color-blind friendly palette

---

## Table Requirements

All tables in LaTeX `table` environment:

```latex
\begin{table}[!t]
\centering
\caption{Title}
\label{tab:label}
\begin{tabular}{@{}lcc@{}}
\toprule
Metric & Value & Reference \\
\midrule
... \\
\bottomrule
\end{tabular}
\end{table}
```

---

## Cover Letter Template

```
Dear Editor,

We are pleased to submit our manuscript "GlycoSMILES2BAP: An 
Automated Pipeline for Stereochemistry-Preserving Glycan 
Structure Prediction with AlphaFold 3" for consideration in 
Bioinformatics.

AlphaFold 3 represents a breakthrough in structure prediction, 
but as Huang et al. (2025) recently demonstrated, standard 
input formats fail to preserve glycan stereochemistry. Our 
tool addresses this critical bottleneck by automatically 
converting standard glycan notations to AF3-compatible format.

Key contributions:
1. Automated CCD+BAP format generation
2. >98% stereochemistry accuracy (vs ~60% baseline)
3. Processing time reduced from hours to seconds
4