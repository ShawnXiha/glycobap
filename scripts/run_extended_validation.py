#!/usr/bin/env python3
"""
Extended PDB Validation for GlycoSMILES2BAP
Validates 12 PDB structures (original 4 + 8 new)
"""

import sys
import os
import json

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ccd_mapper import CCDMapper

OUTPUT_DIR = "./results/pdb_validation/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Extended validation cases: original 4 + 8 new = 12 total
VALIDATION_CASES = [
    # Original 4 cases
    {"id": "V001", "pdb": "5NSC", "structure": "Fucosylated", 
     "expected_ccd": ["FUC", "GAL", "GLC"], "key_test": "L-configuration"},
    {"id": "V002", "pdb": "1L6R", "structure": "Lactose",
     "expected_ccd": ["GAL", "GLC"], "key_test": "Epimer distinction"},
    {"id": "V003", "pdb": "2VXR", "structure": "Sialyllactose",
     "expected_ccd": ["SIA", "GAL", "GLC"], "key_test": "C2 anomeric (CRITICAL)"},
    {"id": "V004", "pdb": "5K65", "structure": "M3 N-glycan",
     "expected_ccd": ["MAN", "MAN", "BMA", "NAG", "NAG"], "key_test": "Branch topology"},
    # New 8 cases
    {"id": "V005", "pdb": "4NXU", "structure": "A2 N-glycan",
     "expected_ccd": ["SIA", "GAL", "NAG", "MAN", "BMA", "NAG", "NAG"], "key_test": "Bi-antennary"},
    {"id": "V006", "pdb": "1NPU", "structure": "GM1 ganglioside",
     "expected_ccd": ["SIA", "GAL", "NGA", "GAL", "GLC"], "key_test": "Multiple SIA"},
    {"id": "V007", "pdb": "2JCP", "structure": "Core-2 O-glycan",
     "expected_ccd": ["NGA", "GAL", "NAG"], "key_test": "O-linked"},
    {"id": "V008", "pdb": "3WBM", "structure": "Heparin fragment",
     "expected_ccd": ["GCS", "IDR"], "key_test": "Sulfation"},
    {"id": "V009", "pdb": "4DO4", "structure": "High-mannose M9",
     "expected_ccd": ["MAN", "MAN", "MAN", "MAN", "MAN", "MAN", "MAN", "MAN", "MAN"], "key_test": "Large branched"},
    {"id": "V010", "pdb": "1SLA", "structure": "Hyaluronan",
     "expected_ccd": ["GCU", "NAG"], "key_test": "Linear polymer"},
    {"id": "V011", "pdb": "5FON", "structure": "Blood group A",
     "expected_ccd": ["NGA", "GAL", "FUC"], "key_test": "Combined challenges"},
    {"id": "V012", "pdb": "2W8G", "structure": "Keratan sulfate",
     "expected_ccd": ["GAL", "NAG", "GAL", "NAG"], "key_test": "Alternating"},
]

# CCD mapping test data
CCD_TESTS = [
    ("fuc", "alpha", "l", "FUC", "C1", "O5"),
    ("gal", "beta", "d", "GAL", "C1", "O5"),
    ("neu5ac", "alpha", "d", "SIA", "C2", "O6"),
    ("man", "alpha", "d", "MAN", "C1", "O5"),
    ("man", "beta", "d", "BMA", "C1", "O5"),
    ("glcnac", "beta", "d", "NAG", "C1", "O5"),
    ("galnac", "beta", "d", "NGA", "C1", "O5"),