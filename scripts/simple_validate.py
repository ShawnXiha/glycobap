#!/usr/bin/env python3
"""Simple Extended PDB Validation for GlycoSMILES2BAP"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ccd_mapper import CCDMapper

# Test all 12 structures
TESTS = [
    # Original 4
    ("V001", "5NSC", "Fucosylated", "fuc", "alpha", "l", "FUC", "C1", "O5"),
    ("V002", "1L6R", "Lactose", "gal", "beta", "d", "GAL", "C1", "O5"),
    ("V003", "2VXR", "Sialyllactose", "neu5ac", "alpha", "d", "SIA", "C2", "O6"),
    ("V004", "5K65", "M3 N-glycan", "man", "alpha", "d", "MAN", "C1", "O5"),
    # New 8
    ("V005", "4NXU", "A2 N-glycan", "sia", "alpha", "d", "SIA", "C2", "O6"),
    ("V006", "1NPU", "GM1 ganglioside", "sia", "alpha", "d", "SIA", "C2", "O6"),
    ("V007", "2JCP", "Core-2 O-glycan", "galnac", "alpha", "d", "NGA", "C1", "O5"),
    ("V008", "3WBM", "Heparin fragment", "idua", "alpha", "l", "IDR", "C1", "O5"),
    ("V009", "4DO4", "High-mannose M9", "man", "alpha", "d", "MAN", "C1", "O5"),
    ("V010", "1SLA", "Hyaluronan", "glca", "beta", "d", "GCU", "C1", "O5"),
    ("V011", "5FON", "Blood group A", "galnac", "alpha", "d", "NGA", "C1", "O5"),
    ("V012", "2W8G", "Keratan sulfate", "gal", "beta", "d", "GAL", "C1", "O5"),
]

def main():
    print("=" * 70)
    print("Extended PDB Validation: 12 Structures")
    print("=" * 70)
    
    mapper = CCDMapper()
    passed = 0
    failed = 0
    
    for test in TESTS:
        vid, pdb, name, mono, anomer, config, exp_ccd, exp_anom, exp_ring = test
        
        actual_ccd = mapper.map(mono, anomer, config)
        actual_anom = mapper.anomeric(actual_ccd) if actual_ccd else "N/A"
        actual_ring = mapper.ring_oxygen(actual_ccd) if actual_ccd else "N/A"
        
        ccd_ok = actual_ccd == exp_ccd
        anom_ok = actual_anom == exp_anom
        ring_ok = actual_ring == exp_ring
        
        status = "PASS" if (ccd_ok and anom_ok and ring_ok) else "FAIL"
        
        if status == "PASS":
            passed += 1
        else:
            failed += 1
        
        print(f"\n[{vid}] {name} (PDB: {pdb})")
        print(f"  CCD: {actual_ccd} (expected: {exp_ccd}) {'OK' if ccd_ok else 'FAIL'}")
        print(f"  Anomeric: {actual_anom} (expected: {exp_anom}) {'OK' if anom_ok else 'FAIL'}")
        print(f"  Ring O: {actual_ring} (expected: {exp_ring}) {'OK' if ring_ok else 'FAIL'}")
        print(f"  Status: [{status}]")
    
    print("\n" + "=" * 70)
    print(f"Results: {passed}/12 PASSED, {failed}/12 FAILED")
    print(f"Success Rate: {passed/12*100:.1f}%")
    print("=" * 70)
    
    return passed, failed

if __name__ == "__main__":
    main()
