#!/usr/bin/env python3
"""
Independent Validation Experiment for GlycoSMILES2BAP
Generates validation data, runs comparison, and computes complexity metrics
"""

import json
import os
import random
import time
from collections import Counter, defaultdict
from datetime import datetime

# Set random seed for reproducibility
random.seed(42)

# Output directory
OUTPUT_DIR = "./results/validation_experiment"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ============================================================================
# VALIDATION STRUCTURES (100 diverse glycans)
# ============================================================================

VALIDATION_STRUCTURES = [
    # N-glycans (25)
    {"id": "V001", "iupac": "Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "category": "N-glycan", "expected_residues": 5},
    {"id": "V002", "iupac": "Man(a1-2)Man(a1-3)[Man(a1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "category": "N-glycan", "expected_residues": 7},
    {"id": "V003", "iupac": "Man(a1-2)Man(a1-2)Man(a1-3)[Man(a1-2)Man(a1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "category": "N-glycan", "expected_residues": 9},
    {"id": "V004", "iupac": "Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)[Fuc(a1-6)]GlcNAc", "category": "N-glycan", "expected_residues": 6},
    {"id": "V005", "iupac": "Gal(b1-4)GlcNAc(b1-2)Man(a1-3)[Gal(b1-4)GlcNAc(b1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "category": "N-glycan", "expected_residues": 9},
    {"id": "V006", "iupac": "Neu5Ac(a2-6)Gal(b1-4)GlcNAc(b1-2)Man(a1-3)[Neu5Ac(a2-6)Gal(b1-4)GlcNAc(b1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "category": "N-glycan", "expected_residues": 11},
    {"id": "V007", "iupac": "Neu5Ac(a2-3)Gal(b1-4)GlcNAc(b1-2)Man(a1-3)[Gal(b1-4)GlcNAc(b1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "category": "N-glycan", "expected_residues": 10},
    {"id": "V008", "iupac": "Gal(b1-4)GlcNAc(b1-2)Man(a1-3)[Gal(b1-4)GlcNAc(b1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)[Fuc(a1-6)]GlcNAc", "category": "N-glycan", "expected_residues": 10},
    {"id": "V009", "iupac": "GlcNAc(b1-4)Man(a1-3)[GlcNAc(b1-4)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "category": "N-glycan", "expected_residues": 7},
    {"id": "V010", "iupac": "Gal(b1-4)GlcNAc(b1-4)Man(a1-3)[Gal(b1-4)GlcNAc(b1-2)Man