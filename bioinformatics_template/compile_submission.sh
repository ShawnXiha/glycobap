#!/bin/bash
# Final compilation script for GlycoSMILES2BAP submission
# Date: 2026-03-21

echo "=================================================="
echo "Compiling GlycoSMILES2BAP Final Manuscript"
echo "=================================================="

# Create output directory
mkdir -p output

# Check for pdflatex
if command -v pdflatex &> /dev/null; then
    echo "Using pdflatex..."
    
    # First pass
    echo ">>> Pass 1: pdflatex..."
    pdflatex -interaction=nonstopmode -output-directory=output paper_submission.tex
    
    # Bibtex
    echo ">>> Running bibtex..."
    cd output
    bibtex paper_submission 2>/dev/null || true
    cd ..
    
    # Second pass
    echo ">>> Pass 2: pdflatex..."
    pdflatex -interaction=nonstopmode -output-directory=output paper_submission.tex
    
    # Third pass
    echo ">>> Pass 3: pdflatex..."
    pdflatex -interaction=nonstopmode -output-directory=output paper_submission.tex
    
    # Check result
    if [ -f "output/paper_submission.pdf" ]; then
        echo ""
        echo "=================================================="
        echo "SUCCESS: paper_submission.pdf generated!"
        echo "Location: output/paper_submission.pdf"
        echo "Size: $(du -h output/paper_submission.pdf | cut -f1)"
        echo "=================================================="
    else
        echo "ERROR: PDF not generated. Check output/paper_submission.log"
    fi
    
elif command -v latexmk &> /dev/null; then
    echo "Using latexmk..."
    latexmk -pdf -output-directory=output paper_submission.tex
    
else
    echo "ERROR: No LaTeX compiler found."
    echo "Please install texlive or miktex."
    echo ""
    echo "On Ubuntu/Debian: sudo apt install texlive-full"
    echo "On macOS: brew install mactex"
    exit 1
fi
