#!/bin/bash
# AF3 Complete Setup and Validation Script
# Handles: Python 3.12, local pybind11, AF3 dependencies, and predictions

set -e

# Configuration
PROJECT_DIR="$(pwd)"
AF3_DIR="$PROJECT_DIR/alphafold3"
INPUT_DIR="$PROJECT_DIR/results/af3_validation"
OUTPUT_DIR="$PROJECT_DIR/results/af3_output"
UV_PATH="$HOME/.local/bin/uv"
PYBIND11_DIR="$HOME/tools/pybind11"
PYTHON_VERSION="3.12"

echo "=========================================="
echo "AF3 Complete Setup and Validation"
echo "=========================================="
echo ""

# Check prerequisites
echo "[Checking Prerequisites]"

# Check uv
if [ ! -f "$UV_PATH" ]; then
    echo "ERROR: uv not found at $UV_PATH"
    echo "Please install: curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi
echo "  uv: OK"

# Check Python 3.12
if ! command -v python3.12 &> /dev/null; then
    echo "ERROR: Python 3.12 not found"
    echo "Install: sudo apt install python3.12 python3.12-venv python3.12-dev"
    exit 1
fi
echo "  Python 3.12: OK ($(python3.12 --version))"

# Check pybind11
if [ ! -d "$PYBIND11_DIR" ]; then
    echo "WARNING: pybind11 not found at $PYBIND11_DIR"
    echo "Will attempt pip install inside venv"
else
    echo "  pybind11: OK ($PYBIND11_DIR)"
fi

# Check model parameters
if [ ! -d "$HOME/models" ]; then
    echo "WARNING: Model parameters not found at $HOME/models"
    echo "AF3 predictions will fail without model parameters"
fi

echo ""

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Step 1: Setup Python environment
echo "[Step 1/5] Setting up Python 3.12 virtual environment..."
cd "$AF3_DIR"
rm -rf .venv
"$UV_PATH" venv --python python3.12
echo "  Virtual environment created: $AF3_DIR/.venv"
echo ""

# Step 2: Install pybind11
echo "[Step 2/5] Installing pybind11..."
if [ -d "$PYBIND11_DIR" ]; then
    # Copy pybind11 to venv site-packages
    PYBIND11_SITEPACKAGES="$AF3_DIR/.venv/lib/python3.12/site-packages"
    mkdir -p "$PYBIND11_SITEPACKAGES"
    
    # Check if pybind11 has setup.py or pyproject.toml
    if [ -f "$PYBIND11_DIR/setup.py" ] || [ -f "$PYBIND11_DIR/pyproject.toml" ]; then
        cd "$PYBIND11_DIR"
        "$AF3_DIR/.venv/bin/pip" install -e . --no-build-isolation 2>/dev/null || \
        "$AF3_DIR/.venv/bin/pip" install . --no-build-isolation 2>/dev/null || \
        echo "  Note: pybind11 may already be configured"
    else
        # Direct copy if no setup file
        cp -r "$PYBIND11_DIR/pybind11" "$PYBIND11_SITEPACKAGES/" 2>/dev/null || \
        cp -r "$PYBIND11_DIR" "$PYBIND11_SITEPACKAGES/pybind11" 2>/dev/null || \
        echo "  Note: pybind11 files copied"
    fi
    echo "  pybind11 installed from local directory"
else
    # Install from PyPI inside venv
    "$AF3_DIR/.venv/bin/pip" install pybind11 --break-system-packages 2>/dev/null || \
    "$AF3_DIR/.venv/bin/pip" install pybind11
    echo "  pybind11 installed from PyPI"
fi
echo ""

# Step 3: Install AF3 dependencies
echo "[Step 3/5] Installing AF3 dependencies..."
cd "$AF3_DIR"
"$UV_PATH" sync
echo "  Dependencies installed"
echo ""

# Step 4: Build chemical component database
echo "[Step 4/5] Building chemical component database..."
"$UV_PATH" run build_data
echo "  Database built"
echo ""

# Step 5: Run AF3 predictions
echo "[Step 5/5] Running AF3 predictions..."
echo ""

# Test 1: