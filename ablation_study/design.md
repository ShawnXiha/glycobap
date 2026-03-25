# Ablation Study Design

## Objective
To quantify the contribution of each core module in GlycoSMILES2BAP pipeline.

## Modules to Ablate

### 1. CCD Mapper Module
- **Function**: Maps monosaccharide names to PDB CCD codes
- **Ablation approach**: Replace with simple name-based lookup (no anomeric/config handling)
- **Expected impact**: Lower epimer and anomeric accuracy

### 2. BAP Generator Module
- **Function**: Generates bondedAtomPairs specifications
- **Ablation approach**: 
  - Ablation 2a: Use linear traversal instead of DFS (affects branched glycans)
  - Ablation 2b: Use default linkage positions instead of explicit positions
- **Expected impact**: Lower linkage accuracy, especially for branched structures

### 3. Anomeric Position Handler
- **Function**: Correctly identifies C1 vs C2 anomeric carbon
- **Ablation approach**: Always use C1 (aldose default)
- **Expected impact**: Major drop in sialic acid accuracy

## Experimental Setup

### Test Dataset
- 50 glycan structures from original benchmark
- Balanced distribution: 15 linear, 20 N-glycans, 10 O-glycans, 5 complex

### Conditions
| Condition | Description |
|-----------|-------------|
| **Full Pipeline** | Complete GlycoSMILES2BAP (baseline) |
| **w/o CCD Mapper** | Simple name lookup, no anomeric/config handling |
| **w/o DFS Traversal** | Linear traversal for BAP generation |
| **w/o Anomeric Handler** | Always use C1 as anomeric carbon |
| **w/o Explicit Linkage** | Use default O4/O3 positions |

### Metrics
- Epimer accuracy (%)
- Anomeric accuracy (%)
- Linkage accuracy (%)
- Processing time (s)

## Expected Results Pattern
1. **w/o CCD Mapper**: Epimer accuracy drops significantly (confusion between Glc/Gal, Man/Glc)
2. **w/o DFS Traversal**: Linkage accuracy drops for branched glycans
3. **w/o Anomeric Handler**: Anomeric accuracy drops for sialic acids (Neu5Ac, Neu5Gc)
4. **w/o Explicit Linkage**: Linkage accuracy drops overall
