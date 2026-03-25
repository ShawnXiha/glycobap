# GlycoSMILES2BAP: An Automated Pipeline for Stereochemistry-Preserving Glycan Structure Prediction with AlphaFold 3

## 15-Minute Presentation (English Version)

**Speaker: Qiang Xia**  
**Affiliation: Zhejiang Xinghe Tea Technology Co., Ltd.**

---

# Slide 1: Title Slide

## GlycoSMILES2BAP
### An Automated Pipeline for Stereochemistry-Preserving Glycan Structure Prediction with AlphaFold 3

**Qiang Xia**  
Zhejiang Xinghe Tea Technology Co., Ltd.  
Hangzhou, Zhejiang, China

*Keywords: AlphaFold 3, glycans, stereochemistry, structure prediction*

---

# Slide 2: Outline (1 min)

## Presentation Overview

1. **Background & Motivation** (3 min)
   - Glycan importance and diversity
   - AlphaFold 3 breakthrough
   - The stereochemistry problem

2. **Method: GlycoSMILES2BAP** (5 min)
   - Pipeline architecture
   - Three core modules
   - Key technical innovations

3. **Results & Validation** (4 min)
   - Benchmark performance
   - Ablation study
   - Case studies

4. **Conclusions & Future Work** (2 min)

---

# Slide 3: Why Glycans Matter? (1.5 min)

## Glycans: Essential Biological Molecules

### Biological Significance
- **50%+ of human proteins** undergo glycosylation
- Essential roles in:
  - Protein folding
  - Cell-cell recognition
  - Immune responses
  - Pathogen-host interactions

### Structural Diversity Challenge
- **GlyTouCan**: 200,000+ unique structures
- Diversity arises from:
  - Monosaccharide composition
  - Linkage positions (1-2, 1-3, 1-4, 1-6)
  - Anomeric configurations (α/β)
  - Branching patterns

**Implication**: Accurate structure prediction is crucial for understanding biological mechanisms

---

# Slide 4: AlphaFold 3 Breakthrough (1.5 min)

## AlphaFold 3: A Paradigm Shift

### Revolutionary Achievement
- Unprecedented accuracy for protein-ligand complexes
- **Includes glycan ligands** - major advance for glycobiology
- Potential applications:
  - Glycoprotein engineering
  - Vaccine design
  - Therapeutic development

### The Promise
```
"Accurate glycan structure prediction could accelerate 
research in glycoprotein engineering, vaccine design, 
and therapeutic development"
```

**But there's a critical problem...**

---

# Slide 5: The Stereochemistry Problem (2 min)

## AF3 Input Format Determines Accuracy

### Huang et al. (2025) Key Finding

| Input Format | Stereochemistry Accuracy | Issue |
|--------------|-------------------------|-------|
| **SMILES** | ~62% | Epimer confusion, anomeric inversion |
| **userCCD** | ~82% | Linkage errors persist |
| **CCD+BAP** | ~100% | ✓ Perfect stereochemistry |

### The Practical Barrier

**CCD+BAP format requires:**
- Manual atom-by-atom specification
- **30-60 minutes per structure**
- Expert knowledge of carbohydrate chemistry

**Scale problem:**
- 100 glycan variants → 50-100 hours of expert time
- GlyTouCan (200K entries) → impractical

---

# Slide 6: The Core Challenge (1 min)

## The Input Format Dilemma

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│   SMILES        →    62% accuracy    (Unreliable)   │
│   userCCD       →    82% accuracy    (Still flawed) │
│                                                     │
│   Manual BAP    →   100% accuracy    (Impractical)  │
│                    30-60 min/structure              │
│                                                     │
│   ❌ Accessible but WRONG  OR  ✓ Correct but IMPOSSIBLE │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Question**: Can we automate BAP generation?

---

# Slide 7: Our Solution (1 min)

## GlycoSMILES2BAP: Bridging the Gap

### Goal
Convert standard glycan notations → AF3-compatible CCD+BAP format

### Approach
- **Input**: IUPAC-condensed,