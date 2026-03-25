#!/usr/bin/env python3
"""
GlycoSMILES2BAP: Automated Glycan to CCD+BAP Converter for AlphaFold 3

This module provides the core pipeline for converting glycan structures
from IUPAC-condensed, WURCS, or GlycoCT format to AF3-compatible 
CCD + bondedAtomPairs JSON format.

Author: GlycoSMILES2BAP Project
License: MIT
"""

import json
from typing import Dict, List, Optional, Union
from dataclasses import dataclass, field
from pathlib import Path

# Import local modules
try:
    from ccd_mapper import CCDMapper, MonosaccharideType
    from bap_generator import BAPGenerator
except ImportError:
    # Handle case when running as standalone
    pass


@dataclass
class GlycanNode:
    """Represents a single monosaccharide node in the glycan tree."""
    id: int
    monosaccharide: str
    anomer: str  # alpha or beta
    ring_type: str = "pyranose"  # pyranose or furanose
    modifications: List[str] = field(default_factory=list)
    

@dataclass  
class GlycanEdge:
    """Represents a glycosidic linkage between two monosaccharides."""
    donor_id: int
    acceptor_id: int
    donor_position: int  # Position on donor (usually anomeric C1)
    acceptor_position: int  # Position on acceptor (e.g., 4 for 1-4 linkage)
    linkage_type: str = "O-glycosidic"  # O-glycosidic or N-glycosidic


@dataclass
class GlycanTopology:
    """Represents the complete glycan structure as a tree."""
    nodes: List[GlycanNode]
    edges: List[GlycanEdge]
    root_id: int = 0
    name: str = ""
    iupac_notation: str = ""
    

class GlycoSMILES2BAP:
    """
    Main converter class for glycan structure conversion to AF3 format.
    
    Usage:
        converter = GlycoSMILES2BAP()
        result = converter.convert("Gal(b1-4)Glc", format="IUPAC")
        print(json.dumps(result, indent=2))
    """
    
    def __init__(self, ccd_mapping_file: Optional[str] = None):
        """
        Initialize the converter.
        
        Args:
            ccd_mapping_file: Path to custom CCD mapping JSON file.
                            If None, uses default mapping.
        """
        self.ccd_mapper = CCDMapper(ccd_mapping_file)
        self.bap_generator = BAPGenerator()
        
    def convert(
        self, 
        glycan_input: str, 
        format: str = "IUPAC",
        validate: bool = True
    ) -> Dict:
        """
        Convert glycan notation to AF3-compatible CCD+BAP format.
        
        Args:
            glycan_input: Glycan structure string
            format: Input format - "IUPAC", "WURCS", or "GlycoCT"
            validate: Whether to validate output stereochemistry
            
        Returns:
            Dictionary with 'ccdCodes' and 'bondedAtomPairs' keys
            
        Raises:
            ValueError: If input format is unsupported or parsing fails
        """
        # Step 1: Parse input to topology
        topology = self._parse_input(glycan_input, format)
        
        # Step 2: Map monosaccharides to CCD codes
        ccd_codes = self.ccd_mapper.map_all(topology.nodes)
        
        # Step 3: Generate bondedAtomPairs from topology
        bonded_pairs = self.bap_generator.generate(topology.edges, ccd_codes)
        
        # Step 4: Validate if requested
        if validate:
            self._validate_output(ccd_codes, bonded_pairs)
        
        return {
            "name": topology.name,
            "iupac": topology.iupac_notation,
            "ccdCodes": ccd_codes,
            "bondedAtomPairs": bonded_pairs
        }
    
    def _parse_input(self, glycan_input: str, format: str) -> GlycanTopology:
        """
        Parse input glycan string to GlycanTopology.
        
        Args:
            glycan_input: Input string
            format: Format type
            
        Returns:
            GlycanTopology object
        """
        format = format.upper()
        
        if format == "IUPAC":
            return self._parse_iupac(glycan_input)
        elif format == "WURCS":
            return self._parse_wurcs(glycan_input)
        elif format