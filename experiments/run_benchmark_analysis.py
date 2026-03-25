#!/usr/bin/env python3
"""
Benchmark Analysis Script for GlycoSMILES2BAP
Generates: complexity metrics, statistical analysis, comparison data
"""

import json
import os
import random
from collections import Counter
from typing import Dict, List, Any
import math

random.seed(42)

OUTPUT_DIR = "./results/benchmark_analysis"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# =============================================================================
# PART 1: Define Validation Structures (Independent Set)
# =============================================================================

VALIDATION_STRUCTURES = [
    # Linear glycans (20)
    {"id": "V001", "iupac": "Gal(b1-4)Glc", "category": "linear", "residues": 2},
    {"id": "V002", "iupac": "Gal(b1-4)GlcNAc(b1-3)Gal(b1-4)Glc", "category": "linear", "residues": 4},
    {"id": "V003", "iupac": "Glc(a1-4)Glc(a1-4)Glc", "category": "linear", "residues": 3},
    {"id": "V004", "iupac": "Glc(b1-4)Glc(b1-4)Glc(b1-4)Glc", "category": "linear", "residues": 4},
    {"id": "V005", "iupac": "Man(b1-4)GlcNAc(b1-4)GlcNAc", "category": "linear", "residues": 3},
    {"id": "V006", "iupac": "Gal(b1-3)GlcNAc", "category": "linear", "residues": 2},
    {"id": "V007", "iupac": "Fuc(a1-2)Gal(b1-4)Glc", "category": "linear", "residues": 3},
    {"id": "V008", "iupac": "Neu5Ac(a2-3)Gal(b1-4)Glc", "category": "linear", "residues": 3},
    {"id": "V009", "iupac": "GlcNAc(b1-4)GlcNAc", "category": "linear", "residues": 2},
    {"id": "V010", "iupac": "Gal(b1-4)GlcNAc(b1-6)Gal", "category": "linear", "residues": 3},
    
    # N-glycans (40)
    {"id": "V011", "iupac": "Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "category": "n_glycan", "residues": 5},
    {"id": "V012", "iupac": "Man(a1-2)Man(a1-3)[Man(a1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "category": "n_glycan", "residues": 7},
    {"id": "V013", "iupac": "Man(a1-2)Man(a1-2)Man(a1-3)[Man(a1-2)Man(a1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "category": "n_glycan", "residues": 9},
    {"id": "V014", "iupac": "Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)[Fuc(a1-6)]GlcNAc", "category": "n_glycan", "residues": 6},
    {"id": "V015", "iupac": "Gal(b1-4)GlcNAc(b1-2)Man(a1-3)[Gal(b1-4)GlcNAc(b1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "category": "n_glycan", "residues": 