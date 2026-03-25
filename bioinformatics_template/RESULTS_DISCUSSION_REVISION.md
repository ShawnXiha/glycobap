# Results, Discussion, and Conclusion Revision Summary

## Paper-Writing Skill Applied

### Results Section Improvements

**Before (Original Structure):**
- Simple subsections: Benchmark Dataset → Stereochemistry Accuracy → Statistical Analysis → Ablation Study → Case Studies
- Tables presented without structured observations
- Case studies as separate narratives

**After (Paper-Writing Template Applied):**

#### 1. Main Results (RQ1) - Structured Observations
Using the three-part observation structure:
1. **Bold title (innovation → result)**
2. **Empirical evidence**
3. **Mechanistic explanation**

Example:
```
\textbf{GlycoSMILES2BAP achieves near-perfect stereochemistry accuracy approaching manual specification.} 
The pipeline achieves 98.5% epimer accuracy, 98.2% anomeric accuracy, and 96.8% linkage accuracy, 
compared to ~60% overall accuracy for SMILES format. This 38-percentage-point improvement demonstrates 
that automated CCD+BAP generation can match expert manual specification quality.
```

#### 2. Ablation Study (RQ2) - Module Contributions
Each module's contribution explained with:
- What it does
- Why it matters
- Quantitative impact

#### 3. Practical Validation (RQ3) - Error Correction & Scalability
- Literature error correction: 100% success rate
- Database-scale processing: 94% success on 100 structures

### Discussion Section Improvements

**Before:**
- Strengths and Limitations as numbered lists

**After (Paper-Writing Counterintuitive Tactics Applied):**

#### Strengths Section
Using mechanism-first approach:
1. Automation mechanism → democratization outcome
2. CCD mapping accuracy → stereochemistry preservation
3. Processing efficiency → database-scale enablement

#### Limitations Section (Tactic 2: Declare Scope Boundaries)
- State limitation explicitly with reasoning
- Explain mitigation pathway
- Avoid defensive language

Example:
```
\textbf{CCD coverage limitation:} While 28+ monosaccharides are supported, rare or modified sugars 
(e.g., GlcN, GalN) lack standard CCD entries. This reflects PDB database limitations rather than 
methodological constraints. Users can extend the CCD mapping table for custom monosaccharides.
```

### Conclusion Section Improvements

**Before:**
- Generic summary
- Future directions as bullet list

**After (Paper-Writing Template Applied):**

1. **Problem-solution framing**: Restate the stereochemistry preservation challenge
2. **Quantified achievement**: >98% accuracy, >2000x speedup
3. **Community impact**: Enables AF3 glycan modeling at scale
4. **Scope declaration**: Targets common mammalian glycans; see limitations for edge cases

## Key Paper-Writing Tactics Applied

1. ✅ **Lower the Verbal Temperature**: Replaced "significantly outperforms" with specific metrics
2. ✅ **Declare Scope Boundaries**: Explicitly stated method targets in Conclusion
3. ✅ **Mechanism Before Metrics**: Explained WHY each module works before reporting numbers
4. ✅ **Use Claim-Evidence Thread**: Every claim anchored to Table/Figure
5. ✅ **Keep One Anchor Figure**: Figure 3 (Error Correction) as the decisive validation
6. ✅ **Delete Unsupported Claims**: Removed "revolutionizes" type language
7. ✅ **Show Failure as Competence Signal**: Included 6 failed structures analysis in Case Study 4

## LaTeX Structure Changes

```latex
% OLD STRUCTURE
\section{Results}
\subsection{Benchmark Dataset}
\subsection{Stereochemistry Accuracy}
\subsection{Statistical Analysis}
\subsection{Ablation Study}
\subsection{Case Studies}

% NEW STRUCTURE (Paper-Writing)
\section{Results}
\subsection{Main Results (RQ1)}
% Structured observations with method name as subject
\subsection{Ablation Study (RQ2)}
% Module contributions with mechanistic explanations
\subsection{Practical Validation (RQ3)}
\subsubsection{Literature Error Correction}
\subsubsection{Database-Scale Processing}

\section{Discussion}
\subsection{Strengths}
% Mechanism-first explanations
\subsection{Limitations}
% Scope boundaries declared with mitigation pathways

\section{Conclusions}
% Problem-solution framing + quantified achievement + community impact
```

## Files Updated

- `glycosmiles2bap_complete_v2.tex` - Complete paper (8 pages