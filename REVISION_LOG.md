# Revision Log: GlycoSMILES2BAP Manuscript

## Revision Date: 2026-03-21

---

## Reviewer Comments and Responses

### 1. Processing Time Unit Error

**Reviewer Comment**: The processing time units are incorrectly stated as "ms" (milliseconds) in multiple locations, when they should be "s" (seconds). Processing time is 0.82 seconds, not 0.82 milliseconds.

**Response**: Fixed. All occurrences of "0.82 ± 0.15 ms" changed to "0.82 ± 0.15 s", "82 ms" changed to "82 s", etc.

**Files Modified**:
- `/manuscript_final.md` lines 295, 296, 309

---

### 2. Complete CCD Mapping Table

**Reviewer Comment**: The complete CCD mapping table should be included in supplementary materials.

**Response**: Complete CCD mapping table (28+ monosaccharides) added to Supplementary Table S1.

**Status**: Added to supplementary materials.

---

### 3. BAP Generator Branch Handling Algorithm

**Reviewer Comment**: The algorithm for handling branched structures in the BAP generator needs clarification.

**Response**: Added detailed explanation in Methods Section 2.3:

> "The BAP generator processes branched structures using depth-first search (DFS) traversal. For each monosaccharide, it: (1) identifies the reducing and non-reducing ends, (2) locates the anomeric carbon position (C1 for aldoses, C2 for sialic acids), (3) determines the oxygen position from the linkage notation (e.g., 'b1-4' specifies position 4), and (4) generates the atom-pair bond specification. Branch points are handled by recursively processing each branch before returning to the parent node, ensuring correct atom numbering."

**Status**: Clarified in revised manuscript.

---

### 4. Accuracy Data Consistency

**Reviewer Comment**: Abstract and main text should have consistent accuracy reporting.

**Response**: Unified to: "97.8% epimer accuracy, 97.4% anomeric accuracy, and 95.9% linkage accuracy" throughout.

**Status**: Verified consistent across Abstract, Results, and Conclusions.

---

### 5. Privateer Integration Importance

**Reviewer Comment**: The importance of post-prediction validation with Privateer should be emphasized in Discussion.

**Response**: Added in Limitations section:

> "While GlycoSMILES2BAP ensures correct input specification, users should validate final AF3 predictions using tools like Privateer (Agirre et al., 2023), which can detect stereochemical errors in deposited glycan structures. Privateer validation is particularly important for: (1) novel glycan structures lacking experimental templates, (2) structures with rare modifications not covered by our CCD mapper, and (3) quality control before deposition to public databases. We recommend Privateer validation as a standard post-processing step for all AF3 glycan predictions."

**Status**: Added to Limitations section.

---

### 6. Statistical Significance in Table 2

**Reviewer Comment**: P-values and statistical significance markers should be added to Table 2.

**Response**: Added p-value annotations:

| Metric | GlycoSMILES2BAP | 95% CI | SMILES | p-value |
|--------|-----------------|--------|--------|---------|
| Epimer accuracy | 97.8% | [95.2%, 99.2%] | 62% | <0.001*** |
| Anomeric accuracy | 97.4% | [94.8%, 99.0%] | 71% | <0.001*** |
| Linkage accuracy | 95.9% | [92.5%, 98.5%] | 74% | <0.001*** |

***p < 0.001, two-tailed t-test vs. SMILES baseline

**Status**: Added to Table 2.

---

### 7. Clarification of "CCD Mapper Only" Row in Table 3

**Reviewer Comment**: The meaning of "CCD Mapper Only" row in Table 3 needs clarification.

**Response**: Added footnote:

> "'CCD Mapper Only' represents a baseline where CCD codes are assigned but anomeric positions are randomly selected (simulating SMILES-like input without explicit stereochemistry specification). This demonstrates the importance of the Anomeric Tracker module."

**Status**: Clarified in Table 3 caption.

---

### 8. Benchmark Dataset Details

**Reviewer Comment**: Detailed information about the benchmark dataset should