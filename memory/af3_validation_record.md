# AF3 Validation Record for GlycoSMILES2BAP

## Date: 2026-03-24

---

## AF3 Installation Status

### Directory Structure
- **Location**: `/alphafold3/`
- **Source Code**: Cloned from google-deepmind/alphafold3
- **Main Script**: `run_alphafold.py`

### Key Files Examined
1. `run_alphafold.py` - Main inference script
2. `docs/input.md` - Input format documentation
3. `docker/Dockerfile` - Docker build configuration
4. `docs/installation.md` - Installation instructions

---

## AF3 Input Format Analysis

### Glycan Specification Requirements

From `docs/input.md`:

1. **CCD Codes**: Glycans specified as ligands with `ccdCodes` field
   - Example: `"ccdCodes": ["NAG", "NAG", "BMA", "MAN", "MAN"]`

2. **BondedAtomPairs**: Critical for glycan stereochemistry
   - Format: `[["entity_id", residue_index, "atom_name"], ["entity_id", residue_index, "atom_name"]]`
   - Example: `[["G", 1, "C1"], ["G", 2, "O4"]]`

3. **Glycan Definition Pattern**:
   ```json
   {
     "ligand": {
       "id": "G",
       "ccdCodes": ["SIA", "GAL", "BGC"]
     }
   }
   ```

4. **Bonds Definition**:
   ```json
   "bondedAtomPairs": [
     [["G", 1, "C2"], ["G", 2, "O3"]],
     [["G", 2, "C1"], ["G", 3, "O4"]]
   ]
   ```

---

## Validation Input Files Created

### File Locations
- `/results/af3_validation/sialyllactose_bap.json` - BAP format (GlycoSMILES2BAP output)
- `/results/af3_validation/sialyllactose_smiles.json` - SMILES format (comparison)
- `/results/af3_validation/lactose_bap.json` - Simple test case

### V003: Sialyllactose (Critical Test)

**IUPAC**: Neu5Ac(a2-3)Gal(b1-4)Glc

**Key Validation Points**:
1. Neu5Ac anomeric carbon at C2 (ketose property)
2. Ring oxygen at O6 (not O5 like hexoses)
3. Alpha configuration on Sia-Gal linkage
4. Beta configuration on Gal-Glc linkage

**BAP Format Expected Behavior**:
- Explicit atom pairs force correct C2 placement
- Prevents AF3 from defaulting to C1

**SMILES Format Expected Behavior**:
- May incorrectly place anomeric bond at C1
- ~60% stereochemistry accuracy per Huang et al. (2025)

---

## AF3 Running Requirements

### Hardware Requirements
- NVIDIA GPU with Compute Capability 8.0+
- A100 80GB or H100 80GB recommended
- 64GB+ RAM for genetic search stage
- Up to 1TB disk space for databases

### Software Requirements
- Docker with NVIDIA Container Toolkit
- CUDA 12.6
- Python 3.12

### Command Template
```bash
python run_alphafold.py \
  --json_path=/path/to/input.json \
  --model_dir=/path/to/models \
  --output_dir=/path/to/output \
  --run_data_pipeline=false
```

Note: `--run_data_pipeline=false` for ligand-only predictions (no MSA needed)

---

## Expected Validation Outcome

### Success Criteria

1. **BAP Format**: >98% stereochemistry accuracy
   - Correct C2 for sialic acids
   - Correct alpha/beta configurations
   - Correct linkage positions

2. **SMILES Format**: ~60% accuracy (baseline)
   - Expected errors in sialic acid anomeric position
   - Epimer confusion possible

3. **Improvement Delta**: >35% accuracy improvement with BAP vs SMILES

---

## Next Steps

1. [ ] Obtain GPU resources (A100/H100)
2. [ ] Download model parameters from Google DeepMind
3. [ ] Build Docker container or install locally
4. [ ] Run validation with BAP format inputs
5. [ ] Run comparison with SMILES inputs
6. [ ] Analyze output structures