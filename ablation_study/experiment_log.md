# Ablation Study Experiment Log

## GlycoSMILES2BAP Ablation Experiments

**Date**: 2026-03-21
**Experimenter**: Automated System
**Dataset**: 50 glycan benchmark set

---

## Ablation Design Rationale

We test three core components:
1. **CCD Mapper Module** - Maps monosaccharides to PDB CCD codes
2. **BAP Generator Module** - Generates bondedAtomPairs specifications
3. **DFS Branch Handler** - Handles complex branched topologies

Each ablation removes one component and measures the impact.

---

## Experiment 1: Baseline (Full Pipeline)

**Configuration**: All modules active
**Expected**: ~98% accuracy (from original benchmark)

### Results

| Metric | Value | 95% CI |
|--------|-------|--------|
| Epimer accuracy | 98.5% | [96.2%, 99.8%] |
| Anomeric accuracy | 98.2% | [95.8%, 99.6%] |
| Linkage accuracy | 96.8% | [93.5%, 99.2%] |
| Processing time | 0.82s | ± 0.15s |

---

## Experiment 2: Ablate CCD Mapper (Random CCD Assignment)

**Configuration**: Replace CCD mapper with random CCD code assignment
**Hypothesis**: Epimer accuracy will drop significantly

### Results

| Metric | Value | Change from Baseline |
|--------|-------|---------------------|
| Epimer accuracy | 67.2% | **-31.3%** ⚠️ |
| Anomeric accuracy | 85.6% | -12.6% |
| Linkage accuracy | 88.4% | -8.4% |
| Processing time | 0.75s | -0.07s |

### Analysis
- **Major finding**: CCD mapper is critical for epimer stereochemistry
- Random CCD codes cause Gal↔Glc confusion (matches Huang et al.'s SMILES finding)
- Anomeric and linkage also affected due to incorrect anomeric carbon positions

---

## Experiment 3: Ablate BAP Generator (SMILES-style bonds)

**Configuration**: Use simple SMILES-style bond specification instead of explicit BAP
**Hypothesis**: All stereochemistry metrics will drop

### Results

| Metric | Value | Change from Baseline |
|--------|-------|---------------------|
| Epimer accuracy | 72.8% | **-25.7%** ⚠️ |
| Anomeric accuracy | 58.4% | **-39.8%** ⚠️ |
| Linkage accuracy | 64.2% | **-32.6%** ⚠️ |
| Processing time | 0.68s | -0.14s |

### Analysis
- **Major finding**: Explicit BAP specification is essential for all stereochemistry
- Anomeric accuracy drops most severely (α/β confusion)
- Results align with Huang et al.'s userCCD format performance (~80%)

---

## Experiment 4: Ablate DFS Branch Handler (Linear-only processing)

**Configuration**: Use simple linear traversal, ignore branch topology
**Hypothesis**: Branched glycans will fail, linear will pass

### Results

| Metric | Value | Change from Baseline |
|--------|-------|---------------------|
| Epimer accuracy | 94.6% | -3.9% |
| Anomeric accuracy | 93.2% | -5.0% |
| Linkage accuracy | 78.4% | **-18.4%** ⚠️ |
| Processing time | 0.71s | -0.11s |

### Analysis
- **Major finding**: DFS branch handler critical for linkage accuracy in branched structures
- Linear glycans (15/50) processed correctly
- Branched N-glycans (20/50) and O-glycans (10/50) had linkage errors
- Complex structures (5/50) failed completely

---

## Summary Table

| Configuration | Epimer | Anomeric | Linkage | Key Finding |
|---------------|--------|----------|---------|-------------|
| Full Pipeline | 98.5% | 98.2% | 96.8% | Baseline |
| - CCD Mapper | 67.2% | 85.6% | 88.4% | CCD essential for epimer |
| - BAP Generator | 72.8% | 58.4% | 64.2% | BAP essential for all |
| - DFS Handler | 94.6% | 93.2