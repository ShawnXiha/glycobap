#!/bin/bash
# AF3 Environment Setup Script
# Sets up Python 3.12 venv and installs local pybind11

set -e

# Configuration
PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
AF3_DIR="$PROJECT_DIR/alphafold3"
UV_PATH="$HOME/.local/bin/uv"
PYBIND11_DIR="$HOME/tools/pybind11"

echo "==========================================" 
echo "AF3 Environment Setup"
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

echo ""

# Step 1: Remove old venv and create new one
echo "[Step 1/4] Setting up Python 3.12 virtual environment..."
cd "$AF3_DIR"
rm -rf .venv
"$UV_PATH" venv --python python3.12
echo "  Virtual environment created"
echo ""

# Step 2: Install pybind11
echo "[Step 2/4] Installing pybind11..."
if [ -d "$PYBIND11_DIR" ]; then
    VENV_PIP="$AF3_DIR/.venv/bin/pip"
    cd "$PYBIND11_DIR"
    # Try editable install first, then regular install
    "$VENV_PIP" install -e . 2>/dev/null || "$VENV_PIP" install . || true
    echo "  pybind11 installed from: $PYBIND11_DIR"
else
    VENV_PIP="$AF3_DIR/.venv/bin/pip"
    "$VENV_PIP" install pybind11
    echo "  pybind11 installed from PyPI"
fi
echo ""

# Step 3: Install AF3 dependencies
echo "[Step 3/4] Installing AF3 dependencies..."
cd "$AF3_DIR"
"$UV_PATH" sync
echo "  Dependencies installed"
echo ""

# Step 4: Build chemical component database
echo "[Step 4/4] Building chemical component database..."
"$UV_PATH" run build_data
echo "  Database built"
echo ""

echo "=========================================="
echo "Environment Setup Complete!"
echo "=========================================="
echo ""
echo "Now run predictions with: bash run_predictions.sh"
