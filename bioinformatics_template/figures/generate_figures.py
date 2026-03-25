#!/usr/bin/env python3
"""
Figure Generation Script for GlycoSMILES2BAP Manuscript
Generates publication-quality figures in TIFF/EPS format for Bioinformatics journal
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

# Create output directory
os.makedirs('/bioinformatics_template/figures', exist_ok=True)

# Set publication-quality defaults
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
    'font.size': 10,
    'axes.titlesize': 12,
    'axes.labelsize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.1
})

def generate_pipeline_figure():
    """Generate Figure 1: Pipeline Architecture"""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Define box style
    box_style = dict(boxstyle='round,pad=0.3', facecolor='#E8F4FD', 
                     edgecolor='#2B6CB0', linewidth=2)
    
    # Input box
    ax.text(1, 7, 'Input\nGlycan Notation\n(IUPAC/WURCS)', 
            ha='center', va='center', fontsize=10,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#C6F6D5', 
                     edgecolor='#38A169', linewidth=2))
    
    # Module boxes
    modules = [
        ('Parser', 'AST\n(Abstract Syntax Tree)', 2, 4.5),
        ('CCD Mapper', 'CCD Codes', 5, 4.5),
        ('BAP Generator', 'bondedAtomPairs\n(JSON)', 8, 4.5),
    ]
    
    for name, output, x, y in modules:
        ax.text(x, y+0.8, name, ha='center', va='center', fontsize=11,
               fontweight='bold', bbox=box_style)
        ax.text(x, y-0.8, output, ha='center', va='center', fontsize=9,
               style='italic')
    
    # Output box
    ax.text(5, 1.5, 'Output\nAF3-compatible JSON', 
            ha='center', va='center', fontsize=10,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FED7D7', 
                     edgecolor='#E53E3E', linewidth=2))
    
    # Arrows
    arrow_style = dict(arrowstyle='->', lw=2, color='#4A5568')
    ax.annotate('', xy=(2, 5.5), xytext=(1.5, 6.3), arrowprops=arrow_style)
    ax.annotate('', xy=(3.5, 4.5), xytext=(2.8, 4.5), arrowprops=arrow_style)
    ax.annotate('', xy=(6.5, 4.5), xytext=(5.5, 4.5), arrowprops=arrow_style)
    ax.annotate('', xy=(5, 2.3), xytext=(8, 3.5), arrowprops=arrow_style)
    
    # Title
    ax.text(5, 7.5, 'Figure 1: GlycoSMILES2BAP Pipeline Architecture', 
            ha='center', va='center', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('/bioinformatics_template/figures/figure1_pipeline.tiff', 
                format='tiff', dpi=300)
    plt.savefig('/bioinformatics_template/figures/figure1_pipeline.eps', 
                format='eps')
    plt.close()
    print("Generated Figure 1: Pipeline Architecture")

def generate_accuracy_figure():
    """Generate Figure 2: Accuracy Comparison Bar Chart"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Data
    methods = ['GlycoSMILES2BAP', 'SMILES', 'userCCD', 'Manual BAP']
    metrics = ['Epimer\nAccuracy', 'Anomeric\nAccuracy', '