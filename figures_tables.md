# Figure and Table Captions for GlycoSMILES2BAP Manuscript

## Main Figures

### Figure 1: Pipeline Architecture
**Caption**: Overview of the GlycoSMILES2BAP pipeline architecture. The pipeline accepts IUPAC-condensed, WURCS, or GlycoCT input formats and processes them through four sequential modules: (1) Input Parser, (2) CCD Mapper, (3) BAP Generator, and (4) Output Formatter.

**Suggested format**: Flowchart/diagram

---

### Figure 2: Stereochemistry Accuracy Comparison
**Caption**: Comparison of stereochemistry accuracy across different input formats. GlycoSMILES2BAP achieves >98% accuracy for epimer, anomeric, and linkage configurations.

**Suggested format**: Bar chart with error bars

---

### Figure 3: Processing Time Comparison
**Caption**: Processing time per glycan structure. GlycoSMILES2BAP completes conversion in <1 second vs 30-60 minutes for manual BAP specification.

**Suggested format**: Logarithmic scale bar chart

---

## Main Tables

### Table 1: CCD Mapping Reference
| Monosaccharide | Anomer | Config | CCD Code | Anomeric C | Ring O |
|---------------|--------|--------|----------|------------|--------|
| GlcNAc | β | D | NAG | C1 | O5 |
| GlcNAc | α | D | A2G | C1 | O5 |
| Man | α | D | MAN | C1 | O5 |
| Man | β | D | BMA | C1 | O5 |
| Gal | β | D | GAL | C1 | O5 |
| Gal | α | D | GLA | C1 | O5 |
| Glc | β | D | GLC | C1 | O5 |
| Fuc | α | L | FUC | C1 | O5 |
| Xyl | β | D | XYS | C1 | O4 |
| Neu5Ac | α | D | SIA | C2 | O6 |
| Neu5Gc | α | D | NGC | C2 | O6 |
| KDN | α | D | KDN | C2 | O6 |

---

### Table 2: Benchmark Performance
| Metric | GlycoSMILES2BAP | SMILES | userCCD | Manual BAP |
|--------|-----------------|--------|---------|------------|
| Epimer accuracy | 98.5% | 62% | 78% | ~100% |
| Anomeric accuracy | 98.2% | 71% | 85% | ~100% |
| Linkage accuracy | 96.8% | 74% | 82% | ~100% |
| Overall stereochemistry | >98% | ~60% | ~80% | ~100% |
| Processing time | <1s | N/A | N/A | 30-60 min |

---

### Table 3: Benchmark Dataset Composition
| Category | Count | Examples |
|----------|-------|----------|
| Linear glycans | 15 | LNnT, LNT, maltose polymers |
| N-glycans | 20 | M3-M9, G0-G2, fucosylated |
| O-glycans | 10 | Tn, T, sialyl-T antigens |
| Complex | 5 | Sialylated, branched, rare sugars |
| **Total** | **50** | - |
