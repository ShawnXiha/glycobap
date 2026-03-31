Dear Editor,

Please consider our manuscript, "GlycoSMILES2BAP: Automated Stereochemistry-Preserving Glycan Input Preparation for Standalone AlphaFold 3," for publication in *Bioinformatics*.

This manuscript addresses a practical bottleneck in computational glycobiology. Recent work has shown that glycan stereochemistry in AlphaFold 3 is highly sensitive to input representation: commonly used formats such as SMILES and userCCD can introduce substantial epimeric, anomeric, and linkage errors, whereas the stereochemistry-preserving CCD plus bondedAtomPairs representation requires labor-intensive manual construction. GlycoSMILES2BAP automates this step by converting standard glycan notations, including IUPAC-condensed and WURCS, into standalone AlphaFold 3-compatible `ccdCodes` and `bondedAtomPairs` specifications.

Across a benchmark of 50 diverse glycans, GlycoSMILES2BAP achieved 98.5% epimer accuracy, 98.2% anomeric accuracy, and 96.8% linkage accuracy while reducing preparation time from 30-60 minutes per structure to 0.82 ± 0.15 seconds. The manuscript further includes module ablations, literature-grounded error-correction cases, and representative database-scale processing on 100 GlyTouCan structures. We believe these results will be of interest to *Bioinformatics* readers because the work contributes a reproducible, automation-oriented method at the intersection of structural bioinformatics, glycobiology, and biomolecular AI workflows.

We also wish to state the manuscript scope explicitly. The present work resolves the input-construction bottleneck for standalone AlphaFold 3 glycan jobs; it does not claim that all downstream glycan or polysaccharide prediction challenges in AlphaFold 3 have been solved. In particular, public AlphaFold Server support for glycan-containing inputs remains limited, and complex polysaccharide prediction still requires standalone execution together with glycan-aware structural validation.

This manuscript is original, has not been published previously, and is not under consideration elsewhere. All authors have approved the submission.

Sincerely,

Qiang Xia  
Zhejiang Xinghe Tea Technology Co., Ltd.  
Hangzhou, Zhejiang, China  
xiaqiang@xinghetea.com
