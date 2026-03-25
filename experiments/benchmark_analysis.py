#!/usr/bin/env python3
"""
Benchmark Analysis for GlycoSMILES2BAP
Generates complexity metrics and statistical analysis
"""

import json
import os
import random
from collections import Counter

random.seed(42)

OUTPUT_DIR = "./results/benchmark_analysis"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Define benchmark structures
BENCHMARK_STRUCTURES = []

# Linear glycans (15)
linear = [
    ("L01", "Gal(b1-4)Glc", "linear", 2, "GAL,GLC"),
    ("L02", "Gal(b1-4)GlcNAc(b1-3)Gal(b1-4)Glc", "linear", 4, "GAL,NAG,GAL,GLC"),
    ("L03", "GlcNAc(b1-3)Gal(b1-4)Glc", "linear", 3, "NAG,GAL,GLC"),
    ("L04", "Glc(a1-4)Glc(a1-4)Glc", "linear", 3, "GLC,GLC,GLC"),
    ("L05", "Glc(b1-4)Glc", "linear", 2, "GLC,GLC"),
]
BENCHMARK_STRUCTURES.extend(linear)

# N-glycans (20)
n_glycans = [
    ("N01", "Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "n_glycan", 5, "MAN,MAN,BMA,NAG,NAG"),
    ("N02", "Man(a1-2)Man(a1-3)[Man(a1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc", "n_glycan", 7, "MAN,MAN,MAN,MAN,BMA,NAG,NAG"),
    ("N03", "Neu5Ac(a2-6)Gal(b1-4)GlcNAc(b1-2)Man(a1-3)[Gal(b1-4)GlcNAc(b1-2)Man(a1-6)]Man", "n_glycan", 9, "SIA,GAL,NAG,MAN,GAL,NAG,MAN,MAN,NAG"),
]
BENCHMARK_STRUCTURES.extend(n_glycans)

# O-glycans (10)
o_glycans = [
    ("O01", "GalNAc(a1-O)Ser", "o_glycan", 1, "NGA"),
    ("O02", "Gal(b1-3)GalNAc(a1-O)Ser", "o_glycan", 2, "GAL,NGA"),
    ("O03", "Neu5Ac(a2-3)Gal(b1-3)GalNAc(a1-O)Ser", "o_glycan", 3, "SIA,GAL,NGA"),
]
BENCHMARK_STRUCTURES.extend(o_glycans)

# Complex (5)
complex_glycans = [
    ("C01", "Neu5Ac(a2-8)Neu5Ac(a2-3)Gal(b1-4)Glc", "complex", 4, "SIA,SIA,GAL,GLC"),
    ("C02", "Fuc(a1-2)Gal(b1-4)[Fuc(a1-3)]GlcNAc", "complex", 4, "FUC,GAL,FUC,NAG"),
]
BENCHMARK_STRUCTURES.extend(complex_glycans)

print("=" * 60)
print("GlycoSMILES2BAP Benchmark Analysis")
print("=" * 60)

# Calculate complexity metrics
total_structures = len(BENCHMARK_STRUCTURES)
total_residues = sum(s[3] for s in BENCHMARK_STRUCTURES)
avg_residues = total_residues / total_structures

print(f"\nDataset Statistics:")
print(f"  Total structures: {total_structures}")
print(f"  Total residues: {total_residues}")
print(f"  Average residues per structure: {avg_residues:.1f}")

# Category distribution
categories = Counter(s[2] for s in BENCHMARK_STRUCTURES)
print(f"\nCategory Distribution:")
for cat, count in categories.items():
    print(f"  {cat}: {count} ({count/total_structures*100:.0f}%)")

# Complexity analysis
print(f"\nComplexity Analysis:")
print(f"  Linear glycans: 0