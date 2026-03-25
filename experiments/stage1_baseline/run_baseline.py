#!/usr/bin/env python3
"""
Stage 1 Baseline Test: GlycoSMILES2BAP Validation
Tests the existing implementation to establish baseline metrics.
"""

import sys
sys.path.insert(0, '/home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides/src')

import json
import time

# Test cases
TEST_CASES = [
    {"name": "Lactose", "iupac": "Gal(b1-4)Glc", "expected_ccd": ["GLA", "GLC"]},
    {"name": "Maltose", "iupac": "Glc(a1-4)Glc", "expected_ccd": ["GLC", "GLC"]},
    {"name": "Sialyllactose", "iupac": "Neu5Ac(a2-3)Gal(b1-4)Glc", "expected_ccd": ["SIA", "GLA", "GLC"]},
    {"name": "Man3_core", "iupac": "Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "expected_ccd": ["MAN", "MAN", "MAN", "NAG", "NAG"]},
]

results = {
    "stage": "Stage 1: Initial Implementation",
    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    "tests": []
}

# Test 1: CCD Mapper
print("=" * 60)
print("TEST 1: CCD Mapper Module")
print("=" * 60)

try:
    from ccd_mapper import CCDMapper
    mapper = CCDMapper()
    
    test_sugars = [
        ("Glc", "a", "GLC"),
        ("Glc", "b", "GLC"),
        ("Gal", "b", "GLA"),
        ("Man", "a", "MAN"),
        ("Man", "b", "MAN"),
        ("Fuc", "a", "FUC"),
        ("Neu5Ac", "a", "SIA"),
        ("GlcNAc", "b", "NAG"),
    ]
    
    passed = 0
    failed = 0
    for sugar, anomer, expected in test_sugars:
        ccd = mapper.get_ccd(sugar, anomer)
        status = "PASS" if ccd == expected else "FAIL"
        if status == "PASS":
            passed += 1
        else:
            failed += 1
        print(f"  {sugar}({anomer}) -> {ccd} (expected: {expected}) [{status}]")
    
    print(f"\n  Result: {passed}/{len(test_sugars)} passed")
    results["tests"].append({
        "name": "CCD Mapper",
        "passed": passed,
        "total": len(test_sugars),
        "status": "PASS" if passed == len(test_sugars) else "PARTIAL"
    })
except Exception as e:
    print(f"  ERROR: {e}")
    results["tests"].append({"name": "CCD Mapper", "status": "ERROR", "error": str(e)})

# Test 2: BAP Generator
print("\n" + "=" * 60)
print("TEST 2: BAP Generator Module")
print("=" * 60)

try:
    from bap_generator import BAPGenerator
    gen = BAPGenerator()
    
    # Test BAP generation
    bap = gen.generate_bond("GLA", "GLC", 1, 4, "b")
    expected_bap = [["GLA-1", "C1", "GLC-2", "O4"]]
    
    status = "PASS" if bap else "FAIL"
    print(f"  BAP for Gal(b1-4)Glc: {bap}")
    print(f"  Status: {status}")
    
    results["tests"].append({
        "name": "BAP Generator",
        "status": status,
        "output": str(bap)
    })
except Exception as e:
    print(f"  ERROR: {e}")
    results["tests"].append({"name": "BAP Generator", "status": "ERROR", "error": str(e)})

# Test 3: Performance
print("\n" + "=" * 60)
print("TEST 3: Performance Benchmark")
print("=" * 60)

try:
    from ccd_mapper import CCDMapper
    mapper = CCDMapper()
    
    start = time.time()
    for _ in range(1000):
        mapper.get_ccd("Glc