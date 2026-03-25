# Direction Summary (Rebuilt Idea Tournament)

## Tournament Info

- **Seed Direction**: AF3 intrinsic limitations in polysaccharide stereochemistry/linkage fidelity
- **Total Candidates**: 18 (from `idea-tree.md`)
- **Tournament Rounds**: 5 Swiss rounds (from `idea-rankings.md`)
- **Date**: 2026-03-19

## Top-3 Directions

### Direction 1: Compiler-NGlycan-IUPAC2BAP (C01) — Elo: 1561.9

- **Core Idea**: Build an end-to-end compiler that converts IUPAC-condensed glycans into AF3-ready CCD + bondedAtomPairs JSON with deterministic residue ordering and atom-level linkage semantics. The pipeline uses GlyLES-like AST parsing plus curated CCD mapping to eliminate ambiguity before AF3 sampling.
- **Key Strength**: Highest combined **feasibility + relevance + clarity**; directly targets root-cause input ambiguity documented in AF3 glycan studies.
- **Primary Risk**: Rare monosaccharides and tricky motifs (especially sialic/ketose leaving-atom behavior) may cause edge-case failures.
- **Connection to Prior Work**: Leverages GlyLES and AF3 BAP practices (`PMC10035253`, `PMC12448869`, AF3 repo/rdkit_utils), but extends them into a production-grade AF3 compiler workflow.
- **evo-memory Status**: [x] Builds on M_I feasible direction A (Input Format Solutions)

### Direction 2: ConstraintRescoringEnsemble (C14) — Elo: 1548.0

- **Core Idea**: Produce a constrained conformer/model ensemble and re-score candidates with chemistry-aware objectives (stereochemistry, linkage validity, torsion plausibility), selecting the most chemically consistent structure instead of accepting a single AF3 output.
- **Key Strength**: Strong **novelty/impact tradeoff** with manageable engineering scope versus full long-timescale MD.
- **Primary Risk**: Score objective design may overfit to handcrafted constraints and miss valid uncommon conformers.
- **Connection to Prior Work**: Bridges AF3 static outputs with GLYCAM-informed quality heuristics (from recovered GLYCAM references) without requiring expensive full MD as default.
- **evo-memory Status**: [x] New direction adjacent to M_I direction C (Ensemble Generation)

### Direction 3: CommunityBenchmarkArchive (C18) — Elo: 1543.8

- **Core Idea**: Publish a reproducible glycan benchmark archive with canonical inputs, AF3 outputs, validation scorecards, and versioned regression snapshots to drive community comparability and internal CI.
- **Key Strength**: Highest **relevance + scalability** for long-term reliability and external adoption.
- **Primary Risk**: Curation and annotation quality control can become bottleneck if taxonomy and provenance standards are weak.
- **Connection to Prior Work**: Extends benchmark culture from AF3/structure benchmarking literature and incorporates standardized CCD conventions from PDB carbohydrate remediation work.
- **evo-memory Status**: [x] Builds on M_I direction D (Benchmark Development)

## Cross-Direction Analysis

### Common Threads

All top-3 directions prioritize **system reliability over one-off model fixes**: (1) correct input construction, (2) constrained post-generation selection, (3) benchmark/CI reproducibility. This indicates the strongest path is a pipeline architecture rather than isolated algorithmic tweaks.

### Dimension Patterns

Top ideas consistently scored highest on **feasibility and relevance**. Tournament signal suggests this problem benefits most from engineering-rigorous infrastructure (compiler, quality gate, benchmark) before pushing harder into high-cost dynamics-heavy methods.

### Missing Aspects

No top-3 direction fully resolves **long-timescale glycan dynamics** in a first pass. This is acceptable for MVP scope but should remain a Phase-2 extension for flexible/sialylated motifs.

## Recommendation

**Selected for proposal extension**: Direction 1 — **Compiler-NGlycan-IUPAC2BAP (C01)**

**Reasoning**: It is the highest Elo direction and best addresses the root-cause failure mode (input ambiguity), while enabling C14 and C18 as natural downstream amplifiers.

## evo-memory Actions

- [x] Captured top-3 promising directions in this summary.
- [ ] Trigger IDE update in evo-memory process with this top-3 set.
- [x] Preserved optionality: C14 and C18 retained as parallel fallback/augmentation tracks.
