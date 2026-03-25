# Research Proposal (Tournament Winner Extension)

## Title

**Compiler-NGlycan-IUPAC2BAP: A Deterministic Glycan Input Compiler for Stereochemistry-Reliable AlphaFold 3 Polysaccharide Modeling**

---

## 1. Background

### 1.1 Problem Definition

AlphaFold 3 (AF3) can model glycans, but glycan input representation is highly sensitive: generic ligand formats (especially direct SMILES/userCCD paths) often produce stereochemical and linkage errors in predicted carbohydrate structures. The project problem is:

> Given a glycan in human-used notation (IUPAC-condensed initially), generate AF3-compatible ligand input (`ccdCodes` + `bondedAtomPairs`) such that anomeric configuration, epimer identity, and glycosidic linkage position are preserved at modeling time.

### 1.2 Inputs / Outputs / Constraints

- **Input:** IUPAC-condensed glycan string (phase-1); optional future extensions WURCS/GlycoCT.
- **Output:** AF3 JSON ligand block with ordered `ccdCodes`, explicit `bondedAtomPairs`, and validation metadata.
- **Hard constraints:**
  1. Preserve α/β anomeric intent.
  2. Preserve linkage topology (e.g., 1–3 vs 1–6, branching).
  3. Avoid chemically inconsistent leaving-atom/valence artifacts in known sensitive motifs (e.g., sialic acid cases).
  4. Produce deterministic output for reproducible benchmarking/CI.

### 1.3 Why Existing Solutions Are Insufficient

Recovered references and prior notes show:

1. **AF3 glycan literature** demonstrates BAP is the most reliable syntax, while simplified inputs frequently introduce stereochemistry/linkage errors (`PMC12448869`).
2. **GlyLES** is excellent for IUPAC parsing and SMILES generation, but not a complete AF3 BAP compiler by itself (`PMC10035253`, GitHub `kalininalab/GlyLES`).
3. Existing workflows are often semi-manual and do not provide deterministic, CI-friendly compile+validate loops.

### 1.4 Scope and Non-goals

- **In scope (this proposal):**
  - Deterministic IUPAC→BAP compiler (winner direction C01)
  - Validation and benchmark coupling for reliability
  - Phased support for high-frequency glycan motifs in AF3 use cases
- **Out of scope (initial phase):**
  - Full long-timescale MD as default production path
  - Universal support for every rare monosaccharide day-1
  - New AF3 model training/fine-tuning

---

## 2. Related Work

### 2.1 AF3 and Glycan Modeling

- AF3 foundational architecture and multimolecule prediction capability (Nature AF3 paper: `10.1038/s41586-024-07487-w`).
- Glycan-focused AF3 evaluation shows input syntax is critical and BAP provides highest stereochemical fidelity (`10.1093/glycob/cwaf048`, `PMC12448869`).

### 2.2 Glycan Representation / Conversion Infrastructure

- **GlyLES** provides grammar-based IUPAC parsing and conversion support (`PMC10035253`, `github.com/kalininalab/GlyLES`).
- AF3 internal tooling includes `rdkit_utils` for CCD-like generation from molecular representations, but this does not automatically solve all glycan-specific linkage/stereochemistry caveats (`github.com/google-deepmind/alphafold3/.../rdkit_utils.py`).
- PDB carbohydrate remediation and CCD standardization provide critical ground truth and nomenclature consistency (`PMC8457362`).

### 2.3 Dynamics and Validation Context

- GLYCAM/Web + force-field tooling supports physically informed carbohydrate conformational refinement and simulation (`PMC12247649`, GLYCAM repos).
- AF3 broad benchmark studies indicate strong local modeling but domain-dependent global limitations, reinforcing the value of domain-specific validation gates (`PMC12661943`).

### 2.4 Gap This Proposal Addresses

There is still no widely adopted, deterministic open-source compiler that takes practical glycan notations and emits AF3-ready BAP JSON with explicit chemistry-aware safeguards and benchmark/CI integration. This proposal targets that exact gap.

---

## 3. Proposed Method

### 3.1 High-level Approach

We propose a **deterministic glycan input compiler** that transforms IUPAC-condensed glycans into AF3 BAP JSON by combining parsing, canonical intermediate graphing, CCD mapping, atom-level bond construction, and chemistry-aware validation.

### 3.2 Method Pipeline

1. **Parse Layer (IUPAC → Graph Skeleton)**
   - Use GlyLES-style grammar parsing to recover residue tree and linkage annotations.
2. **Canonical Graph Layer**
   - Convert parse output to canonical residue-linkage graph (stable ordering rules for branch traversal).
3. **CCD Mapping Layer**
   - Map each residue to CCD code candidate set with anomer/ring/isomer constraints.
4. **Bond Construction Layer**
   - Generate `bondedAtomPairs` using atom templates per linkage class.
5. **Sensitive-Motif Patching Layer**
   - Apply explicit patch rules for known leaving-atom/valence pitfalls in sialylated and related motifs.
6. **Validation Layer**
   - Run compile-time checks for anomer consistency, linkage target consistency, valence sanity, and branch completeness.
7. **Emission Layer**
   - Output AF3 JSON fragment plus provenance metadata (rules applied, warnings, confidence tags).

### 3.3 Key Insight

The key insight is that AF3 glycan reliability is less limited by downstream sampling than by **upstream representational ambiguity**. If linkage topology and stereochemical intent are encoded deterministically at atom-pair level before AF3 inference, major failure classes are reduced at source.

### 3.4 Assumptions

- Input glycan can be parsed into an unambiguous rooted graph for the targeted motif set.
- CCD mapping coverage for targeted monosaccharide classes is available or can be curated incrementally.
- AF3 BAP syntax remains stable enough for compiler integration.

### 3.5 Three Testable Contributions

1. **C1 (Primary, technical):** A deterministic IUPAC→BAP compiler that produces AF3-ready JSON and preserves intended anomeric/linkage semantics on a curated benchmark.
2. **C2 (Secondary, analysis):** A chemistry-aware validation framework that classifies and quantifies compile/output failures (epimer, anomer, linkage position, leaving-atom issues).
3. **C3 (Tertiary, resource):** A reproducible benchmark/CI package containing inputs, compiled JSON, AF3 outputs, and scorecards to enable regression tracking and external reuse.

---

## 4. Experiment Plan

### 4.1 Datasets

- **Phase A (MVP):** 50 curated structures covering common N/O-glycan motifs, representative branching, and sensitive linkages.
- **Phase B (Full):** 200 structures with broader motif diversity, including sialylated and complex branches.

Data provenance combines curated references from existing glycan resources and PDB-supported carbohydrate standards (per prior project direction and recovered references).

### 4.2 Baselines

At least three baseline flows:

1. **Baseline-B0:** direct SMILES input flow to AF3 (where applicable)
2. **Baseline-B1:** userCCD/rdkit_utils conversion flow
3. **Baseline-B2:** existing manual BAP template workflow (human-authored)

### 4.3 Metrics

Primary and secondary metrics:

- **Primary metric:** stereochemistry/linkage correctness rate (% structures without critical errors)
- **Secondary metrics:**
  - anomer correctness rate
  - linkage-position correctness rate
  - compile success rate
  - deterministic reproducibility rate (same input → identical JSON)
  - error taxonomy counts by class

### 4.4 Ablation Design

- **Ablation A1:** remove motif-specific patching layer (measure sialic/edge-case degradation)
- **Ablation A2:** remove canonical ordering (measure reproducibility and regression instability)
- **Ablation A3:** remove validation gate (measure downstream undetected failure inflation)

### 4.5 Stage Mapping to Execution

- **Stage 1:** reproduce baseline workflows and benchmark harness
- **Stage 2:** implement and tune core compiler + mapping rules
- **Stage 3:** validate proposed method vs baselines (MVP benchmark)
- **Stage 4:** run ablations and error taxonomy analysis

---

## 5. Expected Results

### 5.1 Quantitative Targets

- **MVP benchmark (50 structures):**
  - ≥95% compile success
  - ≥90% critical stereochemistry/linkage correctness
  - 100% deterministic emission for repeated runs
- **Expanded benchmark (200 structures):**
  - ≥90% compile success
  - ≥85% critical correctness

### 5.2 Qualitative Expectations

- Largest gains vs baselines will appear in branched and sialylated motifs where generic input paths are most error-prone.
- Error types will shift from silent structural failures to explicit, classifiable warnings/fails.
- CI regression dashboards will reveal stable/unstable motif classes and guide prioritized rule extension.

---

## 6. Risks and Mitigations

### 6.1 Technical Risks

1. **Risk:** CCD mapping gaps for rare/modified monosaccharides.
   - **Mitigation:** tiered support matrix + explicit unsupported tags + template contribution path.

2. **Risk:** motif patch rules become brittle or overfit.
   - **Mitigation:** keep rules minimal, evidence-backed, and benchmark-validated; require provenance trace for each patch.

3. **Risk:** AF3 input schema changes.
   - **Mitigation:** schema adapter layer and versioned emitters.

### 6.2 Resource Risks

1. **Risk:** benchmark curation effort larger than expected.
   - **Mitigation:** MVP 50-first phased rollout before 200 expansion.

2. **Risk:** AF3 run budget constraints for large regression matrix.
   - **Mitigation:** prioritized critical-motif smoke set per PR + scheduled full nightly runs.

### 6.3 Evaluation Risks

1. **Risk:** correctness metric misses dynamic plausibility.
   - **Mitigation:** add optional secondary dynamic checks (short GLYCAM rescue subset) for flagged motifs.

### 6.4 Fallback Plans

- If full compiler generality stalls, lock to high-impact motif subset and deliver robust domain-limited version first.
- If automatic repair quality is unstable, keep strict validator-only mode and require manual review for ambiguous cases.

---

## References (from recovered `large_tool_results`)

1. AF3 paper: https://doi.org/10.1038/s41586-024-07487-w
2. AF3 glycan limitations and BAP usage: https://doi.org/10.1093/glycob/cwaf048 (PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC12448869/)
3. GlyLES paper: https://doi.org/10.1186/s13321-023-00704-0 (PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC10035253/)
4. AF3 source + tool references: https://github.com/google-deepmind/alphafold3
5. GLYCAM-Web modeling context: https://pmc.ncbi.nlm.nih.gov/articles/PMC12247649/
6. PDB carbohydrate CCD modernization: https://pmc.ncbi.nlm.nih.gov/articles/PMC8457362/
7. AF3 broad benchmark context: https://pmc.ncbi.nlm.nih.gov/articles/PMC12661943/
