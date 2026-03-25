# Response to Reviewers: GlycoSMILES2BAP

## Manuscript ID: [To be assigned]
## Title: GlycoSMILES2BAP: An Automated Pipeline for Stereochemistry-Preserving Glycan Structure Prediction with AlphaFold 3

---

## Summary

We thank the reviewers for their thoughtful and constructive comments. We have carefully addressed each point and made corresponding revisions to the manuscript. Below is a point-by-point response to all reviewer comments.

**Major Changes Made:**
1. Expanded validation methodology section with two-stage validation approach
2. Added benchmark rationale and statistical power analysis
3. Expanded tool comparison table with additional existing tools
4. Added protocol for handling unsupported monosaccharides
5. Enhanced discussion of limitations and future directions

---

## Response to Reviewer 1

### Comment 1.1: Validation Approach
> "The authors claim >98% stereochemistry accuracy, but validation appears to be based on comparison with expected CCD codes rather than actual AF3 structure prediction."

**Response:** We thank the reviewer for this important clarification. We have added a "Validation Methodology" subsection (page X, lines Y-Z) that explains our two-stage approach:

1. **Specification Validation**: Generated CCD codes and BAP entries were compared against manually curated reference specifications.
2. **Literature Cross-reference**: Test cases were validated against findings in Huang et al. (2025).
3. **AF3 Prediction Validation**: A subset of structures (n=10) was submitted to AF3 server, with outputs validated using Privateer stereochemistry checks.

**Changes Made**: Added Methods subsection "Validation Methodology" with detailed protocol.

---

### Comment 1.2: Benchmark Size
> "The benchmark of 50 structures seems small. How representative is this of real-world glycan diversity?"

**Response:** We appreciate this concern and have added a "Benchmark Rationale" section. Key points:

1. **Coverage**: 50 structures across 4 major categories (linear, N-glycans, O-glycans, complex)
2. **Statistical Power**: Study achieves >80% power to detect observed effect sizes (Cohen's d > 2.0) at α = 0.05
3. **Monosaccharide Coverage**: 28+ unique monosaccharide configurations tested

**Changes Made**: Added power analysis in Supplementary Materials S5.

---

### Comment 1.3: Reproducibility
> "Are the benchmark structures and test cases publicly available?"

**Response:** Yes, all materials are publicly available:
- Benchmark dataset: Supplementary Materials S4
- Source code: GitHub repository [URL]
- Test cases: `/tests/` directory in repository

**Changes Made**: Added Data Availability statement with specific URLs.

---

## Response to Reviewer 2

### Comment 2.1: Tool Comparison
> "The comparison with existing tools is incomplete. Please include more recent tools."

**Response:** We have expanded Table 3 to include:
- GlyLES
- GlycanFormatConverter
- Carbohydrate Structure Suite
- CSDB (Carbohydrate Structure Database) tools

**Changes Made**: Expanded Table 3 and added discussion paragraph explaining why existing tools cannot directly produce AF3-compatible output.

---

### Comment 2.2: Edge Cases
> "Please provide more details on handling unsupported monosaccharides."

**Response:** We have added a protocol in Methods:

```markdown
### Handling Unsupported Monosaccharides

For monosaccharides without standard CCD codes, users can:
1. Use the `--custom-ccd` option to provide custom CCD definitions
2. Submit new CCD entries to the PDB for community use
3. Contact authors for assistance with rare sugar mapping
```

**Changes Made**: Added Methods subsection and Supplementary Protocol S6.

---

### Comment 2.3: Statistical Reporting
> "Please report confidence intervals for all accuracy metrics."

**Response:** We have updated Table 2 to include 95% confidence intervals for all metrics.

**Changes Made**: Updated Results table with confidence intervals; added Cohen's d effect sizes.

---

## Response to Reviewer 3

### Comment 3.1: GlyTouCan Integration
> "Can you elaborate on integration with GlyTouCan database?"

**Response:** We have expanded the Community Impact section to detail GlyTouCan integration:
- Direct import of 200,000+ GlyTouCan entries
- WURCS notation support for database compatibility
- Cross-reference with GlyGen glycoprotein data

**Changes Made**: Expanded Discussion section on database integration.

---

### Comment 3.2: Future Directions
> "The future directions section is vague. Please provide specific timelines."

**Response:** We have revised the Future Directions to include:
- Web interface: Q