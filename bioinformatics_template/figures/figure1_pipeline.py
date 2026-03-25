#!/usr/bin/env python3
"""
Figure 1: Pipeline Architecture Diagram
Generates publication-quality pipeline flowchart for Bioinformatics journal
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Set up publication-quality settings
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica'],
    'font.size': 10,
    'axes.linewidth': 1.0,
    'figure.dpi': 300
})

def create_pipeline_diagram():
    """Create pipeline architecture flowchart"""
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Color scheme
    colors = {
        'input': '#E8F4FD',      # Light blue
        'process': '#FFF3E0',     # Light orange
        'output': '#E8F5E9',      # Light green
        'arrow': '#424242',       # Dark gray
        'text': '#212121',        # Near black
        'border': '#1565C0'       # Blue
    }
    
    # Title
    ax.text(5, 9.5, 'GlycoSMILES2BAP Pipeline Architecture', 
            ha='center', va='center', fontsize=14, fontweight='bold')
    
    # Input box
    input_box = FancyBboxPatch((0.5, 7), 3, 1.5, 
                                boxstyle="round,pad=0.1,rounding_size=0.2",
                                facecolor=colors['input'], 
                                edgecolor=colors['border'],
                                linewidth=2)
    ax.add_patch(input_box)
    ax.text(2, 7.75, 'INPUT', ha='center', va='center', 
            fontsize=11, fontweight='bold', color=colors['text'])
    ax.text(2, 7.35, 'IUPAC / WURCS', ha='center', va='center',
            fontsize=9, color=colors['text'])
    
    # Parser module
    parser_box = FancyBboxPatch((3.5, 5.5), 3, 1.5,
                                 boxstyle="round,pad=0.1,rounding_size=0.2",
                                 facecolor=colors['process'],
                                 edgecolor='#E65100',
                                 linewidth=2)
    ax.add_patch(parser_box)
    ax.text(5, 6.25, 'PARSER', ha='center', va='center',
            fontsize=11, fontweight='bold', color=colors['text'])
    ax.text(5, 5.85, 'GlyLES Integration', ha='center', va='center',
            fontsize=9, color=colors['text'])
    
    # CCD Mapper module
    ccd_box = FancyBboxPatch((3.5, 3.5), 3, 1.5,
                              boxstyle="round,pad=0.1,rounding_size=0.2",
                              facecolor=colors['process'],
                              edgecolor='#E65100',
                              linewidth=2)
    ax.add_patch(ccd_box)
    ax.text(5, 4.25, 'CCD MAPPER', ha='center', va='center',
            fontsize=11, fontweight='bold', color=colors['text'])
    ax.text(5, 3.85, '28+ Monosaccharides', ha='center', va='center',
            fontsize=9, color=colors['text'])
    
    # BAP Generator module
    bap_box = FancyBboxPatch((3.5, 1.5), 3, 1.5,
                              boxstyle="round,pad=0.1,rounding_size=0.2",
                              facecolor=colors['process'],
                              edgecolor='#E65100',
                              linewidth=2)
    ax.add_patch(bap_box)
    ax.text(5, 2.25, 'BAP GENERATOR', ha='center', va='center',
            fontsize=11, fontweight='bold', color=colors['text'])
    ax.text(5, 1.85, 'Topology → Bonds', ha='center', va='center',
            fontsize=9, color=colors['text'])
    
    # Output box
    output_box = FancyBboxPatch((6.5, 3.