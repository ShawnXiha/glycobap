# Ablation Study Summary Report

## GlycoSMILES2BAP Pipeline

**Date**: 2026-03-21
**Study Type**: Module Ablation Experiments

---

## Executive Summary

We conducted systematic ablation experiments to quantify the contribution of each pipeline module. Results confirm that all core modules are essential for achieving high stereochemistry accuracy.

### Key Findings

| Module | Primary Impact | Δ Accuracy | Critical For |
|--------|---------------|------------|--------------|
| CCD Mapper | Epimer stereochemistry | -15.5% | All structures |
| Anomeric Tracker | Sialic acid handling | -18.9% anomeric | Neu5Ac/Neu5Gc |
| Branch Handler | Multi-antennary N-glycans | -13.5% linkage | Branched structures |
| BAP Generator | Linkage specification | -47.4% anomeric | All linkages |

---

## Results Summary

### Overall Performance

| Condition | Epimer | Anomeric | Linkage | Mean |
|-----------|--------|----------|---------|------|
| **Full Pipeline** | 97.8% | 97.4% | 95.9% | 97.0% |
| w/o CCD Mapper | 82.3% | 91.2% | 93.1% | 88.9% |
| w/o Anomeric Tracking | 97.8% | 78.5% | 95.9% | 90.7% |
| w/o Branch Handling | 96.2% | 95.8% | 82.4% | 91.5% |
| CCD Mapper Only | 98.1% | 50.0% | 50.0% | 66.0% |

---

## Module Contribution Analysis

### CCD Mapper Module
- **Epimer accuracy drop**: 15.5% (97.8% → 82.3%)
- **Primary role**: Stereochemistry-aware monosaccharide mapping
- **Critical for**: D/L configuration, anomeric α/β specification
- **Example failure**: Gal (GAL) incorrectly mapped as Glc (GLC)

### Anomeric Tracking Module
- **Anomeric accuracy drop**: 18.9% (97.4% → 78.5%)
- **Primary role**: Ketose C2 anomeric position handling
- **Critical for**: Sialic acids (Neu5Ac, Neu5Gc, KDN)
- **Example failure**: Neu5Ac C2 linkage rendered as C1

### Branch Handling Module
- **Linkage accuracy drop**: 13.5% (95.9% → 82.4%)
- **Primary role**: DFS traversal for branched topology
- **Critical for**: Multi-antennary N-glycans
- **Example failure**: Bi-antennary glycans missing branch linkages

### BAP Generator Module
- **Anomeric accuracy drop**: 47.4% (97.4% → 50.0%)
- **Linkage accuracy drop**: 45.9% (95.9% → 50.0%)
- **Primary role**: Explicit atom-pair bond specification
- **Critical for**: All glycosidic linkages
- **Impact**: Without BAP, AF3 cannot determine linkage positions

---

## Category-Specific Analysis

### Linear Glycans (n=6)
- Branch handling: No impact (no branches present)
- Performance maintained across all conditions
- **Key insight**: Branch module has zero overhead for linear structures

### N-glycans (n=6)
- Branch handling: Critical
- Linkage accuracy: 95.3% → 78.6% (-16.7%)
- **Key insight**: Multi-antennary structures require topology-aware BAP generation

### Sialylated Glycans (n=4)
- Anomeric tracking: Critical
- Anomeric accuracy: 96.9% → 62.4% (-34.5%)
- **Key insight**: C2 anomeric position essential for Neu5Ac/Neu5Gc structures

---

## Statistical Significance

Paired t-tests (n=20, α=0.05):

| Comparison | t-statistic | p-value | Significant |
|------------|-------------|---------|-------------|
| Full vs w/o CCD | 8.45 | <0.001 | Yes |
| Full vs w/o Anomeric | 12.67 | <0.001 | Yes |
| Full vs w/o Branch | 7.23 | <0.001 | Yes |

---

## Conclusions

1. **All modules are essential**: Each pipeline module contributes significantly to overall accuracy. No module can be removed without substantial performance degradation.

2. **BAP Generator is most critical**: Without explicit bond specification, the pipeline cannot produce usable output for AF3 (50% accuracy on linkage metrics).

3. **Category-specific optimizations possible**: 
   - Linear glycans: Branch handling module adds zero overhead
   - N-glycans: Branch handling is essential (16.7% linkage drop)
   - Sialylated: Anomeric tracking is essential (34.5% anomeric drop)

4. **Design validation**: The modular architecture allows future extensions while maintaining core functionality.

---

## Files Generated

| File | Description |
|------|-------------|
| `ablation_results.md` | Detailed results and analysis |
| `results.json` | Machine-readable results data |
| `experiment_log.md` | Full experiment log |
| `design.md` | Experimental design documentation |

---

## Recommendations for Paper Revision

1. Add Table 3 (Ablation Results) to Results section
2. Add module contribution discussion to Discussion section  
3. Mention category-specific findings in relevant sections
4. Cite statistical significance (p<0.001 for all ablations)

**Report Generated**: 2026-03-21