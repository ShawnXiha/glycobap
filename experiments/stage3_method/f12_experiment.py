#!/usr/bin/env python3
"""Stage 3: F12 Error Correction Experiment - Simplified"""

import sys
sys.path.insert(0, '/home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides/src')

print("=" * 60)
print("Stage 3: F12 Error Correction Experiment")
print("=" * 60)

from ccd_mapper import CCDMapper

mapper = CCDMapper()

# Test cases representing literature error corrections
ERROR_CASES = [
    ("Fuc", "alpha", "l", "FUC", "anomeric", "Case-01: Fucose anomer correction"),
    ("Man", "alpha", "d", "MAN", "anomeric", "Case-04a: Mannose anomer"),
    ("Man", "beta", "d", "BMA", "anomeric", "Case-04b: Beta-mannose"),
    ("GlcNAc", "beta", "d", "NAG", "linkage", "Case-03: N-linkage correction"),
    ("Gal", "beta", "d", "GAL", "epimer", "Case-09: Gal epimer"),
    ("Neu5Ac", "alpha", "d", "SIA", "anomeric", "Case-10: Sialic acid C2"),
    ("Fuc", "alpha", "l", "FUC", "conformation", "Case-02: Conformation"),
]

print("\nTesting error correction capability:")
print("-" * 60)

results = {"passed": 0, "failed": 0, "by_type": {}}

for mono, anomer, config, expected, error_type, desc in ERROR_CASES:
    result = mapper.map(mono, anomer, config)
    anomeric_pos = mapper.anomeric(result) if result else None
    ring_o = mapper.ring_oxygen(result) if result else None
    
    status = "PASS" if result == expected else "FAIL"
    if status == "PASS":
        results["passed"] += 1
    else:
        results["failed"] += 1
    
    if error_type not in results["by_type"]:
        results["by_type"][error_type] = {"pass": 0, "fail": 0}
    results["by_type"][error_type]["pass" if status == "PASS" else "fail"] += 1
    
    print(f"{desc}")
    print(f"  Input: {mono}({anomer},{config}) -> {result} (expected {expected}) [{status}]")
    if result:
        print(f"  Anomeric: {anomeric_pos}, Ring O: {ring_o}")

print("\n" + "=" * 60)
print("RESULTS SUMMARY")
print("=" * 60)
print(f"Total cases: {len(ERROR_CASES)}")
print(f"Passed: {results['passed']}")
print(f"Failed: {results['failed']}")
print(f"Correction rate: {results['passed']/len(ERROR_CASES)*100:.1f}%")

print("\nBy error type:")
for etype, counts in results["by_type"].items():
    rate = counts["pass"] / (counts["pass"] + counts["fail"]) * 100
    print(f"  {etype}: {counts['pass']}/{counts['pass']+counts['fail']} ({rate:.0f}%)")

# Save results
import json
with open('/experiments/stage3_method/f12_results.json', 'w') as f:
    json.dump({
        "experiment": "F12_Error_Correction",
        "total_cases": len(ERROR_CASES),
        "passed": results["passed"],
        "failed": results["failed"],
        "correction_rate": results["passed"]/len(ERROR_CASES),
        "by_error_type": results["by_type"]
    }, f, indent=2)

print("\nResults saved to f12_results.json")
