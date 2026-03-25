#!/usr/bin/env python3
"""
Stage 1 Baseline Test: GlycoSMILES2BAP Validation
Tests the existing implementation to establish baseline metrics.
"""

import sys
sys.path.insert(0, '/home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides/src')

import json
import time
from typing import Dict, List

# Test cases from benchmark
TEST_CASES = [
    # Simple linear glycans
    {"name": "Lactose", "iupac": "Gal(b1-4)Glc", "expected_ccd": ["GLA", "GLC"]},
    {"name": "Maltose", "iupac": "Glc(a1-4)Glc", "expected_ccd": ["GLC", "GLC"]},
    {"name": "Cellobiose", "iupac": "Glc(b1-4)Glc", "expected_ccd": ["GLC", "GLC"]},
    
    # Sialylated glycans (anomeric at C2)
    {"name": "Sialyllactose", "iupac": "Neu5Ac(a2-3)Gal(b1-4)Glc", "expected_ccd": ["SIA", "GLA", "GLC"]},
    
    # Fucosylated glycans
    {"name": "Fucosyllactose", "iupac": "Fuc(a1-2)Gal(b1-4)Glc", "expected_ccd": ["FUC", "GLA", "GLC"]},
    
    # N-glycan core
    {"name": "Man3_core", "iupac": "Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", 
     "expected_ccd": ["MAN", "MAN", "MAN", "NAG", "NAG"]},
    
    # Complex branched
    {"name": "Biantennary", "iupac": "Gal(b1-4)GlcNAc(b1-2)Man(a1-3)[Gal(b1-4)GlcNAc(b1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc",
     "expected_ccd": ["GLA", "NAG", "MAN", "GLA", "NAG", "MAN", "MAN", "NAG", "NAG"]},
]

def test_ccd_mapper():
    """Test CCD Mapper module."""
    from ccd_mapper import CCDMapper
    
    mapper = CCDMapper()
    results = []
    
    for case in TEST_CASES:
        try:
            # Map expected monosaccharides
            mapped = []
            for sugar in case["iupac"].replace("(", " ").replace(")", " ").replace("[", " ").replace("]", " ").split():
                if sugar in ["Gal", "Glc", "Man", "Fuc", "GlcNAc", "Neu5Ac", "Neu5Gc"]:
                    ccd = mapper.get_ccd(sugar, "b" if "(b" in case["iupac"] else "a")
                    if ccd:
                        mapped.append(ccd)
            results.append({
                "name": case["name"],
                "status": "PASS" if len(mapped) > 0 else "FAIL",
                "mapped_count": len(mapped)
            })
        except Exception as e:
            results.append({
                "name": case["name"],
                "status": "ERROR",
                "error": str(e)
            })
    
    return results

def test_bap_generator():
    """Test BAP Generator module."""
    from bap_generator import BAPGenerator
    
    generator = BAPGenerator()
    results = []
    
    # Test basic BAP generation
    test_bonds = [
        {"donor": "GLA", "acceptor": "GLC", "donor_pos": 1, "acceptor_pos": 4, "anomer": "b"},
        {"donor": "MAN", "acceptor": "MAN", "donor_pos": 1, "acceptor_pos": 6, "anomer": "a"},
    ]
    
    for bond in test_bonds:
        try:
            bap = generator.generate_bond(
                donor_ccd=bond["donor"],
                acceptor_ccd=bond["acceptor"],
                donor_position=bond["donor