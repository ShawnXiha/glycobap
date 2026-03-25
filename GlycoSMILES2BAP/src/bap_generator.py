#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BAP Generator Module
Converts glycan topology into AF3-compatible bond specifications.

Author: Qiang Xia
Email: xiaqiang@xinghetea.com
"""

import json
from typing import List, Dict, Tuple, Optional


class BAPGenerator:
    """
    Generates bondedAtomPairs (BAP) specifications for AF3.
    
    The BAP format requires explicit atom-to-atom bond specifications,
    which is the key to stereochemistry preservation in AF3.
    """
    
    def __init__(self):
        """Initialize BAP generator."""
        self.bonds = []
    
    def generate_bap(self, 
                     glycan_ast: Dict,
                     ccd_codes: List[str]) -> List[Dict]:
        """
        Generate BAP entries from glycan AST and CCD codes.
        
        Parameters
        ----------
        glycan_ast : Dict
            Abstract Syntax Tree from the parser
        ccd_codes : List[str]
            List of CCD codes from the mapper
        
        Returns
        -------
        List[Dict]
            List of bondedAtomPair dictionaries
        """
        self.bonds = []
        
        if 'linkages' not in glycan_ast:
            return self.bonds
        
        for linkage in glycan_ast['linkages']:
            donor_idx = linkage['donor_index']
            acceptor_idx = linkage['acceptor_index']
            donor_atom = self._get_donor_atom(linkage['donor_monosaccharide'])
            acceptor_atom = f"O{linkage['linkage_position']}"
            
            bap_entry = {
                "residue1": donor_idx + 1,  # AF3 uses 1-based indexing
                "atom1": donor_atom,
                "residue2": acceptor_idx + 1,
                "atom2": acceptor_atom,
                "order": 1
            }
            self.bonds.append(bap_entry)
        
        return self.bonds
    
    def _get_donor_atom(self, monosaccharide: str) -> str:
        """
        Get the donor anomeric carbon atom.
        
        - Aldoses: C1
        - Ketoses (sialic acids): C2
        
        Parameters
        ----------
        monosaccharide : str
            Monosaccharide name
        
        Returns
        -------
        str
            Anomeric carbon atom identifier
        """
        # Sialic acids use C2 as anomeric carbon
        sialic_acids = ['Neu5Ac', 'Neu5Gc', 'KDN', 'Neu5Ac9Ac', 'Neu5Gc9Ac']
        
        if monosaccharide in sialic_acids or monosaccharide.lower() in [s.lower() for s in sialic_acids]:
            return "C2"
        else:
            return "C1"
    
    def generate_af3_json(self,
                          ccd_codes: List[str],
                          protein_sequence: str = "",
                          protein_name: str = "glycoprotein") -> Dict:
        """
        Generate complete AF3 JSON input.
        
        Parameters
        ----------
        ccd_codes : List[str]
            List of CCD codes for glycan residues
        protein_sequence : str, optional
            Protein sequence (if modeling glycoprotein)
        protein_name : str, optional
            Name of the protein
        
        Returns
        -------
        Dict
            AF3-compatible JSON structure
        """
        af3_input = {
            "name": protein_name,
            "modelSeeds": [1],
            "sequences": {}
        }
        
        # Add protein sequence if provided
        if protein_sequence:
            af3_input["sequences"]["protein"] = [{
                "id": "A",
                "sequence": protein_sequence
            }]
        
        # Add ligand (glycan)
        ligand_entry = {
            "id": "B",
            "ccd_codes": ccd_codes
        }
        
        # Add BAP if bonds exist
        if self.bonds:
            ligand_entry["bondedAtomPairs"] = self.bonds
        
        af3_input["sequences"]["ligand"] = [ligand_entry]
        
        return af3_input
    
    def to_json_file(self, 
                     output_path: str,
                     ccd_codes: List[str],
                     protein_sequence: str = "",
                     protein_name: str = "glycoprotein") -> None:
        """
        Save AF3 input to JSON file.
        
        Parameters
        ----------
        output_path : str
            Path to output JSON file
       