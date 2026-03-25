# Evolution Report: Cycle 1 — IDE

**Date**: 2026-03-20
**Trigger**: Completed rebuilt `idea-tournament` (Phase 3 direction summary available), requiring IDE update to M_I.
**Source Artifacts**: `direction-summary.md`, `idea-rankings.md`, `idea-tree.md`, prior `memory/ideation-memory.md`, evo-memory protocol/templates under `/home/qiang/.agents/skills/evo-memory/`.

## Changes Made

### Added

- Structured notation canonicalization for glycan input fidelity in structure prediction: added as new feasible direction (derived from C01 winner, abstracted to reusable level).
- Domain-constraint rescoring for structured-output model selection: added as new feasible direction (derived from C14 rank #2).
- Domain-specific benchmarking with versioned regression CI for structure predictors: added as new feasible direction (derived from C18 rank #3).
- Post-hoc stereochemistry/linkage validation and targeted local repair: added as feasible direction to preserve prior B-direction knowledge in structured schema.

### Updated

- `memory/ideation-memory.md`: migrated from legacy unstructured notes to schema-compliant M_I format (headers/sections/fielded entries).

### Removed/Archived

- None (legacy material retained conceptually and noted under Archive section of M_I).

## Reasoning

This IDE update used the latest tournament evidence where top-3 directions were explicitly ranked and justified (`direction-summary.md`: Direction 1/2/3; `idea-rankings.md`: final Elo table). Per IDE protocol, directions were stored at reusable abstraction level (direction, not implementation artifact). For example, C01 was abstracted away from concrete AF3 JSON/BAP implementation details into a broader direction about canonical representation for input fidelity; this reduces schema-coupling risk and improves transferability to future model/interface changes.

Deduplication logic was applied against prior memory contents: the legacy file already implied A/B/C/D direction families but in unstructured prose. Instead of duplicating near-identical entries, we reconciled and normalized into fielded entries with evidence, status, retrieval tags, and validation plans. We did not mark any direction as unsuccessful because no IVE-classified fundamental failure evidence exists yet.

Judgment calls: (1) retained a structured B-direction entry (post-hoc validation/repair) despite not being top-3 this cycle to prevent loss of prior actionable knowledge; (2) kept statuses as `feasible` for all added entries since there is only one rebuilt tournament cycle of explicit ranking evidence and no exhaustion signal.

## Impact on Future Cycles

- **For idea-tournament**: M_I can now seed Level-1 branches with high-signal reusable directions (canonicalization, constraint rescoring, benchmark+CI) and preserve complementary repair direction; retrieval quality should improve due to explicit tags and evidence fields.
- **For experiment-pipeline**: While M_E is unchanged, the new M_I validation plans provide clearer handoff targets for downstream experiment design and success criteria.
- **Confidence level**: Medium-high. Ranking evidence is explicit and recent (single rebuilt cycle), but multi-cycle confirmation is still pending.

## Raw Evidence Summary

- `direction-summary.md` records top-3 with Elo and final recommendation:
  - Direction 1 C01, Elo 1561.9 (selected for proposal extension)
  - Direction 2 C14, Elo 1548.0
  - Direction 3 C18, Elo 1543.8
- `idea-rankings.md` final table confirms ranking stability after 5 Swiss rounds.
- Prior `ideation-memory.md` had unstructured but matching A/B/C/D research opportunity patterns; converted to structured entries instead of duplicate append.
