# AF3 Server Polysaccharide Limitation and Solution Memo

Date: 2026-03-31

## Executive conclusion

The current blocker is not primarily our JSON generation. The blocker is that the public AlphaFold Server and standalone AlphaFold 3 use different input dialects, and the public server does not currently support translating glycan-containing `alphafoldserver` JSON into the standalone `alphafold3` format. For pure glycans or complex branched glycans/polysaccharides, uploading our generated JSON to the public server is therefore not a valid validation route.

This means:

1. `GlycoSMILES2BAP` can still be a valid contribution as an **input compiler** for standalone AF3.
2. The paper should **not** claim that the AF3 server route is solved.
3. If we want true AF3 prediction results on glycans/polysaccharides, the highest-confidence path is still **standalone AF3 with approved model parameters**.

## What the official AF3 documentation says

### 1. Public server and standalone AF3 are different

The official AlphaFold 3 repository states that the public server is available, but with a **more limited set of ligands and covalent modifications** than standalone AF3.

Source:
- https://github.com/google-deepmind/alphafold3

Relevant lines:
- README: the public server is available "with a more limited set of ligands and covalent modifications."

### 2. Standalone AF3 supports the flexible JSON features we need

The official `docs/input.md` states that the standalone `alphafold3` format offers more flexibility for:

- custom ligands
- branched glycans
- covalent bonds between entities
- `bondedAtomPairs`

Source:
- https://raw.githubusercontent.com/google-deepmind/alphafold3/main/docs/input.md

### 3. Glycans in `alphafoldserver` JSON are explicitly not supported by the converter

The same official AF3 input documentation says:

- if the detected input format is `alphafoldserver` and that JSON specifies glycans, the converter raises an error
- translating glycans from `alphafoldserver` format to `alphafold3` format is not currently supported

Source:
- https://raw.githubusercontent.com/google-deepmind/alphafold3/main/docs/input.md

This is the key reason your server upload path fails.

## What this means for our current project

## Diagnosis

Our project solves:

- conversion from IUPAC/WURCS to AF3-style `ccdCodes` + `bondedAtomPairs`
- stereochemistry-preserving glycan input generation
- batch generation of standalone AF3-compatible JSON

Our project does **not** yet solve:

- public AlphaFold Server compatibility for pure glycans or complex polysaccharides
- AF3 model-weight access approval
- AF3's own downstream handling of all polysaccharide classes after input generation

## Therefore the paper's strongest defensible claim is

`GlycoSMILES2BAP solves the input-generation bottleneck for standalone AF3 glycan modeling, but does not remove current AF3 server and model-level limitations for polysaccharide prediction.`

That is a much safer claim than "we solved AF3 polysaccharide modeling."

## Practical solution paths

## Path A: Exact AF3 route, strongest but blocked by access

Goal:
- obtain actual AF3 predictions using the intended `alphafold3` dialect

Required steps:
- obtain approved AlphaFold 3 model parameters from Google
- run standalone AF3 locally or on institutional GPU
- use our generated `alphafold3` JSON directly
- validate predicted glycans with glycan-specific quality checks

Why this is the correct route:
- it bypasses the public server dialect limitation
- it preserves `bondedAtomPairs`
- it is the only route fully aligned with our current pipeline design

Operational note:
- the official repo says model parameters must be requested from Google and access is granted at Google's discretion

Source:
- https://github.com/google-deepmind/alphafold3

Assessment:
- Best scientific fit
- Currently blocked only by parameter access and compute

## Path B: Collaborator route for standalone AF3

If direct parameter approval is slow or denied, the next-best route is:

- collaborate with a lab that already has approved AF3 weights
- provide them our generated JSON plus minimal execution instructions
- ask them to run a narrow validation panel instead of a full benchmark

Recommended validation subset:
- one linear glycan
- one sialylated glycan with C2 anomeric dependence
- one branched N-glycan
- one sulfated or repeating polysaccharide fragment

Why this helps:
- it validates the central technical claim without waiting for full infrastructure setup
- it is more credible than public-server screenshots

## Path C: Keep the paper, but reposition the contribution

If AF3 weights remain inaccessible, the paper can still be publishable if the scope is tightened.

Recommended framing:
- input compiler / canonicalization tool
- stereochemistry-preserving AF3 JSON generation
- benchmarked syntax correctness and literature/PDB validation
- enabling technology for future standalone AF3 glycan studies

Claims to avoid:
- "solves AF3 polysaccharide prediction"
- "validated on AlphaFold Server"
- "end-to-end AF3 prediction established for complex polysaccharides"

Recommended revised limitation statement:
- "The current work resolves AF3 input construction rather than the full downstream prediction problem. Public AlphaFold Server routes remain limited for glycan-containing jobs, and standalone AF3 validation depends on model parameter access and glycan-aware structural assessment."

## Path D: Use orthogonal validation instead of server validation

If the real scientific question is whether our generated structures are chemically correct before AF3 inference, then orthogonal validation is a reasonable substitute.

Two practical options:

1. PDB-grounded validation
- compare generated CCD/BAP specifications against known experimentally resolved glycan structures
- especially useful for branch topology, anomeric position, and uncommon sugar mapping

2. Privateer-based structure validation
- validate stereochemistry, ring conformation, connectivity, and geometry on predicted or reference structures

Useful sources:
- Privateer validation docs: https://cloud.ccp4.ac.uk/manuals/html-taskref/doc.task.Privateer.html
- CCP4/Privateer overview: https://ftp.ccp4.ac.uk/ccp4/7.0/unpacked/checkout/ccp4i2/docs/tasks/privateer_validate/index.html
- N-glycan validation paper: https://pubmed.ncbi.nlm.nih.gov/37219590/

Assessment:
- Good for paper strengthening
- Does not prove AF3 server compatibility
- Does help prove that our compiler preserves chemically meaningful glycan information

## Path E: Alternative predictors for exploratory comparison

If the goal is to get a working predictor for glycan-containing complexes while AF3 remains blocked, an alternative model can be used as a side experiment, but not as a substitute claim for AF3.

### Chai-1

The Chai-1 repository says it supports:

- proteins
- ligands
- glycosylations
- user constraints including covalent bonds
- advanced contexts for branched ligands

Source:
- https://github.com/chaidiscovery/chai-lab

Assessment:
- Real fallback for exploratory modeling
- stronger than public AF3 server for flexible local experimentation
- should be presented as an alternative predictor, not as AF3 validation

### Glycosylator

Glycosylator is useful for:

- glycan and glycoprotein modeling
- topology construction
- clash reduction and conformational sampling

Source:
- https://github.com/tlemmin/glycosylator

Assessment:
- better for structure building/refinement than for AF3-equivalent benchmarking
- useful as a complementary modeling or preprocessing tool

## Important scientific caveat: even AF3 does not fully solve polysaccharides

Recent glycobiology analysis emphasizes that AF3 glycan modeling is context dependent and still has important failure modes.

Relevant observations from Huang et al.:
- AF3 can generate plausible glycan-protein complex models in some contexts
- but incorrect stereochemistry, linkages, or conformations still occur
- confidence metrics like pLDDT are not reliable for glycan quality
- longer HS/CS polymers and some complex polysaccharides remain problematic
- glycan dynamics often require complementary methods such as MD or ensemble approaches

Source:
- https://academic.oup.com/glycob/article/35/10/cwaf048/8242499

Implication for our paper:
- even with standalone AF3 access, the strongest honest claim is still around **input quality and reproducibility**, not universal polysaccharide correctness

## Recommended decision for this project

## Immediate recommendation

Use the following project position going forward:

1. Treat public AlphaFold Server as **not a viable validation target** for our glycan JSON workflow.
2. Treat standalone AF3 as the intended downstream engine.
3. Keep the paper centered on:
   - input canonicalization
   - CCD/BAP generation
   - stereochemistry preservation
   - benchmark and ablation results
4. Add a clear limitation:
   - public server incompatibility for glycan-containing jobs
   - downstream AF3 polysaccharide behavior remains partially unresolved

## Best next experiment

The highest-value next experiment is not another server upload attempt.

It is:

- secure standalone AF3 access, or
- obtain one collaborator-run standalone AF3 validation panel, or
- add a rigorous orthogonal validation section using PDB references plus Privateer

## Suggested manuscript language

You can safely use language close to:

"GlycoSMILES2BAP resolves the AF3 glycan input-specification bottleneck by generating stereochemistry-preserving `ccdCodes` and `bondedAtomPairs` from standard glycan notations. However, public AlphaFold Server support for glycan-containing inputs remains limited, and full end-to-end validation for complex polysaccharides depends on standalone AF3 execution and downstream glycan-aware structural validation."

## Source list

- AlphaFold 3 repository: https://github.com/google-deepmind/alphafold3
- AlphaFold 3 input documentation: https://raw.githubusercontent.com/google-deepmind/alphafold3/main/docs/input.md
- AF3 issue on branched glycans: https://github.com/google-deepmind/alphafold3/issues/288
- AF3 issue on glycosylation input confusion: https://github.com/google-deepmind/alphafold3/issues/216
- AF3 issue on local glycan prediction mismatch: https://github.com/google-deepmind/alphafold3/issues/406
- JAAG compatibility note: https://github.com/google-deepmind/alphafold3/issues/537
- Chai-1 repository: https://github.com/chaidiscovery/chai-lab
- Glycosylator repository: https://github.com/tlemmin/glycosylator
- Privateer docs: https://cloud.ccp4.ac.uk/manuals/html-taskref/doc.task.Privateer.html
- Privateer validation page: https://ftp.ccp4.ac.uk/ccp4/7.0/unpacked/checkout/ccp4i2/docs/tasks/privateer_validate/index.html
- Privateer N-glycan paper: https://pubmed.ncbi.nlm.nih.gov/37219590/
- Modeling glycans with AF3: https://academic.oup.com/glycob/article/35/10/cwaf048/8242499
