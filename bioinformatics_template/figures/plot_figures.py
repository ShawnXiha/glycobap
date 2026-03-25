#!/usr/bin/env python3
"""
Figure Generation Script for GlycoSMILES2BAP Manuscript
Bioinformatics Journal Format - Publication Quality Figures
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

# Create output directory
os.makedirs('/bioinformatics_template/figures/output', exist_ok=True)

# Set publication quality settings
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica'],
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.linewidth': 0.8,
    'xtick.major.width': 0.8,
    'ytick.major.width': 0.8,
})

def generate_accuracy_figure():
    """Generate Figure 2: Accuracy Comparison Bar Chart"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Data
    methods = ['GlycoSMILES2BAP', 'SMILES', 'userCCD', 'Manual BAP']
    epimer = [98.5, 62, 78, 99.5]
    anomeric = [98.2, 71, 85, 99.5]
    linkage = [96.8, 74, 82, 99.5]
    
    x = np.arange(len(methods))
    width = 0.25
    
    # Create bars
    bars1 = ax.bar(x - width, epimer, width, label='Epimer Accuracy', 
                   color='#2E86AB', edgecolor='black', linewidth=0.5)
    bars2 = ax.bar(x, anomeric, width, label='Anomeric Accuracy', 
                   color='#A23B72', edgecolor='black', linewidth=0.5)
    bars3 = ax.bar(x + width, linkage, width, label='Linkage Accuracy', 
                   color='#F18F01', edgecolor='black', linewidth=0.5)
    
    # Add error bars for GlycoSMILES2BAP (95% CI)
    ci_epimer = [1.8]
    ci_anomeric = [1.9]
    ci_linkage = [2.8]
    ax.errorbar(x[0] - width, epimer[0], yerr=ci_epimer, fmt='none', 
                color='black', capsize=3, capthick=1)
    ax.errorbar(x[0], anomeric[0], yerr=ci_anomeric, fmt='none', 
                color='black', capsize=3, capthick=1)
    ax.errorbar(x[0] + width, linkage[0], yerr=ci_linkage, fmt='none', 
                color='black', capsize=3, capthick=1)
    
    # Customize
    ax.set_ylabel('Accuracy (%)', fontweight='bold')
    ax.set_xlabel('Input Format', fontweight='bold')
    ax.set_title('Stereochemistry Accuracy by Input Format', fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(methods)
    ax.set_ylim(0, 110)
    ax.legend(loc='upper left', frameon=True, fancybox=False, edgecolor='black')
    ax.yaxis.grid(True, linestyle='--', alpha=0.3)
    ax.set_axisbelow(True)
    
    # Add significance markers
    ax.annotate('***', xy=(x[0] - width, 100), ha='center', fontsize=10)
    ax.annotate('***', xy=(x[0], 100), ha='center', fontsize=10)
    ax.annotate('***', xy=(x[0] + width, 100), ha='center', fontsize=10)
    
    plt.tight_layout()
    
    # Save in multiple formats
    plt.savefig('/bioinformatics_template/figures/output/figure2_accuracy.tif', 
                format='tiff', compression='lzw')
    plt.savefig('/bioinformatics_template/figures/output/figure2_accuracy.eps', 
                format='eps')
    plt.savefig('/bioinformatics_template/figures/output/figure2_accuracy.png', 
                format='png')
    plt.close()
    print("Figure 2 (Accuracy) generated successfully")


def generate_timing_figure():
    """Generate Figure 3: Processing Time Comparison"""
   