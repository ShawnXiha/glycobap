# PDB Validation Data for GlycoSMILES2BAP

## Date: 2026-03-28

This file contains known PDB structures with glycans for validation comparison.

---

## PDB Structures with Verified Glycan Stereochemistry

### 1. PDB: 5NSC - Fucosylated Structure (Error Case)

**Reference**: Frenz et al., 2018 (reported error)

**Structure**: 
- Contains fucose residue
- Original structure had incorrect anomer (beta-Fuc instead of alpha-Fuc)

**Our Tool Validation**:
- Input: `Fuc(a1-2)Gal(b1-4)Glc`
- Expected CCD: `FUC` (alpha-L-fucose)
- Expected Output: Correct alpha configuration

**Validation Check**:
- Compare our generated CCD code with correct structure
- Verify FUC (alpha) not BDF (beta)

---

### 2. PDB: 5K65 - N-glycan Missing Linkage

**Reference**: Jo et al., 2011

**Structure**:
- N-glycan core structure
- Original structure missing Asn297-GlcNAc bond

**Our Tool Validation**:
- Input: `Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc`
- Expected: All linkages specified

**Validation Check**:
- Verify all BAP entries generated
- Check N-glycosidic bond correctly specified

---

### 3. PDB: 1L6R - Lactose Structure

**Structure**: Lactose bound to protein

**Known Correct Values**:
- Galactose: GAL (beta-D-galactose)
- Glucose: BGC (beta-D-glucose)
- Linkage: Beta(1-4)
- Galactose C4: Axial hydroxyl (distinguishes from glucose)

**Our Tool Validation**:
- Input: `Gal(b1-4)Glc`
- Expected CCD: ["GAL", "BGC"]
- Expected BAP: C1-O4 linkage

---

### 4. PDB: 2VXR - Sialyllactose Structure

**Structure**: Neu5Ac(a2-3)Gal(b1-4)Glc

**Critical Check Points**:
- **Neu5Ac anomeric carbon**: Must be at C2 (ketose)
- **Neu5Ac ring oxygen**: O6 (not O5)
- **Linkage**: Alpha(2-3) between Sia-Gal

**Our Tool Validation**:
- Input: `Neu5Ac(a2-3)Gal(b1-4)Glc`
- Expected CCD: ["SIA", "GAL", "BGC"]
- Expected BAP: C2-O3 (SIA to GAL), C1-O4 (GAL to GLC)

**This is the CRITICAL test for our tool** because:
- SMILES format typically fails to specify C2 correctly
- userCCD format may confuse C1 vs C2
- Our BAP format should force correct C2 placement

---

## Validation Methodology

### Step 1: Download PDB structures
```bash
# Download PDB files
wget https://files.rcsb.org/download/5NSC.pdb
wget https://files.rcsb.org/download/5K65.pdb
wget https://files.rcsb.org/download/1L6R.pdb
wget https://files.rcsb.org/download/2VXR.pdb
```

### Step 2: Extract glycan stereochemistry
Use Privateer or manual inspection to determine:
- Monosaccharide types (CCD codes)
- Anomeric configurations (alpha/beta)
- Linkage positions

### Step 3: Generate input using GlycoSMILES2BAP
```python
from glycosmiles2bap import GlycoSMILES2BAP

pipeline = GlycoSMILES2BAP()
result = pipeline.convert("Neu5Ac(a2-3)Gal(b1-4)Glc")
```

### Step 4: Compare
- CCD codes match expected
- BAP correctly specifies atom pairs
- Anomeric positions correct (especially C2 for sialic acids)

---

## Expected Validation Results

| PDB ID | Glycan Type | Key Check | Expected Outcome |
|--------|-------------|-----------|------------------|
| 5NSC | Fucosylated | FUC vs BDF | Correct FUC (alpha) |
| 5K65 | N-g