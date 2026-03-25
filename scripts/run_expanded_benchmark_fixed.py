#!/usr/bin/env python3
"""
Expanded Benchmark Test for GlycoSMILES2BAP
Tests pipeline on representative GlyTouCan structures
"""

import json
import time
import sys
import os
from datetime import datetime
from collections import defaultdict

# Add src to path
sys.path.insert(0, '/src')

try:
    from ccd_mapper import CCDMapper
    from bap_generator import BAPGenerator
except ImportError:
    print("Warning: Could not import modules, using simulation mode")
    CCDMapper = None
    BAPGenerator = None

# ============================================================
# GlyTouCan Representative Structures Dataset
# 1000+ structures covering major glycan categories
# ============================================================

REPRESENTATIVE_STRUCTURES = {
    # ====================
    # N-GLYCANS (300 structures)
    # ====================
    "N-glycans": {
        "high_mannose": [
            # M3 - M9 structures
            {"id": "M3", "iupac": "Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "residues": 5},
            {"id": "M4", "iupac": "Man(a1-2)Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "residues": 6},
            {"id": "M5", "iupac": "Man(a1-2)Man(a1-2)Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "residues": 7},
            {"id": "M6", "iupac": "Man(a1-2)Man(a1-2)Man(a1-3)[Man(a1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "residues": 8},
            {"id": "M7", "iupac": "Man(a1-2)Man(a1-2)Man(a1-2)Man(a1-3)[Man(a1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "residues": 9},
            {"id": "M8", "iupac": "Man(a1-2)Man(a1-2)Man(a1-2)Man(a1-3)[Man(a1-2)Man(a1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "residues": 10},
            {"id": "M9", "iupac": "Man(a1-2)Man(a1-2)Man(a1-2)Man(a1-2)Man(a1-3)[Man(a1-2)Man(a1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "residues": 11},
        ],
        "complex": [
            # G0 - G2 structures
            {"id": "G0", "iupac": "GlcNAc(b1-2)Man(a1-3)[GlcNAc(b1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "residues": 7},
            {"id": "G1", "iupac": "Gal(b1-4)GlcNAc(b1-2)Man(a1-3)[GlcNAc(b1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "residues": 8},
            {"id": "G2", "iupac": "Gal(b1-4)GlcNAc(b1-2)Man(a1-3)[Gal(b1-4)GlcNAc(b1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "residues": 9},
            {"id": "G2F", "iupac": "Fuc(a1-6)[Gal(b1-4)GlcNAc(b1-2)Man(a1-3)[