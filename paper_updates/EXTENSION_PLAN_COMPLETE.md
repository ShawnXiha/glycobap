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

---

# PART 2: PDB Validation Expansion Plan

## 2.1 Current PDB Validation (n=4)

| PDB | Structure | Key Test |
|-----|-----------|----------|
| 5NSC | Fucosylated | L-configuration |
| 1L6R | Lactose | Epimer distinction |
| 2VXR | Sialyllactose | C2 anomeric |
| 5K65 | M3 N-glycan | Branch topology |

## 2.2 Proposed Additional Structures (n=8 more)

### New Structures to Add:

| ID | PDB | Structure | Key Test | Reason |
|----|-----|-----------|----------|--------|
| V005 | 4NXU | A2 N-glycan | Bi-antennary topology | Complex branching |
| V006 | 1NPU | GM1 ganglioside | Multiple sialic acids | Ketose clustering |
| V007 | 2JCP | Core-2 O-glycan | O-linked specificity | O-glycan handling |
| V008 | 3WBM | Heparin disaccharide | Sulfation modification | Modified monosaccharides |
| V009 | 4DO4 | High-mannose M9 | Large branched | Scalability test |
| V010 | 1SLA | Hyaluronan fragment | Repeating disaccharide | Linear polymer |
| V011 | 5FON | Blood group A | Epimer + linkage | Combined challenges |
| V012 | 2W8G | Keratan sulfate | Gal+GlcNAc alternating | Unusual linkage |

### Total: n=12 (original 4 + 8 new)

## 2.3 Validation Method for New Structures

1. **Extract IUPAC notation** from PDB structure annotations
2. **Run GlycoSMILES2BAP** to generate CCD codes
3. **Compare with PDB-deposited CCD codes**
4. **Verify anomeric positions** match crystallographic data
5. **Document any discrepancies**

---

# PART 3: Paper Modification Plan

## 3.1 Introduction Changes

Add paragraph after line 54:

