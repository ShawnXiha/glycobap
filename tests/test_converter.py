"""
Test suite for GlycoSMILES2BAP converter
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
import json
from src.ccd_mapper import CCDMapper
from src.bap_generator import BAPGenerator


class TestCCDMapper(unittest.TestCase):
    """Test cases for CCD Mapper module"""
    
    def setUp(self):
        self.mapper = CCDMapper()
    
    def test_glcna_beta_mapping(self):
        """Test GlcNAc beta mapping to NAG"""
        result = self.mapper.map_residue("GlcNAc", "beta", "D")
        self.assertEqual(result, "NAG")
    
    def test_glcna_alpha_mapping(self):
        """Test GlcNAc alpha mapping to A2G"""
        result = self.mapper.map_residue("GlcNAc", "alpha", "D")
        self.assertEqual(result, "A2G")
    
    def test_mannose_mapping(self):
        """Test mannose mapping"""
        result = self.mapper.map_residue("Man", "alpha", "D")
        self.assertEqual(result, "MAN")
        
        result = self.mapper.map_residue("Man", "beta", "D")
        self.assertEqual(result, "BMA")
    
    def test_galactose_mapping(self):
        """Test galactose mapping"""
        result = self.mapper.map_residue("Gal", "beta", "D")
        self.assertEqual(result, "GAL")
        
        result = self.mapper.map_residue("Gal", "alpha", "D")
        self.assertEqual(result, "GLA")
    
    def test_fucose_mapping(self):
        """Test fucose (L-config) mapping"""
        result = self.mapper.map_residue("Fuc", "alpha", "L")
        self.assertEqual(result, "FUC")
    
    def test_sialic_acid_mapping(self):
        """Test sialic acid mapping"""
        result = self.mapper.map_residue("Neu5Ac", "alpha", "D")
        self.assertEqual(result, "SIA")
    
    def test_unknown_residue(self):
        """Test handling of unknown residue"""
        result = self.mapper.map_residue("Unknown", "beta", "D")
        self.assertIsNone(result)
    
    def test_get_anomeric_position(self):
        """Test anomeric carbon position retrieval"""
        pos = self.mapper.get_anomeric_position("NAG")
        self.assertEqual(pos, "C1")
        
        # Sialic acid is a ketose, anomeric carbon is C2
        pos = self.mapper.get_anomeric_position("SIA")
        self.assertEqual(pos, "C2")


class TestBAPGenerator(unittest.TestCase):
    """Test cases for BAP Generator module"""
    
    def setUp(self):
        self.generator = BAPGenerator()
    
    def test_single_bap_generation(self):
        """Test single bondedAtomPair generation"""
        bap = self.generator.generate_bap(
            donor_residue_id=1,
            acceptor_residue_id=2,
            donor_ccd="NAG",
            acceptor_ccd="GAL",
            linkage_position=(4, 1)
        )
        
        self.assertEqual(bap["residue1"], 1)
        self.assertEqual(bap["atom1"], "C1")
        self.assertEqual(bap["residue2"], 2)
        self.assertEqual(bap["atom2"], "O4")
        self.assertEqual(bap["order"], 1)
    
    def test_sialic_acid_bap(self):
        """Test BAP generation for sialic acid"""
        bap = self.generator.generate_bap(
            donor_residue_id=1,
            acceptor_residue_id=2,
            donor_ccd="SIA",
            acceptor_ccd="GAL",
            linkage_position=(3, 2)
        )
        
        # Sialic acid anomeric carbon is C2
        self.assertEqual(bap["atom1"], "C2")
    
    def test_topology_to_bap(self):
        """Test topology to BAP conversion"""
        topology = [
            {"donor_idx": 0, "acceptor_idx": 1, "linkage": (4, 1)},
            {"donor_idx": 1, "acceptor_idx": 2, "linkage": (4, 1)},
        ]
        ccd_codes = ["NAG", "GAL", "GLC"]
        
        bap_list = self.generator.generate_from_topology(topology, ccd_codes)
        
        self.assertEqual(len(bap_list), 2)
        self.assertEqual(bap_list[0]["residue1"], 1)
        self.assertEqual(bap_list[0]["residue2"], 2)
        self