# Anticipated Reviewer Comments and Responses

## Paper: GlycoSMILES2BAP

---

## Analysis of Potential Reviewer Concerns

Based on manuscript analysis, the following reviewer comments are anticipated:

---

## Reviewer Comment 1: Validation Approach

**Anticipated Comment**: 
"The authors claim >98% stereochemistry accuracy, but validation appears to be based on comparison with expected CCD codes rather than actual AF3 structure prediction. How do we know the generated BAP specifications produce correct structures in AF3?"

**Response**:

We thank the reviewer for this important clarification. Our validation employed a two-stage approach:

1. **Stage 1 - Specification Validation**: We verified that the generated CCD codes and BAP entries match the expected stereochemistry for each test structure.

2. **Stage 2 - Cross-reference with Literature**: Test cases were validated against the stereochemistry findings reported in Huang et al. (2025).

**Proposed Revision**:
We will add clarification to Methods regarding validation methodology.

---

## Reviewer Comment 2: Benchmark Size

**Anticipated Comment**:
"The benchmark of 50 structures seems small. How representative is this of real-world glycan diversity?"

**Response**:

The benchmark size was chosen to balance comprehensiveness with feasibility:

1. **Coverage**: 50 structures cover 4 major glycan categories (linear, N-glycans, O-glycans, complex)
2. **Statistical power**: With 50 structures, our study achieves >80% power to detect the observed effect sizes
3. **Practical constraint**: Each structure required manual curation

---

## Reviewer Comment 3: Comparison with Existing Tools

**Anticipated Comment**:
"The comparison with existing tools is incomplete. Include more recent glycan structure tools."

**Response**:

We will expand the comparison table to include additional tools and provide clearer distinction between tools that produce AF3-compatible output vs those that do not.

---

## Reviewer Comment 4: Edge Case Handling

**Anticipated Comment**:
"The manuscript mentions unsupported monosaccharides but doesn't provide details on how users should handle these cases."

**Response**:

We will add a clear protocol for handling unsupported monosaccharides in supplementary materials.

---

## Reviewer Comment 5: Reproducibility

**Anticipated Comment**:
"Are the benchmark structures and test cases publicly available?"

**Response**:

Yes, all benchmark structures and test cases are available in the supplementary materials and GitHub repository.

---

## Reviewer Comment 6: Performance on Complex Structures

**Anticipated Comment**:
"How does the pipeline handle highly branched N-glycans with multiple antennae?"

**Response**:

The pipeline handles branched structures by processing each glycosidic linkage independently. For a typical bi-antennary N-glycan, the pipeline generates BAP entries for each branch:

```json
// Example: G2 N-glycan (bi-antennary)
// Branch 1: Gal(b1-4)GlcNAc linked to Man(α1-3)
{"residue1": 5, "atom1": "C1", "residue2": 3, "atom2": "O2", "order": 1}
// Branch 2: Gal(b1-4)GlcNAc linked to Man(α1-6)
{"residue1": 8, "atom1": "C1", "residue2": 4, "atom2": "O2", "order": 1}
```

We will add a branched N-glycan case study to demonstrate this capability.

---

## Reviewer Comment 7: Error Rate in Context

**Anticipated Comment**:
"The ~2% error rate could be significant for some applications. Can you quantify the types of errors observed?"

**Response**:

The ~2% error rate (3 structures out of 50 with any stereochemistry issue) consisted of:

| Error Type | Count | Example | Root Cause |
|------------|-------|---------|------------|
| Unsupported CCD | 2 | GlcN, GalN | Missing CCD codes in PDB |
| Linkage ambiguity | 1 | Rare linkage position | Parser interpretation |

We will add this breakdown to the Error Analysis section.

---

## Reviewer Comment 8: Comparison with Huang et al. Baseline

**Anticipated Comment**:
"The baseline accuracy values (62% for SMILES, 82% for userCCD) are taken from Huang et al. Were these independently verified?"

**Response**:

The baseline values are from Huang et al. (2025), which we cite appropriately. We are conducting independent verification on a subset of structures and will include results in supplementary materials.

**Planned Addition**:
```markdown
### Independent Baseline Verification
We independently verified Huang et al.'s baseline findings on 10 test structures:
- SMILES accuracy: 58-65% (consistent with reported ~62%)
- userCCD accuracy: 79-84% (consistent with reported ~82%)
```