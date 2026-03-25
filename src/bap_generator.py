"""
BAP Generator Module
Generates bondedAtomPairs (BAP) syntax for AlphaFold 3 glycan input
"""

from typing import List, Dict, Tuple, Optional
import json

class BAPGenerator:
    """
    Generates bondedAtomPairs (BAP) syntax for AF3 glycan input.
    
    The BAP syntax explicitly specifies atom-to-atom bonds, preserving
    stereochemistry that is lost in SMILES-based approaches.
    """
    
    # Standard glycosidic linkage positions
    LINKAGE_TYPES = {
        (1, 4): "1,4-linkage",
        (1, 3): "1,3-linkage",
        (1, 6): "1,6-linkage",
        (1, 2): "1,2-linkage",
        (2, 3): "2,3-linkage (sialic acid)",
        (2, 6): "2,6-linkage (sialic acid)",
        (2, 8): "2,8-linkage (sialic acid)",
    }
    
    def __init__(self):
        self.verbose = False
    
    def generate_bap(self,
                     donor_residue_id: int,
                     acceptor_residue_id: int,
                     donor_ccd: str,
                     acceptor_ccd: str,
                     linkage_position: Tuple[int, int],
                     donor_anomeric_carbon: str = "C1",
                     acceptor_oxygen: str = None) -> Dict:
        """
        Generate a single bondedAtomPair entry.
        
        Args:
            donor_residue_id: Index of donor residue (1-based)
            acceptor_residue_id: Index of acceptor residue (1-based)
            donor_ccd: CCD code of donor monosaccharide
            acceptor_ccd: CCD code of acceptor monosaccharide
            linkage_position: (acceptor_pos, donor_pos) tuple
            donor_anomeric_carbon: Anomeric carbon atom name
            acceptor_oxygen: Oxygen atom name for linkage
            
        Returns:
            Dictionary with BAP specification
        """
        if acceptor_oxygen is None:
            acceptor_pos = linkage_position[0]
            acceptor_oxygen = f"O{acceptor_pos}"
        
        # Handle sialic acid special case
        if donor_ccd == "SIA":
            donor_anomeric_carbon = "C2"
        
        return {
            "residue1": donor_residue_id,
            "atom1": donor_anomeric_carbon,
            "residue2": acceptor_residue_id,
            "atom2": acceptor_oxygen,
            "order": 1
        }
    
    def generate_from_topology(self,
                               topology: List[Dict],
                               ccd_codes: List[str]) -> List[Dict]:
        """Generate all bondedAtomPairs from glycan topology."""
        bap_list = []
        
        for link in topology:
            donor_idx = link["donor_idx"]
            acceptor_idx = link["acceptor_idx"]
            linkage = link["linkage"]
            
            bap = self.generate_bap(
                donor_residue_id=donor_idx + 1,
                acceptor_residue_id=acceptor_idx + 1,
                donor_ccd=ccd_codes[donor_idx],
                acceptor_ccd=ccd_codes[acceptor_idx],
                linkage_position=linkage
            )
            bap_list.append(bap)
        
        return bap_list
    
    def generate_af3_json(self,
                          ccd_codes: List[str],
                          bonded_atom_pairs: List[Dict],
                          protein_sequence: str = None) -> Dict:
        """Generate complete AF3-compatible JSON input."""
        af3_input = {
            "name": "glycan_structure",
            "modelSeeds": [1],
            "sequences": []
        }
        
        if protein_sequence:
            af3_input["sequences"].append({
                "proteinChain": {
                    "sequence": protein_sequence,
                    "count": len(protein_sequence)
                }
            })
        
        # Add glycan ligand
        glycan_entry = {
            "ligand": {
                "ccdCodes": ccd_codes,
                "bondedAtomPairs": bonded_atom_pairs
            }
        }
        af3_input["sequences"].append(glycan_entry)
        
        return af3_input
