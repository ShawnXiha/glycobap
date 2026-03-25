#!/usr/bin/env python3
"""
Stage 3: F3 GlyTouCan Batch Processing Experiment
Tests GlycoSMILES2BAP's ability to process large-scale glycan structures.
"""

import sys
sys.path.insert(0, '/home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides/src')

import json
import time
from typing import Dict, List

print("=" * 60)
print("Stage 3: F3 GlyTouCan Batch Processing Experiment")
print("=" * 60)

from ccd_mapper import CCDMapper
from bap_generator import BAPGenerator

# Initialize modules
mapper = CCDMapper()
generator = BAPGenerator()

# Representative glycan structures (subset of GlyTouCan)
GLYTOUCAN_SUBSET = [
    # N-glycans (mammalian)
    {"id": "G00001MO", "name": "Man3_core", "monosaccharides": [("Man", "alpha", "d"), ("Man", "alpha", "d"), ("Man", "beta", "d"), ("GlcNAc", "beta", "d"), ("GlcNAc", "beta", "d")]},
    {"id": "G00002MO", "name": "Man5", "monosaccharides": [("Man", "alpha", "d"), ("Man", "alpha", "d"), ("Man", "alpha", "d"), ("Man", "alpha", "d"), ("Man", "alpha", "d"), ("Man", "beta", "d"), ("GlcNAc", "beta", "d"), ("GlcNAc", "beta", "d")]},
    {"id": "G00003MO", "name": "NA2", "monosaccharides": [("Gal", "beta", "d"), ("GlcNAc", "beta", "d"), ("Man", "alpha", "d"), ("Gal", "beta", "d"), ("GlcNAc", "beta", "d"), ("Man", "alpha", "d"), ("Man", "beta", "d"), ("GlcNAc", "beta", "d"), ("GlcNAc", "beta", "d")]},
    {"id": "G00004MO", "name": "A2", "monosaccharides": [("Neu5Ac", "alpha", "d"), ("Gal", "beta", "d"), ("GlcNAc", "beta", "d"), ("Man", "alpha", "d"), ("Neu5Ac", "alpha", "d"), ("Gal", "beta", "d"), ("GlcNAc", "beta", "d"), ("Man", "alpha", "d"), ("Man", "beta", "d"), ("GlcNAc", "beta", "d"), ("GlcNAc", "beta", "d")]},
    
    # O-glycans
    {"id": "G00050MO", "name": "Core1", "monosaccharides": [("Gal", "beta", "d"), ("GalNAc", "alpha", "d")]},
    {"id": "G00051MO", "name": "Core2", "monosaccharides": [("Gal", "beta", "d"), ("GlcNAc", "beta", "d"), ("GalNAc", "alpha", "d")]},
    {"id": "G00052MO", "name": "Sialyl Core1", "monosaccharides": [("Neu5Ac", "alpha", "d"), ("Gal", "beta", "d"), ("GalNAc", "alpha", "d")]},
    
    # Glycosaminoglycans
    {"id": "G00100MO", "name": "Hyaluronan_fragment", "monosaccharides": [("GlcA", "beta", "d"), ("GlcNAc", "beta", "d")]},
    {"id": "G00101MO", "name": "Chondroitin_fragment", "monosaccharides": [("GlcA", "beta", "d"), ("GalNAc", "beta", "d")]},
    {"id": "G00102MO", "name": "Heparin_fragment", "monosaccharides": [("IdoA", "alpha", "l"), ("GlcNS", "alpha", "d")]},
    
    # Fucosylated structures
    {"id": "G00200MO", "name": "LewisX", "monosaccharides": [("