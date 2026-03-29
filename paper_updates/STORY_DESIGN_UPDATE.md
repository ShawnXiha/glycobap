# Story Design Update - March 2026

## New Validation Results Integration

### Original Story Arc
1. **Problem**: AF3 glycan modeling has stereochemistry accuracy problem
2. **Solution**: GlycoSMILES2BAP automated pipeline
3. **Validation**: Benchmark testing + case studies

### Updated Story Arc (with PDB Validation)

1. **Problem**: AF3 glycan modeling has stereochemistry accuracy problem
   - SMILES format: ~60% accuracy
   - Manual BAP: 30-60 minutes per structure
   - Key issue: Sialic acid anomeric position (C2 vs C1)

2. **Solution**: GlycoSMILES2BAP automated pipeline
   - CCD Mapper: 28+ monosaccharide configurations
   - Anomeric tracking: C2 for ketoses, C1 for aldoses
   - Ring oxygen: O4/O5/O6 for different sugar types

3. **Validation** (EXPANDED):
   - **Benchmark**: 50 diverse glycans (97.8% accuracy)
   - **Ablation**: Systematic module testing
   - **NEW: PDB Structure Validation**: 4 critical test cases
     - V001: Fucosylated (5NSC) - FUC alpha-L
     - V002: Lactose (1L6R) - GAL beta-D
     - V003: Sialyllactose (2VXR) - SIA C2 anomeric (CRITICAL)
     - V004: M3 N-glycan (5K65) - Branch topology
   - **Result**: 4/4 PASSED (100%)

### Key Narrative Enhancement

#### Critical Test: Sialic Acid C2 Anomeric
- **Why Critical**: Sialic acids are ketoses (anomeric at C2, not C1)
- **SMILES Failure**: Places anomeric bond at C1 (incorrect)
- **Our Success**: Correctly identifies C2 as anomeric position
- **Validation**: PDB:2VXR confirms SIA with C2 anomeric

#### Literature Connection
- Huang et al. (2025): Documented ~60% SMILES accuracy
- Frenz et al. (2018): PDB:5NSC wrong anomer case
- Jo et al. (2011): PDB:5K65 missing linkage case
- Our tool corrects all documented errors

### Updated Evidence Chain

| Claim | Evidence | Source |
|-------|----------|--------|
| High epimer accuracy | 98.5% on 50 structures | Benchmark |
| High anomeric accuracy | 97.4% on 50 structures | Benchmark |
| C2 handling correct | SIA → C2, O6 | PDB:2VXR validation |
| Fucose L-config correct | FUC → alpha-L | PDB:5NSC validation |
| Branch handling correct | All CCD codes match | PDB:5K65 validation |
| Error correction | 10/10 cases | Literature errors |

### Paper Section Updates Required

1. **Methods**: Add PDB validation methodology
2. **Experiments**: Add PDB validation results table
3. **Related Work**: Add comparison with validation approaches
4. **Abstract**: Add PDB validation mention
5. **Title**: Consider emphasizing stereochemistry validation

### Key Messages for Each Section

#### Methods (New Subsection)
- PDB structure validation methodology
- Test case selection rationale
- Comparison approach (CCD codes, anomeric positions, ring oxygens)

#### Experiments (New Results)
- Table: PDB Validation Results (4 test cases)
- Discussion of critical SIA C2 test
- Connection to literature error cases

#### Related Work
- Comparison with Privateer validation tool
- PDB structure validation approaches
- Limitations of AF Server for glycan validation

#### Abstract
- Add: "Validated against known PDB structures including critical sialic acid test"
- Emphasize: C2 anomeric position handling

#### Title
- Current: "GlycoSMILES2BAP: An Automated Pipeline for Stereochemistry-Preserving Glycan Structure Prediction with AlphaFold 3"
- Consider: Add "validation" or "verification" element
