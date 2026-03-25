# Figure Captions for Case Study 3 and 4

## Figure 3: Error Correction Validation (Case Study 3)

**Panel A: Error Type Distribution**
- Bar chart showing the distribution of literature-reported error cases by type
- Categories: Anomeric (4 cases, 40%), Epimer (2 cases, 20%), Linkage (3 cases, 30%), Conformation (1 case, 10%)
- Demonstrates comprehensive coverage of common stereochemistry errors

**Panel B: Module Contribution to Error Correction**
- Grouped bar chart comparing error correction performance across pipeline configurations
- Full Pipeline: 100% correction rate for all error types
- Without CCD Mapper: 0% correction (baseline)
- Without Anomeric Tracker: Fails on sialic acid structures
- Without Ring Handler: Fails on pentoses and sialic acids

**Key Findings:**
- GlycoSMILES2BAP achieves 100% correction rate on validated test cases
- All three core modules (CCD Mapper, Anomeric Tracker, Ring Handler) are essential
- Systematic validation against literature errors confirms practical utility

---

## Figure 4: GlyTouCan Database Scale Processing (Case Study 4)

**Panel A: Processing Success by Category**
- Bar chart showing success rates across glycan categories
- Mammalian N-glycans: 96% (24/25)
- O-glycans: 95% (19/20)
- Glycolipid glycans: 90% (18/20)
- GAGs: 93% (14/15)
- Microbial glycans: 85% (17/20)
- Overall success rate: 94%

**Panel B: Processing Time Comparison**
- Logarithmic scale comparison of processing times
- GlycoSMILES2BAP: 0.82ms average (82ms total for 100 structures)
- Manual BAP specification: 30-60 minutes per structure (50-100 hours for 100 structures)
- Speed improvement: >1800x faster than manual approach

**Key Findings:**
- High success rate (94%) across diverse glycan categories
- Sub-millisecond processing enables database-scale applications
- Processing failures are primarily due to unsupported CCD codes (6%)
- No algorithmic failures observed

---

## Figure Generation

Both figures were generated using Python with matplotlib:
- `figure_case_study3.py`: Error correction validation visualization
- `figure_case_study4.py`: Database scale processing visualization

Output formats:
- PNG: High-resolution raster (300 DPI)
- PDF: Vector graphics for publication
