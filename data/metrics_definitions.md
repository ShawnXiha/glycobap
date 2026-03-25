# Metrics Definitions: GlycoSMILES2BAP Evaluation

## Primary Metrics

### 1. Stereochemistry Accuracy

**Definition**: Percentage of monosaccharide residues with correct stereochemical configuration.

**Components**:
- **Epimer accuracy**: Correct distinction between stereoisomers (e.g., D-galactose vs D-glucose)
- **Anomeric accuracy**: Correct α/β configuration at anomeric carbon
- **Linkage accuracy**: Correct glycosidic bond positions (e.g., 1→4 vs 1→6)

**Calculation**:
```
Stereochemistry Accuracy = (Correct residues / Total residues) × 100%
```

**Ground Truth**: PDB experimental structures validated by Privateer

---

### 2. Structural Accuracy

**RMSD (Root Mean Square Deviation)**:
- Measures atomic position deviation from experimental structure
- Computed over glycan heavy atoms after optimal superposition
- Units: Ångströms (Å)

**Formula**:
```
RMSD = sqrt(Σ(di²) / N)
```
where di is the distance between atom i in predicted and experimental structures

**Thresholds**:
- < 1.0 Å: Excellent
- 1.0-2.0 Å: Good
- 2.0-3.0 Å: Acceptable
- > 3.0 Å: Poor

---

### 3. Glycosidic Torsion Angles

**Definition**: Deviation of glycosidic linkage torsion angles (φ, ψ) from experimental values.

**Torsion Angle Definitions**:
- φ (phi): O5-C1-O1-Cx' (donor anomeric)
- ψ (psi): C1-O1-Cx'-Cx+1' (acceptor)

**Calculation**:
```
Δφ = |φ_predicted - φ_experimental|
Δψ = |ψ_predicted - ψ_experimental|

# Handle angle wrapping
if Δφ > 180°: Δφ = 360° - Δφ
if Δψ > 180°: Δψ = 360° - Δψ
```

**Thresholds**:
- < 15°: Excellent
- 15-30°: Good
- 30-60°: Acceptable
- > 60°: Poor

---

### 4. Processing Time

**Definition**: Wall-clock time to convert glycan notation to AF3-compatible JSON.

**Measurement**: 
- Start: Input string received
- End: Valid JSON output written
- Units: milliseconds (ms)

**Threshold**: < 1000 ms per glycan

---

## Secondary Metrics

### Ring Puckering

**Cremer-Pople Parameters**:
- Q: Total puckering amplitude
- θ: Polar angle
- φ: Azimuthal angle

**Ideal Values**:
- 4C1 chair: θ ≈ 0° or 180°
- Boat conformations: θ ≈ 90°

---

### Error Detection Metrics (Validator)

**Recall**:
```
Recall = TP / (TP + FN)
```
- TP: True positives (correctly detected errors)
- FN: False negatives (missed errors)
- Target: > 90%

**Precision**:
```
Precision = TP / (TP + FP)
```
- FP: False positives (incorrect error flags)
- Target: > 85%

---

## Statistical Analysis

### Hypothesis Testing

**Primary Test**: Two-sample t-test
- H0: No difference between GlycoSMILES2BAP and baseline (SMILES/userCCD)
- Ha: GlycoSMILES2BAP accuracy > baseline accuracy
- Significance level: α = 0.01

**Effect Size**: Cohen's d
```
d = (μ1 - μ2) / σ_pooled
```
- Small: d = 0.2
- Medium: d = 0.5
- Large: d = 0.8

### Confidence Intervals

**95% CI for accuracy**:
```
CI = μ ± 1.96 × (σ / √n)
```

---

## Benchmark Categories

### Category 1: Linear Glycans
- Disaccharides: Maltose, Lactose, Sucrose
- Trisaccharides: Maltotriose, Raffinose
- Tetrasaccharides: LNnT, LNT

### Category 2: Branched N-glycans
- High-mannose: M3, M5, M6, M7, M9
- Hybrid: H1, H2
- Complex: G0, G1, G2, A1, A2

### Category