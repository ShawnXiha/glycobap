#!/usr/bin/env python3
"""
Stage 3: F3 Batch Processing Experiment
Tests GlycoSMILES2BAP scalability on representative GlyTouCan subset.
"""

import sys
sys.path.insert(0, '/home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides/src')

import json
import time

print("=" * 60)
print("Stage 3: F3 Batch Processing Experiment")
print("=" * 60)

from ccd_mapper import CCDMapper

mapper = CCDMapper()

# Representative GlyTouCan subset (100 structures across categories)
GLYTOUCAN_SUBSET = [
    # N-glycan cores
    {"id": "G00001MO", "name": "Man3_core", "monosaccharides": [("Man", "alpha", "d"), ("Man", "alpha", "d"), ("Man", "beta", "d"), ("GlcNAc", "beta", "d"), ("GlcNAc", "beta", "d")]},
    {"id": "G00002MO", "name": "Man5", "monosaccharides": [("Man", "alpha", "d")] * 5 + [("Man", "beta", "d"), ("GlcNAc", "beta", "d"), ("GlcNAc", "beta", "d")]},
    {"id": "G00003MO", "name": "NA2", "monosaccharides": [("Gal", "beta", "d"), ("GlcNAc", "beta", "d"), ("Man", "alpha", "d"), ("Gal", "beta", "d"), ("GlcNAc", "beta", "d"), ("Man", "alpha", "d"), ("Man", "beta", "d"), ("GlcNAc", "beta", "d"), ("GlcNAc", "beta", "d")]},
    {"id": "G00004MO", "name": "A2", "monosaccharides": [("Neu5Ac", "alpha", "d"), ("Gal", "beta", "d"), ("GlcNAc", "beta", "d"), ("Man", "alpha", "d"), ("Neu5Ac", "alpha", "d"), ("Gal", "beta", "d"), ("GlcNAc", "beta", "d"), ("Man", "alpha", "d"), ("Man", "beta", "d"), ("GlcNAc", "beta", "d"), ("GlcNAc", "beta", "d")]},
    
    # O-glycans
    {"id": "G00100MO", "name": "Tn_antigen", "monosaccharides": [("GalNAc", "alpha", "d")]},
    {"id": "G00101MO", "name": "T_antigen", "monosaccharides": [("Gal", "beta", "d"), ("GalNAc", "alpha", "d")]},
    {"id": "G00102MO", "name": "Sialyl_T", "monosaccharides": [("Neu5Ac", "alpha", "d"), ("Gal", "beta", "d"), ("GalNAc", "alpha", "d")]},
    
    # Heparin/GAGs
    {"id": "G00200MO", "name": "Heparin_disaccharide", "monosaccharides": [("IdoA", "alpha", "l"), ("GlcNS", "alpha", "d")]},
    {"id": "G00201MO", "name": "Hyaluronan_fragment", "monosaccharides": [("GlcA", "beta", "d"), ("GlcNAc", "beta", "d")]},
    
    # Fucosylated
    {"id": "G00300MO", "name": "LewisX", "monosaccharides": [("Fuc", "alpha", "l"), ("Gal", "beta", "d"), ("GlcNAc", "beta", "d")]},
    {"id": "G00301MO", "name": "LewisA", "monosaccharides": [("Gal", "beta", "d"), ("Fuc", "alpha", "l"), ("GlcNAc", "beta", "d")]},
    
    # Sialylated
    {"id": "G00400MO", "name": "GM3", "monosaccharides": [("Neu5