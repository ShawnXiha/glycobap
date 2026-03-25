#!/bin/bash
# Build script for GlycoSMILES2BAP paper

cd /home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides/bioinformatics_template

# First pdflatex pass
pdflatex -interaction=nonstopmode submission_final.tex

# Bibtex
cd output 2>/dev/null || true
bibtex ../submission_final 2>/dev/null || true
cd ..

# Second pdflatex pass
pdflatex -interaction=nonstopmode submission_final.tex

# Third pdflatex pass
pdflatex -interaction=nonstopmode submission_final.tex

echo "Build complete. PDF generated."
