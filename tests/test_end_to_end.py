#!/usr/bin/env python3
"""
End-to-End Integration Tests for GlycoSMILES2BAP Pipeline
Tests the complete pipeline from input to AF3 JSON output
"""

import sys
import os
import json

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ccd_mapper import CCDMapper
from bap_generator import BAPGenerator

def run_all_tests():
    """Run all end-to-end tests"""
    results = {
        "passed": 0,
        "failed": 0,
        "tests": []
    }
    
    # Test 1: CCD Mapper - Common Monosaccharides
    print("=" * 60)
    print("TEST 1: CCD Mapper - Common Monosaccharides")
    print("=" * 60)
    
    common_tests = [
        ("GlcNAc", "beta", "D", "NAG"),
        ("GlcNAc", "alpha", "D", "A2G"),
        ("Man", "alpha", "D", "MAN"),
        ("Man", "beta", "D", "BMA"),
        ("Gal", "beta", "D", "GAL"),
        ("Gal", "alpha", "D", "GLA"),
        ("Glc", "beta", "D", "GLC"),
        ("Fuc", "alpha", "L", "FUC"),
        ("Xyl", "beta", "D", "XYS"),
        ("Neu5Ac", "alpha", "D", "SIA"),
    ]
    
    mapper = CCDMapper()
    for mono, anomer, config, expected in common_tests:
        result = mapper.map_residue(mono, anomer, config)
        if result == expected:
            print(f"  PASS: {mono} ({anomer}, {config}) -> {result}")
            results["passed"] += 1
        else:
            print(f"  FAIL: {mono} ({anomer}, {config}) -> {result} (expected {expected})")
            results["failed"] += 1
    
    # Test 2: CCD Mapper - Rare Monosaccharides
    print("\n" + "=" * 60)
    print("TEST 2: CCD Mapper - Rare Monosaccharides")
    print("=" * 60)
    
    rare_tests = [
        ("KDN", "alpha", "D", "KDN"),
        ("KDN", "beta", "D", "KDN"),
        ("GalA", "alpha", "D", "GAL"),
        ("GlcA", "beta", "D", "GCU"),
        ("Rha", "alpha", "L", "RAM"),
        ("Rha", "beta", "L", "RAM"),
        ("Ara", "alpha", "L", "ARA"),
        ("Ara", "beta", "L", "ARB"),
        ("Rib", "beta", "D", "RIB"),
        ("Fru", "beta", "D", "FRU"),
        ("Neu5Gc", "alpha", "D", "NGC"),
        ("MurNAc", "alpha", "D", "MUR"),
    ]
    
    for mono, anomer, config, expected in rare_tests:
        result = mapper.map_residue(mono, anomer, config)
        if result == expected:
            print(f"  PASS: {mono} ({anomer}, {config}) -> {result}")
            results["passed"] += 1
        else:
            print(f"  FAIL: {mono} ({anomer}, {config}) -> {result} (expected {expected})")
            results["failed"] += 1
    
    # Test 3: Anomeric Position Special Cases
    print("\n" + "=" * 60)
    print("TEST 3: Anomeric Position Special Cases")
    print("=" * 60)
    
    anomer_tests = [
        ("SIA", "C2", "Sialic acid (ketose)"),
        ("SLB", "C2", "Beta-sialic acid"),
        ("KDN", "C2", "KDN (ketose)"),
        ("NGC", "C2", "Neu5Gc (ketose)"),
        ("NAG", "C1", "GlcNAc (aldose)"),
        ("MAN", "C1", "Mannose (aldose)"),
        ("GAL", "C1", "Galactose (aldose)"),
    ]
    
    for ccd_code, expected_pos, description in anomer_tests:
        result = mapper.get_anomeric_position(ccd_code)
        if result