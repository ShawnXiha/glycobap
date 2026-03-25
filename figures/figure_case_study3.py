#!/usr/bin/env python3
"""
Case Study 3: Error Correction Visualization
Generates figures for literature error correction validation
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Set up the figure style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14

# =============================================================================
# Figure 1: Error Correction Success Rate by Error Type
# =============================================================================

fig1, ax1 = plt.subplots(figsize=(10, 6))

error_types = ['Anomeric\n(n=4)', 'Epimer\n(n=2)', 'Linkage\n(n=3)', 'Conformation\n(n=1)', 'Overall\n(n=10)']
corrected = [4, 2, 3, 1, 10]
total = [4, 2, 3, 1, 10]
colors = ['#2ecc71', '#3498db', '#e74c3c', '#9b59b6', '#f39c12']

bars = ax1.bar(error_types, corrected, color=colors, edgecolor='black', linewidth=1.5)

# Add percentage labels
for i, (bar, corr, tot) in enumerate(zip(bars, corrected, total)):
    percentage = (corr / tot) * 100
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
             f'{percentage:.0f}%', ha='center', va='bottom', fontweight='bold', fontsize=12)

ax1.set_ylabel('Number of Cases Corrected', fontweight='bold')
ax1.set_xlabel('Error Type', fontweight='bold')
ax1.set_title('Case Study 3: GlycoSMILES2BAP Error Correction Validation', fontweight='bold', fontsize=14)
ax1.set_ylim(0, 12)
ax1.axhline(y=10, color='red', linestyle='--', alpha=0.5, label='Total cases')

# Add legend
legend_patches = [
    mpatches.Patch(color='#2ecc71', label='Anomeric errors (α/β)'),
    mpatches.Patch(color='#3498db', label='Epimer errors (D/L)'),
    mpatches.Patch(color='#e74c3c', label='Linkage errors'),
    mpatches.Patch(color='#9b59b6', label='Conformation errors'),
    mpatches.Patch(color='#f39c12', label='Overall success')
]
ax1.legend(handles=legend_patches, loc='upper right', frameon=True)

plt.tight_layout()
plt.savefig('/home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides/figures/figure_cs3_correction_rates.png', dpi=300, bbox_inches='tight')
plt.savefig('/home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides/figures/figure_cs3_correction_rates.pdf', bbox_inches='tight')
print("Figure 1 saved: figure_cs3_correction_rates.png/pdf")

# =============================================================================
# Figure 2: Module Contribution to Error Correction
# =============================================================================

fig2, ax2 = plt.subplots(figsize=(10, 6))

modules = ['Full Pipeline', 'w/o CCD\nMapper', 'w/o Anomeric\nTracker', 'w/o Ring\nHandler']
anomeric_correct = [4, 0, 0, 4]
epimer_correct = [2, 0, 2, 2]
linkage_correct = [3, 0, 3, 3]

x = np.arange(len(modules))
width = 0.25

bars1 = ax2.bar(x - width, anomeric_correct, width, label='Anomeric', color='#2ecc71', edgecolor='black')
bars2 = ax2.bar(x, epimer_correct, width, label='Epimer', color='#3498db', edgecolor='black')
bars3 = ax2.bar(x + width, linkage_correct, width, label='Linkage', color='#e74c3c', edgecolor='black')

ax2.set_ylabel('Cases Corrected', fontweight='bold')
ax2.set_xlabel('Pipeline Configuration', fontweight='bold')
ax2.set_title('Module Contribution to Error Correction', fontweight='bold', fontsize=14)
ax2.set_xticks(x)
ax2.set_xticklabels(modules)
ax2.legend(loc='upper right',