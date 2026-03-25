"""
Validator Module
Integrates stereochemistry validation for AF3 glycan predictions
"""

from typing import Dict, List, Optional, Tuple
import json

class StereochemistryValidator:
    """
    Validates glycan stereochemistry using Privateer-like checks.
    
    Detects common stereochemistry errors in AF3 glycan predictions:
    - Epimer confusion (e.g., galactose vs glucose)
    - Anomeric inversion (alpha vs beta)
    - Linkage position errors
    """
    
    # Expected stereochemistry for common monosaccharides
    STEREOCHEMISTRY_RULES = {
        # Glucose family (C4 hydroxyl equatorial)
        'GLC': {'C4': 'equatorial', 'anomer': 'beta'},
        'GLA': {'C4': 'axial', 'anomer': 'alpha'},  # Galactose
        
        # Mannose (C2 hydroxyl axial)
        'MAN': {'C2': 'axial', 'anomer': 'alpha'},
        'BMA': {'C2': 'axial', 'anomer': 'beta'},
        
        # GlcNAc
        'NAG': {'C4': 'equatorial', 'anomer': 'beta'},
        'A2G': {'C4': 'equatorial', 'anomer': 'alpha'},
        
        # Fucose (L-sugar)
        'FUC': {'C4': 'axial', 'anomer': 'alpha'},
        
        # Sialic acid
        'SIA': {'anomer': 'alpha'},  # C2 is anomeric
    }
    
    # Common error patterns to detect
    ERROR_PATTERNS = {
        'epimer_confusion': [
            ('GAL', 'GLC', 'C4'),  # Galactose vs Glucose at C4
            ('MAN', 'GLC', 'C2'),  # Mannose vs Glucose at C2
        ],
        'anomeric_inversion': [
            ('alpha', 'beta'),  # Common inversion
        ],
    }
    
    def __init__(self):
        self.errors_detected = []
        self.warnings = []
    
    def validate_epimer(self, 
                        ccd_code: str, 
                        observed_positions: Dict) -> Tuple[bool, Optional[str]]:
        """
        Validate epimer configuration.
        
        Args:
            ccd_code: Expected CCD code
            observed_positions: Dict of observed hydroxyl positions
            
        Returns:
            (is_valid, error_message)
        """
        if ccd_code not in self.STEREOCHEMISTRY_RULES:
            return True, None  # Skip unknown residues
        
        expected = self.STEREOCHEMISTRY_RULES[ccd_code]
        
        for carbon, expected_pos in expected.items():
            if carbon.startswith('C') and carbon in observed_positions:
                observed = observed_positions[carbon]
                if observed != expected_pos:
                    error = f"Epimer error in {ccd_code}: {carbon} expected {expected_pos}, got {observed}"
                    self.errors_detected.append(error)
                    return False, error
        
        return True, None
    
    def validate_anomer(self,
                        ccd_code: str,
                        observed_anomer: str) -> Tuple[bool, Optional[str]]:
        """
        Validate anomeric configuration.
        
        Args:
            ccd_code: Expected CCD code
            observed_anomer: Observed anomeric configuration
            
        Returns:
            (is_valid, error_message)
        """
        if ccd_code not in self.STEREOCHEMISTRY_RULES:
            return True, None
        
        expected_anomer = self.STEREOCHEMISTRY_RULES[ccd_code].get('anomer')
        if expected_anomer and observed_anomer != expected_anomer:
            error = f"Anomeric error in {ccd_code}: expected {expected_anomer}, got {observed_anomer}"
            self.errors_detected.append(error)
            return False, error
        
        return True, None
    
    def validate_linkage(self,
                         donor_ccd: str,
                         acceptor_ccd: str,
                         donor_position: int,
                         acceptor_position: int) -> Tuple[bool, Optional[str]]:
        """
        Validate glycosidic linkage.
        
        Args:
            donor_ccd: CCD code of donor
            acceptor_ccd: CCD code of acceptor
            donor_position: Linkage position on donor
            acceptor_position: Linkage position on acceptor
            
        Returns:
            (is_valid, error_message)
        """
        # Check for sialic acid (anomeric position is C2)
        if donor_ccd == 'SIA' and donor_position != 2:
            warning = f"Sialic acid linkage