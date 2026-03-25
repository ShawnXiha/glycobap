# AF3 Validation Experiment Plan for GlycoSMILES2BAP

## Date: 2026-03-24

## Objective
Validate that GlycoSMILES2BAP-generated CCD+BAP format produces stereochemically correct glycan structures in AlphaFold 3 predictions.

---

## Validation Structures (n=5)

### V001: Lactose (Basic Test)
- **IUPAC**: Gal(β1-4)Glc
- **Test Case**: Basic beta linkage
- **Expected CCD**: [GAL, BGC]
- **Critical Check**: Galactose C4-OH axial (not equatorial like Glc)

### V002: LNnT (Chain Test)
- **IUPAC**: Gal(β1-4)GlcNAc(β1-3)Gal(β1-4)Glc
- **Test Case**: Multi-linkage chain
- **Expected CCD**: [GAL, NAG, GAL, BGC]
- **Critical Check**: Correct O3 and O4 linkage positions

### V003: Sialyllactose (CRITICAL TEST)
- **IUPAC**: Neu5Ac(α2-3)Gal(β1-4)Glc
- **Test Case**: Sialic acid C2 anomeric position
- **Expected CCD**: [SIA, GAL, BGC]
- **CRITICAL**: Neu5Ac uses C2 as anomeric carbon (ketose property)
- **CRITICAL**: Ring oxygen is O6 (not O5 like hexoses)
- **Validation**: If SMILES used, AF3 would incorrectly place bond at C1

### V004: M3 N-glycan (Branch Test)
- **IUPAC**: Man(α1-3)[Man(α1-6)]Man(β1-4)GlcNAc(β1-4)GlcNAc
- **Test Case**: Branch handling
- **Expected CCD**: [MAN, MAN, BMA, NAG, NAG]
- **Critical Check**: Branch topology preserved (Man-Man-Man core)

### V005: Fucosylated (Config Test)
- **IUPAC**: Fuc(α1-2)Gal(β1-4)Glc
- **Test Case**: L-configuration fucose
- **Expected CCD**: [FUC, GAL, BGC]
- **Critical Check**: Fucose is L-config (not D like most sugars)

---

## Validation Methodology

### Step 1: Generate AF3 Input Files
Using GlycoSMILES2BAP:
```json
{
  "name": "test_glycan",
  "ligand": {
    "ccdCodes": ["SIA", "GAL", "BGC"],
    "bondedAtomPairs": [
      {"donor": {"residueIndex": 1, "atomName": "C2"}, 
       "acceptor": {"residueIndex": 2, "atomName": "O3"}}
    ]
  }
}
```

### Step 2: Run AF3 Prediction
- Use AF3 server or local installation
- Input: GlycoSMILES2BAP-generated JSON
- Control: SMILES input for comparison

### Step 3: Analyze Output Structure
Using Privateer or manual inspection:
1. Check anomeric carbon position
2. Verify epimer configuration (Gal vs Glc)
3. Confirm linkage positions (O3 vs O4)
4. Validate branch topology

### Step 4: Compare with SMILES Baseline
- Run same structures with SMILES input
- Compare stereochemistry accuracy
- Document differences

---

## Expected Outcomes

| Structure | BAP Expected | SMILES Expected | Key Difference |
|-----------|--------------|-----------------|----------------|
| V001 Lactose | Correct Gal β1-4 | Possible Glc confusion | Epimer accuracy |
| V002 LNnT | All linkages correct | Linkage position errors | Multi-bond handling |
| V003 Sialyllactose | C2 correct | C1 incorrect (critical) | Ketose handling |
| V004 M3 N-glycan | Branch correct | Branch topology error | Branch handling |
| V005 Fucosylated | L-config correct | D-config possible | Config handling |

---

## Success Criteria

1. **Epimer Accuracy**: >95% correct monosaccharide identification
2. **Anomeric Accuracy**: >95% correct α/β configuration
3. **Linkage Accuracy**: >95