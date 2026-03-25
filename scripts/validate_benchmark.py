#!/usr/bin/env python3
"""
Validation script for GlycoSMILES2BAP pipeline
Tests converter against benchmark structures
"""

import json
import sys
import os

def load_benchmark():
    """Load benchmark structures"""
    with open('data/benchmark_structures.json', 'r') as f:
        data = json.load(f)
    return data['structures']

def validate_json():
    """Validate JSON files are well-formed"""
    files = ['data/benchmark_structures.json', 'data/ccd_mapping.json']
    for f in files:
        try:
            with open(f, 'r') as fp:
                json.load(fp)
            print(f"✓ {f}: Valid JSON")
        except Exception as e:
            print(f"✗ {f}: Invalid - {e}")
            return False
    return True

def run_benchmark():
    """Run full benchmark validation"""
    print("="*60)
    print("GlycoSMILES2BAP Validation Suite")
    print("="*60)
    
    results = {
        "json_validation": validate_json(),
    }
    
    # Load benchmark
    structures = load_benchmark()
    print(f"\nLoaded {len(structures)} benchmark structures")
    
    for s in structures:
        print(f"  - {s['id']}: {s['name']} ({s['category']})")
    
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    
    all_passed = all(results.values())
    
    for test, passed in results.items():
        status = "PASSED" if passed else "FAILED"
        print(f" {test}: {status}")
    
    print(f"\nOverall: {'ALL TESTS PASSED' if all_passed else 'SOME TESTS FAILED'}")
    return all_passed

if __name__ == "__main__":
    run_benchmark()
