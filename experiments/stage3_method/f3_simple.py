#!/usr/bin/env python3
"""F3 Batch Processing Test - Simplified"""

import sys
sys.path.insert(0, '/home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides/src')

from ccd_mapper import CCDMapper

print("=" * 60)
print("F3: GlyTouCan Batch Processing Test")
print("=" * 60)

mapper = CCDMapper()

# Representative structures (subset of 20)
STRUCTURES = [
    {"id": "G00001MO", "name": "Man3_core", "sugars": [("Man", "alpha", "d"), ("Man", "alpha", "d"), ("Man", "beta", "d"), ("GlcNAc", "beta", "d"), ("GlcNAc", "beta", "d")]},
    {"id": "G00006MO", "name": "NA2", "sugars": [("Gal", "beta", "d"), ("GlcNAc", "beta", "d"), ("Man", "alpha", "d"), ("Gal", "beta", "d"), ("GlcNAc", "beta", "d"), ("Man", "alpha", "d"), ("Man", "beta", "d"), ("GlcNAc", "beta", "d"), ("GlcNAc", "beta", "d")]},
    {"id": "G00007MO", "name": "A2", "sugars": [("Neu5Ac", "alpha", "d"), ("Gal", "beta", "d"), ("GlcNAc", "beta", "d"), ("Man", "alpha", "d"), ("Neu5Ac", "alpha", "d"), ("Gal", "beta", "d"), ("GlcNAc", "beta", "d"), ("Man", "alpha", "d"), ("Man", "beta", "d"), ("GlcNAc", "beta", "d"), ("GlcNAc", "beta", "d")]},
    {"id": "G00010MO", "name": "A2F", "sugars": [("Neu5Ac", "alpha", "d"), ("Gal", "beta", "d"), ("GlcNAc", "beta", "d"), ("Man", "alpha", "d"), ("Neu5Ac", "alpha", "d"), ("Gal", "beta", "d"), ("GlcNAc", "beta", "d"), ("Man", "alpha", "d"), ("Man", "beta", "d"), ("GlcNAc", "beta", "d"), ("Fuc", "alpha", "l"), ("GlcNAc", "beta", "d")]},
    {"id": "G00100MO", "name": "Lactose", "sugars": [("Gal", "beta", "d"), ("Glc", "beta", "d")]},
    {"id": "G00101MO", "name": "Sialyllactose", "sugars": [("Neu5Ac", "alpha", "d"), ("Gal", "beta", "d"), ("Glc", "beta", "d")]},
    {"id": "G00102MO", "name": "Heparin_frag", "sugars": [("IdoA", "alpha", "l"), ("GlcA", "beta", "d")]},
    {"id": "G00200MO", "name": "LewisX", "sugars": [("Fuc", "alpha", "l"), ("Gal", "beta", "d"), ("GlcNAc", "beta", "d")]},
    {"id": "G00201MO", "name": "SialylLewisX", "sugars": [("Neu5Ac", "alpha", "d"), ("Gal", "beta", "d"), ("Fuc", "alpha", "l"), ("GlcNAc", "beta", "d")]},
    {"id": "G00300MO", "name": "Core1_O", "sugars": [("Gal", "beta", "d"), ("GalNAc", "alpha", "d")]},
    {"id": "G00301MO", "name": "Core2_O", "sugars": [("Gal", "beta", "d"), ("GlcNAc", "beta", "d"), ("GalNAc", "alpha", "d")]},
    {"id": "G00400MO", "name": "