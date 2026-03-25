# Evolution Report: ESE (Experiment Strategy Evolution)

## Cycle: 2
## Type: ESE - Experiment Success
## Date: 2026-03-21

---

## Trigger

Ablation experiment pipeline completed successfully:
- **Stage 1**: Ablation design - Completed
- **Stage 2**: Ablation execution - Completed
- **Stage 3**: Results analysis - Completed
- **Stage 4**: Paper update - Completed

All stages passed their success criteria.

---

## Extracted Strategies

### 1. Data Processing Strategies

#### Strategy: Representative Subset Sampling for Ablation
- **Context**: When conducting ablation studies on structured data pipelines
- **Pattern**: Use n=20 representative samples spanning all categories (Linear, N-glycan, O-glycan, Sialylated) rather than full benchmark
- **Evidence**: Cycle 2 ablation study achieved statistical significance (p<0.001) with n=20
- **Generality**: Broadly applicable - works for any modular pipeline where category-specific behavior matters
- **Retrieval Tags**: ablation, sampling, statistical-power, category-balanced

#### Strategy: Category-Balanced Benchmark Construction
- **Context**: Building evaluation benchmarks for multi-domain problems
- **Pattern**: Ensure each category has sufficient representation (n≥4 per category) for category-specific analysis
- **Evidence**: Enabled identification of category-specific module impacts (e.g., Branch Handling critical for N-glycans)
- **Generality**: Domain-specific to problems with categorical structure variation
- **Retrieval Tags**: benchmark, category-balance, statistical-power

### 2. Architecture Strategies

#### Strategy: Modular Pipeline Design for Ablation
- **Context**: Designing pipelines that need to be validated module-by-module
- **Pattern**: Each module should be independently testable with clear input/output contracts
- **Evidence**: CCD Mapper, Anomeric Tracker, Branch Handler, and BAP Generator could each be ablated without breaking the pipeline
- **Generality**: Broadly applicable to any software pipeline
- **Retrieval Tags**: modular-design, ablation-friendly, pipeline-architecture

#### Strategy: DFS Traversal for Tree-Structured Data
- **Context**: Processing branched glycan topologies
- **Pattern**: Use depth-first search from reducing end to non-reducing ends for systematic coverage
- **Evidence**: Branch handling module achieved 95.9% linkage accuracy on branched structures; removal caused 13.5% drop
- **Generality**: Domain-specific to tree-structured data (glycans, parse trees, ASTs)
- **Retrieval Tags**: dfs, tree-traversal, branched-structures, topology

#### Strategy: Category-Aware Anomeric Position Tracking
- **Context**: Handling different monosaccharide types with varying anomeric positions
- **Pattern**: Use C1 for aldoses, C2 for ketoses/sialic acids, with explicit category checking
- **Evidence**: Anomeric tracking removal caused 18.9% accuracy drop, especially 34.5% for sialylated glycans
- **Generality**: Domain-specific to carbohydrate chemistry
- **Retrieval Tags**: anomeric-position, sialic-acid, ketose, aldose

### 3. Evaluation Strategies

#### Strategy: Multi-Metric Ablation Reporting
- **Context**: Reporting ablation study results
- **Pattern**: Report all three dimensions (Epimer, Anomeric, Linkage) with delta-from-baseline for each
- **Evidence**: Table 3 in manuscript clearly shows module contributions across all metrics
- **Generality**: Broadly applicable for multi-dimensional evaluation
- **Retrieval Tags**: ablation-reporting, multi-metric, delta-analysis

#### Strategy: Category-Specific Failure Analysis
- **Context**: Understanding where modules matter most
- **Pattern**: Break down ablation results by category (Linear, N-glycan, O-glycan, Sialylated)
- **Evidence**: Revealed that Branch Handling has zero overhead for linear glycans but is critical for N-glycans
- **Generality**: Broadly applicable when categories have different structural properties
- **Retrieval Tags**: category-analysis, failure-patterns, module-impact

### 4. Debugging Strategies

#### Strategy: Module Removal Diagnosis
- **Context**: When pipeline performance drops unexpectedly
- **Pattern**: Systematically remove one module at a time to isolate contribution
- **Evidence**: Ablation study revealed BAP Generator is essential (47% accuracy drop without it)
- **Generality**: Broadly applicable for modular systems
- **Retrieval Tags**: debugging, module-is