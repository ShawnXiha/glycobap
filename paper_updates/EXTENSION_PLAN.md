# Paper Extension Plan: GlyLES Comparison & PDB Validation Expansion

## Overview

Based on Scholar-Evaluation and Scientific-Critical-Thinking analysis, this plan addresses two critical gaps:
1. **Missing comparison with existing tools** (GlyLES, GlycanFormatConverter)
2. **Small PDB validation sample size** (n=4 insufficient)

---

# PART 1: GlyLES Comparison Plan

## 1.1 GlyLES Tool Analysis

**GlyLES** (Glycan Language Model Embeddings) is a recent tool for glycan representation.

### Key Features of GlyLES:
- Converts glycan structures to machine-readable formats
- Uses language model embeddings for glycan representation
- Published in JCIM 2024 (Tiwari et al.)

### Comparison Dimensions:

| Aspect | GlyLES | GlycoSMILES2BAP |
|--------|--------|-----------------|
| Primary Purpose | Glycan embeddings | AF3 input generation |
| Input Format | IUPAC, WURCS | IUPAC, WURCS, GlycoCT |
| Output Format | Embeddings | CCD + BAP |
| AF3 Compatible | No (different purpose) | Yes (designed for AF3) |
| Stereochemistry Focus | Not primary | Primary design goal |
| Processing Time | Not reported | <1s |

### Key Differentiators:
1. **Purpose**: GlyLES generates embeddings; we generate AF3-compatible input
2. **Stereochemistry**: Our tool explicitly tracks anomeric positions (C1 vs C2)
3. **Validation**: We provide PDB-validated stereochemistry handling

## 1.2 GlycanFormatConverter Comparison

**GlycanFormatConverter** (Shin et al., 2024):
- Python package for glycan format conversion
- Converts between IUPAC, WURCS, GlycoCT, KCF
- Does NOT generate AF3-specific BAP format

### Comparison:

| Aspect | GlycanFormatConverter | GlycoSMILES2BAP |
|--------|----------------------|-----------------|
| Format Conversion | Multiple formats | IUPAC/WURCS → CCD+BAP |
| AF3 BAP Output | No | Yes |
| Stereochemistry Validation | No | Yes (PDB validated) |
| CCD Mapping | No | Yes (28+ monosaccharides) |

## 1.3 Planned Addition to Paper

### Section: Related Work (NEW)

Add subsection: "Existing Glycan Format Tools"

```latex
\subsection{Existing Glycan Format Tools}

Several tools exist for glycan format conversion:

\textbf{GlycanFormatConverter} \citep{shin2024} provides conversion between multiple glycan formats (IUPAC, WURCS, GlycoCT, KCF). However, it does not generate AF3-specific CCD+BAP format.

\textbf{GlyLES} \citep{tiwari2024} generates language model embeddings for glycan structures. While useful for machine learning applications, it does not address AF3 input generation.

Our work differs in two key aspects: (1) we specifically target AF3-compatible CCD+BAP output, and (2) we provide explicit stereochemistry validation through PDB structure comparison.
```

### Section: Results (NEW Table)

Add comparison table:

```latex
\begin{table}[h]
\centering
\caption{Comparison with Existing Glycan Tools}
\begin{tabular}{lccc}
\toprule
Feature & GlyLES & GlycanFormatConverter & Ours \\
\midrule
Format Conversion & Yes & Yes & Yes \\
AF3 BAP Output & No & No & Yes \\
Stereochemistry Validation & No & No & Yes (PDB) \\
CCD Mapping & No & No & Yes (28+) \\
Anomeric Position Tracking & No & No & Yes \\
\bottomrule
\end{tabular}
\label{tab:tool_comparison}
\end{table}
```

---

# PART 2: PDB Validation Expansion Plan

## 2.1 Current PDB Validation (n=4)

| PDB | Structure | Key Test |
|-----|-----------|----------|
| 5NSC | Fucosylated | L-configuration |
| 1L6R | Lactose | Epimer distinction |
| 2VXR | Sialyllactose | C2 anomeric |
| 5K65 | M3 N-glycan | Branch topology |

## 2.2 Proposed Additional Structures

### Selection Criteria:
1. Cover additional stereochemistry challenges
2. Include diverse glycan types
3. Have verified correct structures in PDB
4. Represent