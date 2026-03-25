#!/usr/bin/env python3
"""
Independent Validation Set Generator for GlycoSMILES2BAP
Generates validation set and complexity metrics
"""

import json
import os
import random
import time
from collections import Counter, defaultdict

# Set random seed for reproducibility
random.seed(42)

# Output directory
OUTPUT_DIR = "./results/independent_validation"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ============================================================================
# GlyTouCan Representative Structures for Independent Validation
# ============================================================================

VALIDATION_STRUCTURES = [
    # N-glycans (25 structures)
    {"id": "VAL_N001", "category": "N-glycan", "iupac": "Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "branches": 2, "residues": 5},
    {"id": "VAL_N002", "category": "N-glycan", "iupac": "Man(a1-2)Man(a1-3)[Man(a1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "branches": 2, "residues": 7},
    {"id": "VAL_N003", "category": "N-glycan", "iupac": "Man(a1-2)Man(a1-2)Man(a1-3)[Man(a1-2)Man(a1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "branches": 2, "residues": 9},
    {"id": "VAL_N004", "category": "N-glycan", "iupac": "Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)[Fuc(a1-6)]GlcNAc", "branches": 2, "residues": 6},
    {"id": "VAL_N005", "category": "N-glycan", "iupac": "Gal(b1-4)GlcNAc(b1-2)Man(a1-3)[Gal(b1-4)GlcNAc(b1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "branches": 2, "residues": 9},
    {"id": "VAL_N006", "category": "N-glycan", "iupac": "Neu5Ac(a2-6)Gal(b1-4)GlcNAc(b1-2)Man(a1-3)[Neu5Ac(a2-6)Gal(b1-4)GlcNAc(b1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "branches": 2, "residues": 11},
    {"id": "VAL_N007", "category": "N-glycan", "iupac": "Neu5Ac(a2-3)Gal(b1-4)GlcNAc(b1-2)Man(a1-3)[Neu5Ac(a2-3)Gal(b1-4)GlcNAc(b1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)[Fuc(a1-6)]GlcNAc", "branches": 2, "residues": 12},
    {"id": "VAL_N008", "category": "N-glycan", "iupac": "Gal(b1-4)GlcNAc(b1-4)Man(a1-3)[Gal(b1-4)GlcNAc(b1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "branches": 2, "residues": 10},
    {"id": "VAL_N009", "category": "N-glycan", "iupac": "GlcNAc(b1-4)Man(a1-3)[GlcNAc(b1-4)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "branches": 2, "residues": 7},
