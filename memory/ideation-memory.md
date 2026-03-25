# Ideation Memory

Last Updated: 2026-03-21
Total Cycles: 3

## Feasible Directions

### Structured notation canonicalization for glycan input fidelity in structure prediction

- **Summary**: Convert human glycan notations into canonical, unambiguous structural representations before model inference to reduce stereochemistry/linkage failures at source.
- **Why Promising**: Highest-ranked direction in latest tournament; directly targets root-cause input ambiguity and has strong feasibility with existing open-source parsing/tooling.
- **Requirements**: Reliable parser stack (e.g., IUPAC-focused initially), residue/linkage canonicalization rules, curated mapping layer, deterministic emission constraints, chemistry-aware validation hooks.
- **Validation Plan**:
  1. Build MVP conversion path for common N/O-glycan motifs.
  2. Compare converted-input predictions against baseline input modes on curated benchmark.
  3. Quantify anomer/linkage correctness and compile determinism.
  4. Analyze edge-case failures (e.g., sialylated motifs) and iterate rules.
- **Evidence**: Idea tournament rebuild (2026-03-19), Rank #1, Elo 1561.9 (`direction-summary.md`, `idea-rankings.md`).
- **Status**: ✅ VALIDATED - Full implementation (GlycoSMILES2BAP) achieves 97.8% epimer, 97.4% anomeric, 95.9% linkage accuracy on n=1000 benchmark. Ablation study confirms all modules essential.
- **Evidence (Updated)**: ESE cycle 2 (2026-03-21) - Experiment pipeline completed successfully. All 4 stages passed. Ablation study quantified module contributions. Paper manuscript updated with Table 3.
- **Related Entries**: Post-hoc stereochemistry/linkage validation and targeted local repair; Domain-constraint rescoring for structured outputs
- **Retrieval Tags**: glycan-input, canonicalization, AF3, stereochemistry, linkage, notation-parsing, BAP
- **Date Added**: 2026-03-20
- **Last Updated**: 2026-03-21

### Domain-constraint rescoring for structured-output model selection

- **Summary**: Use domain-validity constraints to re-rank model/conformer candidates and select chemically/plausibility-consistent outputs instead of single-pass acceptance.
- **Why Promising**: High tournament rank with good novelty-feasibility balance; compatible with multiple post-generation pipelines and not tied to one predictor.
- **Requirements**: Constraint definitions (stereochemistry/linkage/torsion), candidate generation source, scoring aggregator, calibrated thresholding for accept/reject decisions.
- **Validation Plan**:
  1. Implement constrained rescoring over candidate sets.
  2. Benchmark selected-vs-unselected structures on quality metrics.
  3. Run ablation by constraint category to measure marginal utility.
  4. Stress-test on high-flexibility glycan subsets.
- **Evidence**: Idea tournament rebuild (2026-03-19), Rank #2, Elo 1548.0 (`direction-summary.md`, `idea-rankings.md`).
- **Status**: feasible
- **Related Entries**: Structured notation canonicalization for glycan input fidelity in structure prediction; Domain-specific benchmarking with versioned regression CI
- **Retrieval Tags**: rescoring, constraints, ensemble-selection, structural-validity, glycan-quality, post-prediction
- **Date Added**: 2026-03-20
- **Last Updated**: 2026-03-20

### Domain-specific benchmarking with versioned regression CI for structure predictors

- **Summary**: Build benchmark archives with canonical inputs, standardized scorecards, and regression snapshots to expose systematic model weaknesses and prevent silent regressions.
- **Why Promising**: Top-3 ranked direction with strong relevance/scalability; creates reusable evaluation infrastructure independent of any single method implementation.
- **Requirements**: Curated case selection, canonical input packaging, metric definitions, versioned artifact storage, CI integration and reporting.
- **Validation Plan**:
  1. Release MVP benchmark subset with provenance and metrics.
  2. Integrate CI regression checks on representative smoke set.
  3. Expand coverage and track failure taxonomy over versions.
  4. Validate reproducibility via repeated runs/version diffs.
- **Evidence**: Idea tournament rebuild (2026-03-19), Rank #3, Elo 1543.8 (`direction-summary.md`, `idea-rankings.md`).
- **Status**: feasible
- **Related Entries**: Structured notation canonicalization for glycan input fidelity in structure prediction; Post-hoc stereochemistry/linkage validation and targeted local repair
- **Retrieval Tags**: benchmark, regression-ci, reproducibility, structure-prediction, glycan-evaluation, versioning
- **Date Added**: 2026-03-20
- **Last Updated**: 2026-03-20

### Post-hoc stereochemistry/linkage validation and targeted local repair

- **Summary**: Detect stereochemistry/linkage failure classes after prediction and apply bounded, auditable local correction or triage workflows.
- **Why Promising**: Persistently practical direction from prior ideation; complements upstream canonicalization and improves robustness for edge-case motifs.
- **Requirements**: Error taxonomy, validator rules/tooling, local edit policies, provenance logging for correction traceability.
- **Validation Plan**:
  1. Define failure taxonomy and detection rules.
  2. Measure detection recall on curated error cases.
  3. Evaluate correction success and side-effect rates.
  4. Connect fail classes to upstream rule improvements.
- **Evidence**: Prior ideation memory direction B (legacy file content, 2025 cycle notes); reinforced indirectly by tournament QC/repair branches.
- **Status**: feasible
- **Related Entries**: Structured notation canonicalization for glycan input fidelity in structure prediction; Domain-constraint rescoring for structured-output model selection
- **Retrieval Tags**: posthoc-validation, stereochemistry, linkage-errors, local-repair, quality-gate
- **Date Added**: 2026-03-20
- **Last Updated**: 2026-03-20

### Antibody Fc Glycan Optimization Case Study (Idea Tournament Round 2)

- **Summary**: Create comprehensive case study demonstrating GlycoSMILES2BAP application in therapeutic antibody Fc glycan optimization workflow, showing direct connection to drug development.
- **Why Promising**: Highest-ranked idea in Round 2 tournament (Elo 1620); excellent feasibility (9/10) with publicly available data; demonstrates immediate practical value in pharmaceutical industry.
- **Requirements**: Fc glycan variant library design, AF3 prediction pipeline, structural analysis comparing glycan effects on Fc receptor binding, validation against literature experimental data.
- **Validation Plan**:
  1. Select 3-5 Fc glycan variants (G0, G1, G2, afucosylated)
  2. Generate AF3 input using GlycoSMILES2BAP
  3. Predict Fc-glycan complex structures
  4. Analyze glycan effects on FcγR binding sites
  5. Compare with published experimental data
- **Evidence**: Idea Tournament Round 2 (2026-03-21), Rank #1, Elo 1620. Top scores: Feasibility 9/10, Relevance 9/10, Clarity 9/10 (`IDEA_TOURNAMENT_ROUND2_FINAL.md`).
- **Status**: feasible (pending implementation)
- **Related Entries**: GlycoSMILES2BAP validated direction; Error correction case studies
- **Retrieval Tags**: antibody, Fc-glycan, drug-development, therapeutic, case-study, AF3-application
- **Date Added**: 2026-03-21
- **Last Updated**: 2026-03-21

### Glycan Structure Error Correction Case Studies (Idea Tournament Round 2)

- **Summary**: Systematically document cases where GlycoSMILES2BAP corrects common errors in glycan structure prediction, creating a valuable reference showing tool's unique value proposition.
- **Why Promising**: Highest novelty (9/10) in Round 2; demonstrates tool's practical correction capability; creates educational resource for glycobiology community.
- **Requirements**: Literature review of reported glycan structure errors, comparison of SMILES/userCCD vs GlycoSMILES2BAP outputs, visual documentation of corrections, quantitative error reduction analysis.
- **Validation Plan**:
  1. Collect literature-reported stereochemistry errors
  2. Process same structures with GlycoSMILES2BAP
  3. Compare outputs to identify corrections
  4. Document error patterns and corrections
  5. Create visual comparison figures
- **Evidence**: Idea Tournament Round 2 (2026-03-21), Rank #2, Elo 1595. Top scores: Novelty 9/10, Feasibility 9/10 (`IDEA_TOURNAMENT_ROUND2_FINAL.md`).
- **Status**: feasible (pending implementation)
- **Related Entries**: Antibody Fc glycan case; GlyTouCan structure database
- **Retrieval Tags**: error-correction, stereochemistry, validation, case-study, literature-analysis
- **Date Added**: 2026-03-21
- **Last Updated**: 2026-03-21

### GlyTouCan Structure Prediction Database (Idea Tournament Round 2)

- **Summary**: Create publicly accessible database of predicted glycan structures for representative GlyTouCan entries, demonstrating scalability and providing valuable community resource.
- **Why Promising**: Strong scalability demonstration (9/10 feasibility); creates lasting research resource; enables future benchmarking studies.
- **Requirements**: GlyTouCan representative subset selection, batch processing pipeline, structure storage format, public repository setup, metadata documentation.
- **Validation Plan**:
  1. Select top 1000 representative GlyTouCan entries
  2. Implement batch processing with GlycoSMILES2BAP
  3. Generate and store predicted structures
  4. Create public repository with documentation
  5. Enable community access and feedback
- **Evidence**: Idea Tournament Round 2 (2026-03-21), Rank #3, Elo 1585. Top scores: Feasibility 9/10, Clarity 9/10 (`IDEA_TOURNAMENT_ROUND2_FINAL.md`).
- **Status**: feasible (pending implementation)
- **Related Entries**: Glycan error correction cases; Benchmark development
- **Retrieval Tags**: database, GlyTouCan, scalability, community-resource, batch-processing
- **Date Added**: 2026-03-21


- Legacy unstructured ideation notes (2025) were refactored into structured M_I entries on 2026-03-20 and preserved in git/session history.
