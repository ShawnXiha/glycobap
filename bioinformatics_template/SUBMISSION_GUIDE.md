# Bioinformatics Journal Submission Package

## Target Journal
**Bioinformatics (Oxford University Press)**
- Impact Factor: 5.4-5.8
- Quartile: Q1
- APC: ~$3,799 USD

## Package Contents

### Main Manuscript Files
| File | Description |
|------|-------------|
| `paper.tex` | Complete LaTeX manuscript |
| `references.bib` | BibTeX bibliography |
| `tables.tex` | Formatted tables |

### Figures (SVG format - ready for conversion)
| File | Description |
|------|-------------|
| `figures/figure1_pipeline.svg` | Pipeline architecture diagram |
| `figures/figure2_accuracy.svg` | Accuracy comparison bar chart |
| `figures/figure3_timing.svg` | Processing time comparison |

### Figure Generation Scripts (Python)
| File | Description |
|------|-------------|
| `figures/plot_figures.py` | Main figure generation script |
| `figures/figure1_pipeline.py` | Pipeline diagram generator |
| `figures/figure2_accuracy.py` | Accuracy chart generator |
| `figures/figure3_timing.py` | Timing chart generator |

---

## Figure Conversion Instructions

Bioinformatics requires figures in TIFF or EPS format. Convert SVG files:

### Using Inkscape (recommended)
```bash
# Convert to EPS
inkscape figure1_pipeline.svg --export-eps=figure1_pipeline.eps

# Convert to TIFF (300 DPI)
inkscape figure1_pipeline.svg --export-type=png --export-filename=figure1_pipeline.png
convert figure1_pipeline.png -density 300 figure1_pipeline.tiff
```

### Using ImageMagick
```bash
convert -density 300 figure1_pipeline.svg figure1_pipeline.tiff
```

---

## LaTeX Compilation

### Using pdflatex
```bash
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
```

### Using Overleaf
1. Upload all files to Overleaf
2. Set `paper.tex` as main document
3. Compile

---

## Journal Requirements Checklist

### Manuscript Format
- [x] Abstract (structured with Motivation, Results, Availability, Contact)
- [x] Keywords (5-10 keywords)
- [x] Section numbering
- [x] References in author-date format
- [x] Tables formatted with booktabs

### Figures
- [ ] Convert SVG to TIFF/EPS (300 DPI minimum)
- [ ] Figure legends in manuscript
- [ ] Color-blind friendly palette used

### Supplementary Materials
- [ ] Benchmark dataset (CSV)
- [ ] Code availability statement
- [ ] README with installation instructions

### Submission Items
- [ ] Cover letter
- [ ] Author information
- [ ] Conflict of interest statement
- [ ] Data availability statement

---

## Bioinformatics Format Specifications

### Document Class
```latex
\documentclass[numsec,webpdf,modern,large]{bioinfo}
```

### Bibliography Style
```latex
\bibliographystyle{author-date}
```

### Figure Requirements
- Width: Single column 85mm, Double column 180mm
- Resolution: 300 DPI minimum for TIFF
- Format: TIFF, EPS, or PDF
- No JPEG for line drawings

### Table Requirements
- Use booktabs package
- No vertical lines
- Minimal horizontal lines
- Caption above table

---

## Quick Start

1. **Compile manuscript**:
   ```bash
   cd bioinformatics_template
   pdflatex paper.tex
   bibtex paper
   pdflatex paper.tex
   ```

2. **Convert figures**:
   ```bash
   cd figures
   for f in *.svg; do
     inkscape "$f" --export-eps="${f%.svg}.eps"
   done
   ```

3. **Submit to OUP**:
   - Go to https://academic.oup.com/bioinformatics
   - Click "Submit"
   - Upload all files
   - Complete submission form

---

## Notes

- SVG figures can be edited in Inkscape, Adobe Illustrator, or any vector graphics editor
- Python scripts provided for regenerating figures with different data
- tables.tex contains all formatted tables for easy modification
