# GlycoSMILES2BAP Dataset Documentation (English)

## Overview

This folder contains all experimental data and documentation for the GlycoSMILES2BAP project. The data supports the manuscript "GlycoSMILES2BAP: An Automated Pipeline for Stereochemistry-Preserving Glycan Structure Prediction with AlphaFold 3".

---

## Directory Structure

```
data/
├── README_en.md          # English documentation (this file)
├── README_zh.md          # Chinese documentation
├── METHODOLOGY.md        # Data processing methodology
├── raw/                  # Raw experimental data
│   ├── benchmark_dataset.csv
│   ├── benchmark_detailed.csv
│   ├── error_correction_cases.csv
│   └── glytoucan_processing.csv
└── processed/            # Processed analysis results
    ├── benchmark_results.csv
    ├── ablation_results.csv
    └── module_contributions.csv
```

---

## Dataset Descriptions

### 1. Benchmark Dataset (`raw/benchmark_dataset.csv`)

**Purpose**: Core benchmark dataset for evaluating GlycoSMILES2BAP performance.

**Contents**: 50 diverse glycan structures for systematic evaluation.

**Columns**:
| Column | Description | Type |
|--------|-------------|------|
| structure_id | Unique identifier | String |
| iupac_notation | IUPAC-condensed notation | String |
| wurcs_notation | WURCS format string | String |
| category | Structural category | String |
| residue_count | Number of monosaccharide residues | Integer |
| branch_count | Number of branches | Integer |
| has_sialic_acid | Contains Neu5Ac/Neu5Gc | Boolean |
| has_fucose | Contains fucose | Boolean |

**Categories**:
- Linear glycans (15): LNnT, LNT, maltose polymers
- N-glycans (20): M3-M9, G0-G2, fucosylated variants
- O-glycans (10): Tn, T, sialyl-T antigens
- Complex (5): Sialylated, branched, rare sugars

---

### 2. Detailed Benchmark Data (`raw/benchmark_detailed.csv`)

**Purpose**: Residue-level ground truth annotations for accuracy calculation.

**Contents**: Per-residue CCD codes and linkage specifications.

**Columns**:
| Column | Description | Type |
|--------|-------------|------|
| structure_id | Structure identifier | String |
| residue_position | Position in sequence | Integer |
| monosaccharide | Monosaccharide name | String |
| anomer | Anomeric configuration (α/β) | String |
| absolute_config | D/L configuration | String |
| ccd_code | Expected CCD code | String |
| anomeric_carbon | Anomeric carbon position | String |
| ring_oxygen | Ring oxygen position | String |
| donor_linkage | Donor linkage position | String |
| acceptor_residue | Acceptor residue position | Integer |
| acceptor_oxygen | Acceptor oxygen position | String |

---

### 3. Error Correction Cases (`raw/error_correction_cases.csv`)

**Purpose**: Literature-reported glycan structure errors for validation.

**Contents**: 10 documented error cases from structural biology publications.

**Columns**:
| Column | Description | Type |
|--------|-------------|------|
| case_id | Case identifier | Integer |
| pdb_id | PDB structure ID | String |
| error_type | Error classification | String |
| source_publication | Literature reference | String |
| pmid | PubMed ID | String |
| resolution_angstrom | Crystal resolution | Float |
| original_error | Error description | String |
| correct_structure | Correct specification | String |
| glycosmiles2bap_correction | Tool-generated correction | String |
| validation_status | Correction verified | Boolean |

**Error Types**:
- Anomeric errors (4): α/β configuration errors
- Epimer errors (2): Stereochemistry inversion at C4
- Linkage errors (3): Missing or incorrect glycosidic bonds
- Conformation errors (1): High-energy ring conformations

---

### 4. GlyTouCan Processing Data (`raw/glytoucan_processing.csv`)

**Purpose**: Database-scale processing results.

**Contents**: 100 representative GlyTouCan structures with processing outcomes.

**Columns**:
| Column | Description | Type |
|--------|-------------|------|
| glytoucan_id | GlyTouCan accession ID | String |
| iupac_notation | IUPAC-condensed notation | String |
| category | Structure category | String |
| residue_count | Number of