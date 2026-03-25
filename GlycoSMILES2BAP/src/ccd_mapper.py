#!/usr/bin/env python3
"""
CCD Mapper Module for GlycoSMILES2BAP

This module maps monosaccharide residues to their corresponding 
Chemical Component Dictionary (CCD) codes for AlphaFold 3 input.

Author: Qiang Xia
License: MIT
"""

import re
from typing import Dict, Optional, Tuple
from dataclasses import dataclass


@dataclass
class CCDMapping:
    """Data class for CCD mapping information."""
    ccd_code: str
    anomeric_carbon: str  # C1 for aldoses, C2 for ketoses (sialic acids)
    ring_oxygen: str      # O4 for pentoses, O5 for hexoses, O6 for sialic acids
    absolute_config: str  # D or L


# CCD Mapping Table: (monosaccharide, anomer, config) -> CCDMapping
CCD_TABLE: Dict[Tuple[str, str, str], CCDMapping] = {
    # GlcNAc - N-acetylglucosamine
    ('glcnac', 'b', 'd'): CCDMapping('NAG', 'C1', 'O5', 'D'),
    ('glcnac', 'a', 'd'): CCDMapping('A2G', 'C1', 'O5', 'D'),
    
    # GalNAc - N-acetylgalactosamine  
    ('galnac', 'b', 'd'): CCDMapping('NGA', 'C1', 'O5', 'D'),
    ('galnac', 'a', 'd'): CCDMapping('A3G', 'C1', 'O5', 'D'),
    
    # Mannose
    ('man', 'a', 'd'): CCDMapping('MAN', 'C1', 'O5', 'D'),
    ('man', 'b', 'd'): CCDMapping('BMA', 'C1', 'O5', 'D'),
    
    # Galactose
    ('gal', 'b', 'd'): CCDMapping('GAL', 'C1', 'O5', 'D'),
    ('gal', 'a', 'd'): CCDMapping('GLA', 'C1', 'O5', 'D'),
    
    # Glucose
    ('glc', 'b', 'd'): CCDMapping('GLC', 'C1', 'O5', 'D'),
    ('glc', 'a', 'd'): CCDMapping('GLA', 'C1', 'O5', 'D'),
    
    # Fucose (6-deoxygalactose) - L-configuration
    ('fuc', 'a', 'l'): CCDMapping('FUC', 'C1', 'O5', 'L'),
    ('fuc', 'b', 'l'): CCDMapping('FUB', 'C1', 'O5', 'L'),
    
    # Sialic acids - C2 anomeric carbon (ketoses)
    ('neu5ac', 'a', 'd'): CCDMapping('SIA', 'C2', 'O6', 'D'),
    ('neu5gc', 'a', 'd'): CCDMapping('NGC', 'C2', 'O6', 'D'),
    ('neu5ac', 'b', 'd'): CCDMapping('BSI', 'C2', 'O6', 'D'),  # beta-sialic acid
    
    # Xylose - pentose (O4 ring oxygen)
    ('xyl', 'b', 'd'): CCDMapping('XYS', 'C1', 'O4', 'D'),
    ('xyl', 'a', 'd'): CCDMapping('AXY', 'C1', 'O4', 'D'),
    
    # Arabinose
    ('ara', 'a', 'l'): CCDMapping('ARA', 'C1', 'O4', 'L'),
    ('ara', 'b', 'l'): CCDMapping('ARB', 'C1', 'O4', 'L'),
    
    # Rhamnose
    ('rha', 'a', 'l'): CCDMapping('RAM', 'C1', 'O5', 'L'),
    
    # Galacturonic acid
    ('galac', 'a', 'd'): CCDMapping('GAD', 'C1', 'O5', 'D'),
    
    # Glucuronic acid
    ('glcac', 'b', 'd'): CCDMapping('GCU', 'C1', 'O5', 'D'),
}


class CCDMapper:
    """
