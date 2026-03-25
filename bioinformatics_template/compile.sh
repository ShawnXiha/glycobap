#!/bin/bash
# LaTeX Compilation Script for Bioinformatics Submission
# Author: Qiang Xia
# Date: 2025-01

echo "=== Compiling GlycoSMILES2BAP manuscript ==="

# Check if pdflatex is available
if ! command -v pdflatex &> /dev/null
then
    echo "Error: pdflatex not found. Please install a LaTeX distribution."
    echo "Recommended: texlive-full (sudo apt install texlive-full)"
    exit 1
fi

# Create output directory
mkdir -p output

# First compilation
echo ">>> First pdflatex pass..."
pdflatex -interaction=nonstopmode -output-directory=output paper.tex

# Bibtex
echo ">>> Running bibtex..."
cd output
bibtex paper

# Second compilation
echo ">>> Second pdflatex pass..."
pdflatex -interaction=nonstopmode paper.tex

# Third compilation (for references)
echo ">>> Third pdflatex pass..."
pdflatex -interaction=nonstopmode paper.tex

cd ..

echo "=== Compilation complete ==="
echo "Output files in: output/"
echo "  - paper.pdf (main document)"
echo "  - paper.aux"
echo "  - paper.bbl"
echo ""

# Check for errors
if [ -f "output/paper.pdf" ]; then
    echo "SUCCESS: paper.pdf generated successfully!"
    echo "File size: $(du -h output/paper.pdf | cut -f1)"
else
    echo "ERROR: Compilation failed. Check output/paper.log for details."
    exit 1
fi
