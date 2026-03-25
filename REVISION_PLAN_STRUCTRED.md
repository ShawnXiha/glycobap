# GlycoSMILES2BAP Revision Plan

**Document Type**: Structured Experimental Plan  
**Created**: 2026-03-23  
**Based On**: Peer Review Comments (6 Major + 5 Minor Problems)  
**Prior Knowledge**: `/memory/ideation-memory.md`, `/memory/experiment-memory.md`

---

## 1. Assumptions & Scope

### What We Know
- **Existing validation**: n=1000 benchmark already completed (97.8% epimer, 97.4% anomeric, 95.9% linkage)
- **Ablation study**: Completed with quantified module contributions
- **GlyTouCan data**: 100 representative structures available, but needs expansion with proper IDs
- **Tools**: GlyLES and GlycanFormatConverter mentioned but not systematically compared

### Scope Decisions
- Focus on addressing peer review concerns while maintaining paper structure
- Prioritize P0 tasks that directly affect paper acceptance
- Leverage existing experiment memory for proven strategies (case-insensitive CCD mapping, sialic acid handling)

### Out of Scope
- Major algorithmic changes to the core pipeline (validated as working)
- New feature development beyond review requirements

---

## 2. Stages (Numbered)

---

### Stage 1: Benchmark Reconstruction (P0-1)

**Goal**: Reconstruct benchmark with proper GlyTouCan IDs, ≥100 structures, transparent train/test split

**Success Signals**:
- [ ] Benchmark contains ≥100 glycan structures with GlyTouCan IDs
- [ ] Train/test split documented (suggest 80/20 or 70/30)
- [ ] Branching degree and complexity metrics included in dataset description
- [ ] All structures have traceable provenance

**What to Run**:
1. Query GlyTouCan API for diverse glycan structures with complete annotations
2. Select structures covering: N-glycans (bi-, tri-, tetra-antennary), O-glycans, glycolipids, GAGs
3. Assign GlyTouCan IDs (format: GXXXXXMO)
4. Compute branching degree and complexity metrics (residue count, linkage types)
5. Create stratified train/test split by category
6. Document selection criteria and exclusion rules

**Expected Artifacts**:
- `/data/benchmark_v2/structures.json` - Full benchmark with GlyTouCan IDs
- `/data/benchmark_v2/train_set.json` - Training subset
- `/data/benchmark_v2/test_set.json` - Held-out test subset
- `/data/benchmark_v2/complexity_metrics.csv` - Branching degree, size metrics

**Dependencies**: 
- Requires GlyTouCan API access or local database snapshot
- Builds on existing `/data/glytoucan_representative_structures.json`

---

### Stage 2: AF3 Structural Validation (P0-2)

**Goal**: Validate AF3 output structures against PDB reference structures (10-20 cases)

**Success Signals**:
- [ ] 10-20 glycan structures with PDB references identified
- [ ] AF3 predictions generated using GlycoSMILES2BAP inputs
- [ ] RMSD comparison between predicted and reference structures
- [ ] Stereochemistry validation (anomeric, epimer, linkage)

**What to Run**:
1. Curate PDB structures with glycan annotations (resolution < 2.5Å)
2. Extract reference glycan conformations
3. Generate AF3 input using GlycoSMILES2BAP
4. Run AF3 predictions (note: requires AF3 access)
5. Compute RMSD and stereochemistry metrics
6. Document any discrepancies

**Expected Artifacts**:
- `/validation/af3_pdb_comparison/` - Directory with comparison results
- `/validation/af3_pdb_comparison/rmsd_table.csv` - RMSD values
- `/validation/af3_pdb_comparison/stereochemistry_validation.csv`
- Figure for manuscript: Predicted vs Reference overlay

**Dependencies**:
- AF3 access (AlphaFold 3 server or local installation)
- PDB structures with quality glycan electron density
- **Blocks Stage 3 until complete**

---

### Stage 3: Statistical Methods Correction (P0-3)

**Goal**: Replace inappropriate t-test with bootstrap confidence intervals for proportion data

**Success Signals**:
- [ ] t-test removed from accuracy comparisons
- [ ] Bootstrap CI (1000+ iterations) reported for all accuracy metrics
- [ ] McNemar's test used for paired categorical comparisons
- [ ] Statistical methods section updated

**What to Run**:
1. Implement bootstrap sampling (n=