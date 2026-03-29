# Paper Extension Final Plan

## Based on Scholar-Evaluation & Critical-Thinking Analysis

**Date**: 2026-03-28
**Goal**: Address two critical gaps identified in review

---

# PART 1: GlyLES & Existing Tools Comparison

## 1.1 Tools to Compare

| Tool | Reference | Purpose | AF3 Output |
|------|-----------|---------|------------|
| GlyLES | Tiwari et al. 2024 | Glycan embeddings | No |
| GlycanFormatConverter | Shin et al. 2024 | Format conversion | No |
| Privateer | Agirre et al. 2023 | Validation only | No |
| GlycoSMILES2BAP | This work | AF3 input generation | Yes |

## 1.2 Key Differentiators

1. **AF3 Compatibility**: Only our tool generates CCD+BAP format
2. **Stereochemistry Focus**: Explicit C1 vs C2 anomeric tracking
3. **PDB Validation**: 100% on critical test cases

## 1.3 Paper Addition: Related Work Section

Add new subsection after Introduction:

```latex
\subsection{Existing Glycan Format Tools}

Several tools address glycan format conversion:

\textbf{GlycanFormatConverter} \citep{shin2024} provides conversion between IUPAC, WURCS, GlycoCT, and KCF formats. However, it does not generate AF3-specific CCD+BAP output.

\textbf{GlyLES} \citep{tiwari2024} generates language model embeddings for glycan structures, useful for machine learning applications but not designed for AF3 input.

\textbf{Privateer} \citep{agirre2023} validates glycan stereochemistry in PDB structures but does not generate input formats.

Our work differs in three aspects: (1) AF3-specific CCD+BAP output, (2) explicit stereochemistry validation, and (3) anomeric position tracking as core design.
```

## 1.4 Paper Addition: Comparison Table

```latex
\begin{table}[h]
\centering
\caption{Comparison with Existing Glycan Tools}
\begin{tabular}{lcccc}
\toprule
Feature & GlyLES & GlycanFormatConverter & Privateer & Ours \\
\midrule
Format Conversion & Yes & Yes & No & Yes \\
AF3 BAP Output & No & No & No & Yes \\
Stereochemistry Validation & No & No & Yes & Yes \\
CCD Mapping & No & No & No & Yes \\
Anomeric Tracking & No & No & Partial & Yes \\
Processing Time & - & - & - & <1s \\
\bottomrule
\end{tabular}
\label{tab:tool_comparison}
\end{table}
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
| V005 | 4NXU | A2 N-glycan | Bi-antennary | Complex branching |
| V006 | 1NPU | GM1 ganglioside | Multiple SIA | Ketose clustering |
| V007 | 2JCP | Core-2 O-glycan | O-linked | O-glycan handling |
| V008 | 3WBM | Heparin fragment | Sulfation | Modifications |
| V009 | 4DO4 | High-mannose M9 | Large branched | Scalability |
| V010 | 1SLA | Hyaluronan | Repeating unit | Linear polymer |
| V011 | 5FON | Blood group A | Combined | Multiple challenges |
| V012 | 2W8G | Keratan sulfate | Alternating | Unusual linkage |

**Total: n=12 (original 4 + 8 new)**

## 2.3 Validation Method

For each new structure:
1. Extract IUPAC notation from PDB
2.