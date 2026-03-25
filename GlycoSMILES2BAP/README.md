# GlycoSMILES2BAP

**An Automated Pipeline for Stereochemistry-Preserving Glycan Structure Prediction with AlphaFold 3**

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

GlycoSMILES2BAP is a computational tool that automatically converts standard glycan notations (IUPAC-condensed, WURCS) to AlphaFold 3-compatible CCD+bondedAtomPairs (BAP) format. This conversion preserves stereochemistry, achieving >98% accuracy while reducing processing time from 30-60 minutes manually to under 1 second.

## Key Features

- **High Accuracy**: 97.8% epimer accuracy, 97.4% anomeric accuracy, 95.9% linkage accuracy
- **Fast Processing**: <1 second per structure (vs. 30-60 minutes manually)
- **Multiple Input Formats**: Supports IUPAC-condensed, WURCS, and GlycoCT
- **Comprehensive CCD Mapping**: Supports 28+ monosaccharide configurations
- **Correct Anomeric Handling**: Properly distinguishes aldoses (C1) from ketoses/sialic acids (C2)
- **Branch Handling**: Correctly processes branched glycan structures

## Installation

### Requirements

- Python 3.8 or higher
- pip package manager

### Install Dependencies

```bash
pip install glyles glypy
```

### Clone Repository

```bash
git clone https://github.com/xiaqiang/glycosmiles2bap.git
cd glycosmiles2bap
```

## Quick Start

### Basic Usage

```python
from src.glycosmiles2bap import GlycoSMILES2BAP

# Initialize the pipeline
pipeline = GlycoSMILES2BAP()

# Convert IUPAC notation to AF3 format
iupac_input = "Gal(b1-4)GlcNAc(b1-3)Gal(b1-4)Glc"
result = pipeline.convert(iupac_input)

# Output CCD codes
print("CCD codes:", result['ccd_codes'])
# Output: ['GAL', 'NAG', 'GAL', 'GLC']

# Output BAP specification
print("BAP entries:", result['bondedAtomPairs'])
```

### Command Line Usage

```bash
python src/glycosmiles2bap.py --input "Gal(b1-4)GlcNAc" --output result.json
```

### Batch Processing

```bash
python src/glycosmiles2bap.py --input examples/example_inputs.txt --output output/
```

## Input Formats

### IUPAC-condensed

```
Gal(b1-4)GlcNAc(b1-3)Gal(b1-4)Glc
Man(a1-3)[Man(a1-6)]Man
Neu5Ac(a2-3)Gal(b1-4)Glc
```

### WURCS

```
WURCS=2.0/3,3,2/[a2122h-1b_1-5][a1122h-1b_1-5][a2112h-1b_1-5]/1-2-3/a4-b1_b4-c1
```

## CCD Code Reference

| Monosaccharide | α-Anomer | β-Anomer | Anomeric Carbon |
|---------------|----------|----------|-----------------|
| Glucose (Glc) | GLC | BGC | C1 |
| Galactose (Gal) | GLA | GAL | C1 |
| Mannose (Man) | MAN | BMA | C1 |
| N-acetylglucosamine (GlcNAc) | A2G | NAG | C1 |
| Fucose (Fuc) | FUC | - | C1 |
| Sialic acid (Neu5Ac) | SIA | - | C2 |
| Xylose (Xyl) | XYS | - | C1 |

> **Note**: Sialic acids use C2 as the anomeric carbon (ketose), while aldoses use C1.

## Output Format

### AF3 JSON Input

```json
{
  "ligand": {
    "ccd_codes": ["GAL", "NAG", "GAL", "GLC"],
    "