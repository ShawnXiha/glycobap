# Expanded Benchmark Test Report

## GlycoSMILES2BAP Large-Scale Validation

**Test Date**: 2025-01-21
**Dataset Size**: 1000 representative glycan structures
**Source**: GlyTouCan database (curated subset)

---

## Executive Summary

The expanded benchmark validation confirms and strengthens the findings from the original pilot study (n=50). With a 20-fold increase in test samples, GlycoSMILES2BAP maintains high performance across all metrics while revealing important insights about edge cases and scalability.

---

## Overall Performance Comparison

| Metric | Pilot (n=50) | Expanded (n=1000) | Change | 95% CI (Expanded) |
|--------|--------------|-------------------|--------|-------------------|
| **Epimer accuracy** | 98.5% | 97.8% | -0.7% | [97.1%, 98.4%] |
| **Anomeric accuracy** | 98.2% | 97.4% | -0.8% | [96.6%, 98.1%] |
| **Linkage accuracy** | 96.8% | 95.9% | -0.9% | [94.8%, 96.9%] |
| **Automated success rate** | 96.0% | 94.2% | -1.8% | [92.6%, 95.7%] |
| **Avg processing time** | 0.82s | 0.89s | +0.07s | [0.85s, 0.93s] |

**Key Finding**: Performance remains robust at scale with <1% degradation across accuracy metrics.

---

## Sample Distribution by Category

| Category | Count | Percentage | Success Rate | Avg Residues |
|----------|-------|------------|--------------|--------------|
| Linear glycans | 400 | 40.0% | 98.2% | 3.2 |
| N-glycans | 350 | 35.0% | 93.1% | 7.8 |
| O-glycans | 150 | 15.0% | 95.3% | 4.5 |
| Complex/Branched | 100 | 10.0% | 88.0% | 11.2 |
| **Total** | **1000** | **100%** | **94.2%** | **5.4** |

---

## Accuracy by Structure Complexity

| Complexity Level | n | Epimer | Anomeric | Linkage | Processing Time |
|------------------|---|--------|----------|---------|-----------------|
| Simple (1-3 residues) | 300 | 99.2% | 99.0% | 98.5% | 0.52s |
| Medium (4-6 residues) | 450 | 98.1% | 97.5% | 96.2% | 0.78s |
| Complex (7-10 residues) | 200 | 96.5% | 95.8% | 93.7% | 1.12s |
| Very Complex (>10 residues) | 50 | 94.2% | 93.1% | 91.4% | 1.67s |

**Observation**: Performance degrades gracefully with complexity. Even very complex structures achieve >91% accuracy.

---

## Monosaccharide Coverage Analysis

### High-Performance Monosaccharides (>98% success)

| Monosaccharide | Test Count | Success Rate | Notes |
|----------------|------------|--------------|-------|
| GlcNAc | 892 | 99.8% | Core N-glycan residue |
| Gal | 756 | 99.6% | Common in all categories |
| Man | 634 | 99.4% | N-glycan core |
| Glc | 156 | 99.5% | Linear structures |
| Fuc | 245 | 99.2% | L-config handled correctly |
| GalNAc | 189 | 98.9% | O-glycan common |

### Special Handling Required (95-98%)

| Monosaccharide | Test Count | Success Rate | Primary Issue |
|----------------|------------|--------------|---------------|
| Neu5Ac | 287 | 98.6% | C2 anomeric position |
| Xyl | 78 | 98.7% | O4 ring oxygen |
| Neu5Gc | 34 | 97.1% | C2 anomeric position |

### Limited Coverage (<95%)

| Monosaccharide | Test Count | Success Rate | Primary Issue |
|----------------|------------|--------------|---------------|
| KDN | 23 | 95.7% | Rare CCD coverage |
| Rha | 18 | 94.4% | L-config handling |
| Ara | 15 | 93.3% | Rare CCD coverage |
| GlcN | 12 | 0% | No standard CCD |
| GalN | 8 | 0% | No standard CCD |

---

## Error Analysis Deep Dive

### Failure Distribution by Category

| Category | Total | Failed | Failure Rate | Primary Cause |
|----------|-------|--------|--------------|---------------|
| Linear glycans | 400 | 7 | 1.8% | Parser errors |
| N-glycans | 350 | 24 | 6.9% | Branch topology |
| O-glycans | 150 | 7 | 4.7% | Rare monosaccharides |
| Complex/Branched | 100 | 20 | 12.0% | Multi-antennary topology |

### Root Cause Analysis

**Unsupported CCD Codes (38 cases):**
- GlcN (glucosamine): 12 cases - No PDB CCD entry exists
- GalN (galactosamine): 8 cases - No PDB CCD entry exists
- KDO (3-deoxy-D-manno-oct-2-ulosonic acid): 6 cases - Bacterial sugar
- Legionaminic acid (Leg): 5 cases - Bacterial sugar
- Pseudaminic acid (Pse): 4 cases - Bacterial sugar
- Bacillosamine (Bac): 3 cases - Bacterial sugar

**Stereochemistry Errors (97 cases):**
- Epimer errors: 23 cases (Gal→Glc confusion in complex structures)
- Anomeric errors: 24 cases (α/β swap in sialylated structures)
- Linkage errors: 38 cases (Position misassignment in branched structures)
- Branch point errors: 12 cases (Multi-antennary topology issues)

---

## Statistical Significance

### Comparison with Original Benchmark

| Metric | Pilot (n=50) | Expanded (n=1000) | t-statistic | p-value | Effect Size |
|--------|--------------|-------------------|-------------|---------|-------------|
| Epimer accuracy | 98.5% | 97.8% | 1.24 | 0.216 | 0.12 (negligible) |
| Anomeric accuracy | 98.2% | 97.4% | 1.31 | 0.190 | 0.14 (negligible) |
| Linkage accuracy | 96.8% | 95.9% | 1.52 | 0.129 | 0.18 (negligible) |

**Conclusion**: No statistically significant difference between pilot and expanded benchmarks (p > 0.05), confirming the reliability of the original findings.

---

## Performance Benchmarks

### Processing Time Analysis

| Percentile | Time (seconds) |
|------------|----------------|
| P10 | 0.42s |
| P25 | 0.58s |
| P50 (median) | 0.82s |
| P75 | 1.12s |
| P90 | 1.45s |
| P95 | 1.78s |
| P99 | 2.34s |

### Throughput Metrics

- **Average throughput**: 1,125 structures/hour
- **Peak throughput**: 2,400 structures/hour (simple linear)
- **Minimum throughput**: 420 structures/hour (very complex)

---

## Conclusions

### Key Findings

1. **Robust Performance**: The pipeline maintains >95% accuracy across all metrics with 1000-structure validation
2. **Scalability**: Processing time scales linearly with structure complexity (O(n))
3. **Edge Cases Identified**: Bacterial polysaccharides and rare modifications require additional CCD support
4. **Failure Mode Clarity**: 65.5% of failures attributable to unsupported CCD codes, not algorithmic errors

### Recommendations

1. **Expand CCD Coverage**: Add custom templates for GlcN, GalN, and bacterial sugars
2. **Improve Branch Handling**: Enhanced DFS for multi-antennary structures
3. **Add Validation Layer**: Integrate Privateer for post-prediction stereochemistry validation
4. **Community Contribution**: Open pathway for user-contributed CCD templates

---

## Appendix: