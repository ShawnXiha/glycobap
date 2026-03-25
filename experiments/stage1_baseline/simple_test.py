#!/usr/bin/env python3
"""
Stage 1 Baseline Test: Simple GlycoSMILES2BAP Validation
Tests CCD Mapper and BAP Generator modules.
"""

import sys
sys.path.insert(0, '/home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides/src')

import json
import time

def main():
    print("=" * 60)
    print("Stage 1: Baseline Test - GlycoSMILES2BAP")
    print("=" * 60)
    
    results = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "tests": []
    }
    
    # Test 1: CCD Mapper
    print("\n[Test 1] CCD Mapper Module")
    try:
        from ccd_mapper import CCDMapper
        mapper = CCDMapper()
        
        test_cases = [
            ("Glc", "b", "GLC"),
            ("Glc", "a", "GLC"),
            ("Gal", "b", "GLA"),
            ("Man", "a", "MAN"),
            ("Fuc", "a", "FUC"),
            ("Neu5Ac", "a", "SIA"),
            ("GlcNAc", "b", "NAG"),
        ]
        
        passed = 0
        for sugar, anomer, expected in test_cases:
            result = mapper.get_ccd(sugar, anomer)
            status = "PASS" if result == expected else f"FAIL (got {result})"
            print(f"  {sugar}({anomer}) -> {expected}: {status}")
            if result == expected:
                passed += 1
        
        print(f"  Result: {passed}/{len(test_cases)} passed")
        results["tests"].append({
            "name": "CCD Mapper",
            "passed": passed,
            "total": len(test_cases),
            "status": "PASS" if passed == len(test_cases) else "PARTIAL"
        })
    except Exception as e:
        print(f"  ERROR: {e}")
        results["tests"].append({"name": "CCD Mapper", "status": "ERROR", "error": str(e)})
    
    # Test 2: BAP Generator
    print("\n[Test 2] BAP Generator Module")
    try:
        from bap_generator import BAPGenerator
        generator = BAPGenerator()
        
        # Test basic BAP generation
        test_bonds = [
            (1, 2, "C1", "O4"),
            (2, 3, "C1", "O6"),
        ]
        
        passed = 0
        for donor_id, acceptor_id, donor_atom, acceptor_atom in test_bonds:
            try:
                bap = generator.generate_bap(donor_id, acceptor_id, donor_atom, acceptor_atom)
                if bap:
                    passed += 1
                    print(f"  BAP({donor_id},{acceptor_id}): {bap}")
            except Exception as e:
                print(f"  BAP({donor_id},{acceptor_id}): ERROR - {e}")
        
        print(f"  Result: {passed}/{len(test_bonds)} passed")
        results["tests"].append({
            "name": "BAP Generator",
            "passed": passed,
            "total": len(test_bonds),
            "status": "PASS" if passed == len(test_bonds) else "PARTIAL"
        })
    except Exception as e:
        print(f"  ERROR: {e}")
        results["tests"].append({"name": "BAP Generator", "status": "ERROR", "error": str(e)})
    
    # Test 3: Performance
    print("\n[Test 3] Performance Test")
    try:
        from ccd_mapper import CCDMapper
        mapper = CCDMapper()
        
        start = time.time()
        for _ in range(1000):
            mapper.get_ccd("Glc", "b")
        elapsed = time.time() - start
        
        print(f"  1000 CCD lookups: {elapsed*1000:.2f}ms")
        print(f"  Average: {elapsed:.6f}s per lookup")
        results["tests"].append({
            "name": "Performance",
            "time_1000_lookups": f"{elapsed*1000:.2f}ms",
            "status": "PASS"
        })
    except Exception as e:
        print(f"  ERROR: {e}")
        results["tests"].append({"name": "Performance", "status": "ERROR", "error": str(e)})
    
    # Summary
    print("\n"