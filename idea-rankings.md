# Idea Tournament Phase 2 — Elo Ranking (Swiss, 5 Rounds)

## Tournament Setup

- **Candidate pool:** 18 leaves from `idea-tree.md` (C01–C18)
- **Initial Elo:** 1500 for all candidates
- **K-factor:** 32
- **Dimensions (equal weights):** Novelty / Feasibility / Relevance / Clarity
- **Pairing:** Swiss-style (random Round 1, then near-rating pairing without rematch preference)
- **Rounds:** 5

---

## Candidate Legend

| ID | Candidate |
|---|---|
| C01 | Compiler-NGlycan-IUPAC2BAP |
| C02 | Canonicalizer-WURCS-GlycoCT |
| C03 | SialicLeavingAtomPatcher |
| C04 | GlycolipidGPIComposer |
| C05 | BatchConverterConfidence |
| C06 | ConverterTemplateFallback |
| C07 | PrivateerGateValidator |
| C08 | RDKitLocalRepair |
| C09 | RingPuckerDetector |
| C10 | LinkageTorsionQC |
| C11 | CIQualityGate |
| C12 | ErrorTaxonomyDashboard |
| C13 | AF3+GLYCAM-ShortEnsemble |
| C14 | ConstraintRescoringEnsemble |
| C15 | MDforSialylatedFlexibleChains |
| C16 | TransitionStateAwareEnsemble |
| C17 | GlycoBench50to200 |
| C18 | CommunityBenchmarkArchive |

---

## Round-by-Round Scorecards (Condensed)

> Composite score = average of 4 dimension scores (1–10). Winner determined by higher composite.

### Round 1

| Match | Idea A | Idea B | A Scores (N/F/R/C) | B Scores (N/F/R/C) | Composite A/B | Winner |
|---|---|---|---|---|---|---|
| R1-M1 | C01 | C12 | 8/9/10/9 | 5/8/7/8 | 9.00 / 7.00 | C01 |
| R1-M2 | C17 | C04 | 8/9/10/9 | 7/6/7/7 | 9.00 / 6.75 | C17 |
| R1-M3 | C07 | C15 | 7/9/9/9 | 8/6/8/7 | 8.50 / 7.25 | C07 |
| R1-M4 | C13 | C06 | 7/7/8/8 | 6/8/7/8 | 7.50 / 7.25 | C13 |
| R1-M5 | C03 | C10 | 8/8/9/8 | 7/8/8/8 | 8.25 / 7.75 | C03 |
| R1-M6 | C08 | C14 | 7/8/8/8 | 8/8/9/9 | 7.75 / 8.50 | C14 |
| R1-M7 | C05 | C11 | 6/9/8/8 | 7/9/9/9 | 7.75 / 8.50 | C11 |
| R1-M8 | C02 | C16 | 7/7/8/8 | 8/7/8/7 | 7.50 / 7.50 (tie-break relevance) | C16 |
| R1-M9 | C09 | C18 | 6/7/7/7 | 8/8/10/9 | 6.75 / 8.75 | C18 |

### Round 2

| Match | Idea A | Idea B | Composite A/B | Winner | Key reason |
|---|---|---|---|---|---|
| R2-M1 | C01 | C17 | 8.75 / 8.50 | C01 | Direct root-cause fix outranks benchmark-only route |
| R2-M2 | C07 | C13 | 8.50 / 7.75 | C07 | Validation gate more feasible for immediate reliability |
| R2-M3 | C03 | C14 | 8.00 / 8.50 | C14 | Broader correction+rescoring impact |
| R2-M4 | C16 | C18 | 7.75 / 8.50 | C18 | Community reproducibility + deployment leverage |
| R2-M5 | C11 | C04 | 8.50 / 7.00 | C11 | CI regression prevention is higher systemic value |
| R2-M6 | C10 | C06 | 8.00 / 7.25 | C10 | Better measurable quality signal |
| R2-M7 | C08 | C02 | 8.00 / 7.50 | C08 | Immediate local repair utility |
| R2-M8 | C15 | C12 | 7.75 / 6.75 | C15 | More direct scientific/technical contribution |
| R2-M9 | C05 | C09 | 7.75 / 6.75 | C05 | Better operational utility |

### Round 3

| Match | Idea A | Idea B | Composite A/B | Winner | Key reason |
|---|---|---|---|---|---|
| R3-M1 | C01 | C07 | 8.75 / 8.50 | C01 | Upstream correctness beats downstream-only gate |
| R3-M2 | C17 | C13 | 8.50 / 7.75 | C17 | Benchmark utility > short MD rescue breadth |
| R3-M3 | C18 | C14 | 8.75 / 8.50 | C18 | Stronger relevance and community scaling |
| R3-M4 | C11 | C03 | 8.50 / 8.00 | C11 | CI hardening higher long-term reliability |
| R3-M5 | C16 | C08 | 7.75 / 8.00 | C08 | Better short-cycle feasibility |
| R3-M6 | C10 | C15 | 8.00 / 7.75 | C10 | Cheaper and cleaner metric integration |
| R3-M7 | C05 | C04 | 7.75 / 7.00 | C05 | Higher operational throughput value |
| R3-M8 | C02 | C12 | 7.50 / 6.75 | C02 | Better technical breadth |
| R3-M9 | C06 | C09 | 7.25 / 6.75 | C06 | More practical fallback benefit |

### Round 4

| Match | Idea A | Idea B | Composite A/B | Winner |
|---|---|---|---|---|
| R4-M1 | C01 | C17 | 8.75 / 8.75 | Draw |
| R4-M2 | C07 | C18 | 8.50 / 8.75 | C07 |
| R4-M3 | C13 | C11 | 7.75 / 8.50 | C11 |
| R4-M4 | C14 | C08 | 8.50 / 8.00 | C14 |
| R4-M5 | C10 | C05 | 8.00 / 7.75 | C10 |
| R4-M6 | C03 | C16 | 8.00 / 7.75 | C03 |
| R4-M7 | C15 | C02 | 7.75 / 7.50 | C15 |
| R4-M8 | C06 | C04 | 7.25 / 7.00 | C06 |
| R4-M9 | C09 | C12 | 6.75 / 6.75 (tie-break clarity) | C09 |

### Round 5

| Match | Idea A | Idea B | Composite A/B | Winner | Key reason |
|---|---|---|---|---|---|
| R5-M1 | C01 | C07 | 8.75 / 8.50 | C01 | Most complete root-cause addressability |
| R5-M2 | C17 | C11 | 8.50 / 8.50 (tie-break feasibility) | C17 | Benchmark foundation more directly reusable |
| R5-M3 | C18 | C13 | 8.75 / 7.75 | C18 | Broader relevance and archive reuse |
| R5-M4 | C14 | C10 | 8.50 / 8.00 | C14 | Better integrated selection objective |
| R5-M5 | C03 | C08 | 8.00 / 8.00 (tie-break feasibility) | C08 | Wider repair generality |
| R5-M6 | C15 | C05 | 7.75 / 7.75 (tie-break novelty) | C15 | Stronger scientific novelty |
| R5-M7 | C16 | C06 | 7.75 / 7.25 | C16 | Better scientific upside |
| R5-M8 | C02 | C09 | 7.50 / 6.75 | C02 | Better practical conversion breadth |
| R5-M9 | C04 | C12 | 7.00 / 6.75 | C04 | Higher direct domain utility |

---

## Final Elo Rankings (after 5 rounds)

| Rank | ID | Idea | Elo | W-D-L |
|---:|---|---|---:|---:|
| 1 | **C01** | **Compiler-NGlycan-IUPAC2BAP** | **1561.9** | 4-1-0 |
| 2 | C14 | ConstraintRescoringEnsemble | 1548.0 | 4-0-1 |
| 3 | C18 | CommunityBenchmarkArchive | 1543.8 | 4-0-1 |
| 4 | C11 | CIQualityGate | 1540.5 | 4-0-1 |
| 5 | C17 | GlycoBench50to200 | 1535.3 | 3-1-1 |
| 6 | C07 | PrivateerGateValidator | 1518.1 | 3-0-2 |
| 7 | C08 | RDKitLocalRepair | 1516.1 | 3-0-2 |
| 8 | C10 | LinkageTorsionQC | 1515.9 | 3-0-2 |
| 9 | C15 | MDforSialylatedFlexibleChains | 1515.9 | 3-0-2 |
| 10 | C16 | TransitionStateAwareEnsemble | 1485.5 | 2-0-3 |
| 11 | C03 | SialicLeavingAtomPatcher | 1485.3 | 2-0-3 |
| 12 | C02 | Canonicalizer-WURCS-GlycoCT | 1484.0 | 2-0-3 |
| 13 | C05 | BatchConverterConfidence | 1482.7 | 2-0-3 |
| 14 | C06 | ConverterTemplateFallback | 1481.3 | 2-0-3 |
| 15 | C13 | AF3+GLYCAM-ShortEnsemble | 1457.5 | 1-0-4 |
| 16 | C04 | GlycolipidGPIComposer | 1456.0 | 1-0-4 |
| 17 | C09 | RingPuckerDetector | 1452.0 | 1-0-4 |
| 18 | C12 | ErrorTaxonomyDashboard | 1420.2 | 0-0-5 |

---

## Top-3 for Phase 3 Summarization

1. **C01 — Compiler-NGlycan-IUPAC2BAP (1561.9)**
2. **C14 — ConstraintRescoringEnsemble (1548.0)**
3. **C18 — CommunityBenchmarkArchive (1543.8)**

Convergence note: top-3 stabilized by Rounds 4–5 with only minor internal margin shifts; ranking considered stable for 18-candidate field.
