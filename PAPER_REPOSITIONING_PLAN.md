# Paper Repositioning Plan

Date: 2026-03-31

## Goal

Reframe the manuscript from a claim about "solving AF3 polysaccharide prediction" to a narrower and more defensible claim about solving the **input-construction bottleneck** for standalone AlphaFold 3 glycan modeling.

## Core positioning

### Old framing to avoid

- solved AF3 glycan or polysaccharide modeling
- validated through the public AlphaFold Server
- end-to-end AF3 prediction problem resolved

### New framing to adopt

- automated compiler from standard glycan notations to standalone AF3-compatible `ccdCodes + bondedAtomPairs`
- stereochemistry-preserving input generation for AF3 glycan jobs
- reproducible and scalable input preparation
- enabling technology for future standalone AF3 glycan and polysaccharide studies

## Claim hierarchy

### Primary claim

GlycoSMILES2BAP automatically generates stereochemistry-preserving AF3-compatible glycan input from IUPAC-condensed and WURCS notations.

### Secondary claim

The generated input is substantially more accurate and scalable than SMILES- or userCCD-based preparation, based on benchmark, ablation, and reference validation.

### Limitation boundary

The method resolves input construction, not the full downstream prediction problem. Public AlphaFold Server support for glycan-containing jobs remains limited, and full end-to-end validation for complex polysaccharides still depends on standalone AF3 access plus glycan-aware structural validation.

## Section-by-section edits

### Abstract

- replace broad "enabling accurate, reproducible structure prediction" with narrower "enabling accurate, reproducible AF3 input preparation"
- add one sentence making standalone AF3 scope explicit

### Introduction

- keep Huang et al. problem setup
- add a scope boundary sentence:
  - this work targets AF3 input construction rather than all downstream glycan prediction failures

### Methods

- keep technical content
- prefer "standalone AF3-compatible JSON" where precision matters

### Results

- keep benchmark and ablation claims
- avoid implying these are end-to-end server prediction results

### Discussion / Limitations

- explicitly state that public AlphaFold Server is not currently a suitable validation route for glycan-containing jobs
- state that downstream AF3 behavior on complex polysaccharides remains an open problem
- keep Privateer/PDB validation as orthogonal support

### Conclusion

- conclude on input generation, reproducibility, and scalability
- avoid claiming resolution of AF3 polysaccharide prediction itself

## Safe manuscript sentence

"GlycoSMILES2BAP resolves the AF3 glycan input-specification bottleneck by generating stereochemistry-preserving `ccdCodes` and `bondedAtomPairs` from standard glycan notations. However, public AlphaFold Server support for glycan-containing inputs remains limited, and full end-to-end validation for complex polysaccharides depends on standalone AF3 execution and downstream glycan-aware structural validation."
