# AF3 验证完整运行指南

## 问题修复记录

### 问题1: Python版本不兼容
- **错误**: Python 3.14与Flax不兼容
- **解决**: 使用Python 3.12创建虚拟环境

### 问题2: 缺少chemical_component_sets.pickle
- **错误**: FileNotFoundError: chemical_component_sets.pickle
- **解决**: 运行 `uv run build_data`

### 问题3: pip externally-managed-environment
- **错误**: 无法使用pip安装本地pybind11
- **解决**: 在虚拟环境内安装

---

## 运行步骤

### Step 1: 进入项目目录

```bash
cd /home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides
```

### Step 2: 运行环境设置脚本

```bash
bash setup_env.sh
```

这会：
- 删除旧的Python 3.14 venv
- 创建Python 3.12虚拟环境
- 从`~/tools/pybind11`安装本地pybind11
- 安装AF3依赖
- 构建化学组件数据库

### Step 3: 运行预测脚本

```bash
bash run_predictions.sh
```

---

## 分步手动运行

如果脚本失败，可以手动分步运行：

```bash
cd /home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides/alphafold3

# 1. 删除旧venv
rm -rf .venv

# 2. 创建Python 3.12 venv
~/.local/bin/uv venv --python python3.12

# 3. 安装pybind11（在venv内）
.venv/bin/pip install ~/tools/pybind11

# 4. 安装AF3依赖
~/.local/bin/uv sync

# 5. 构建数据库
~/.local/bin/uv run build_data

# 6. 运行预测
~/.local/bin/uv run python run_alphafold.py \
  --json_path=../results/af3_validation/sialyllactose_bap.json \
  --output_dir=../results/af3_output/sialyllactose_bap \
  --model_dir=$HOME/models \
  --run_data_pipeline=false
```

---

## 验证文件清单

### 输入文件 (`/results/af3_validation/`)
- `sialyllactose_bap.json` - 关键测试（C2 anomeric）
- `lactose_bap.json` - 基线测试
- `sialyllactose_smiles.json` - SMILES对比

### 输出目录 (`/results/af3_output/`)
- `sialyllactose_bap/` - BAP格式预测结果
- `lactose_bap/` - Lactose预测结果
- `sialyllactose_smiles/` - SMILES预测结果

### 脚本文件
- `setup_env.sh` - 环境设置脚本
- `run_predictions.sh` - 预测运行脚本
- `run_af3_full.sh` - 一体化脚本

---

## 关键验证点

### Sialyllactose (CRITICAL)
检查AF3输出中的：
1. Neu5Ac anomeric carbon是否在C2（酮糖特性）
2. SIA-GAL连接是否为Alpha(2-3)
3. GAL-GLC连接是否为Beta(1-4)

### 预期结果
- **BAP格式**: >98%立体化学正确
- **SMILES格式**: ~60%立体化学错误（对比验证）

---

## 常见错误解决

| 错误 | 原因 | 解决方案 |
|------|------|---------|
| `KeyError: '__annotations__'` | Python 3.14不兼容 | 使用Python 3.12 |
| `FileNotFoundError: chemical_component_sets.pickle` | 未构建数据库 | 运行 `uv run build_data` |
| `externally-managed-environment` | 系统pip限制 | 在venv内安装 |
| `No module named 'absl'` | 依赖未安装 | 运行 `uv sync` |
