#!/usr/bin/env python3
"""
Extended PDB Validation for GlycoSMILES2BAP - 12 Structures
"""

import sys
import os
import json

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ccd_mapper import CCDMapper

OUTPUT_DIR = "./results/pdb_validation/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    print("=" * 70)
    print("EXTENDED PDB VALIDATION: 12 Structures (4 Original + 8 New)")
    print("=" * 70)
    print()
    
    mapper = CCDMapper()
    
    # CCD mapping tests
    tests = [
        # Original 4 - Critical stereochemistry tests
        ("V001", "5NSC", "Fucosylated", "fuc", "alpha", "l", "FUC", "C1", "O5"),
        ("V002", "1L6R", "Lactose", "gal", "beta", "d", "GAL", "C1", "O5"),
        ("V003", "2VXR", "Sialyllactose", "neu5ac", "alpha", "d", "SIA", "C2", "O6"),
        ("V004", "5K65", "M3 N-glycan", "man", "alpha", "d", "MAN", "C1", "O5"),
        
        # New 8 - Extended coverage
        ("V005", "4NXU", "A2 N-glycan", "sia", "alpha", "d", "SIA", "C2", "O6"),
        ("V006", "1NPU", "GM1 ganglioside", "sia", "alpha", "d", "SIA", "C2", "O6"),
        ("V007", "2JCP", "Core-2 O-glycan", "galnac", "beta", "d", "NGA", "C1", "O5"),
        ("V008", "3WBM", "Heparin fragment", "glca", "beta", "d", "GCS", "C1", "O5"),
        ("V009", "4DO4", "High-mannose M9", "man", "alpha", "d", "MAN", "C1", "O5"),
        ("V010", "1SLA", "Hyaluronan", "glca", "beta", "d", "GCU", "C1", "O5"),
        ("V011", "5FON", "Blood group A", "galnac", "alpha", "d", "NGA", "C1", "O5"),
        ("V012", "2W8G", "Keratan sulfate", "gal", "beta", "d", "GAL", "C1", "O5"),
    ]
    
    results = []
    passed = 0
    failed = 0
    
    for test in tests:
        vid, pdb, structure, mono, anomer, config, exp_ccd, exp_anomeric, exp_ring_o = test
        
        # Run CCD mapper
        actual_ccd = mapper.map(mono, anomer, config)
        actual_anomeric = mapper.anomeric(actual_ccd) if actual_ccd else None
        actual_ring_o = mapper.ring_oxygen(actual_ccd) if actual_ccd else None
        
        # Check results
        ccd_match = actual_ccd == exp_ccd
        anomeric_match = actual_anomeric == exp_anomeric
        ring_o_match = actual_ring_o == exp_ring_o
        all_match = ccd_match and anomeric_match and ring_o_match
        
        status = "PASS" if all_match else "FAIL"
        if all_match:
            passed += 1
        else:
            failed += 1
        
        # Print result
        symbol = "✅" if all_match else "❌"
        print(f"[{vid}] {pdb}: {structure}")
        print(f"  CCD: {actual_ccd} (expected: {exp_ccd}) {'✓' if ccd_match else '✗'}")
        print(f"  Anomeric: {actual_anomeric} (expected: {exp_anomeric}) {'✓' if anomeric_match else '✗'}")
        print(f"  Ring O: {actual_ring_o} (expected: {exp_ring_o}) {'✓' if