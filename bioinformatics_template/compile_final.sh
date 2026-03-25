#!/bin/bash
# Compile script for GlycoSMILES2BAP manuscript
# Bioinformatics (Oxford) journal format

echo "=========================================="
echo "Compiling GlycoSMILES2BAP manuscript..."
echo "=========================================="

# Check if bioinfo.cls exists
if [ ! -f "bioinfo.cls" ]; then
    echo "Warning: bioinfo.cls not found."
    echo "Please download from: https://github.com/RagnarGrootKoerkamp/oxford-bioinformatics-template"
    echo "Or use Overleaf template: https://www.overleaf.com/latex/templates/oup-general-template/fqkhysbcbpwv"
fi

# Compile main manuscript
echo "Step 1: pdflatex..."
pdflatex -interaction=nonstopmode main_manuscript.tex

echo "Step 2: bibtex..."
bibtex main_manuscript

echo "Step 3: pdflatex (2x)..."
pdflatex -interaction=nonstopmode main_manuscript.tex
pdflatex -interaction=nonstopmode main_manuscript.tex

# Check if PDF was generated
if [ -f "main_manuscript.pdf" ]; then
    echo "=========================================="
    echo "SUCCESS: main_manuscript.pdf generated!"
    echo "=========================================="
else
    echo "ERROR: Compilation failed. Check log files."
fi

# Clean auxiliary files (optional)
# rm -f *.aux *.log *.bbl *.blg *.out *.toc

echo "Done."
