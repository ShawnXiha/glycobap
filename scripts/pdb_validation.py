#!/usr/bin/env python3
"""
PDB Structure Validation for GlycoSMILES2BAP

Validates tool output against known PDB structures.
"""

import json
import os
import sys

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

OUTPUT_DIR = "./results/pdb_validation/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Validation test cases
VALIDATION_CASES = [
    {
        "id": "V001",
        "pdb_id": "5NSC",
        "name": "Fucosylated",
        "iupac": "Fuc(a1-2)Gal(b1-4)Glc",
        "expected_ccd": ["FUC", "GAL", "GLC"],
        "critical": "FUC must be alpha-L (not beta-L)"
    },
    {
        "id": "V002",
        "pdb_id": "1L6R",
        "name": "Lactose",
        "iupac": "Gal(b1-4)Glc",
        "expected_ccd": ["GAL", "GLC"],
        "critical": "GAL C4 axial (not equatorial)"
    },
    {
        "id": "V003",
        "pdb_id": "2VXR",
        "name": "Sialyllactose",
        "iupac": "Neu5Ac(a2-3)Gal(b1-4)Glc",
        "expected_ccd": ["SIA", "GAL", "GLC"],
        "critical": "SIA anomeric at C2 (not C1)"
    },
    {
        "id": "V004",
        "pdb_id": "5K65",
        "name": "M3_N-glycan",
        "iupac": "Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc",
        "expected_ccd": ["MAN", "MAN", "BMA", "NAG", "NAG"],
        "critical": "Branch topology correct"
    }
]

# CCD Mapping table for validation
CCD_TABLE = {
    # Glucose
    "GLC": {"name": "alpha-D-glucose", "anomer": "alpha", "config": "D", "anomeric_c": "C1"},
    "BGC": {"name": "beta-D-glucose", "anomer": "beta", "config": "D", "anomeric_c": "C1"},
    # Galactose
    "GAL": {"name": "beta-D-galactose", "anomer": "beta", "config": "D", "anomeric_c": "C1"},
    "GLA": {"name": "alpha-D-galactose", "anomer": "alpha", "config": "D", "anomeric_c": "C1"},
    # Mannose
    "MAN": {"name": "alpha-D-mannose", "anomer": "alpha", "config": "D", "anomeric_c": "C1"},
    "BMA": {"name": "beta-D-mannose", "anomer": "beta", "config": "D", "anomeric_c": "C1"},
    # N-acetylglucosamine
    "NAG": {"name": "N-acetyl-beta-D-glucosamine", "anomer": "beta", "config": "D", "anomeric_c": "C1"},
    "A2G": {"name": "N-acetyl-alpha-D-glucosamine", "anomer": "alpha", "config": "D", "anomeric_c": "C1"},
    # Fucose
    "FUC": {"name": "alpha-L-fucose", "anomer": "alpha", "config": "L", "anomeric_c": "C1"},
    "BDF": {"name": "beta-L-fucose", "anomer": "beta", "config": "L", "anomeric_c": "C1"},
    # Sialic acid
    "SIA": {"name": "alpha-N-acetylneuraminic acid", "anomer": "alpha", "config": "D", "anomeric_c": "C2"},
    "SLB": {"name": "beta-N-acetylneuraminic acid", "anomer": "beta", "config": "D", "