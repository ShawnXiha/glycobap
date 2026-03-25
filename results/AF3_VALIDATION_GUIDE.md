# AF3 Validation Guide for GlycoSMILES2BAP

## Purpose
Validate that GlycoSMILES2BAP-generated BAP format produces stereochemically correct glycan structures in AlphaFold 3 predictions.

## Prerequisites
- AlphaFold 3 installed at `~/tools/alphafold3`
- GlycoSMILES2BAP output JSON files (prepared in `./results/af3_validation_structures.json`)

## Validation Structures

### V001: Lactose (Basic Beta Linkage)
```json
{
  "ccdCodes": ["GAL", "BGC"],
  "bondedAtomPairs": [
    {"donor": {"residueIndex": 1, "atomName": "C1"}, 
     "acceptor": {"residueIndex": 2, "atomName": "O4"}}
  ]
}
```
**Validation Points:**
- Galactose C4 hydroxyl should be axial (not equatorial like glucose)
- Beta linkage geometry correct

### V003: Sialyllactose (CRITICAL - Sialic Acid Test)
```json
{
  "ccdCodes": ["SIA", "GAL", "BGC"],
  "bondedAtomPairs": [
    {"donor": {"residueIndex": 1, "atomName": "C2"}, 
     "acceptor": {"residueIndex": 2, "atomName": "O3"}},
    {"donor": {"residueIndex": 2, "atomName": "C1"}, 
     "acceptor": {"residueIndex": 3, "atomName": "O4"}}
  ]
}
```
**CRITICAL Validation Points:**
- Neu5Ac anomeric carbon MUST be at C2 (not C1)
- Ring oxygen MUST be O6 (not O5)
- This tests the ketose-specific handling

### V004: M3 N-glycan (Branch Handling)
```json
{
  "ccdCodes": ["MAN", "MAN", "BMA", "NAG", "NAG"],
  "bondedAtomPairs": [
    {"donor": {"residueIndex": 1, "atomName": "C1"}, "acceptor": {"residueIndex": 3, "atomName": "O3"}},
    {"donor": {"residueIndex": 2, "atomName": "C1"}, "acceptor": {"residueIndex": 3, "atomName": "O6"}},
    {"donor": {"residueIndex": 3, "atomName": "C1"}, "acceptor": {"residueIndex": 4, "atomName": "O4"}},
    {"donor": {"residueIndex": 4, "atomName": "C1"}, "acceptor": {"residueIndex": 5, "atomName": "O4"}}
  ]
}
```
**Validation Points:**
- Branch topology preserved (α1-3 and α1-6 arms)
- Both MAN residues correctly positioned

## Step-by-Step Validation Procedure

### Step 1: Prepare AF3 Input JSON
For each validation structure, create AF3 input file:

```json
{
  "name": "V001_lactose",
  "modelSeeds": [42],
  "sequences": [
    {
      "glycan": {
        "ccdCodes": ["GAL", "BGC"],
        "bondedAtomPairs": [
          [{"residueIndex": 1, "atomName": "C1"}, {"residueIndex": 2, "atomName": "O4"}]
        ]
      }
    }
  ]
}
```

### Step 2: Run AF3 Prediction
```bash
cd ~/tools/alphafold3
python run_af3.py --input ./validation/V001_lactose.json --output ./results/V001/
```

### Step 3: Analyze Output
1. Load predicted PDB structure
2. Check stereochemistry using Privateer:
```bash
privateer --input ./results/V001/model.pdb
```

### Step 4: Validation Checklist

#### For Each Structure:
- [ ] Epimer configuration correct (e.g., Gal vs Glc)
- [ ] Anomeric configuration correct (α vs β)
- [ ] Linkage positions correct (e.g., 1-4 vs 1-3)
- [ ] Branch topology preserved (for branched glycans)

#### For Sialic Acid (V003):
- [