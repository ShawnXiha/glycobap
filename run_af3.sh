#!/bin/bash
# AF3 Validation Run Script
# Date: 2026-03-24

cd /home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides/alphafold3

# Check if uv environment exists
if [ ! -d ".venv" ]; then
    echo "Installing dependencies with uv..."
    /home/qiang/.local/bin/uv sync --no-dev
fi

# Run AF3 prediction for sialyllactose (BAP format)
echo "Running AF3 prediction for sialyllactose_bap.json..."
/home/qiang/.local/bin/uv run python run_alphafold.py \
    --json_path=/home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides/results/af3_validation/sialyllactose_bap.json \
    --model_dir=/home/qiang/models \
    --output_dir=/home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides/results/af3_output \
    --run_data_pipeline=false

echo "AF3 prediction completed."
