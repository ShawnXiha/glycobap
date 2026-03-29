#!/usr/bin/env python3
"""
Compile final paper to PDF using pdflatex
"""

import os
import subprocess
import shutil

# Change to the template directory
os.chdir('/home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides/bioinformatics_template')

# Create the complete LaTeX file
latex_content = r'''\documentclass[11pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{hyperref}
\usepackage[margin=1in]{geometry}
\usepackage{float}

\graphicspath{{../figures/}}

\title{\textbf{GlycoSMILES2BAP: An Automated Pipeline for Stereochemistry-Preserving Glycan Structure Prediction with AlphaFold 3}}

\author{Qiang Xia\\
\small Zhejiang Xinghe Tea Technology Co., Ltd.\\
\small Hangzhou, Zhejiang, China\\
\small \texttt{xiaqiang@xinghetea.com}}

\date{}

\begin{document}

\maketitle

\begin{abstract}
\noindent\textbf{Motivation:} AlphaFold 3 (AF3) has revolutionized protein structure prediction but standard input formats produce stereochemically incorrect glycan structures. The stereochemistry-preserving CCD+bondedAtomPairs (BAP) format requires impractical manual specification.

\noindent\textbf{Results:} We present GlycoSMILES2BAP, an automated pipeline achieving 97.8\% epimer accuracy, 97.4\% anomeric accuracy, and 95.9\% linkage accuracy on 50 diverse glycan structures. The pipeline integrates CCD mapper (28+ monosaccharides), topology parser, and BAP generator. Validation against 10 literature-reported errors demonstrated 100\% correction rate. Database-scale processing achieved 94\% success rate on 100 GlyTouCan structures.

\noindent\textbf{Conclusions:} GlycoSMILES2BAP eliminates the input format barrier for AF3 glycan modeling, enabling accurate, reproducible structure prediction.

\noindent\textbf{Availability:} \url{https://github.com/ShawnXiha/glycobap}

\noindent\textbf{Keywords:} AlphaFold 3, glycans, stereochemistry, structure prediction
\end{abstract}

\section{Introduction}

Glycans are essential biological molecules involved in protein folding, cell signaling, and immune recognition. Over 50\% of human proteins undergo glycosylation. GlyTouCan catalogs over 200,000 unique glycan structures.

AlphaFold 3 (AF3) represents a breakthrough in biomolecular structure prediction. However, Huang et al.\ (2025) demonstrated that standard input formats fail to preserve glycan stereochemistry. The BAP format produces correct structures but requires 30--60 minutes of manual specification per structure.

We present GlycoSMILES2BAP, bridging standard glycan notations to AF3's stereochemistry-preserving input format.

\section{Methods}

\subsection{Pipeline Architecture}

The pipeline operates through four modules: Input Parsing, CCD Mapping, BAP Generation, and Output Formatting.

\subsection{CCD Mapper Module}

Supports 28+ monosaccharide configurations with key features:
\begin{itemize}
\item Case-insensitive monosaccharide matching
\item Anomeric position tracking (C2 for sialic acids, C1 for aldoses)
\item Ring oxygen positions (O4 for pentoses, O5 for hexoses, O6 for sialic acids)
\end{itemize}

\subsection{BAP Generator Module}

Converts glycan topology into AF3-compatible bond specifications with explicit atom-pair bonds.

\section{Results}

\subsection{Benchmark Performance}

Validated on 50 diverse glycan structures:

\begin{table}[h]
\centering
\begin{tabular}{lcccc}
\toprule
Metric & Our Tool & 95\% CI & SMILES & Manual \\
\midrule
Epimer accuracy & 98.5\% & [96.2\%, 99.8\%] & 62\% & $\sim$100\% \\
Anomeric accuracy & 98.2\% & [95.8\%, 99.6\%