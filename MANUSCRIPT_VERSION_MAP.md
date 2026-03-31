# Manuscript Version Map

## Purpose

This file fixes the manuscript source of truth after multiple interrupted EvoScientist resume/restart cycles created duplicated and partially overwritten `md` and `tex` drafts.

Date reviewed: 2026-03-31

## Canonical Source

- Canonical prose source: `manuscript_final.md`
- Canonical submission TeX: `bioinformatics_template/glycosmiles2bap_submission_canonical.tex`

Rationale:
- `manuscript_final.md` is structurally complete from title through references.
- It contains the cleanest end-to-end narrative among the final markdown variants.
- Several newer-looking TeX files were truncated during interrupted runs and are not safe as source-of-truth files.

## Trust Levels

### Tier 1: Use

These files are the only files that should be treated as current source-of-truth manuscript assets.

| File | Role | Status | Notes |
|------|------|--------|-------|
| `manuscript_final.md` | Canonical prose manuscript | Use | Complete title, abstract, methods, results, conclusions, back matter, references |
| `bioinformatics_template/glycosmiles2bap_submission_canonical.tex` | Canonical TeX submission manuscript | Use | Rebuilt from `manuscript_final.md` to provide one compilable TeX entry point |

### Tier 2: Reference Only

These files contain useful material but should not be edited as the primary manuscript.

| File | Status | Why not canonical |
|------|--------|-------------------|
| `manuscript_final_2026年3月23日revision.md` | Reference only | Complete, but includes duplicated/overwritten introduction text from interrupted resume cycles |
| `FINAL_PAPER_STATUS.md` | Reference only | Status report, not manuscript source |
| `memory/MEMORY.md` | Reference only | Project memory summary, not manuscript source |
| `memory/SESSION_SUMMARY_2026-03-28.md` | Reference only | Session history, validation context, not manuscript source |

### Tier 3: Deprecated or Truncated

These files should not be used as the basis for future edits without manual recovery.

| File | Status | Failure mode |
|------|--------|--------------|
| `bioinformatics_template/glycosmiles2bap_SUBMISSION.tex` | Deprecated | Truncated in Data Availability section; mixed 1000-structure claims with incomplete URL |
| `bioinformatics_template/glycosmiles2bap_FINAL.tex` | Deprecated | Truncated in Introduction; not compilable |
| `bioinformatics_template/glycosmiles2bap_COMPLETE.tex` | Deprecated | Truncated in Methods; partial overwrite from older template |
| `bioinformatics_template/part1_intro_final.tex` | Deprecated | Incomplete split-part manuscript fragment |
| `bioinformatics_template/part2_methods_final.tex` | Deprecated | Incomplete split-part manuscript fragment |
| `bioinformatics_template/part3_results_final.tex` | Deprecated | Incomplete split-part manuscript fragment |
| `bioinformatics_template/part4_discussion_final.tex` | Deprecated | Incomplete split-part manuscript fragment |
| `bioinformatics_template/submission_final.tex` | Deprecated | Longer than the truncated files, but still incomplete and cut inside figure block |
| `bioinformatics_template/PAPER_SUBMISSION_READY.tex` | Deprecated | Older branch with 1000-structure framing and different assembly strategy |

## Version History Interpretation

The manuscript appears to have evolved through at least three phases:

1. Early benchmark paper:
   - 50-structure benchmark
   - 98.5 / 98.2 / 96.8 accuracy framing
   - 100 GlyTouCan scalability set

2. Review-strengthening phase:
   - Added tool comparison
   - Added ablation study
   - Added uncertainty reporting and error-handling language
   - Extended PDB validation session notes in memory files

3. Interrupted resume/restart phase:
   - Some files were rewritten from alternate templates
   - Some files switched to 1000-structure language
   - Multiple TeX files were cut off mid-document

## Current Project State

- Scientific direction: validated
- Benchmark and ablation narrative: present
- Review-response strengthening: present in memory and status files
- Manuscript risk: source fragmentation, not missing content
- Immediate working policy: edit only Tier 1 files unless doing targeted recovery

## Editing Policy Going Forward

1. Update prose in `manuscript_final.md` first.
2. Propagate accepted text changes into `bioinformatics_template/glycosmiles2bap_submission_canonical.tex`.
3. Do not resume edits in `glycosmiles2bap_SUBMISSION.tex`, `glycosmiles2bap_FINAL.tex`, or split-part `part*_final.tex`.
4. If old content must be recovered, copy specific passages manually into the canonical files instead of reviving deprecated files wholesale.
