#!/usr/bin/env python3
# -*- coding: utf-8 -*-

content = r'''\documentclass[numsec,webpdf,modern,large]{bioinfo}

% Packages
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{hyperref}
\usepackage{siunitx}
\usepackage{longtable}
\usepackage{algorithm}
\usepackage{algorithmic}

% Bibliography
\bibliographystyle{author-date}

\Title{GlycoSMILES2BAP: An Automated Pipeline for Stereochemistry-Preserving Glycan Structure Prediction with AlphaFold 3}

\Author[1]{Qiang Xia$^{*}$}

\Affiliation[1]{Zhejiang Xinghe Tea Technology Co., Ltd., Hangzhou, Zhejiang, China}

\History{Received on XXXX; revised on XXXX; accepted on XXXX}

\Editor{Editor Name}

\Abstract{
\textbf{Motivation:} AlphaFold 3 (AF3) has revolutionized protein structure prediction and expanded capabilities to include glycan ligands. However, recent work by Huang et al.\ (2025) identified a critical limitation: standard input formats (SMILES, userCCD) produce stereochemically incorrect glycan structures, while the stereochemistry-preserving CCD+bondedAtomPairs (BAP) format requires impractical manual atom-by-atom specification.

\textbf{Results:} We present GlycoSMILES2BAP, an automated pipeline that converts standard glycan notations (IUPAC-condensed, WURCS) to AF3-compatible CCD+BAP format. The pipeline integrates three core modules: (1) a CCD mapper supporting 28+ monosaccharide configurations, (2) a topology parser extracting linkage information, and (3) a BAP generator producing explicit atom-pair bond specifications. Validated on a curated benchmark of 50 glycan structures spanning linear, branched, N-linked, and O-linked categories, GlycoSMILES2BAP achieves $>$98\% stereochemistry accuracy compared to $\sim$60\% for SMILES-based approaches, with processing time $<$1 second per structure versus 30--60 minutes for manual specification.

\textbf{Availability:} Open-source implementation available at \url{https://github.com/xiaqiang/glycosmiles2bap}

\textbf{Contact:} \href{mailto:xiaqiang@xinghetea.com}{xiaqiang@xinghetea.com}
}

\Keywords{AlphaFold 3, glycans, stereochemistry, structure prediction, CCD, bondedAtomPairs}

\begin{document}

\maketitle

\section{Introduction}

Glycans are essential biological molecules involved in protein folding, cell signaling, immune recognition, and pathogen interaction \citep{varki2017}. Over 50\% of human proteins undergo glycosylation, making accurate glycan structure prediction crucial for understanding biological mechanisms and developing therapeutics \citep{helenius2004}. GlyTouCan, the international glycan structure repository, catalogs over 200,000 unique glycan structures \citep{tiemeyer2016}, highlighting the scale of structural diversity that researchers need to navigate. This diversity---arising from variations in monosaccharide composition, linkage positions, anomeric configurations, and branching patterns---poses unique challenges for computational structure prediction.

AlphaFold 3 (AF3) represents a breakthrough in biomolecular structure prediction, achieving unprecedented accuracy for protein--ligand complexes including glycans \citep{abramson2024}. This advancement has generated considerable excitement in the glycobiology community, as accurate glycan structure prediction could accelerate research in glycoprotein engineering, vaccine design, and therapeutic glycosylation.

\subsection{The Stereochemistry Problem in AF3 Glycan Modeling}

However, a fundamental challenge emerges when using AF3 for glycan modeling. \citet{huang2025} systematically demonstrated that AF3's standard input formats fail to preserve glycan stereochemistry. Their analysis revealed three input format categories with distinct behaviors:

\begin{enumerate}
\item \textbf{SMILES format:} The Simplified Molecular Input Line Entry System (SMILES) is a widely-used notation for representing molecular structures as text strings. However, AF3 produces incorrect stereoisomers when processing glycan SMILES---most critically, epimer confusion where galactose (Gal) is modeled as glucose (Glc), and incorrect anomeric configurations where $\alpha$-linkages are rendered as $\beta$-linkages or vice versa. The