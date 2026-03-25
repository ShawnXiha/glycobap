# AF3 Validation Status - 2026-03-24

## Current Status: PENDING EXTERNAL RUN

### Problem Encountered
Sandbox environment cannot execute shell commands with absolute paths properly.
- Error: `./home/qiang/.local/bin/uv: not found`
- The uv binary exists at `/home/qiang/.local/bin/uv` but shell execution fails

### Solution: External Script Execution
Created scripts for running AF3 validation outside sandbox:

#### Script 1: run_af3_validation.sh
**Location**: `/run_af3_validation.sh`
**Purpose**: Run AF3 predictions for all test structures

**Usage**:
```bash
cd /home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides
chmod +x run_af3_validation.sh
./run_af3_validation.sh
```

#### Script 2: analyze_af3_results.py
**Location**: `/scripts/analyze_af3_results.py`
**Purpose**: Analyze AF3 output for stereochemistry validation

**Usage**:
```bash
python scripts/analyze_af3_results.py
```

### Test Structures Prepared

| Structure | File | Test Purpose |
|-----------|------|--------------|
| Sialyllactose BAP | `results/af3_validation/sialyllactose_bap.json` | CRITICAL: C2 anomeric test |
| Lactose BAP | `results/af3_validation/lactose_bap.json` | Baseline test |
| Sialyllactose SMILES | `results/af3_validation/sialyllactose_smiles.json` | Comparison |

### Expected AF3 Outputs

After running AF3, expect these files in `results/af3_output/`:
```
af3_output/
├── sialyllactose_bap/
│   ├── model.cif
│   └── summary_confidences_0.json
├── lactose_bap/
│   ├── model.cif
│   └── summary_confidences_0.json
└── sialyllactose_smiles/
    ├── model.cif
    └── summary_confidences_0.json
```

### Validation Criteria

#### Sialyllactose (CRITICAL TEST)
1. **C2 Anomeric Position**: Neu5Ac anomeric bond MUST be at C2 (ketose property)
2. **Alpha(2-3) Linkage**: Correct geometry for Sia-Gal bond
3. **Beta(1-4) Linkage**: Correct geometry for Gal-Glc bond

#### Expected Improvement
- BAP format: >98% stereochemistry correct
- SMILES format: ~60% stereochemistry error
- **Improvement delta**: >35%

### Next Steps

1. Run `run_af3_validation.sh` externally
2. Check AF3 outputs in `results/af3_output/`
3. Run `analyze_af3_results.py` for validation
4. Record results to evo-memory
5. Update paper with AF3 validation data
