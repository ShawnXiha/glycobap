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
    {
        "id": "V001",
        "pdb": "5NSC",
        "structure": "Fucosylated",
        "iupac": "Fuc(a1-2)Gal(b1-4)Glc",
        "expected_ccd": ["FUC", "GAL", "GLC"],
        "key_test": "L-configuration",
        "anomeric": {"FUC": "C1"},
        "ring_o": {"FUC": "O5"}
    },
    {
        "id": "V002",
        "pdb": "1L6R",
        "structure": "Lactose",
        "iupac": "Gal(b1-4)Glc",
        "expected_ccd": ["GAL", "GLC"],
        "key_test": "Epimer distinction",
        "anomeric": {"GAL": "C1"},
        "ring_o": {"GAL": "O5"}
    },
    {
        "id": "V003",
        "pdb": "2VXR",
        "structure": "Sialyllactose",
        "iupac": "Neu5Ac(a2-3)Gal(b1-4)Glc",
        "expected_ccd": ["SIA", "GAL", "GLC"],
        "key_test": "C2 anomeric (CRITICAL)",
        "anomeric": {"SIA": "C2"},
        "ring_o": {"SIA": "O6"}
    },
    {
        "id": "V004",
        "pdb": "5K65",
        "structure": "M3 N-glycan",
        "iupac": "Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc",
        "expected_ccd": ["MAN", "MAN", "BMA", "NAG", "NAG"],
        "key_test": "Branch topology",
        "anomeric": {"MAN": "C1", "BMA": "C1", "NAG": "C1"},
        "ring_o": {"MAN": "O5", "BMA": "O5", "NAG": "O5"}
    },
    # New 8 cases
    {
        "id": "V005",
        "pdb": "4NXU",
        "structure": "A2 N-glycan",
        "iupac": "Neu5Ac(a2-6)Gal(b1-4)GlcNAc(b1-2)Man(a1-6)[Neu5Ac(a2-6)Gal(b1-4)GlcNAc(b1-2)Man(a1-3)]Man(b1-4)GlcNAc(b1-4)GlcNAc",
        "expected_ccd": ["SIA", "GAL", "NAG", "MAN", "SIA", "GAL", "NAG", "MAN", "BMA", "NAG", "NAG"],
        "key_test": "Bi-antennary topology",
        "anomeric": {"SIA": "C2", "GAL": "C1", "NAG": "C1", "MAN": "C1", "BMA": "C1"},
        "ring_o": {"SIA": "O6", "GAL": "O5", "NAG": "O5", "MAN": "O5", "BMA": "O5"}
    },
    {
        "id": "V006",
        "pdb": "1NPU",
        "structure": "GM1 ganglioside",
        "iupac": "Neu5Ac(a2-3)[Gal(b1-3)GalNAc(b1-4)]Gal(b1-4)Glc",
        "expected_ccd": ["SIA", "GAL", "NGA", "GAL", "