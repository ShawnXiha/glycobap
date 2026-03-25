#!/bin/bash
# Compile GlycoSMILES2BAP paper for Bioinformatics journal

echo "Compiling GlycoSMILES2BAP LaTeX manuscript..."

# First pass
pdflatex -interaction=nonstopmode glycosmiles2bap_final.tex

# Bibliography
bibtex glycosmiles2bap_final

# Second pass
pdflatex -interaction=nonstopmode glycosmiles2bap_final.tex

# Third pass for references
pdflatex -interaction=nonstopmode glycosmiles2bap_final.tex

echo "Compilation complete. Output: glycosmiles2bap_final.pdf"
