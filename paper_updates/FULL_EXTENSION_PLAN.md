# Paper Extension Plan: Complete Version

## Overview

Based on Scholar-Evaluation (3.625/5) and Scientific-Critical-Thinking analysis:
1. **Missing comparison with existing tools** - Address with GlyLES/GlycanFormatConverter comparison
2. **Small PDB validation sample** - Expand from n=4 to n=12

---

# PART 1: GlyLES Comparison Implementation

## 1.1 Tools to Compare

| Tool | Citation | Purpose | Relevance |
|------|----------|---------|-----------|
| GlyLES | Tiwari et al. 2024 | Glycan embeddings | Different purpose, but same input formats |
| GlycanFormatConverter | Shin et al. 2024 | Format conversion | Direct competitor for format conversion |
| Privateer | Agirre et al. 2023 | Glycan validation | Validation tool comparison |

## 1.2 Comparison Table for Paper

```latex
\begin{table}[h]
\centering
\caption{Comparison with Existing Glycan Tools}
\begin{tabular}{lccc}
\toprule
Feature & GlyLES & GlycanFormatConverter & GlycoSMILES2BAP \\
\midrule
Format Conversion & Yes & Yes & Yes \\
AF3 BAP Output & No & No & Yes \\
Stereochemistry Validation & No & No & Yes (PDB) \\
CCD Mapping & No & No & Yes (28+) \\
Anomeric Position Tracking & No & No & Yes \\
Processing Time & Not reported & Not reported & <1s \\
\bottomrule
\end{tabular}
\label{tab:tool_comparison}
\end{table}
```

## 1.3 Related Work Section Addition

Add to Introduction or create new Related Work section:

```latex
\subsection{Existing Glycan Format Tools}

Several tools exist for glycan format conversion and representation:

\textbf{GlycanFormatConverter} \citep{shin2024} provides conversion between multiple glycan formats (IUPAC, WURCS, GlycoCT, KCF). However, it does not generate AF3-specific CCD+BAP format required for stereochemistry-preserving structure prediction.

\textbf{GlyLES} \citep{tiwari2024} generates language model embeddings for glycan structures, enabling machine learning applications. While valuable for representation learning, it does not address AF3 input generation.

\textbf{Privateer} \citep{agirre2023} validates glycan stereochemistry in crystallographic structures. We use similar validation principles but apply them to CCD mapping verification.

Our work differs from these tools in three key aspects: (1) we specifically target AF3-compatible CCD+BAP output, (2) we provide explicit stereochemistry validation through PDB structure comparison, and (3) we track anomeric positions (C1 vs C2) as a core design feature.
```

---

# PART 2: PDB Validation Expansion

## 2.1 Current Validation (n=4)

| ID | PDB | Structure | Key Test |
|----|-----|-----------|----------|
| V001 | 5NSC | Fucosylated | L-configuration |
| V002 | 1L6R | Lactose | Epimer distinction |
| V003 | 2VXR | Sialyllactose | C2 anomeric |
| V004 | 5K65 | M3 N-glycan | Branch topology |

## 2.2 Proposed Additional Structures (n=8)

| ID | PDB | Structure | Key Test | Reason |
|----|-----|-----------|----------|--------|
| V005 | 4NXU | A2 N-glycan | Bi-antennary topology | Complex branching |
| V006 | 1NPU | GM1 ganglioside | Multiple sialic acids | Ketose clustering |
| V007 | 2JCP | Core-2 O-glycan | O-linked specificity | O-glycan handling |
| V008 | 3WBM | Heparin fragment | Sulfation | Modified monosaccharides |
| V009 | 4DO4 | High-mannose M9 | Large branched | Scalability |
| V010 | 1SLA | Hyaluronan | Repeating disaccharide | Linear polymer |
| V011 | 5FON | Blood group A | Epimer + linkage | Combined challenges |
| V012 | 2W8G | Keratan sulfate | Gal+GlcNAc alternating | Unusual linkage |

## 2.3