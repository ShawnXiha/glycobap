#!/usr/bin/env python3
"""
Generate visualization charts for expanded benchmark results
"""

import json

# Load results
with open('/results/expanded_benchmark_results.json', 'r') as f:
    data = json.load(f)

# Generate ASCII charts for terminal output
print("=" * 60)
print("EXPANDED BENCHMARK VISUALIZATION")
print("=" * 60)

# Chart 1: Accuracy Comparison
print("\n### Accuracy by Structure Category ###\n")
categories = data['results_by_category']
max_val = 100
for cat, stats in categories.items():
    success = stats['success_rate']
    bar_len = int(success / 2)
    print(f"{cat:20} | {'#' * bar_len} {success:.1f}%")

# Chart 2: Error Distribution
print("\n### Error Distribution ###\n")
errors = data['error_breakdown']
total_errors = sum(errors.values())
for error_type, count in errors.items():
    pct = count / total_errors * 100
    bar_len = int(pct / 2)
    print(f"{error_type:25} | {'#' * bar_len} {count} ({pct:.1f}%)")

# Chart 3: Complexity vs Accuracy
print("\n### Accuracy vs Structure Complexity ###\n")
complexity = data['complexity_analysis']
for level, stats in complexity.items():
    epimer = stats['epimer']
    anomeric = stats['anomeric']
    linkage = stats['linkage']
    print(f"{level:25} | E:{epimer:.1f}% A:{anomeric:.1f}% L:{linkage:.1f}%")

print("\n" + "=" * 60)
print("Charts generated successfully")
