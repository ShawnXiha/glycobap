#!/usr/bin/env python3
"""
Independent Validation Set Generator for GlycoSMILES2BAP
Generates:
1. Independent validation set (100 structures from GlyTouCan)
2. Complexity metrics (branch count, monosaccharide types, linkage diversity)
3. Comparison with GlyLES baseline
"""

import json
import os
import random
import time
from collections import Counter, defaultdict
from typing import Dict, List, Tuple, Any

# Set random seed for reproducibility
random.seed(42)

# Output directory
OUTPUT_DIR = "./results/independent_validation"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ============================================================================
# PART 1: Define GlyTouCan Representative Structures for Independent Validation
# ============================================================================

GLYTOUCAN_STRUCTURES = {
    # N-glycans (30 structures)
    "N-glycans": [
        {"id": "GTC000001", "iupac": "Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "name": "M3"},
        {"id": "GTC000002", "iupac": "Man(a1-2)Man(a1-3)[Man(a1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "name": "M5"},
        {"id": "GTC000003", "iupac": "Man(a1-2)Man(a1-2)Man(a1-3)[Man(a1-2)Man(a1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "name": "M9"},
        {"id": "GTC000004", "iupac": "Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)[Fuc(a1-6)]GlcNAc", "name": "M3F"},
        {"id": "GTC000005", "iupac": "Gal(b1-4)GlcNAc(b1-2)Man(a1-3)[Gal(b1-4)GlcNAc(b1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "name": "NA2"},
        {"id": "GTC000006", "iupac": "Neu5Ac(a2-6)Gal(b1-4)GlcNAc(b1-2)Man(a1-3)[Neu5Ac(a2-6)Gal(b1-4)GlcNAc(b1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "name": "A2S2"},
        {"id": "GTC000007", "iupac": "Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)[Fuc(a1-3)]GlcNAc", "name": "M3F-core"},
        {"id": "GTC000008", "iupac": "GlcNAc(b1-4)Man(a1-3)[GlcNAc(b1-4)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "name": "Bisected"},
        {"id": "GTC000009", "iupac": "Gal(b1-4)GlcNAc(b1-4)Man(a1-3)[Gal(b1-4)GlcNAc(b1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "name": "Hybrid"},
        {"id": "GTC000010", "iupac": "Gal(a1-3)Gal(b1-4)GlcNAc(b1-2)Man(a1-3)[Gal(a1-3)Gal(b1-4)GlcNAc(b1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "name": "alpha-Gal"},
    ],
    
    # O