#!/usr/bin/env python3
"""
PDB Validation for GlycoSMILES2BAP
Step 1: Define test cases and expected CCD codes
"""

import json
import os

OUTPUT_DIR = "./results/pdb_validation/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Test cases for PDB structure validation
CASES = [
    {
        "id": "V001",
        "pdb_id": "5NSC",
        "name": "Fucosylated",
        "iupac": "Fuc(a1-2)Gal(b1-4)Glc",
        "expected_ccd": ["FUC", "GAL", "GLC"],
        "key_check": "FUC = alpha-L-fucose (NOT beta)"
    },
    {
        "id": "V002",
        "pdb_id": "1L6R",
        "name": "Lactose",
        "iupac": "Gal(b1-4)Glc",
        "expected_ccd": ["GAL", "GLC"],
        "key_check": "GAL C4 axial hydroxyl"
    },
    {
        "id": "V003",
        "pdb_id": "2VXR",
        "name": "Sialyllactose",
        "iupac": "Neu5Ac(a2-3)Gal(b1-4)Glc",
        "expected_ccd": ["SIA", "GAL", "GLC"],
        "key_check": "SIA anomeric = C2 (ketose)"
    },
    {
        "id": "V004",
        "pdb_id": "5K65",
        "name": "M3_N-glycan",
        "iupac": "Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc",
        "expected_ccd": ["MAN", "MAN", "BMA", "NAG", "NAG"],
        "key_check": "Branch topology preserved"
    }
]

# CCD code reference table
CCD_TABLE = {
    "FUC": {"name": "alpha-L-fucose", "anomer": "alpha", "config": "L", "anomeric_c": "C1"},
    "BDF": {"name": "beta-L-fucose", "anomer": "beta", "config": "L", "anomeric_c": "C1"},
    "GAL": {"name": "beta-D-galactose", "anomer": "beta", "config": "D", "anomeric_c": "C1"},
    "GLA": {"name": "alpha-D-galactose", "anomer": "alpha", "config": "D", "anomeric_c": "C1"},
    "GLC": {"name": "beta-D-glucose", "anomer": "beta", "config": "D", "anomeric_c": "C1"},
    "BGC": {"name": "beta-D-glucose", "anomer": "beta", "config": "D", "anomeric_c": "C1"},
    "SIA": {"name": "alpha-N-acetylneuraminic acid", "anomer": "alpha", "config": "D", "anomeric_c": "C2"},
    "MAN": {"name": "alpha-D-mannose", "anomer": "alpha", "config": "D", "anomeric_c": "C1"},
    "BMA": {"name": "beta-D-mannose", "anomer": "beta", "config": "D", "anomeric_c": "C1"},
    "NAG": {"name": "beta-D-N-acetylglucosamine", "anomer": "beta", "config": "D", "anomeric_c": "C1"}
}


def validate_ccd_codes(case):
    """Validate CCD codes for a structure."""
    result = {
        "id": case["id"],
        "name": case["name"],
        "expected_ccd": case["expected_ccd"],
        "ccd_details": [],
        "status": "PASS"
    }
    
    for ccd in case["expected_ccd"]:
        if ccd in CCD_TABLE:
            result["ccd_details"].append({
                "ccd": ccd,
                "info": CCD_TABLE[ccd]
            })
        else:
            result["status"] = f"FAIL: Unknown CCD {ccd}"
            break
    
    return result