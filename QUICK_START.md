# Quick Start Guide for AF3 Validation

## 项目概述
验证 GlycoSMILES2BAP 工具生成的糖结构在 AlphaFold 3 中的立体化学准确性。

---

## 当前状态
- [x] 论文修改完成 (v2 PDF已生成)
- [x] 独立验证集数据准备完成
- [x] AF3输入文件已创建
- [ ] **待完成**: 运行AF3预测，验证结果

---

## 快速开始（3步）

### Step 1: 环境设置
```bash
cd /home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides
bash setup_env.sh
```

### Step 2: 运行AF3预测
```bash
bash run_predictions.sh
```

### Step 3: 分析结果
```bash
python3 scripts/analyze_af3_results.py
```

---

## 关键文件位置

### 输入文件
| 文件 | 路径 | 用途 |
|------|------|------|
| sialyllactose_bap.json | `results/af3_validation/` | **CRITICAL测试** - C2 anomeric |
| lactose_bap.json | `results/af3_validation/` | 基线测试 |
| sialyllactose_smiles.json | `results/af3_validation/` | SMILES对比组 |

### 输出文件（预测后生成）
| 文件 | 路径 | 内容 |
|------|------|------|
| model.cif | `results/af3_output/<test_name>/` | AF3预测结构 |
| summary_confidences_0.json | `results/af3_output/<test_name>/` | 置信度分数 |

### 脚本文件
| 文件 | 用途 |
|------|------|
| `setup_env.sh` | 环境设置（Python 3.12 + pybind11 + AF3依赖） |
| `run_predictions.sh` | 运行AF3预测 |
| `scripts/analyze_af3_results.py` | 分析预测结果 |

---

## 常见问题修复

### 问题1: Python版本错误
```
症状: KeyError: '__annotations__' (Flax不兼容)
修复: rm -rf .venv && uv venv --python python3.12
```

### 问题2: 缺失pickle文件
```
症状: FileNotFoundError: chemical_component_sets.pickle
修复: uv run build_data
```

### 问题3: pip externally-managed
```
症状: externally-managed-environment error
修复: 在venv内使用 .venv/bin/pip install
```

### 问题4: pybind11安装失败
```
解决方案: 使用本地 ~/tools/pybind11
设置: setup_env.sh 自动处理
```

---

## 验证要点

### Sialyllactose (CRITICAL)
- [ ] Neu5Ac anomeric carbon 在 **C2** (不是C1)
- [ ] SIA-GAL 连接: Alpha(2-3)
- [ ] GAL-GLC 连接: Beta(1-4)

### Lactose (Baseline)
- [ ] GAL-GLC 连接: Beta(1-4)
- [ ] Galactose C4 羟基 axial

---

## 完成后的下一步

1. 运行 `python3 scripts/analyze_af3_results.py` 分析结果
2. 将验证结果记录到 `/memory/experiment-memory.md`
3. 更新论文 `/bioinformatics_template/glycosmiles2bap_complete_v2.tex`
4. 重新编译PDF

---

## 联系上下文

如需恢复工作，阅读:
1. `WORK_SUMMARY.md` - 完整工作总结
2. `memory/af3_validation_status.md` - 验证状态
3. 本文件 - 快速启动

