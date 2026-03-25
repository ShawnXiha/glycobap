# AF3 Validation Run Instructions

## 当前状态

由于sandbox环境限制，无法直接在内部运行AF3。请在**外部终端**运行以下步骤。

## 运行步骤

### Step 1: 进入项目目录

```bash
cd /home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides
```

### Step 2: 检查模型参数

AF3需要模型参数。检查是否已下载：

```bash
ls -la ~/models/
```

如果没有模型参数，需要从Google DeepMind申请：
- 访问: https://github.com/google-deepmind/alphafold3
- 填写表单申请模型参数

### Step 3: 安装AF3依赖

```bash
cd alphafold3
~/.local/bin/uv sync
```

### Step 4: 构建化学组件数据库（重要！）

```bash
cd /home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides/alphafold3
~/.local/bin/uv run build_data
```

这会生成缺失的文件：
- `src/alphafold3/constants/converters/chemical_component_sets.pickle`
- 其他必要的化学组件文件

### Step 5: 运行验证预测

运行sialyllactose BAP测试（关键测试 - C2 anomeric）：

```bash
cd /home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides/alphafold3

~/.local/bin/uv run python run_alphafold.py \
  --json_path=../results/af3_validation/sialyllactose_bap.json \
  --output_dir=../results/af3_output/sialyllactose_bap \
  --model_dir=$HOME/models \
  --run_data_pipeline=false
```

运行lactose BAP测试（基线）：

```bash
~/.local/bin/uv run python run_alphafold.py \
  --json_path=../results/af3_validation/lactose_bap.json \
  --output_dir=../results/af3_output/lactose_bap \
  --model_dir=$HOME/models \
  --run_data_pipeline=false
```

### Step 5: 检查输出

```bash
ls -la ../results/af3_output/
```

预期输出文件：
- `model.cif` - 预测结构
- `summary_confidences_0.json` - 置信度分数

## 快捷脚本

可以直接运行提供的脚本：

```bash
cd /home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides
bash run_af3_validation.sh
```

## 验证结果分析

预测完成后，运行分析脚本：

```bash
python3 scripts/analyze_af3_results.py
```

## 关键验证点

### Sialyllactose (V003) - CRITICAL

检查项目：
1. **Neu5Ac anomeric carbon**: 应该在C2位置（酮糖特性）
2. **SIA-GAL连接**: Alpha(2-3)几何形状
3. **GAL-GLC连接**: Beta(1-4)几何形状

如果使用SMILES输入，AF3可能会错误地将anomeric bond放在C1。

### Lactose (V001) - Baseline

检查项目：
1. **GAL-GLC连接**: Beta(1-4)
2. **Galactose C4**: 羟基应该是axial（不是equatorial）

## 故障排除

### 问题: `ModuleNotFoundError: No module named 'absl'`
解决: 运行 `uv sync` 安装依赖

### 问题: `No such file or directory: 'model_dir'`
解决: 确保模型参数已下载到 `~/models/`

### 问题: `CUDA out of memory`
解决: 减少batch size或使用更大显存GPU

## 输出文件说明

运行成功后，在 `/results/af3_output/` 目录下会生成：

```
af3_output/
├── sialyllactose_bap/
│   ├── model.cif          # 预测结构
│   ├── summary_confidences_0.json  # 置信度
│   └── ...
├── lactose_bap/
│   └── ...
└── sialyllactose_smiles/  # 如果运行了SMILES对比
    └── ...
```

## 完成后

运行完成后，请将结果文件保存在原位置，然后在会话中告知已完成，我们将继续分析并更新evo-memory。
