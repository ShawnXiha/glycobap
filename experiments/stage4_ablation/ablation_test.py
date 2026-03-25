#!/usr/bin/env python3
"""
Stage 4: Ablation Study for F12/F3
Tests each module's contribution to error correction capability.
"""

import sys
sys.path.insert(0, '/home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides/src')

print("=" * 60)
print("Stage 4: Ablation Study")
print("=" * 60)

from ccd_mapper import CCDMapper

# Ablation configurations
ABLATION_TESTS = {
    "full_pipeline": {
        "description": "Full GlycoSMILES2BAP pipeline",
        "use_ccd_mapper": True,
        "use_anomeric_tracking": True,
        "use_ring_oxygen": True
    },
    "no_ccd_mapper": {
        "description": "Without CCD Mapper (random CCD assignment)",
        "use_ccd_mapper": False,
        "use_anomeric_tracking": True,
        "use_ring_oxygen": True
    },
    "no_anomeric_tracking": {
        "description": "Without anomeric position tracking (always C1)",
        "use_ccd_mapper": True,
        "use_anomeric_tracking": False,
        "use_ring_oxygen": True
    },
    "no_ring_oxygen": {
        "description": "Without ring oxygen tracking (always O5)",
        "use_ccd_mapper": True,
        "use_anomeric_tracking": True,
        "use_ring_oxygen": False
    }
}

# Test cases covering different error types
TEST_CASES = [
    {"sugar": "Neu5Ac", "anomer": "alpha", "config": "d", "expected_ccd": "SIA", 
     "expected_anomeric": "C2", "expected_ring": "O6", "error_type": "anomeric"},
    {"sugar": "Fuc", "anomer": "alpha", "config": "l", "expected_ccd": "FUC",
     "expected_anomeric": "C1", "expected_ring": "O5", "error_type": "epimer"},
    {"sugar": "Man", "anomer": "alpha", "config": "d", "expected_ccd": "MAN",
     "expected_anomeric": "C1", "expected_ring": "O5", "error_type": "anomeric"},
    {"sugar": "Xyl", "anomer": "beta", "config": "d", "expected_ccd": "XYS",
     "expected_anomeric": "C1", "expected_ring": "O4", "error_type": "linkage"},
]

def run_ablation(config_name, config, test_cases):
    """Run ablation test with given configuration."""
    correct_ccd = 0
    correct_anomeric = 0
    correct_ring = 0
    
    mapper = CCDMapper()
    
    for case in test_cases:
        # CCD mapping
        if config["use_ccd_mapper"]:
            ccd = mapper.map(case["sugar"], case["anomer"], case["config"])
        else:
            # Simulate random/baseline assignment
            ccd = "GLC"  # Generic fallback
        
        # Anomeric position
        if config["use_anomeric_tracking"]:
            anomeric = mapper.anomeric(ccd) if ccd else "C1"
        else:
            anomeric = "C1"  # Always assume C1
        
        # Ring oxygen
        if config["use_ring_oxygen"]:
            ring = mapper.ring_oxygen(ccd) if ccd else "O5"
        else:
            ring = "O5"  # Always assume O5
        
        # Check correctness
        if ccd == case["expected_ccd"]:
            correct_ccd += 1
        if anomeric == case["expected_anomeric"]:
            correct_anomeric += 1
        if ring == case["expected_ring"]:
            correct_ring += 1
    
    return {
        "ccd_accuracy": correct_ccd / len(test_cases) * 100,
        "anomeric_accuracy": correct_anomeric / len(test_cases) * 100,
        "ring_accuracy": correct_ring / len(test_cases) * 100
    }

# Run all ablation tests
results = {}
for config_name, config in ABLATION_TESTS.items():
    result = run_ablation(config_name, config, TEST_CASES)
    results[config_name] = result
    
    print(f"\n{config['description']}:")
    print(f" 