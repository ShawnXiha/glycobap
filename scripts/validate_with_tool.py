#!/usr/bin/env python3
"""
PDB Validation Step 2: Use GlycoSMILES2BAP to validate CCD codes
"""

import sys
import os
import json

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ccd_mapper import CCDMapper

OUTPUT_DIR = "./results/pdb_validation/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Test cases
CASES = [
    {"id": "V001", "name": "Fucosylated", "iupac": "Fuc(a1-2)Gal(b1-4)Glc",
     "expected_ccd": ["FUC", "GAL", "GLC"], "key_check": "FUC=alpha-L-fucose"},
    {"id": "V002", "name": "Lactose", "iupac": "Gal(b1-4)Glc",
     "expected_ccd": ["GAL", "GLC"], "key_check": "GAL C4 axial"},
    {"id": "V003", "name": "Sialyllactose", "iupac": "Neu5Ac(a2-3)Gal(b1-4)Glc",
     "expected_ccd": ["SIA", "GAL", "GLC"], "key_check": "SIA anomeric=C2"},
    {"id": "V004", "name": "M3_N-glycan", "iupac": "Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc",
     "expected_ccd": ["MAN", "MAN", "BMA", "NAG", "NAG"], "key_check": "Branch topology"},
]

def parse_iupac_simple(iupac):
    """Simple IUPAC parser for testing."""
    residues = []
    iupac = iupac.replace(" ", "")
    
    # Handle branched structures
    import re
    
    # Pattern for monosaccharide with anomer
    pattern = r'([A-Z][a-z]+(?:NAc|NAc|5Ac|5Gc)?)\(([ab][1-9])\-([1-9])\)'
    
    # Extract residues
    matches = re.findall(pattern, iupac)
    
    for mono, linkage, pos in matches:
        anomer = "alpha" if linkage[0] == "a" else "beta"
        residues.append({"mono": mono, "anomer": anomer})
    
    return residues

def main():
    print("=" * 60)
    print("PDB Validation - Step 2: GlycoSMILES2BAP CCD Mapping")
    print("=" * 60)
    print()
    
    mapper = CCDMapper()
    results = []
    
    for case in CASES:
        print(f"[{case['id']}] {case['name']}")
        print(f"  IUPAC: {case['iupac']}")
        print(f"  Expected CCD: {case['expected_ccd']}")
        
        # Parse IUPAC
        residues = parse_iupac_simple(case['iupac'])
        
        # Map to CCD codes
        actual_ccd = []
        for r in residues:
            mono = r['mono'].lower()
            anomer = r['anomer']
            config = 'l' if mono == 'fuc' else 'd'
            
            ccd = mapper.map(mono, anomer, config)
            if ccd:
                actual_ccd.append(ccd)
                anomeric = mapper.anomeric(ccd)
                print(f"    {mono}({anomer}) -> {ccd} (anomeric: {anomeric})")
            else:
                print(f"    {mono}({anomer}) -> NOT FOUND")
        
        # Compare
        match = actual_ccd == case['expected_ccd']
        status = "PASS" if match else "FAIL"
        
        print(f"  Actual CCD: {actual_ccd}")
        print(f"  Status: [{status}]")
        print()
        
        results.append({
            "id": case['id'],
            "name": case['name'],
            "expected_ccd": case['expected_ccd'],
            "actual_ccd": actual_ccd,
            "match": match,
            "status": status
        })
    
    # Save results
    output_file = os.path.join(OUTPUT_DIR, "validation_results.json") 
    with open(output_file, "w") as f: 
        json.dump(results, f, indent=2) 
    print(f"Results saved to: {output_file}") 

if __name__ == "__main__": 
    main()
