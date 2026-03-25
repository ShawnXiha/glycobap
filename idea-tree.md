# Idea Tournament Rebuild (AF3 Polysaccharide)

## Context and Inputs

- **User goal (G):** Resolve AF3 intrinsic limitations for polysaccharide stereochemistry and linkage correctness with implementable, open-source-first routes.
- **Prior ideation memory (M_I):** `/home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides/memory/ideation-memory.md`
  - **Top-2 retrieved feasible directions (k_I=2):**
    1. **Direction A (Input Format Solutions)** — automate robust glycan input construction.
    2. **Direction B (Post-Hoc Correction)** — detect/repair stereochemical/linkage errors.
  - **Fundamental-failure pruning from M_I:** none explicitly recorded.
- **Recovered open-source references (from `large_tool_results/`):**
  - AF3 glycan limitations + BAP efficacy: https://pmc.ncbi.nlm.nih.gov/articles/PMC12448869/
  - GlyLES (IUPAC→SMILES): https://github.com/kalininalab/GlyLES
  - AF3 code + rdkit_utils: https://github.com/google-deepmind/alphafold3
  - GLYCAM modeling pipeline: https://pmc.ncbi.nlm.nih.gov/articles/PMC12247649/
  - PDB carbohydrate CCD normalization: https://pmc.ncbi.nlm.nih.gov/articles/PMC8457362/
  - AF3 broad benchmark context: https://pmc.ncbi.nlm.nih.gov/articles/PMC12661943/

---

## Phase 1 Tree (One-axis-per-level)

### Level 0 (Seed)

**S0.** AF3 polysaccharide modeling reliability for stereochemistry, anomeric linkage, and deployable workflow quality.

### Level 1 (Technique, 3 branches)

1. **T1 – Input-Compiler Path** (pre-AF3 structural specification)
2. **T2 – Post-Hoc Validation/Repair Path** (after AF3 generation)
3. **T3 – Hybrid Ensemble+Benchmark Path** (generation + dynamic/benchmark coupling)

### Level 2 (Domain, 6 branches)

- **T1-D1:** N/O-glycan chain compiler for AF3 JSON/BAP.
- **T1-D2:** Extended glycoconjugates (glycolipid/GPI/sulfated motifs) compiler.
- **T2-D1:** Stereochemistry and linkage quality control stack.
- **T2-D2:** Automated local correction and re-scoring stack.
- **T3-D1:** MD-informed ensemble rescue for flexible glycans.
- **T3-D2:** Glycan-specific benchmark and continuous evaluation.

### Level 3 (Formulation leaves, N_I=18)

> Target range 15–21 satisfied (N_I=18). Below each leaf follows **Propose → Review → Refine** compactly.

#### T1-D1 leaves (input compiler for N/O glycans)

**C01 — Compiler-NGlycan-IUPAC2BAP**
- Propose: Build IUPAC-condensed → AF3 BAP JSON compiler using GlyLES parse graph + CCD atom-map templates for N-glycans.
- Review: Distinct from format-converter-only ideas because it emits AF3-ready bondedAtomPairs with atom-level linkage semantics.
- Refine: Prioritize β/α linkage fidelity and deterministic residue ordering; output reproducible JSON with validation hooks.

**C02 — Canonicalizer-WURCS-GlycoCT**
- Propose: Multi-format normalizer (WURCS/GlycoCT/IUPAC) to canonical intermediate graph before BAP emission.
- Review: Distinct axis is interoperability breadth, but risk is parser edge-case complexity.
- Refine: Restrict initial scope to human-relevant monosaccharides; surface unsupported motifs explicitly.

**C03 — SialicLeavingAtomPatcher**
- Propose: Dedicated patcher for ketose/sialic leaving-atom anomalies before BAP model generation.
- Review: Highly targeted and practical per AF3 glycan literature caveat on leaving-group behavior.
- Refine: Implement motif-level patch rules with auditable before/after atom diff records.

#### T1-D2 leaves (extended glycoconjugates)

**C04 — GlycolipidGPIComposer**
- Propose: Compose glycan-lipid/GPI templates (e.g., ceramide-linked motifs) with curated bond templates.
- Review: Useful but not directly highest-frequency AF3 failure mode for current project.
- Refine: Keep as extension module after core N/O-glycan path stabilizes.

**C05 — BatchConverterConfidence**
- Propose: Batch compile many glycans and attach confidence flags based on motif support and parser certainty.
- Review: Distinct operationally (throughput + triage), moderate novelty.
- Refine: Include confidence dimensions: parser certainty, CCD coverage, linkage rule certainty.

**C06 — ConverterTemplateFallback**
- Propose: If full compile fails, auto-fallback to nearest validated motif templates and emit partial constrained JSON.
- Review: Improves robustness but risks silent correctness degradation.
- Refine: Only allow fallback with explicit degraded-mode tags and hard validation warnings.

#### T2-D1 leaves (QC validation stack)

**C07 — PrivateerGateValidator**
- Propose: AF3 output gate integrating Privateer-like stereochemistry checks plus linkage atom-consistency checks.
- Review: Strong feasibility and immediate practical value; distinct from correction strategy.
- Refine: Define fail classes: epimer, anomer, linkage-position, valence/leaving-group errors.

**C08 — RDKitLocalRepair**
- Propose: Local graph-level repair proposals using constrained RDKit transformations for specific error classes.
- Review: Distinct from pure validator; feasible for bounded corrections but risk of unintended side-effects.
- Refine: Enforce single-error local edits + structural sanity + provenance log for each fix.

**C09 — RingPuckerDetector**
- Propose: Detect ring pucker plausibility anomalies and annotate high-risk residues for downstream MD rescue.
- Review: Scientifically relevant, but less direct than linkage/stereo hard-errors for MVP.
- Refine: Reframe as supporting metric module, not standalone decision gate.

#### T2-D2 leaves (correction + quality system)

**C10 — LinkageTorsionQC**
- Propose: Glycosidic torsion profile QC against empirical/curated ranges by linkage class.
- Review: Distinct quality axis (conformation profile) and complementary to stereochemistry checks.
- Refine: Position as ranking signal for model selection rather than hard reject criterion in MVP.

**C11 — CIQualityGate**
- Propose: Continuous evaluation pipeline that runs compile→AF3→validate on regression panel each change.
- Review: High feasibility and long-term reliability leverage; strong clarity.
- Refine: Include mandatory fail-on-regression policy for top critical motifs.

**C12 — ErrorTaxonomyDashboard**
- Propose: Dashboard categorizing AF3 glycan failures by type and frequency over benchmark set.
- Review: Valuable observability, but secondary versus direct correction/compile pipeline.
- Refine: Keep lightweight; export machine-readable error registry for automatic triage.

#### T3-D1 leaves (ensemble + dynamics)

**C13 — AF3+GLYCAM-ShortEnsemble**
- Propose: AF3 static outputs followed by short GLYCAM minimization/relaxation ensemble to improve plausible conformers.
- Review: Distinct dynamic axis and literature-supported, but adds compute/time.
- Refine: Bound to short-window rescue mode for flagged flexible residues only.

**C14 — ConstraintRescoringEnsemble**
- Propose: Generate limited conformer ensemble then re-score with stereochemistry/linkage/torsion constraints to select best.
- Review: Strong balance of feasibility and impact; less expensive than full MD.
- Refine: Use multi-score objective combining hard chemistry constraints + benchmark similarity scores.

**C15 — MDforSialylatedFlexibleChains**
- Propose: Targeted MD for high-flexibility sialylated motifs where static AF3 often degrades.
- Review: Focused and plausible but narrower applicability.
- Refine: Trigger only on motif-risk rules to constrain compute budget.

#### T3-D2 leaves (benchmark + ecosystem)

**C16 — TransitionStateAwareEnsemble**
- Propose: Evaluate whether AF3/ensemble captures catalytically relevant non-ground-state ring/linkage conformers.
- Review: High scientific novelty, medium feasibility due to annotation burden.
- Refine: Start with curated enzyme-substrate subset (MAN1A1-like cases).

**C17 — GlycoBench50to200**
- Propose: Build phased glycan benchmark (50 MVP → 200 full) with stereochemistry/linkage/torsion metrics.
- Review: Extremely useful for community and internal evaluation; high feasibility for MVP subset.
- Refine: Define strict inclusion criteria and per-case provenance to avoid noisy labels.

**C18 — CommunityBenchmarkArchive**
- Propose: Public benchmark archive with reproducible JSON inputs, outputs, and validation scorecards.
- Review: High relevance and clarity; strongest community multiplier.
- Refine: Couple archive release to CIQualityGate for continuously updated trusted baselines.

---

## Pruning Log

- **Pruned none as fundamentally infeasible** (no M_I fundamental-failure conflicts).
- **Deferred priority (not pruned) notes:** C04/C09/C12 remain valid but lower MVP priority due to weaker direct impact on immediate AF3 input correctness.

## Diversity Check

- **Inter-branch diversity (L1):** compile vs validate/repair vs ensemble/benchmark are paradigm-distinct.
- **Intra-branch diversity (L2):** each domain imposes different constraints (input representation, chemistry QC, dynamics/benchmarking).
- **Leaf diversity (L3):** leaves map to distinct success criteria (correctness, robustness, observability, dynamic plausibility, benchmark scalability).

---

## Output for Phase 2

Leaf candidate IDs for tournament ranking:

`C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12, C13, C14, C15, C16, C17, C18`
