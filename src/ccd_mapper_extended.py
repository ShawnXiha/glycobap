"""Extended CCD Mapper Module - Includes rare monosaccharides"""

from typing import Optional, List, Dict

class CCDMapperExtended:
    """Extended CCD mapper with rare monosaccharide support."""

    # Comprehensive CCD mapping - common + rare monosaccharides
    CCD_TABLE = {
        # Common hexoses
        ('glc', 'beta', 'd'): 'GLC',
        ('glc', 'alpha', 'd'): 'GLC',
        ('gal', 'beta', 'd'): 'GAL',
        ('gal', 'alpha', 'd'): 'GLA',
        ('man', 'alpha', 'd'): 'MAN',
        ('man', 'beta', 'd'): 'BMA',
        
        # N-acetylated hexosamines
        ('glcnac', 'beta', 'd'): 'NAG',
        ('glcnac', 'alpha', 'd'): 'A2G',
        ('galnac', 'alpha', 'd'): 'NGA',
        ('galnac', 'beta', 'd'): 'A2G',
        
        # Deoxy sugars
        ('fuc', 'alpha', 'l'): 'FUC',
        ('fuc', 'beta', 'l'): 'BDF',
        ('rha', 'alpha', 'l'): 'RAM',
        ('rha', 'beta', 'l'): 'RAM',
        
        # Pentoses
        ('xyl', 'beta', 'd'): 'XYS',
        ('xyl', 'alpha', 'd'): 'XYP',
        ('ara', 'alpha', 'l'): 'ARA',
        ('ara', 'beta', 'l'): 'ARB',
        ('rib', 'beta', 'd'): 'RIB',
        
        # Uronic acids
        ('glca', 'beta', 'd'): 'GCU',
        ('glca', 'alpha', 'd'): 'GCU',
        ('gala', 'beta', 'd'): 'GAL',
        ('idoa', 'alpha', 'l'): 'IDR',
        ('idoa', 'beta', 'l'): 'IDR',
        
        # Sialic acids
        ('neu5ac', 'alpha', 'd'): 'SIA',
        ('neu5ac', 'beta', 'd'): 'SLB',
        ('neu5gc', 'alpha', 'd'): 'NGC',
        ('kdn', 'alpha', 'd'): 'KDN',
        
        # Rare/modified sugars
        ('glcna', 'beta', 'd'): 'GCS',
        ('glcns', 'alpha', 'd'): 'GNS',
        ('manp', 'alpha', 'd'): 'MAN',
        ('glf', 'beta', 'd'): 'GLF',
        
        # O-methylated sugars
        ('omeglc', 'alpha', 'd'): 'GLC',  # Fallback
    }

    # Anomeric carbon positions (key: CCD code, value: position)
    ANOMERIC_POSITIONS = {
        # Standard aldoses - C1
        'GLC': 'C1', 'GAL': 'C1', 'GLA': 'C1', 'MAN': 'C1', 'BMA': 'C1',
        'NAG': 'C1', 'A2G': 'C1', 'NGA': 'C1',
        'FUC': 'C1', 'BDF': 'C1', 'RAM': 'C1',
        'XYS': 'C1', 'XYP': 'C1', 'ARA': 'C1', 'ARB': 'C1', 'RIB': 'C1',
        'GCU': 'C1', 'IDR': 'C1', 'GCS': 'C1', 'GNS': 'C1', 'GLF': 'C1',
        # Ketoses (sialic acids) - C2
        'SIA': 'C2', 'SLB': 'C2', 'NGC': 'C2', 'KDN': 'C2',
    }

    # Ring oxygen positions
    RING_OXYGEN = {
        # Hexoses - O5
        'GLC': 'O5', 'GAL': 'O5', 'GLA': 'O5', 'MAN': 'O5', 'BMA': 'O5',
        'NAG': 'O5', 'A2G': 'O5', 'NGA': 'O5',
        'FUC': 'O5', 'BDF': 'O5', 'RAM': 'O5',
        '