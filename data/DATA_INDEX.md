# GlycoSMILES2BAP Dataset Index

## Data Package for Publication

This folder contains all datasets and documentation required for reproducing the results reported in the manuscript "GlycoSMILES2BAP: An Automated Pipeline for Stereochemistry-Preserving Glycan Structure Prediction with AlphaFold 3".

---

## Directory Structure

```
data/
├── README_en.md              # English data documentation
├── README_cn.md              # Chinese data documentation (中文数据说明)
├── METHODOLOGY_en.md         # English methodology documentation  
├── METHODOLOGY_cn.md         # Chinese methodology documentation (中文方法说明)
├── DATA_INDEX.md             # This file - data index
│
├── raw/                      # Raw data files
│   ├── benchmark_dataset.csv         # Benchmark dataset (50 structures)
│   ├── benchmark_detailed.csv        # Detailed benchmark with categories
│   ├── error_correction_cases.csv    # 10 literature error cases
│   └── glytoucan_processing.csv      # GlyTouCan scale processing data
│
├── processed/                # Processed/analyzed data files
│   ├── benchmark_results.csv         # Benchmark performance results
│   ├── ablation_results.csv          # Ablation study results
│   └── module_contributions.csv      # Module contribution analysis
│
├── documentation/            # Additional documentation
│
└── results/                  # Analysis results and outputs
```

---

## Data Files Description

### Raw Data Files (`raw/`)

| File | Records | Description |
|------|---------|-------------|
| `benchmark_dataset.csv` | 50 | Complete benchmark dataset with IUPAC notation and expected outputs |
| `benchmark_detailed.csv` | 50 | Benchmark with category classification and complexity metrics |
| `error_correction_cases.csv` | 10 | Literature-reported error cases used for validation |
| `glytoucan_processing.csv` | 100 | GlyTouCan database processing results |

### Processed Data Files (`processed/`)

| File | Records | Description |
|------|---------|-------------|
| `benchmark_results.csv` | 4 | Performance comparison (accuracy metrics with 95% CI) |
| `ablation_results.csv` | 5 | Ablation study results (full pipeline vs. ablated conditions) |
| `module_contributions.csv` | 4 | Module contribution analysis (delta from full pipeline) |

---

## Data Usage

### For Reviewers
1. Start with `README_en.md` for overview
2. Check `METHODOLOGY_en.md` for data processing methods
3. Use CSV files for independent verification

### For Reproduction
1. Raw data in `raw/` folder can be used as input
2. Processing scripts available at: https://github.com/xiaqiang/glycosmiles2bap
3. Expected outputs documented in `processed/` folder

### For Citation
If using this data, please cite:
> Xia, Q. (2026). GlycoSMILES2BAP: An Automated Pipeline for Stereochemistry-Preserving Glycan Structure Prediction with AlphaFold 3. Bioinformatics (submitted).

---

## Data Quality Assurance

- All CSV files use UTF-8 encoding
- Missing values marked as "NA"
- Decimal values use point notation (e.g., 0.82)
- Confidence intervals in format [lower, upper]

---

## Contact

For questions about the data, contact:
- Email: xiaqiang@xinghetea.com
- GitHub: https://github.com/xiaqiang/glycosmiles2bap/issues

---

*Last updated: 2026-03-22*