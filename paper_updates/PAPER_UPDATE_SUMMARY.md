# Paper Update Summary - PDB Validation Results

## Update Date: 2026-03-28

## 1. Story Design Update

### Core Narrative Arc (Updated)
1. **Problem**: AF3 glycan modeling limited by stereochemistry errors in standard formats
2. **Solution**: Automated CCD+BAP generation with correct stereochemistry handling
3. **Validation**: Multi-layered validation including NEW PDB structure comparison
4. **Impact**: Enables accurate, scalable glycan structure prediction

### Key Story Points
- **Critical Test**: Sialic acid C2 anomeric position (most important validation)
- **Literature Correction**: PDB:5NSC fucose anomer error corrected
- **Branch Handling**: M3 N-glycan topology preserved
- **Baseline**: Lactose epimer distinction validated

## 2. Methods Section Updates

### Add to Section "Evaluation Metrics":

```latex
\subsection{PDB Structure Validation}

To validate CCD mapping accuracy against experimentally determined structures,
we compared GlycoSMILES2BAP output with known PDB entries. This approach
provides an orthogonal validation method independent of AF3 model predictions.

\textbf{Reference Structures:} We selected four PDB structures covering
critical stereochemistry scenarios:

\begin{itemize}
    \item \textbf{PDB:5NSC} (Fucosylated): Tests fucose L-configuration and 
          anomeric designation (FUC vs. BDF)
    \item \textbf{PDB:1L6R} (Lactose): Tests epimer distinction 
          (galactose C4 axial hydroxyl)
    \item \textbf{PDB:2VXR} (Sialyllactose): \textit{Critical test} for 
          Neu5Ac anomeric position (C2 for ketose)
    \item \textbf{PDB:5K65} (M3 N-glycan): Tests branched structure handling
\end{itemize}

\textbf{Validation Process:}
\begin{enumerate}
    \item Extract expected CCD codes from PDB structure annotations
    \item Run GlycoSMILES2BAP on equivalent IUPAC notation
    \item Compare generated CCD codes against expected
    \item Verify anomeric carbon and ring oxygen positions
\end{enumerate}

This validation confirmed that the CCD Mapper module correctly assigns:
(1) anomeric positions (C1 for aldoses, C2 for sialic acids),
(2) ring oxygen positions (O5 for hexoses, O6 for sialic acids), and
(3) absolute configurations (D/L).
```

## 3. Experiments Section Updates

### Add to "Case Studies" subsection:

```latex
\textbf{Case Study 5: PDB Structure Comparison Validation}

We performed systematic validation against four experimentally determined
PDB structures to verify CCD mapping accuracy. Table~\ref{tab:pdb_validation}
summarizes the results.

\begin{table}[h]
\centering
\caption{PDB Structure Validation Results}
\label{tab:pdb_validation}
\begin{tabular}{lllll}
\toprule
PDB ID & Structure & Key Validation & Expected & Result \\
\midrule
5NSC & Fucosylated & FUC (alpha-L) & FUC & \textbf{PASS} \\
1L6R & Lactose & GAL (beta-D) & GAL & \textbf{PASS} \\
\textbf{2VXR} & \textbf{Sialyllactose} & \textbf{SIA C2 anomeric} & SIA/C2/O6 & \textbf{PASS} \\
5K65 & M3 N-glycan & Branch topology & MAN/BMA/NAG & \textbf{PASS} \\
\bottomrule
\end{tabular}
\end{table}

\textbf{Critical Finding - Sialic Acid C2 Anomeric:}
The most significant validation was PDB:2VXR (sialyllactose), which confirmed
that GlycoSMILES2BAP correctly handles Neu5Ac:
\begin{itemize}
    \item Anomeric carbon: C2 (not C1, as sialic acids are ketoses)
    \item Ring oxygen: O6 (not O5, due to 9-carbon backbone)
    \item CCD code: SIA (alpha-Neu5Ac) correctly assigned
\end{itemize}

This addresses the core stereochemistry problem identified