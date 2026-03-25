#!/usr/bin/env python3
"""
Figure 3: Processing Time Comparison
Generates publication-quality bar chart comparing processing times
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.use('Agg')

# Set publication-quality defaults
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight'
})

def create_processing_time_figure():
    """Create processing time comparison figure."""
    
    fig, ax = plt.subplots(figsize=(7, 5))
    
    # Data
    methods = ['GlycoSMILES2BAP\n(automated)', 'Manual BAP\nspecification']
    times = [0.82, 45]  # 0.82 seconds vs 45 minutes average
    colors = ['#2ecc71', '#e74c3c']
    
    # Create bars (log scale for visualization)
    times_log = np.log10([0.82, 45*60])  # Convert to seconds for log scale
    
    bars = ax.bar(methods, [0.82, 2700], color=colors, edgecolor='black', linewidth=1.5)
    
    # Add value labels
    for bar, time_val in zip(bars, ['0.82 s', '~45 min']):
        height = bar.get_height()
        ax.annotate(time_val,
                    xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 5),
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=14, fontweight='bold')
    
    # Add speedup annotation
    ax.annotate('', xy=(0, 2000), xytext=(1, 2000),
                arrowprops=dict(arrowstyle='<->', color='#3498db', lw=2))
    ax.text(0.5, 2300, '3,300× faster', ha='center', fontsize=12, 
            fontweight='bold', color='#3498db')
    
    # Log scale
    ax.set_yscale('log')
    ax.set_ylim(0.1, 10000)
    
    # Labels
    ax.set_ylabel('Processing Time (seconds)', fontsize=12)
    ax.set_title('Processing Time per Glycan Structure', fontsize=13, fontweight='bold')
    
    # Grid
    ax.yaxis.grid(True, linestyle='--', alpha=0.7)
    ax.set_axisbelow(True)
    
    # Add horizontal line at 1 second threshold
    ax.axhline(y=1, color='#f39c12', linestyle='--', linewidth=1.5, label='1 second threshold')
    ax.legend(loc='upper right')
    
    plt.tight_layout()
    
    # Save in multiple formats
    plt.savefig('figure3_time_comparison.png', dpi=300, bbox_inches='tight')
    plt.savefig('figure3_time_comparison.pdf', dpi=300, bbox_inches='tight')
    plt.savefig('figure3_time_comparison.eps', dpi=300, bbox_inches='tight')
    plt.savefig('figure3_time_comparison.tiff', dpi=300, bbox_inches='tight')
    
    print("Figure 3 saved: figure3_time_comparison.{png,pdf,eps,tiff}")
    
    plt.close()

if __name__ == '__main__':
    create_processing_time_figure()
