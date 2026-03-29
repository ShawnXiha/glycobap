# GlycoSMILES2BAP: An Automated Pipeline for Stereochemistry-Preserving Glycan Structure Prediction with AlphaFold 3

## Authors
**Qiang Xia**
Zhejiang Xinghe Tea Technology Co., Ltd., Hangzhou, Zhejiang, China
*Corresponding author: xiaqiang@xinghetea.com

---

## Abstract

**Motivation:** AlphaFold 3 (AF3) has revolutionized protein structure prediction and expanded capabilities to include glycan ligands. However, recent work by Huang et al. (2025) identified a critical limitation: standard input formats (SMILES, userCCD) produce stereochemically incorrect glycan structures, while the stereochemistry-preserving CCD+bondedAtomPairs (BAP) format requires impractical manual atom-by-atom specification.

**Results:** We present GlycoSMILES2BAP, an automated pipeline that converts standard glycan notations (IUPAC-condensed, WURCS) to AF3-compatible CCD+BAP format. The pipeline integrates three core modules: (1) a CCD mapper supporting 28+ monosaccharide configurations, (2) a topology parser extracting linkage information, and (3) a BAP generator producing explicit atom-pair bond specifications. Validated on an expanded benchmark of 1,000 representative glycan structures from the GlyTouCan database, GlycoSMILES2BAP achieves 97.8% epimer accuracy, 97.4% anomeric accuracy, and 95.9% linkage accuracy compared to ~60% for SMILES-based approaches, with processing time <1 second per structure versus 30-60 minutes for manual specification.

**Availability:** Open-source implementation available at https://github.com/ShawnXiha/glycobap

**Contact:** xiaqiang@xinghetea.com

**Keywords:** AlphaFold 3, glycans, stereochemistry, structure prediction, CCD, bondedAtomPairs

---

## 1. Introduction

Glycans are essential biological molecules involved in protein folding, cell signaling, immune recognition, and pathogen interaction [1]. Over 50% of human proteins undergo glycosylation, making accurate glycan structure prediction crucial for understanding biological mechanisms and developing therapeutics [2]. GlyTouCan, the international glycan structure repository, catalogs over 200,000 unique glycan structures [5], highlighting the scale of structural diversity that researchers need to navigate.

AlphaFold 3 (AF3) represents a breakthrough in biomolecular structure prediction, achieving unprecedented accuracy for protein-ligand complexes including glycans [3]. This advancement has generated considerable excitement in the glycobiology community.

### 1.1 The Stereochemistry Problem

Huang et al. (2025) demonstrated that AF3's standard input formats fail to preserve glycan stereochemistry [4]:
- **SMILES format:** ~62% accuracy, epimer confusion (Gal→Glc)
- **userCCD format:** ~82% accuracy, linkage position errors  
- **CCD+BAP format:** ~100% accuracy, but requires 30-60 min manual specification

### 1.2 Our Contribution

GlycoSMILES2BAP bridges the gap between standard glycan notations and AF3's stereochemistry-preserving input format, enabling automated conversion from IUPAC/WURCS to CCD+BAP.

---

## 2. Methods

### 2.1 Pipeline Architecture

```
Input: Glycan notation (IUPAC-condensed / WURCS)
↓
[Parser] → Abstract Syntax Tree (AST)
↓
[CCD Mapper] → Chemical Component Dictionary codes
↓
[BAP Generator] → bondedAtomPairs specification
↓
Output: AF3-compatible JSON input
```

### 2.2 CCD Mapper Module

Supports 28+ monosaccharide configurations with key design decisions:
- Case-insensitive matching
- Anomeric position tracking (C1 for aldoses, C2 for ketoses/sialic acids)
- Ring oxygen positions (O4 for pentoses, O5 for hexoses, O6 for sialic acids)

### 2.3 BAP Generator Module

**Branch Topology Resolution:** For complex branched glycans (e.g., bi-antennary N-glycans), the BAP generator employs a **depth-first search (DFS)** algorithm to traverse the AST and systematically generate all bond pairs. The DFS traversal proceeds from the reducing end toward non-reducing ends, ensuring complete coverage of all glycosidic linkages.

**Algorithmic complexity:** O(n) time complexity, O(d) space complexity where d is maximum tree depth.

### 2.4 Computational Environment

All benchmark measurements conducted on:
- Intel Core i7-10700 CPU @ 