#!/usr/bin/env python3
"""Stage 1 Baseline Test - Using correct CCDMapper interface"""

import sys
sys.path.insert(0, '/home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides/src')

import json
import time

print("=== Stage 1 Baseline Test ===\n")

results = {
    "stage": "Stage 1 - Initial Implementation",
    "date": "2026-03-21",
    "tests": []
}

# Test 1: CCD Mapper
print("1. Testing CCD Mapper...")
try:
    from ccd_mapper import CCDMapper
    mapper = CCDMapper()
    
    test_cases = [
        ("Man", "alpha", "d", "MAN"),
        ("GlcNAc", "beta", "d", "NAG"),
        ("Gal", "beta", "d", "GAL"),
        ("Fuc", "alpha", "l", "FUC"),
        ("Neu5Ac", "alpha", "d", "SIA"),
        ("Glc", "beta", "d", "GLC"),
        ("Neu5Gc", "alpha", "d", "NGC"),
        ("KDN", "alpha", "d", "KDN"),
        ("Xyl", "beta", "d", "XYS"),
        ("Rha", "alpha", "l", "RAM"),
    ]
    
    passed = 0
    for mono, anomer, config, expected in test_cases:
        result = mapper.map(mono, anomer, config)
        if result == expected:
            passed += 1
            print(f"   {mono}({anomer},{config}) -> {result} OK")
        else:
            print(f"   {mono}({anomer},{config}) -> {result} (expected {expected}) FAIL")
    
    print(f"   CCD Mapper: {passed}/{len(test_cases)} passed")
    results["tests"].append({
        "name": "CCD Mapper",
        "passed": passed,
        "total": len(test_cases),
        "status": "PASS" if passed == len(test_cases) else "PARTIAL"
    })
    
except Exception as e:
    print(f"   ERROR: {e}")
    results["tests"].append({"name": "CCD Mapper", "status": "ERROR", "error": str(e)})

# Test 2: Anomeric Carbon Position
print("\n2. Testing Anomeric Carbon Positions...")
try:
    anomeric_tests = [
        ("MAN", "C1"),  # Aldose
        ("NAG", "C1"),  # Aldose
        ("SIA", "C2"),  # Ketose (sialic acid)
        ("NGC", "C2"),  # Ketose
        ("KDN", "C2"),  # Ketose
        ("GLC", "C1"),  # Aldose
    ]
    
    passed = 0
    for ccd, expected in anomeric_tests:
        result = mapper.anomeric(ccd)
        if result == expected:
            passed += 1
            print(f"   {ccd} anomeric: {result} OK")
        else:
            print(f"   {ccd} anomeric: {result} (expected {expected}) FAIL")
    
    print(f"   Anomeric positions: {passed}/{len(anomeric_tests)} passed")
    results["tests"].append({
        "name": "Anomeric Carbon",
        "passed": passed,
        "total": len(anomeric_tests),
        "status": "PASS" if passed == len(anomeric_tests) else "PARTIAL"
    })
    
except Exception as e:
    print(f"   ERROR: {e}")
    results["tests"].append({"name": "Anomeric Carbon", "status": "ERROR", "error": str(e)})

# Test 3: Ring Oxygen Position
print("\n3. Testing Ring Oxygen Positions...")
try:
    ring_tests = [
        ("MAN", "O5"),  # Hexose
        ("NAG", "O5"),  # Hexosamine
        ("SIA", "O6"),  # Sialic acid
        ("XYS", "O4"),  # Pentose
        ("ARA", "O4"),  # Pentose
    ]
    
    passed = 0
    for ccd, expected in ring_tests:
        result = mapper.ring_oxygen(ccd)
        if result == expected:
            passed += 1
            print(f"   {ccd} ring oxygen: {result} OK")
        else:
            print(f"   {ccd} ring oxygen: {result} (