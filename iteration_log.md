# Experiment-Craft Iteration Log

## Session: 2025-01-XX

---

## Iteration 1: CCD Mapper Bug Fix

### Problem Found
CCD mapper returned `None` for all monosaccharide lookups despite correct table entries.

### Root Cause
Case-sensitivity mismatch:
- Table keys: `('glcnac', 'beta', 'd')` (lowercase config)
- Lookup key: `('glcnac', 'beta', 'D')` (uppercase config from `absolute_config.upper()`)

### Fix Applied
```python
# Before (buggy)
config = absolute_config.upper()  # Returns 'D'

# After (fixed)
config = absolute_config.lower()  # Returns 'd'
```

### Validation Results
```
PASS: GlcNAc (beta, D) -> NAG (expected: NAG)
PASS: GlcNAc (alpha, D) -> A2G (expected: A2G)
PASS: Man (alpha, D) -> MAN (expected: MAN)
PASS: Man (beta, D) -> BMA (expected: BMA)
PASS: Gal (beta, D) -> GAL (expected: GAL)
PASS: Gal (alpha, D) -> GLA (expected: GLA)
PASS: Fuc (alpha, L) -> FUC (expected: FUC)
PASS: Neu5Ac (alpha, D) -> SIA (expected: SIA)
PASS: Neu5Ac (beta, D) -> SLB (expected: SLB)
Result: 9/9 tests passed
```

---

## Iteration 2: BAP Generator Validation

### Tests Performed
1. **Basic BAP Generation**: Standard Gal(b1-4)GlcNAc linkage
2. **Sialic Acid Handling**: SIA uses C2 as anomeric carbon (ketose)
3. **Topology Generation**: Multi-linkage glycans
4. **AF3 JSON Format**: Output structure validation

### Validation Results
```
=== Test 1: Basic BAP Generation ===
BAP: {'residue1': 1, 'atom1': 'C1', 'residue2': 2, 'atom2': 'O4', 'order': 1}
PASS

=== Test 2: Sialic Acid (SIA) ===
SIA BAP: {'residue1': 1, 'atom1': 'C2', 'residue2': 2, 'atom2': 'O3', 'order': 1}
PASS (C2 correctly used for ketose)

=== Test 3: Topology Generation ===
Generated 2 BAP entries
PASS

=== Test 4: AF3 JSON Generation ===
AF3 JSON keys: ['name', 'modelSeeds', 'sequences']
PASS

All BAP Generator Tests: PASSED
```

---

## Iteration 3: Full Pipeline Test

### Test Case: LNnT (Lacto-N-neotetraose)
- Structure: Gal(b1-4)GlcNAc(b1-3)Gal(b1-4)Glc
- 4 monosaccharides, 3 linkages

### Pipeline Steps
1. **CCD Mapping**: Gal→GAL, GlcNAc→NAG, Gal→GAL, Glc→GLC
2. **BAP Generation**: 3 bondedAtomPairs created
3. **AF3 JSON**: Valid output format

### Results
```
CCD codes: ['GAL', 'NAG', 'GAL', 'GLC']
BAP count: 3
=== PIPELINE TEST: PASSED ===
```

---

## Key Learnings

### Technical Insights
1. **Case Sensitivity**: Python dict lookups are case-sensitive; always normalize string keys
2. **Sialic Acid Exception**: Ketoses use different anomeric positions (C2 vs C1)
3. **BAP Format**: Must include residue1, atom1, residue2, atom2, order

### Code Quality Improvements
1. Added type hints for better IDE support
2. Standardized to lowercase for all key lookups
3. Added docstrings with parameter descriptions

### Remaining Edge Cases
1. Rare monosaccharides not in CCD table
2. Branched glycans with multiple acceptors
3. Custom/modifications to standard monosaccharides

---

## Next Iterations

### Priority 1
- [ ] Add error handling for unknown monosaccharides
- [ ] Support custom CCD mappings via config file
- [ ] Add logging for debugging

### Priority 2
- [ ] Expand benchmark to 50 structures
- [ ] Add unit tests for edge