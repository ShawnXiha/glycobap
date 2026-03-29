# Complete Paper Extension Plan

## Date: 2026-03-28
## Purpose: Address Scholar-Evaluation and Scientific-Critical-Thinking findings

---

# PART 1: GlyLES and Existing Tools Comparison

## 1.1 Tools to Compare

| Tool | Purpose | AF3 Compatible | Stereochemistry Validation |
|------|---------|----------------|---------------------------|
| GlyLES (Tiwari 2024) | Glycan embeddings | No | No |
| GlycanFormatConverter (Shin 2024) | Format conversion | No | No |
| Privateer (Agirre 2023) | PDB validation | No | Yes (validation only) |
| **GlycoSMILES2BAP** | AF3 input generation | Yes | Yes (PDB validated) |

## 1.2 Key Differentiators

1. **Purpose**: GlyLES generates embeddings; we generate AF3-compatible input
2. **Stereochemistry**: We explicitly track anomeric positions (C1 vs C2)
3. **Validation**: We provide PDB-validated stereochemistry handling
4. **Output**: Only our tool produces CCD+BAP format for AF3

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
1. Extract IUPAC notation from PDB structure annotations
2. Run GlycoSMILES2BAP to generate CCD codes
3. Compare with PDB-deposited CCD codes
4. Verify anomeric positions match crystallographic data
5. Document any discrepancies

---

# PART 3: Paper Modification Tasks

## Task 1: Update Introduction

Add after first paragraph:
```latex
Several tools address glycan format conversion. GlycanFormatConverter 
\citep{shin2024} provides conversion between IUPAC, WURCS, GlycoCT, and KCF 
formats. GlyLES \citep{tiwari2024} generates language model embeddings for 
glycan structures. However, neither tool addresses AF3-specific CCD+BAP 
input generation with stereochemistry validation.
```

## Task 2: Add Related Work Section

```latex
\subsection{Related Tools}

\textbf{GlycanFormatConverter} \citep{shin2024} provides format conversion 
for multiple glycan notations but does not generate AF3-specific output.

\textbf{GlyLES} \citep{tiwari2024} generates machine learning embeddings 
for glycans but targets different applications.

\textbf{Privateer} \citep{agirre2023} validates glycan stereochemistry 
in PDB structures but does not generate input for structure prediction.

Our work complements these tools by providing AF3-specific CCD+BAP 
generation with stereochemistry validation.
```

## Task 3: Add Comparison Table

```latex
\begin{table}[h]
\centering
\caption{Comparison with Existing Glycan Tools}
\begin{tab