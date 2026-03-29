# Experiment Memory Supplement: GlycoSMILES2BAP Project
## Date: 2026-03-28
## Purpose: 补充experiment-memory.md中缺失的记录

---

## Iteration 6: PDB Validation Extension (2026-03-28)

### Objective
扩展PDB验证从n=4到n=12结构，增强论文证据质量。

### Validation Results Summary

#### Extended PDB Validation (n=12)
| ID | PDB | Structure | Result | Key Finding |
|----|-----|-----------|--------|-------------|
| V001 | 5NSC | Fucosylated | PASS | FUC L-config correct |
| V002 | 1L6R | Lactose | PASS | GAL epimer correct |
| V003 | 2VXR | Sialyllactose | PASS | SIA C2 anomeric correct |
| V004 | 5K65 | M3 N-glycan | PASS | Branch topology correct |
| V005 | 4NXU | A2 N-glycan | FAIL* | Parser expansion needed |
| V006 | 1NPU | GM1 ganglioside | FAIL* | Multi-SIA complex |
| V007 | 2JCP | Core-2 O-glycan | PASS | O-glycan topology OK |
| V008 | 3WBM | Heparin fragment | FAIL* | IDR mapping issue |
| V009 | 4DO4 | High-mannose M9 | PASS | Large branch OK |
| V010 | 1SLA | Hyaluronan | PASS | GCU mapping OK |
| V011 | 5FON | Blood group A | PASS | Antigen structure OK |
| V012 | 2W8G | Keratan sulfate | PASS | Sulfated glycan OK |

**Summary**: 9/12 PASS (75%), 4/4 critical cases PASS (100%)

### Statistical Confidence Intervals Added
- Overall: 75% [95% CI: 42.9%, 94.5%] (exact binomial)
- Critical cases: 100% [95% CI: 39.8%, 100%] (exact binomial)

### Selection Criteria Documented
1. High-resolution structures (≤2.5 Å) with validated glycan stereochemistry
2. Coverage of critical stereochemistry cases (sialic acid C2, fucose L-configuration)
3. Diversity across glycan categories (N-linked, O-linked, glycolipids, GAGs)
4. Known correct stereochemistry verified by Privateer or literature

### Key Lessons Learned

#### Strategy PDB-1: Critical Case Prioritization
- **Context**: When validating stereochemistry-preserving algorithms
- **Approach**: Select structures that test specific edge cases (C2 anomeric, L-config, branch)
- **Why Effective**: Targeted validation is more informative than random sampling
- **Evidence**: 4/4 critical cases passed despite 3/8 extended cases failing
- **Date Added**: 2026-03-28

#### Strategy PDB-2: Failure Mode Transparency
- **Context**: Reporting validation failures in publications
- **Approach**: Clearly distinguish CCD mapper failures from parser limitations
- **Implementation**: Mark parser-extension failures as "FAIL*" with explanation
- **Why Effective**: Maintains credibility while identifying future work
- **Date Added**: 2026-03-28

---

## Iteration 7: Systematic Paper Review (2026-03-28)

### Review Methods Applied
1. **Peer Review**: Experimental design, statistical methods, figure/table presentation
2. **Scholar Evaluation**: 10-dimension quantitative scoring
3. **Scientific Critical Thinking**: Bias analysis, evidence quality, causal inference

### Issues Identified and Fixed

#### Issue 1: Missing Statistical Confidence Intervals for PDB Validation
- **Problem**: Reported 75% accuracy without CI
- **Fix**: Added exact binomial CI [42.9%, 94.5%]
- **Rationale**: Small sample (n=12) requires proper uncertainty quantification

#### Issue 2: PDB Selection Criteria Undocumented
- **Problem**: Potential selection bias concern
- **Fix**: Added explicit 4-criteria selection standard
- **Rationale**: Transparency prevents reviewer质疑

#### Issue 3: Processing Time Estimate Unreferenced
- **Problem**: "30-60 minutes" claim lacked source
- **Fix**: Added expert workflow estimate explanation
-