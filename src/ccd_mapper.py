"""CCD Mapper Module""" 

from typing import Optional

class CCDMapper:
    CCD_TABLE = {
        ("glcnac", "beta", "d"): "NAG",
        ("glcnac", "alpha", "d"): "A2G",
        ("man", "alpha", "d"): "MAN",
        ("man", "beta", "d"): "BMA",
        ("gal", "beta", "d"): "GAL",
        ("gal", "alpha", "d"): "GLA",
        ("glc", "beta", "d"): "GLC",
        ("glc", "alpha", "d"): "GLC",
        ("galnac", "alpha", "d"): "NGA",
        ("galnac", "beta", "d"): "NGA",
        ("fuc", "alpha", "l"): "FUC",
        ("fuc", "beta", "l"): "BDF",
        ("rha", "alpha", "l"): "RAM",
        ("xyl", "beta", "d"): "XYS",
        ("xyl", "alpha", "d"): "XYP",
        ("ara", "alpha", "l"): "ARA",
        ("rib", "beta", "d"): "RIB",
        ("glca", "beta", "d"): "GCU",
        ("idoa", "alpha", "l"): "IDR",
        ("gala", "alpha", "d"): "GTR",
        ("neu5ac", "alpha", "d"): "SIA",
        ("neu5ac", "beta", "d"): "SLB",
        ("neu5gc", "alpha", "d"): "NGC",
        ("kdn", "alpha", "d"): "KDN",
        ("glcna", "beta", "d"): "GCS",
        ("galna", "beta", "d"): "GSQ",
        ("man6p", "alpha", "d"): "M6P",
        ("glc6p", "beta", "d"): "G6P",
    }
    ANOMERIC = {"NAG":"C1","A2G":"C1","MAN":"C1","BMA":"C1","GAL":"C1","GLA":"C1","GLC":"C1","FUC":"C1","XYS":"C1","XYP":"C1","NGA":"C1","RAM":"C1","ARA":"C1","RIB":"C1","GCU":"C1","IDR":"C1","GTR":"C1","BDF":"C1","GCS":"C1","GSQ":"C1","M6P":"C1","G6P":"C1","SIA":"C2","SLB":"C2","NGC":"C2","KDN":"C2"}
    RING_O = {"NAG":"O5","A2G":"O5","MAN":"O5","BMA":"O5","GAL":"O5","GLA":"O5","GLC":"O5","FUC":"O5","XYS":"O4","XYP":"O4","NGA":"O5","RAM":"O5","ARA":"O4","RIB":"O4","GCU":"O5","IDR":"O5","SIA":"O6","SLB":"O6","NGC":"O6","KDN":"O6"}
    def __init__(self): self.custom = {}
    def map(self, mono, anomer, config="D"):
        return self.CCD_TABLE.get((mono.lower().strip(), anomer.lower(), config.lower()))
    def anomeric(self, ccd): return self.ANOMERIC.get(ccd, "C1")
    def ring_oxygen(self, ccd): return self.RING_O.get(ccd, "O5")
