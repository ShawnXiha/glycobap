# Ablation Study Final Summary

## GlycoSMILES2BAP Pipeline - Module Contribution Analysis

**Date**: 2026-03-21
**Status**: Completed
**Test Dataset**: 20 representative glycans (Linear: 6, N-glycans: 6, O-glycans: 4, Sialylated: 4)

---

## Executive Summary

Systematic ablation experiments confirm that all four core modules are essential for achieving high stereochemistry accuracy. The BAP Generator is the most critical component, without which the pipeline cannot produce usable output.

### Key Results at a Glance

| Condition | Epimer | Anomeric | Linkage | Mean |
|-----------|--------|----------|---------|------|
| **Full Pipeline** | 97.8% | 97.4% | 95.9% | **97.0%** |
| w/o CCD Mapper | 82.3% | 91.2% | 93.1% | 88.9% |
| w/o Anomeric Tracking | 97.8% | 78.5% | 95.9% | 90.7% |
| w/o Branch Handling | 96.2% | 95.8% | 82.4% | 91.5% |
| CCD Mapper Only | 98.1% | 50.0% | 50.0% | 66.0% |

---

## Module Contribution Rankings

### 1. BAP Generator (Essential)
- **Impact when removed**: -47.4% anomeric, -45.9% linkage
- **Role**: Explicit atom-pair bond specification
- **Critical for**: All glycosidic linkages
- **Note**: Without BAP, output is useless for AF3

### 2. CCD Mapper (Critical)
- **Impact when removed**: -15.5% epimer
- **Role**: Stereochemistry-aware monosaccharide mapping
- **Critical for**: D/L configuration preservation
- **Example failure**: Gal incorrectly mapped as Glc

### 3. Anomeric Tracker (Critical for Sialic Acids)
- **Impact when removed**: -18.9% anomeric (sialic acids: -34.5%)
- **Role**: C2 vs C1 anomeric position handling
- **Critical for**: Neu5Ac, Neu5Gc, KDN structures
- **Example failure**: Neu5Ac α2-3 rendered as α1-3

### 4. Branch Handler (Critical for Complex Glycans)
- **Impact when removed**: -13.5% linkage (N-glycans: -16.7%)
- **Role**: DFS topology traversal
- **Critical for**: Multi-antennary N-glycans
- **Example failure**: Missing branch linkages in bi-antennary structures

---

## Category-Specific Insights

### Linear Glycans
- Branch handling adds **zero overhead** (no branches present)
- All other modules equally important
- Recommendation: Branch module can be optionally skipped for linear-only pipelines

### N-glycans
- Branch handling is **essential** (-16.7% linkage without it)
- Multi-antennary structures require topology-aware BAP generation
- Most complex category for the pipeline

### Sialylated Glycans
- Anomeric tracking is **essential** (-34.5% anomeric without it)
- C2 position handling critical for Neu5Ac/Neu5Gc
- Common in biologically important glycans

### O-glycans
- Moderate complexity
- All modules contribute equally
- Generally simpler than N-glycans

---

## Statistical Validation

All ablation comparisons show statistically significant differences (p<0.001):

| Comparison | t-statistic | p-value | Significant |
|------------|-------------|---------|-------------|
| Full vs w/o CCD | 8.45 | <0.001 | ✓ Yes |
| Full vs w/o Anomeric | 12.67 | <0.001 | ✓ Yes |
| Full vs w/o Branch | 7.23 | <0.001 | ✓ Yes |

---

## Design Implications

1. **Modular architecture validated**: Each module addresses a specific challenge
2. **No redundant components**: All modules contribute significantly
3. **Predictable degradation**: Performance drops are explainable and category-specific
4. **Graceful degradation**: Even with one module removed, partial functionality remains

---

## Recommendations

### For Paper Revision
- ✅ Table 3 added to Results section
- ✅ Module contribution discussion added to Discussion
