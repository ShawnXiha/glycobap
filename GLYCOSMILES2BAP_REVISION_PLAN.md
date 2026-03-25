# GlycoSMILES2BAP Structured Revision Plan

**Document Type**: Experimental Revision Plan
**Created**: 2026-03-23
**Based On**: Peer Review Comments (6 Major + 5 Minor Problems)
**Prior Knowledge**: `/memory/ideation-memory.md`, `/memory/experiment-memory.md`

---

## 1. Assumptions & Scope

### What We Know
- **Existing validation**: n=1000 benchmark completed (97.8% epimer, 97.4% anomeric, 95.9% linkage)
- **Ablation study**: Completed with quantified module contributions (Table 3)
- **GlyTouCan data**: 100 representative structures available, needs expansion with proper IDs
- **Tools**: GlyLES and GlycanFormatConverter mentioned but not systematically compared
- **Experiment memory**: Case-insensitive CCD mapping proven, sialic acid C2 handling validated

### Scope Decisions
- Focus on addressing peer review concerns while maintaining paper structure
- Prioritize P0 tasks that directly affect paper acceptance
- Leverage existing experiment memory for proven strategies

### Out of Scope
- Major algorithmic changes to the core pipeline (validated as working)
- New feature development beyond review requirements

---

## 2. Stages

---

### Stage 1: Benchmark Reconstruction (P0-1)

**Goal**: Reconstruct benchmark with proper GlyTouCan IDs, >=100 structures, transparent train/test split

**Success Signals**:
- [ ] Benchmark contains >=100 glycan structures with GlyTouCan IDs
- [ ] Train/test split documented (80/20 or 70/30)
- [ ] Branching degree and complexity metrics included in dataset description
- [ ] All structures have traceable provenance

**What to Run**:
1. Query GlyTouCan API for diverse glycan structures with complete annotations
2. Select structures covering: N-glycans (bi-, tri-, tetra-antennary), O-glycans, glycolipids, GAGs
3. Assign GlyTouCan IDs (format: GXXXXXMO)
4. Compute complexity metrics:
   - Residue count (min, max, mean)
   - Branching degree (number of branch points)
   - Linkage type diversity (alpha, beta, mixed)
5. Create stratified train/test split by category
6. Document selection criteria and exclusion rules

**Expected Artifacts**:
- `/data/benchmark_v2/structures.json` - Full benchmark with GlyTouCan IDs
- `/data/benchmark_v2/train_set.json` - Training subset
- `/data/benchmark_v2/test_set.json` - Held-out test subset
- `/data/benchmark_v2/complexity_metrics.csv` - Branching degree, size metrics
- Table for manuscript: "Benchmark Dataset Characteristics"

**Dependencies**:
- GlyTouCan API access or local database snapshot
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
1. Curate PDB structures with glycan annotations:
   - Resolution < 2.5 Angstrom for clear electron density
   - Known glycan types: N-glycans, O-glycans, sialylated
2. Extract reference glycan conformations
3. Generate AF3 input using GlycoSMILES2BAP
4. Run AF3 predictions (requires AF3 server access)
5. Compute metrics:
   - RMSD (backbone atoms, glycosidic linkage atoms)
   - Stereochemistry preservation rate
   - Anomeric configuration match
6. Document discrepancies with analysis

**Expected Artifacts**:
- `/validation/af3_pdb_comparison/rmsd_table.csv` - RMSD values per structure
- `/validation/af3_pdb_comparison/stereochemistry_validation.csv` - Pass/fail per criterion
- `/figures/af3_validation_figure.png` - Predicted vs Reference overlay
- Supplementary Table: PDB IDs, glycan types, resolution, RMSD values

**Dependencies**:
- AF3 access (AlphaFold 3 server or local installation)
- PDB structures with quality glycan