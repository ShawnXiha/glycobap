#!/usr/bin/env python3
"""
GlycoSMILES2BAP: Automated Pipeline for AlphaFold 3 Glycan Structure Prediction

This tool converts standard glycan notations (IUPAC-condensed, WURCS) to 
AF3-compatible CCD+BAP format for stereochemistry-preserving structure prediction.

Author: Qiang Xia
Email: xiaqiang@xinghetea.com
License: MIT
"""

import json
import re
import sys
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class AnomericPosition(Enum):
    """Anomeric carbon positions for different sugar types."""
    ALDOSE = "C1"  # Most sugars (Glc, Gal, Man, etc.)
    KETOSE = "C2"  # Sialic acids (Neu5Ac, Neu5Gc)


class RingOxygen(Enum):
    """Ring oxygen positions based on ring size."""
    PENTOSE = "O4"   # Xylose, Arabinose
    HEXOSE = "O5"    # Glc, Gal, Man, GlcNAc, etc.
    SIALIC = "O6"    # Neu5Ac, Neu5Gc


@dataclass
class Monosaccharide:
    """Represents a single monosaccharide residue."""
    name: str
    anomer: str  # 'a' for alpha, 'b' for beta
    config: str  # 'D' or 'L'
    ccd_code: str
    anomeric_c: str
    ring_oxygen: str


@dataclass
class GlycosidicLinkage:
    """Represents a glycosidic linkage between two residues."""
    donor_idx: int
    donor_atom: str
    acceptor_idx: int
    acceptor_atom: str
    linkage_type: str  # e.g., "1-4", "1-3", "2-6"


# CCD Mapping Table: (name, anomer, config) -> CCD code
CCD_MAPPING = {
    # GlcNAc
    ("glcnac", "b", "d"): ("NAG", AnomericPosition.ALDOSE, RingOxygen.HEXOSE),
    ("glcnac", "a", "d"): ("A2G", AnomericPosition.ALDOSE, RingOxygen.HEXOSE),
    ("nag", "b", "d"): ("NAG", AnomericPosition.ALDOSE, RingOxygen.HEXOSE),
    # Mannose
    ("man", "a", "d"): ("MAN", AnomericPosition.ALDOSE, RingOxygen.HEXOSE),
    ("man", "b", "d"): ("BMA", AnomericPosition.ALDOSE, RingOxygen.HEXOSE),
    # Galactose
    ("gal", "b", "d"): ("GAL", AnomericPosition.ALDOSE, RingOxygen.HEXOSE),
    ("gal", "a", "d"): ("GLA", AnomericPosition.ALDOSE, RingOxygen.HEXOSE),
    # Glucose
    ("glc", "b", "d"): ("GLC", AnomericPosition.ALDOSE, RingOxygen.HEXOSE),
    ("glc", "a", "d"): ("GLA", AnomericPosition.ALDOSE, RingOxygen.HEXOSE),
    # Fucose
    ("fuc", "a", "l"): ("FUC", AnomericPosition.ALDOSE, RingOxygen.HEXOSE),
    ("fuc", "b", "l"): ("BDF", AnomericPosition.ALDOSE, RingOxygen.HEXOSE),
    # Sialic acids (C2 anomeric!)
    ("neu5ac", "a", "d"): ("SIA", AnomericPosition.KETOSE, RingOxygen.SIALIC),
    ("neu5gc", "a", "d"): ("NGC", AnomericPosition.KETOSE, RingOxygen.SIALIC),
    ("sia", "a", "d"): ("SIA", AnomericPosition.KETOSE, RingOxygen.SIALIC),
    # Xylose
    ("xyl", "b", "d"): ("XYS", AnomericPosition.ALDOSE, RingOxygen.PENTOSE),
    ("xyl", "a", "d"): ("XYP", AnomericPosition.AL