#!/usr/bin/env python3
"""
Ablation Study for GlycoSMILES2BAP Pipeline

Tests the contribution of each module:
1. Full Pipeline (baseline)
2. w/o CCD Mapper (use generic mapping)
3. w/o Anomeric Tracking (use C1 for all)
4. w/o Branch Handling (linear only)
5. CCD Mapper Only
"""

import json
import random
from datetime import datetime
from pathlib import Path

# Set seed for reproducibility
random.seed(42)

# Test dataset - representative glycans
TEST_DATA = [
    # Linear glycans
    {"id": "LNnT", "iupac": "Gal(b1-4)GlcNAc(b1-3)Gal(b1-4)Glc", "residues": 4, "linkages": 3, "category": "linear"},
    {"id": "LNT", "iupac": "Gal(b1-3)GlcNAc(b1-3)Gal(b1-4)Glc", "residues": 4, "linkages": 3, "category": "linear"},
    {"id": "LacNAc", "iupac": "Gal(b1-4)GlcNAc", "residues": 2, "linkages": 1, "category": "linear"},
    {"id": "Maltotriose", "iupac": "Glc(a1-4)Glc(a1-4)Glc", "residues": 3, "linkages": 2, "category": "linear"},
    
    # N-glycans
    {"id": "M3", "iupac": "Man(a1-6)[Man(a1-3)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "residues": 5, "linkages": 4, "category": "n_glycan"},
    {"id": "M5", "iupac": "Man(a1-6)[Man(a1-3)]Man(a1-6)[Man(a1-3)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "residues": 7, "linkages": 6, "category": "n_glycan"},
    {"id": "G0", "iupac": "GlcNAc(b1-2)Man(a1-6)[GlcNAc(b1-2)Man(a1-3)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "residues": 7, "linkages": 6, "category": "n_glycan"},
    
    # O-glycans
    {"id": "Tn", "iupac": "GalNAc(a1-O)Ser/Thr", "residues": 1, "linkages": 1, "category": "o_glycan"},
    {"id": "T", "iupac": "Gal(b1-3)GalNAc(a1-O)Ser/Thr", "residues": 2, "linkages": 2, "category": "o_glycan"},
    {"id": "Sialyl-T", "iupac": "Neu5Ac(a2-6)Gal(b1-3)GalNAc(a1-O)Ser/Thr", "residues": 3, "linkages": 3, "category": "o_glycan"},
    
    # Sialylated
    {"id": "LSTb", "iupac": "Neu5Ac(a2-6)Gal(b1-4)GlcNAc(b1-3)Gal(b1-4)Glc", "residues": 5, "linkages": 4, "category": "sialylated"},
    {"id": "LSTa", "iupac": "Neu5Ac(a2-3)Gal(b1-3)GlcNAc(b1-3)Gal(b1-4)Glc", "residues": 5, "linkages": 4, "category": "sialylated"},
    
    # Complex branched
    {"id": "BiAntennary", "iupac": "Gal(b1-4)GlcNAc(b1-2)Man(a1-6)[Gal(b1-4)GlcNAc(b1-2)Man