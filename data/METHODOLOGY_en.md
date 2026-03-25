# Data Processing and Analysis Methodology

## GlycoSMILES2BAP Project

**Version**: 1.0  
**Date**: 2026-03-21  
**Author**: Qiang Xia

---

## 1. Overview

This document describes the data processing and analysis methods used in the GlycoSMILES2BAP project. The methodology covers benchmark construction, accuracy evaluation, ablation studies, and statistical analysis.

---

## 2. Benchmark Dataset Construction

### 2.1 Data Sources

The benchmark dataset was constructed from multiple sources:

| Source | Description | Count |
|--------|-------------|-------|
| GlyTouCan Database | International glycan structure repository | 25 structures |
| Literature Examples | Published glycan structure cases | 15 structures |
| Common Glycans | Standard mammalian glycans | 10 structures |

### 2.2 Category Distribution

Benchmark structures were categorized as follows:

```
Category          Count   Percentage
---------------------------------------
Linear glycans    15      30%
N-glycans         20      40%
O-glycans         10      20%
Complex           5       10%
---------------------------------------
Total             50      100%
```

### 2.3 Selection Criteria

Structures were selected based on:
1. **Diversity**: Covering major glycan categories
2. **Complexity**: Including branching and sialylation
3. **Relevance**: Common in biological systems
4. **Validation**: Known correct structures available

---

## 3. Accuracy Evaluation Methods

### 3.1 Epimer Accuracy

**Definition**: Ratio of correctly identified monosaccharide residues to total residues.

**Formula**:
$$\text{Epimer Accuracy} = \frac{\text{Correctly identified residues}}{\text{Total residues}}$$

**Evaluation Process**:
1. Parse input glycan notation
2. Generate CCD codes for each residue
3. Compare generated CCD codes against reference
4. Calculate accuracy per structure
5. Aggregate across benchmark

### 3.2 Anomeric Accuracy

**Definition**: Ratio of linkages with correct anomeric configuration to total linkages.

**Formula**:
$$\text{Anomeric Accuracy} = \frac{\text{Linkages with correct anomeric configuration}}{\text{Total linkages}}$$

**Special Handling**:
- Aldoses: Anomeric carbon at C1
- Ketoses (Neu5Ac, Neu5Gc, KDN): Anomeric carbon at C2

### 3.3 Linkage Accuracy

**Definition**: Ratio of linkages with correct donor-acceptor positions to total linkages.

**Formula**:
$$\text{Linkage Accuracy} = \frac{\text{Linkages with correct positions}}{\text{Total linkages}}$$

**Validation Criteria**:
1. Donor anomeric carbon matches expected position
2. Acceptor oxygen matches linkage position
3. Residue indices reflect correct topology

---

## 4. Ablation Study Design

### 4.1 Ablation Configurations

| Configuration | Description |
|---------------|-------------|
| Full Pipeline | Complete pipeline with all modules |
| w/o CCD Mapper | CCD Mapper module disabled |
| w/o Anomeric Tracking | Anomeric position tracking disabled |
| w/o Branch Handling | Branch topology handling disabled |
| CCD Mapper Only | Only CCD mapping, no BAP generation |

### 4.2 Testing Protocol

1. **Subset Selection**: 20 representative structures from benchmark
2. **Module Isolation**: Each module tested independently
3. **Metric Collection**: All three accuracy metrics recorded
4. **Statistical Testing**: Paired t-tests for significance

### 4.3 Module Contribution Calculation

$$\Delta_{\text{module}} = \text{Accuracy}_{\text{full}} - \text{Accuracy}_{\text{ablated}}$$

---

## 5. Statistical Analysis Methods

### 5.1 Confidence Intervals

95% confidence intervals calculated using:
$$\text{CI} = \bar{x} \pm t_{\alpha/2, n-1} \times \frac{s}{\sqrt{n}}$$

Where:
- $\bar{x}$ = sample mean
- $s$ = sample standard deviation
- $n$ = sample size
- $t_{\alpha/2, n-1}$ = t-critical value

### 5.2 Effect Size

Cohen's d calculated as:
$$d = \frac{\bar{x}_1 - \bar{x}_2}{s_{\text{pooled}}}$$

Where:
$$s_{\text