# GlycoSMILES2BAP - Bioinformatics Journal Submission Package

## Author
**Qiang Xia (夏强)**  
Zhejiang Xinghe Tea Technology Co., Ltd., Hangzhou, Zhejiang, China  
Email: xiaqiang@xinghetea.com

## Target Journal
**Bioinformatics** (Oxford University Press)  
Impact Factor: 5.4-5.8 | Q1 Journal

## Files Structure

```
/bioinformatics_template/
├── main_manuscript.tex     # Main LaTeX file (includes all parts)
├── part1_header.tex        # Document header and abstract
├── part2_intro.tex         # Introduction section
├── part3_methods.tex       # Methods section
├── part4_results.tex       # Results section
├── part5_discussion.tex    # Discussion and Conclusions
├── references.bib          # BibTeX references
├── cover_letter.tex        # Cover letter
├── compile_final.sh        # Compilation script
└── /figures/
    ├── figure1_pipeline.svg
    ├── figure2_accuracy.svg
    └── figure3_timing.svg
```

## Compilation Instructions

### Prerequisites
1. Install LaTeX distribution (TeXLive, MiKTeX, or MacTeX)
2. Install the bioinfo document class:
   ```bash
   # Download from OUP or use the community-maintained version
   wget https://github.com/RagnarGrootKoerkamp/oxford-bioinformatics-template/raw/main/bioinfo.cls
   ```

### Compile
```bash
cd bioinformatics_template
chmod +x compile_final.sh
./compile_final.sh
```

Or manually:
```bash
pdflatex main_manuscript.tex
bibtex main_manuscript
pdflatex main_manuscript.tex
pdflatex main_manuscript.tex
```

## Figure Conversion

SVG figures need to be converted to EPS or TIFF format for submission:

```bash
# Using Inkscape (recommended)
inkscape figure1_pipeline.svg --export-type=eps --export-filename=figure1_pipeline.eps
inkscape figure1_pipeline.svg --export-type=tiff --export-dpi=300 --export-filename=figure1_pipeline.tiff

# Using rsvg-convert
rsvg-convert -f eps -o figure1_pipeline.eps figure1_pipeline.svg
rsvg-convert -f pdf -o figure1_pipeline.pdf figure1_pipeline.svg

# Using ImageMagick
convert figure1_pipeline.svg -density 300 figure1_pipeline.eps
```

## Submission Checklist

- [ ] Fill in Editor Name in main_manuscript.tex
- [ ] Fill in dates in History section
- [ ] Convert SVG figures to EPS/TIFF format (300 DPI minimum)
- [ ] Compile LaTeX and verify PDF output
- [ ] Review cover letter and update as needed
- [ ] Prepare supplementary materials ZIP
- [ ] Create Graphical Abstract (optional)
- [ ] Submit via OUP online system

## References

Key citations included in references.bib:
1. Abramson et al. (2024) - AlphaFold 3 paper
2. Huang et al. (2025) - Glycan stereochemistry problem
3. Varki (2017) - Glycan biological roles
4. GlyTouCan database citation

## Contact

For questions about this submission:
- Email: xiaqiang@xinghetea.com
- GitHub: https://github.com/xiaqiang/glycosmiles2bap

---
Generated: 2025-01
