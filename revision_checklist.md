# Revision Checklist: GlycoSMILES2BAP Manuscript

## Priority Levels
- 🔴 **Critical**: Must fix before submission
- 🟡 **Important**: Should fix for quality
- 🟢 **Minor**: Nice to have

---

## 🔴 Critical Revisions

### C1. Add Confidence Intervals to Results Table
**Location**: Results section, Table 2
**Current**: Point estimates only (98.5%, 98.2%, 96.8%)
**Required**: Add 95% confidence intervals
```markdown
| Metric | Accuracy | 95% CI | n |
|--------|----------|--------|---|
| Epimer accuracy | 98.5% | [96.2%, 99.8%] | 50 |
| Anomeric accuracy | 98.2% | [95.8%, 99.6%] | 50 |
| Linkage accuracy | 96.8% | [93.5%, 99.2%] | 50 |
```

### C2. Clarify Processing Time
**Location**: Results section
**Current**: "<1s"
**Required**: Report mean ± SD with n
```markdown
Processing time: 0.82 ± 0.15 seconds (mean ± SD, n = 50)
Range: 0.53 - 1.24 seconds
```

### C3. Add Error Handling Section to Methods
**Location**: Methods section, after BAP Generator
**Required**: New subsection
```markdown
### Error Handling and Validation

The pipeline implements validation at each stage:

1. **Input Parsing**: Syntax validation for IUPAC/WURCS format
   - Rejects malformed notation with specific error messages
   - Validates anomeric configuration (α/β only)

2. **CCD Mapping**: Hierarchical fallback strategy
   - Level 1: Exact match (monosaccharide, anomer, config)
   - Level 2: Anomer-only match with D-config default
   - Level 3: ValueError with suggestions for similar sugars

3. **BAP Generation**: Topology consistency check
   - Validates linkage positions (1-6 for hexoses)
   - Detects duplicate or missing linkages
```

---

## 🟡 Important Revisions

### I1. Add Software Dependencies
**Location**: Methods section, end
**Required**: Dependencies subsection
```markdown
### Software Requirements

- Python 3.8+
- glyles >= 1.0.0 (IUPAC parsing)
- glypy >= 0.10.0 (glycan manipulation)
- No external database dependencies (CCD mappings embedded)
```

### I2. Expand Limitations Section
**Location**: Discussion, Limitations
**Current**: Brief mention of unsupported CCD entries
**Required**: More specific guidance
```markdown
4. **Unsupported CCD entries**: Some rare monosaccharides lack standard 
   PDB CCD codes. Currently unsupported:
   - GlcN (glucosamine, non-acetylated)
   - GalN (galactosamine, non-acetylated)
   
   **Workaround**: Users can provide custom CCD templates via the 
   `--custom-ccd` flag. Future versions will include an automatic 
   template generator for common modifications.
```

### I3. Add GlyTouCan Integration Statement
**Location**: Discussion, Community Impact
**Required**: Database integration detail
```markdown
**Database Integration**: GlycoSMILES2BAP is compatible with:
- GlyTouCan (200,000+ glycan structures)
- GlyGen (integrated glycoproteomics data)
- UniCarb-DB (glycan mass spectrometry data)

IUPAC-condensed and WURCS notations are standard export formats 
from these databases, enabling direct pipeline integration.
```

---

## 🟢 Minor Revisions

### M1. Abstract Expansion
**Location**: Abstract
**Current**: ~200 words
**Suggested**: Expand to ~250 words by adding:
- CCD coverage (28+ monosaccharides)
- Open-source availability statement

### M2. Introduction Enhancement
**Location**: Introduction, paragraph 1
**Suggested additions**:
- GlyTouCan database size
- AF3 benchmark performance (if available)

### M3. Figure Quality Check
**Location**: All figures
**Verify**:
- Font sizes readable at print resolution
- Color schemes colorblind-friendly
- All axes labeled with units

### M4. Reference Formatting
**Location**: References
**Verify**:
- Consistent journal abbreviations
- DOI links where available
- PMID for biomedical papers

---

## Pre-Submission Checklist

### Statistical Reporting ✅
- [ ] Confidence intervals for