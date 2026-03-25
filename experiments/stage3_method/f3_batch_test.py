#!/usr/bin/env python3
"""Stage 3: F3 Batch Processing Experiment"""

import sys
sys.path.insert(0, '/home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides/src')

import json
import time

print("=" * 60)
print("Stage 3: F3 Batch Processing Experiment")
print("=" * 60)

from ccd_mapper import CCDMapper

mapper = CCDMapper()

# Test data: representative GlyTouCan structures
TEST_STRUCTURES = [
    # N-glycans
    {"id": "G00001MO", "name": "Man3_core", "sugars": [("Man", "alpha", "d"), ("Man", "alpha", "d"), ("Man", "beta", "d"), ("GlcNAc", "beta", "d"), ("GlcNAc", "beta", "d")]},
    {"id": "G00006MO", "name": "NA2", "sugars": [("Gal", "beta", "d"), ("GlcNAc", "beta", "d"), ("Man", "alpha", "d"), ("Gal", "beta", "d"), ("GlcNAc", "beta", "d"), ("Man", "alpha", "d"), ("Man", "beta", "d"), ("GlcNAc", "beta", "d"), ("GlcNAc", "beta", "d")]},
    {"id": "G00007MO", "name": "A2_sialylated", "sugars": [("Neu5Ac", "alpha", "d"), ("Gal", "beta", "d"), ("GlcNAc", "beta", "d"), ("Man", "alpha", "d")]},
    
    # O-glycans
    {"id": "G00050MO", "name": "Core1", "sugars": [("Gal", "beta", "d"), ("GalNAc", "alpha", "d")]},
    {"id": "G00051MO", "name": "Core2", "sugars": [("Gal", "beta", "d"), ("GlcNAc", "beta", "d"), ("GalNAc", "alpha", "d")]},
    
    # Fucosylated
    {"id": "G00200MO", "name": "LewisX", "sugars": [("Fuc", "alpha", "l"), ("Gal", "beta", "d"), ("GlcNAc", "beta", "d")]},
    
    # Sialylated
    {"id": "G00400MO", "name": "GM3", "sugars": [("Neu5Ac", "alpha", "d"), ("Gal", "beta", "d"), ("Glc", "beta", "d")]},
    
    # GAGs
    {"id": "G00500MO", "name": "Heparin_fragment", "sugars": [("IdoA", "alpha", "l"), ("GlcNS", "alpha", "d")]},
]

# Run batch processing
results = []
total_time = 0
success_count = 0

print("\nProcessing structures:")
print("-" * 60)

for struct in TEST_STRUCTURES:
    start_time = time.time()
    ccd_codes = []
    errors = []
    
    for sugar, anomer, config in struct["sugars"]:
        try:
            ccd = mapper.map(sugar, anomer, config)
            if ccd:
                ccd_codes.append(ccd)
            else:
                errors.append(f"No mapping for {sugar}")
        except Exception as e:
            errors.append(str(e))
    
    elapsed = time.time() - start_time
    total_time += elapsed
    
    success = len(errors) == 0
    if success:
        success_count += 1
    
    results.append({
        "id": struct["id"],
        "name": struct["name"],
        "sugar_count": len(struct["sugars"]),
        "mapped_count": len(ccd_codes),
        "ccd_codes": ccd_codes,
        "success": success,
        "errors": errors,
        "time": elapsed
    })
    
    status = "OK" if success else "ERROR"
    print(f"{struct['id']}: {struct['name']:20s} -> {len(ccd_codes)}/{len(struct['sugars'])} mapped [{status}]")

print("\n" + "=" * 60)
print("RESULTS SUMMARY")
print("="