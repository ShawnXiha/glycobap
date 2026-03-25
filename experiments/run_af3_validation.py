#!/usr/bin/env python3
"""
AF3 Validation Experiment for GlycoSMILES2BAP
Generates AF3-compatible JSON input files for validation
"""

import json
import os

OUTPUT_DIR = "./results/af3_validation"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Validation test structures
STRUCTURES = [
    {"id": "V001", "name": "Lactose", "iupac": "Gal(b1-4)Glc"},
    {"id": "V002", "name": "LNnT", "iupac": "Gal(b1-4)GlcNAc(b1-3)Gal(b1-4)Glc"},
    {"id": "V003", "name": "Sialyllactose", "iupac": "Neu5Ac(a2-3)Gal(b1-4)Glc"},
    {"id": "V004", "name": "M3_N-glycan", "iupac": "Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc"},
    {"id": "V005", "name": "Fucosylated", "iupac": "Fuc(a1-2)Gal(b1-4)Glc"}
]

# Pre-defined AF3 JSON structures
AF3_TEMPLATES = {
    "V001": {
        "name": "Lactose",
        "ligand": {
            "ccdCodes": ["GAL", "BGC"],
            "bondedAtomPairs": [["L-1", "C1", "L-2", "O4"]]
        },
        "validation": {
            "key_test": "Basic beta linkage",
            "expected_anomer": "beta",
            "critical_atoms": {"donor": "C1", "acceptor": "O4"}
        }
    },
    "V002": {
        "name": "LNnT",
        "ligand": {
            "ccdCodes": ["GAL", "NAG", "GAL", "BGC"],
            "bondedAtomPairs": [
                ["L-1", "C1", "L-2", "O4"],
                ["L-2", "C1", "L-3", "O3"],
                ["L-3", "C1", "L-4", "O4"]
            ]
        },
        "validation": {
            "key_test": "Multi-linkage chain",
            "expected_anomer": "all_beta",
            "critical_atoms": {"donors": "C1", "acceptors": "O3/O4"}
        }
    },
    "V003": {
        "name": "Sialyllactose",
        "ligand": {
            "ccdCodes": ["SIA", "GAL", "BGC"],
            "bondedAtomPairs": [
                ["L-1", "C2", "L-2", "O3"],
                ["L-2", "C1", "L-3", "O4"]
            ]
        },
        "validation": {
            "key_test": "Sialic acid C2 anomeric position",
            "expected_anomer": "alpha/beta",
            "critical_atoms": {"SIA_donor": "C2", "SIA_ring": "O6"},
            "note": "Sialic acid MUST use C2 as anomeric carbon"
        }
    },
    "V004": {
        "name": "M3_N-glycan",
        "ligand": {
            "ccdCodes": ["MAN", "MAN", "BMA", "NAG", "NAG"],
            "bondedAtomPairs": [
                ["L-1", "C1", "L-3", "O3"],
                ["L-2", "C1", "L-3", "O6"],
                ["L-3", "C1", "L-4", "O4"],
                ["L-4", "C1", "L-5", "O4"]
            ]
        },
        "validation": {
            "key_test": "Branch handling",
            "expected_anomer": "mixed",
            "critical_atoms": {"branch_point": "L-3 (BMA)"},
            "note": "Branch topology must be preserved"
        }
    },
    "V005": {
        "name": "Fucosylated",
        "ligand": {
            "ccdCodes": ["