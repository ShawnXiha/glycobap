#!/usr/bin/env python3
"""
GlycoSMILES2BAP Expanded Benchmark Test
Tests pipeline on representative structures from GlyTouCan database
"""

import json
import time
import sys
import os
from collections import defaultdict
from datetime import datetime

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

try:
    from glyco_smiles2bap import GlycoSMILES2BAPConverter
    from ccd_mapper import CCDMapper
    from bap_generator import BAPGenerator
except ImportError:
    print("Warning: Could not import main modules. Using mock implementation.")
    GlycoSMILES2BAPConverter = None
    CCDMapper = None
    BAPGenerator = None


class ExpandedBenchmarkTester:
    """Test GlycoSMILES2BAP on expanded benchmark from GlyTouCan"""
    
    def __init__(self):
        self.results = {
            'total_structures': 0,
            'successful': 0,
            'failed': 0,
            'errors': defaultdict(int),
            'processing_times': [],
            'monosaccharide_coverage': defaultdict(int),
            'category_results': defaultdict(lambda: {'success': 0, 'failed': 0}),
            'accuracy_metrics': {
                'epimer_correct': 0,
                'epimer_total': 0,
                'anomeric_correct': 0,
                'anomeric_total': 0,
                'linkage_correct': 0,
                'linkage_total': 0
            }
        }
        
        # Initialize converter if available
        if GlycoSMILES2BAPConverter:
            self.converter = GlycoSMILES2BAPConverter()
        else:
            self.converter = None
    
    def generate_glytoucan_representative_structures(self, n=1000):
        """
        Generate representative glycan structures covering GlyTouCan diversity.
        
        Categories based on GlyTouCan statistics:
        - N-glycans (high mannose, complex, hybrid)
        - O-glycans (core 1-4, sialylated, fucosylated)
        - Glycosphingolipids (ganglio, globo, lacto series)
        - Free oligosaccharides (human milk, plant, bacterial)
        - Lipopolysaccharides (bacterial)
        - Plant glycans (xylan, arabinan, pectin fragments)
        """
        
        structures = []
        
        # ===========================================
        # N-GLYCANS (High Mannose: Man5-9)
        # ===========================================
        n_glycans_high_mannose = [
            # Man5 (Man5GlcNAc2)
            "Man(a1-3)[Man(a1-3)[Man(a1-6)]Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc",
            "Man(a1-2)Man(a1-3)[Man(a1-3)[Man(a1-6)]Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc",
            "Man(a1-2)Man(a1-2)Man(a1-3)[Man(a1-3)[Man(a1-6)]Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc",
            # Man6
            "Man(a1-6)[Man(a1-3)]Man(a1-2)Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc",
            "Man(a1-3)[Man(a1-6)[Man(a1-3)]Man(a1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc",
            # Man7-9
            "Man(a1-2)Man(a1-6)[Man(a1-3)]Man(a1-2)Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc",
            "Man(a1-2)Man(a1-2)Man(a1-6)[Man(a1-3)]Man(a1-2)Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc",
            "Man(a1-2)Man(a1-2)Man(a1-2