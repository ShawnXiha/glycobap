# Fix Python Version Issue for AF3

## Problem
AF3 uses Python 3.14 in the virtual environment, which is incompatible with Flax library.
AF3 requires Python 3.10-3.12.

## Solution

### Step 1: Remove existing virtual environment
```bash
cd /home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides/alphafold3
rm -rf .venv
```

### Step 2: Create new virtual environment with Python 3.12
```bash
# Check available Python versions
python3.12 --version

# If Python 3.12 is not installed, install it
# Ubuntu/Debian:
sudo apt update
sudo apt install python3.12 python3.12-venv

# Create venv with Python 3.12
uv venv --python 3.12
```

### Step 3: Install dependencies
```bash
cd /home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides/alphafold3
~/.local/bin/uv sync
```

### Step 4: Build chemical component database
```bash
~/.local/bin/uv run build_data
```

### Step 5: Run predictions
```bash
# Test sialyllactose BAP
~/.local/bin/uv run python run_alphafold.py \
  --json_path=../results/af3_validation/sialyllactose_bap.json \
  --output_dir=../results/af3_output/sialyllactose_bap \
  --model_dir=$HOME/models \
  --run_data_pipeline=false

# Test lactose BAP
~/.local/bin/uv run python run_alphafold.py \
  --json_path=../results/af3_validation/lactose_bap.json \
  --output_dir=../results/af3_output/lactose_bap \
  --model_dir=$HOME/models \
  --run_data_pipeline=false
```

## Quick Fix Script
Alternatively, run this single command:
```bash
cd /home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides/alphafold3
rm -rf .venv && ~/.local/bin/uv venv --python 3.12 && ~/.local/bin/uv sync && ~/.local/bin/uv run build_data
```

## pybind11 Local Installation

If GitHub is inaccessible, use local pybind11:

```bash
# Set pybind11 path
export pybind11_DIR=$HOME/tools/pybind11

# Or install pybind11 to venv
cd /home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides/alphafold3
source .venv/bin/activate
pip install ~/tools/pybind11
```

### Full Setup with Local pybind11

```bash
cd /home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides/alphafold3

# Remove old venv
rm -rf .venv

# Create new venv with Python 3.12
~/.local/bin/uv venv --python 3.12

# Activate venv
source .venv/bin/activate

# Install pybind11 from local path
pip install ~/tools/pybind11

# Install other dependencies
~/.local/bin/uv sync

# Build database
~/.local/bin/uv run build_data
```

## Verify Python Version
```bash
# Check Python version in venv
.venv/bin/python --version
# Should show: Python 3.12.x
```
