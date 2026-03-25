#!/bin/bash
# AF3 Prediction Script for GlycoSMILES2BAP Validation
# Run AFTER setup_env.sh completes successfully

set -e

# Configuration
PROJECT_DIR="$(pwd)"
AF3_DIR="$PROJECT_DIR/alphafold3"
INPUT_DIR="$PROJECT_DIR/results/af3_validation"
OUTPUT_DIR="$PROJECT_DIR/results/af3_output"
UV_PATH="$HOME/.local/bin/uv"

echo "========================================"
echo "AF3 Predictions for GlycoSMILES2BAP"
echo "========================================"
echo ""

# Check venv exists
if [ ! -d "$AF3_DIR/.venv" ]; then
    echo "ERROR: Virtual environment not found"
    echo "Please run setup_env.sh first"
    exit 1
fi

# Create output directory
mkdir -p "$OUTPUT_DIR"

cd "$AF3_DIR"

# Test 1: Sialyllactose BAP (CRITICAL - C2 anomeric test)
echo "--- Test 1: sialyllactose_bap.json (CRITICAL) ---"
echo "Testing: Neu5Ac C2 anomeric position preservation"
echo ""

"$UV_PATH" run python run_alphafold.py \
    --json_path="$INPUT_DIR/sialyllactose_bap.json" \
    --output_dir="$OUTPUT_DIR/sialyllactose_bap" \
    --model_dir="$HOME/models" \
    --run_data_pipeline=false

echo ""
echo "sialyllactose_bap completed!"
echo ""

# Test 2: Lactose BAP (Baseline)
echo "--- Test 2: lactose_bap.json (Baseline) ---"
echo "Testing: Basic beta linkage"
echo ""

"$UV_PATH" run python run_alphafold.py \
    --json_path="$INPUT_DIR/lactose_bap.json" \
    --output_dir="$OUTPUT_DIR/lactose_bap" \
    --model_dir="$HOME/models" \
    --run_data_pipeline=false

echo ""
echo "lactose_bap completed!"
echo ""

# Test 3: Sialyllactose SMILES (Comparison)
echo "--- Test 3: sialyllactose_smiles.json (SMILES Comparison) ---"
echo "Testing: Expected lower stereochemistry accuracy"
echo ""

"$UV_PATH" run python run_alphafold.py \
    --json_path="$INPUT_DIR/sialyllactose_smiles.json" \
    --output_dir="$OUTPUT_DIR/sialyllactose_smiles" \
    --model_dir="$HOME/models" \
    --run_data_pipeline=false

echo ""
echo "sialyllactose_smiles completed!"
echo ""

# Summary
echo "========================================"
echo "All AF3 Predictions Complete!"
echo "========================================"
echo ""
echo "Output files saved to: $OUTPUT_DIR"
echo ""
ls -la "$OUTPUT_DIR"
echo ""
echo "Next step: Analyze results"
echo "  cd $PROJECT_DIR"
echo "  python3 scripts/analyze_af3_results.py"
