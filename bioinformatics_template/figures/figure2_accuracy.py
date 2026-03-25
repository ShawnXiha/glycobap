#!/usr/bin/env python3
"""
Figure 2: Stereochemistry Accuracy Comparison
Generates a bar chart comparing accuracy across different input formats
"""

import matplotlib.pyplot as plt
import numpy as np

# Set publication-quality defaults
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']
plt.rcParams['font.size'] = 10
plt.rcParams['axes.linewidth'] = 1.0
plt.rcParams['figure.dpi'] = 300

# Data
methods = ['GlycoSMILES2BAP', 'Manual BAP', 'userCCD', 'SMILES']
epimer_accuracy = [98.5, 100, 78, 62]
anomeric_accuracy = [98.2, 100, 85, 71]
linkage_accuracy = [96.8, 100, 82, 74]

x = np.arange(len(methods))
width = 0.25

# Create figure
fig, ax = plt.subplots(figsize=(8, 5), layout='constrained')

# Plot bars
bars1 = ax.bar(x - width, epimer_accuracy, width, label='Epimer', color='#2563eb', alpha=0.9)
bars2 = ax.bar(x, anomeric_accuracy, width, label='Anomeric', color='#16a34a', alpha=0.9)
bars3 = ax.bar(x + width, linkage_accuracy, width, label='Linkage', color='#dc2626', alpha=0.9)

# Add value labels on bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}%',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=8)

add_labels(bars1)
add_labels(bars2)
add_labels(bars3)

# Customize plot
ax.set_ylabel('Accuracy (%)', fontsize=11)
ax.set_xlabel('Input Format', fontsize=11)
ax.set_title('Stereochemistry Preservation by Input Format', fontsize=12, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(methods, fontsize=10)
ax.set_ylim(0, 110)
ax.legend(loc='upper right', frameon=True, fontsize=9)
ax.yaxis.grid(True, linestyle='--', alpha=0.3)
ax.set_axisbelow(True)

# Add horizontal line at 95% threshold
ax.axhline(y=95, color='gray', linestyle='--', linewidth=1, alpha=0.7, label='_nolegend_')
ax.text(3.5, 96, 'Target: 95%', fontsize=8, color='gray', ha='right')

# Save figures
plt.savefig('/bioinformatics_template/figures/figure2_accuracy.tiff', 
            format='tiff', dpi=300, bbox_inches='tight')
plt.savefig('/bioinformatics_template/figures/figure2_accuracy.eps', 
            format='eps', bbox_inches='tight')
plt.savefig('/bioinformatics_template/figures/figure2_accuracy.png', 
            format='png', dpi=300, bbox_inches='tight')

print("Figure 2 saved: figure2_accuracy.tiff, .eps, .png")

# Generate confidence interval version
fig2, ax2 = plt.subplots(figsize=(8, 5), layout='constrained')

# Error bars for GlycoSMILES2BAP (95% CI)
ci_epimer = (96.2, 99.8)
ci_anomeric = (95.8, 99.6)
ci_linkage = (93.5, 99.2)

# Calculate error bar heights
epimer_err = [[98.5 - 96.2], [99.8 - 98.5]]
anomeric_err = [[98.2 - 95.8], [99.6 - 98.2]]
linkage_err = [[96.8 - 93.5], [99.2 - 96.8]]

# Plot with error bars (only for GlycoSMILES2BAP)
x_main = np.arange(3)
accuracies = [98.5, 98.2, 96.8]
errors = [epimer_err, anomeric_err, linkage_err]
colors = ['#2563eb', '#16a34a', '#dc2626']
labels = ['Epimer', 'Anomeric', 'Linkage']

for i, (acc, err, color, label) in enumerate(zip(accur