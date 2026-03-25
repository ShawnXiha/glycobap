#!/usr/bin/env python3
"""
Expanded Benchmark Test for GlycoSMILES2BAP
"""

import json
import time
import sys

# CCD mapping table (simplified)
CCD_TABLE = {
    ('glcnac', 'b', 'd'): 'NAG', ('glcnac', 'a', 'd'): 'A2G',
    ('man', 'a', 'd'): 'MAN', ('man', 'b', 'd'): 'BMA',
    ('gal', 'b', 'd'): 'GAL', ('gal', 'a', 'd'): 'GLA',
    ('glc', 'b', 'd'): 'GLC', ('glc', 'a', 'd'): 'GLA',
    ('fuc', 'a', 'l'): 'FUC',
    ('neu5ac', 'a', 'd'): 'SIA',
    ('neu5gc', 'a', 'd'): 'NGC',
    ('xyl', 'b', 'd'): 'XYS',
    ('galnac', 'b', 'd'): 'NGA',
    ('kdn', 'a', 'd'): 'KDN',
    ('rha', 'a', 'l'): 'RAM',
    ('ara', 'a', 'l'): 'ARA',
}

ANOMERIC_POSITIONS = {
    'SIA': 'C2', 'NGC': 'C2', 'KDN': 'C2',  # ketoses
    'default': 'C1'  # aldoses
}

def parse_iupac(iupac_str):
    """Parse IUPAC notation to extract residues and linkages."""
    residues = []
    linkages = []
    
    import re
    # Pattern: Monosaccharide(anomer1-2)Monosaccharide
    pattern = r'(\w+)\(([ab])(\d)-(\d)\)'
    
    parts = re.split(r'[\[\]]', iupac_str)
    for part in parts:
        matches = re.findall(pattern, part)
        for i, (mono, anomer, donor_pos, acceptor_pos) in enumerate(matches):
            residues.append({
                'monosaccharide': mono.lower(),
                'anomer': anomer,
                'config': 'd' if mono.lower() not in ['fuc', 'rha'] else 'l'
            })
            if i < len(matches) - 1:
                linkages.append({
                    'donor_pos': donor_pos,
                    'acceptor_pos': acceptor_pos
                })
    
    return residues, linkages

def get_ccd_code(mono, anomer, config):
    """Lookup CCD code."""
    key = (mono.lower(), anomer.lower(), config.lower())
    return CCD_TABLE.get(key, f"UNKNOWN:{mono}")

def run_benchmark():
    """Run expanded benchmark test."""
    
    # Expanded dataset - 100 structures
    test_structures = [
        # Linear glycans (40)
        {"id": "L001", "iupac": "Gal(b1-4)Glc", "category": "linear"},
        {"id": "L002", "iupac": "Gal(b1-4)GlcNAc", "category": "linear"},
        {"id": "L003", "iupac": "Gal(b1-3)GlcNAc", "category": "linear"},
        {"id": "L004", "iupac": "GlcNAc(b1-3)Gal", "category": "linear"},
        {"id": "L005", "iupac": "Gal(b1-4)Gal(b1-4)Glc", "category": "linear"},
        {"id": "L006", "iupac": "Gal(b1-4)GlcNAc(b1-3)Gal", "category": "linear"},
        {"id": "L007", "iupac": "Gal(b1-4)GlcNAc(b1-3)Gal(b1-4)Glc", "category": "linear"},
        {"id": "L008", "iupac": "Neu5Ac(a2-3)Gal(b1-4)Glc", "category": "linear"},
        {"id": "L009", "iupac": "Neu5Ac(a2-6)Gal(b1-4)Glc", "category": "linear"},
        {"id": "L010", "iupac": "Fuc(a1-2)Gal(b1-4)Glc", "category": "linear"},
        # N-g