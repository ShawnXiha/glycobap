#!/bin/bash
# AF3 Validation Script for GlycoSMILES2BAP
# Run this script outside the sandbox environment

set -e

# Configuration
AF3_DIR="$(pwd)/alphafold3"
INPUT_DIR="$(pwd)/results/af3_validation"
OUTPUT_DIR="$(pwd)/results/af3_output"
UV_PATH="$HOME/.local/bin/uv"
PYBIND11_DIR="$HOME/tools/pybind11"

echo "==========================================" echo "AF3 Validation for GlycoSMILES2BAP" echo "==========================================" echo ""

# Check uv exists
if [ ! -f "$UV_PATH" ]; then
 echo "ERROR: uv not found at $UV_PATH" echo "Please install uv: curl -LsSf https://astral.sh/uv/install.sh | sh" exit 1 fi

# Check Python 3.12 is available
if ! command -v python3.12 &> /dev/null; then
 echo "ERROR: Python 3.12 not found" echo "AF3 requires Python 3.12 (not 3.14)" echo "Install with: sudo apt install python3.12 python3.12-venv" exit 1 fi

echo "Using Python: $(python3.12 --version)" echo ""

# Check pybind11 local installation
if [ -d "$PYBIND11_DIR" ]; then
 echo "Found local pybind11 at: $PYBIND11_DIR" export CMAKE_PREFIX_PATH="$PYBIND11_DIR:$CMAKE_PREFIX_PATH" export PYTHONPATH="$PYBIND11_DIR:$PYTHONPATH" echo "pybind11 paths configured." else echo "WARNING: Local pybind11 not found at $PYBIND11_DIR" echo "Will try to use pip installed pybind11" fi echo ""

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Step 1: Remove old venv and create new one with Python 3.12
echo "[Step 1] Setting up Python 3.12 environment..." cd "$AF3_DIR" rm -rf .venv "$UV_PATH" venv --python python3.12 echo "Python 3.12 environment created." echo ""

# Step 2: Install dependencies with pybind11 from local dir
echo "[Step 2] Installing dependencies..." cd "$AF3_DIR"

# First install pybind11 from local directory if available
if [ -d "$PYBIND11_DIR" ]; then
 echo "Installing pybind11 from local directory..." cd "$PYBIND11_DIR" "$UV_PATH" pip install --python "$AF3_DIR/.venv/bin/python" . cd "$AF3_DIR" echo "pybind11 installed." fi

# Install other dependencies
"$UV_PATH" sync --no-build-isolation echo "Dependencies installed." echo ""

# Step 3: Build chemical component database
echo "[Step 3] Building chemical component database..." "$UV_PATH" run build_data echo "Database built successfully." echo ""

# Step 4: Run AF3 predictions
echo "[Step 4] Running AF3 predictions..." echo ""

# Test 1: Sialyllactose BAP (CRITICAL - C2 anomeric test)
echo "--- Running: sialyllactose_bap.json ---" "$UV_PATH" run python run_alphafold.py \ --json_path="$INPUT_DIR/sialyllactose_bap.json" \ --output_dir="$OUTPUT_DIR/sialyllactose_bap" \ --model_dir="$HOME/models" \ --run_data_pipeline=false

echo "sialyllactose_bap completed." echo ""

# Test 2: Lactose BAP (Baseline)
echo "--- Running: lactose_bap.json ---" "$UV_PATH" run python run_alphafold.py \ --json_path="$INPUT_DIR/lactose_bap.json" \ --output_dir="$OUTPUT_DIR/lactose_bap" \ --model_dir="$HOME/models" \ --run_data_pipeline=false

echo "lactose_bap completed." echo ""

# Test 3: Sialyllactose SMILES (Comparison)
echo "--- Running: sialyllactose_smiles.json ---" "$UV_PATH" run python run_alphafold.py \ --json_path="$INPUT_DIR/sialyllactose_smiles.json" \ --output_dir="$OUTPUT_DIR/sialyllactose_smiles" \ --model_dir="$HOME/models" \ --run_data_pipeline=false

echo "sialyllactose_smiles completed." echo ""

# Step 5: Summary
echo "==========================================" echo "AF3 Predictions Complete!" echo "==========================================" echo "" echo "Output files saved to: $OUTPUT_DIR" echo "" ls -la "$OUTPUT_DIR"