# GlycoBAP

GlycoBAP is a research project around `GlycoSMILES2BAP`, an automated pipeline for converting standard glycan notations into AlphaFold 3 compatible CCD + bondedAtomPairs (BAP) input.

This repository has been cleaned after multiple interrupted EvoScientist runs. Repeated manuscript drafts, broken TeX files, and transient status notes were removed. What remains is the project core:

- project design and planning
- experiment process and logs
- key results and supporting outputs
- revision/improvement trace
- long-term memory and session memory
- one canonical manuscript source and one canonical submission TeX

## Current Canonical Files

- Prose manuscript: [`manuscript_final.md`](./manuscript_final.md)
- Submission TeX: [`bioinformatics_template/glycosmiles2bap_submission_canonical.tex`](./bioinformatics_template/glycosmiles2bap_submission_canonical.tex)
- Version policy: [`MANUSCRIPT_VERSION_MAP.md`](./MANUSCRIPT_VERSION_MAP.md)

## Repository Structure

### Core documents

- [`plan.md`](./plan.md): main project execution plan
- [`success_criteria.md`](./success_criteria.md): success targets for the project
- [`direction-summary.md`](./direction-summary.md): condensed research direction summary
- [`idea-tree.md`](./idea-tree.md): structured ideation tree
- [`idea-rankings.md`](./idea-rankings.md): ranked ideas from the tournament process
- [`IDEA_TOURNAMENT_ROUND2_FINAL.md`](./IDEA_TOURNAMENT_ROUND2_FINAL.md): final round-2 ideation outcome
- [`GLYCOSMILES2BAP_REVISION_PLAN.md`](./GLYCOSMILES2BAP_REVISION_PLAN.md): revision and strengthening plan
- [`PAPER_PLAN_F12_F3_FULL.md`](./PAPER_PLAN_F12_F3_FULL.md): paper planning artifact
- [`references.md`](./references.md): reference notes and literature anchors

### Experiment process

- [`experiment_log.md`](./experiment_log.md): main experiment and iteration log
- [`AF3_RUN_GUIDE.md`](./AF3_RUN_GUIDE.md): AF3-related validation and run guide

### Results and analysis

- [`figures_tables.md`](./figures_tables.md): figure and table inventory
- [`supplementary_analyses.md`](./supplementary_analyses.md): supporting analysis notes
- [`results/`](./results): benchmark outputs, validation artifacts, charts, and summary reports
- [`data/`](./data): datasets, processed outputs, and data documentation
- [`supplementary_materials/`](./supplementary_materials): supplementary tables and error-case material

### Code

- [`src/`](./src): main implementation
- [`GlycoSMILES2BAP/src/`](./GlycoSMILES2BAP/src): package-style source snapshot
- [`scripts/`](./scripts): validation and batch execution scripts
- [`experiments/`](./experiments): experiment runners and stage-specific code
- [`tests/`](./tests): test coverage for the pipeline

### Memory

- [`memory/`](./memory): persistent project memory, experiment memory, ideation memory, session memory
- [`memory/evolution-reports/`](./memory/evolution-reports): structured evolution reports across cycles

## What Was Removed

The cleanup removed:

- duplicated manuscript drafts
- truncated or overwritten TeX manuscript files
- transient completion/status markdown files generated during interrupted agent runs
- generated LaTeX auxiliary files

The cleanup intentionally did not remove:

- design and ideation artifacts
- experiment logs and result files
- memory records
- source code, data, and validation outputs

## Recommended Reading Order

1. [`README.md`](./README.md)
2. [`MANUSCRIPT_VERSION_MAP.md`](./MANUSCRIPT_VERSION_MAP.md)
3. [`plan.md`](./plan.md)
4. [`direction-summary.md`](./direction-summary.md)
5. [`experiment_log.md`](./experiment_log.md)
6. [`manuscript_final.md`](./manuscript_final.md)
7. [`memory/MEMORY.md`](./memory/MEMORY.md)

## Manuscript Workflow

If the paper needs further revision:

1. Edit [`manuscript_final.md`](./manuscript_final.md) first.
2. Sync accepted changes into [`bioinformatics_template/glycosmiles2bap_submission_canonical.tex`](./bioinformatics_template/glycosmiles2bap_submission_canonical.tex).
3. Do not recreate or resume old draft families.

## Notes

- The project still contains historical result variants from different experimental phases. Before submission, metrics in the markdown manuscript and canonical TeX should be checked for full numerical consistency.
- The `memory` directory is intentionally preserved in full because it captures the agentic research trajectory, debug history, and revision rationale.
