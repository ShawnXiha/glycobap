#!/usr/bin/env python3
"""Generate complete PDF from manuscript_final.md"""

import os
import subprocess

# Read manuscript
with open('/home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides/manuscript_final.md', 'r') as f:
    content = f.read()

# Create LaTeX content
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
\usepackage{longtable}
\usepackage{multirow}
\usepackage{array}

\graphicspath{{../figures/}{figures/}}

\title{\textbf{GlycoSMILES2BAP: An Automated Pipeline for Stereochemistry-Preserving Glycan Structure Prediction with AlphaFold 3}}

\author{Qiang Xia\\
\small Zhejiang Xinghe Tea Technology Co., Ltd.\\
\small Hangzhou, Zhejiang, China\\
\small \texttt{xiaqiang@xinghetea.com}}

\date{}

\begin{document}
\maketitle

\begin{abstract}
\noindent\textbf{Motivation:} AlphaFold 3 (AF3) has revolutionized protein structure prediction and expanded capabilities to include glycan ligands. However, recent work by Huang et al.\ (2025) identified a critical limitation: standard input formats (SMILES, userCCD) produce stereochemically incorrect glycan structures, while the stereochemistry-preserving CCD+bondedAtomPairs (BAP) format requires impractical manual atom-by-atom specification.

\noindent\textbf{Results:} We present GlycoSMILES2BAP, an automated pipeline that converts standard glycan notations (IUPAC-condensed, WURCS) to AF3-compatible CCD+BAP format. The pipeline integrates three core modules: (1) a CCD mapper supporting 28+ monosaccharide configurations, (2) a topology parser extracting linkage information, and (3) a BAP generator producing explicit atom-pair bond specifications. Validated on a curated benchmark of 50 diverse glycan structures with systematic evaluation, GlycoSMILES2BAP achieves 97.8\% epimer accuracy, 97.4\% anomeric accuracy, and 95.9\% linkage accuracy compared to ${\sim}60$\% for SMILES-based approaches, with processing time $<$1 second per structure versus 30--60 minutes for manual specification. Systematic ablation studies confirm that all three core modules contribute significantly to the high accuracy. Furthermore, validation against 10 literature-reported structure errors demonstrated 100\% correction rate, and database-scale processing demonstrated scalability with 94\% success rate on 100 GlyTouCan representative structures.

\noindent\textbf{Conclusions:} GlycoSMILES2BAP eliminates the input format barrier for AF3 glycan modeling, enabling accurate, reproducible structure prediction for the glycobiology community.

\noindent\textbf{Availability:} \url{https://github.com/xiaqiang/glycosmiles2bap}

\noindent\textbf{Keywords:} AlphaFold 3, glycans, stereochemistry, structure prediction, CCD, bondedAtomPairs
\end{abstract}

\section{Introduction}

Glycans are essential biological molecules involved in protein folding, cell signaling, immune recognition, and pathogen interaction [1]. Over 50\% of human proteins undergo glycosylation, making accurate glycan structure prediction crucial for understanding biological mechanisms and developing therapeutics [2]. GlyTouCan, the international glycan structure repository, catalogs over 200,000 unique glycan structures [5], highlighting the scale of structural diversity that researchers need to navigate.

AlphaFold 3 (AF3) represents a breakthrough in biomolecular structure prediction, achieving unprecedented accuracy for protein-ligand complexes including glycans [3]. However, Huang et al.\ (2025) systematically demonstrated that AF3's standard input formats fail to preserve glycan stereochemistry [4]. Their analysis revealed that the CCD+BAP format is the only format producing stereochemically correct structures, achieving near-perfect accuracy. However, BAP specification requires manual atom-by-atom bond designation, taking 30--60 minutes per structure.

Here, we present