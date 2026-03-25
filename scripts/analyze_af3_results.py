#!/usr/bin/env python3
"""
AF3 Results Analysis for GlycoSMILES2BAP Validation
Analyzes stereochemistry preservation in AF3 predicted structures

Run this script after AF3 predictions are complete.
"""

import json
import os
from pathlib import Path

OUTPUT_DIR = Path("./results/af3_output")
ANALYSIS_DIR = Path("./results/af3_analysis")
ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)

def analyze_structure(structure_name, output_path):
    results = {
        "structure": structure_name,
        "status": "pending",
        "stereochemistry_checks": {},
        "notes": []
    }
    
    cif_file = output_path / "model.cif"
    confidence_file = output_path / "summary_confidences_0.json"
    
    if not cif_file.exists():
        results["status"] = "failed"
        results["notes"].append("Missing model.cif file")
        return results
    
    if confidence_file.exists():
        with open(confidence_file) as f:
            confidence = json.load(f)
            results["confidence"] = confidence
    
    results["status"] = "completed"
    results["notes"].append("Structure file found - manual validation required")
    
    if "sialyllactose" in structure_name.lower():
        results["stereochemistry_checks"] = {
            "sialic_acid_c2_anomeric": "CHECK: Neu5Ac anomeric bond at C2 (not C1)",
            "sia_gal_linkage": "CHECK: Alpha(2-3) linkage geometry",
            "gal_glc_linkage": "CHECK: Beta(1-4) linkage geometry"
        }
    elif "lactose" in structure_name.lower():
        results["stereochemistry_checks"] = {
            "gal_glc_linkage": "CHECK: Beta(1-4) linkage geometry",
            "galactose_c4": "CHECK: C4 hydroxyl axial (GAL) vs equatorial (GLC)"
        }
    
    return results

def main():
    print("=" * 60)
    print("AF3 Results Analysis for GlycoSMILES2BAP Validation")
    print("=" * 60)
    print()
    
    structures = [
        ("sialyllactose_bap", "CRITICAL - C2 anomeric test"),
        ("lactose_bap", "Baseline test"),
        ("sialyllactose_smiles", "SMILES comparison")
    ]
    
    all_results = []
    
    for struct_name, description in structures:
        print(f"Analyzing: {struct_name} ({description})")
        print("-" * 50)
        
        output_path = OUTPUT_DIR / struct_name
        
        if output_path.exists():
            result = analyze_structure(struct_name, output_path)
            print(f"  Status: {result['status']}")
            
            if result['stereochemistry_checks']:
                print("  Stereochemistry Checks:")
                for check, desc in result['stereochemistry_checks'].items():
                    print(f"    - {desc}")
        else:
            result = {
                "structure": struct_name,
                "status": "not_found",
                "notes": ["Output directory not found"]
            }
            print(f"  Status: NOT FOUND")
            print(f"  Expected path: {output_path}")
        
        all_results.append(result)
        print()
    
    results_file = ANALYSIS_DIR / "validation_results.json"
    with open(results_file, 'w') as f:
        json.dump(all_results, f, indent=2)
    
    print("=" * 60)
    print("Analysis Summary")
    print("=" * 60)
    print(f"Results saved to: {results_file}")
    print()
    
    print("| Structure | Status | Description |")
    print("|-----------|--------|-------------|")
    for i, (struct_name, desc) in enumerate(structures):
        status = all_results[i]['status']
        print(f"| {struct_name} | {status} | {desc} |")
    print()
    
    completed = sum(1 for r in all_results if r['status'] == 'completed')
    print(f"Completed: {completed}/{len(structures)}")
    
    if completed == len(structures):
        print("\nAll predictions complete! Proceed to manual validation.")
    else:
        print("\nSome predictions are incomplete. Run AF3 first.")

if __name__ == "__main__":
    main()
