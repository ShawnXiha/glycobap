# GlycoSMILES2BAP 项目索引

## 快速链接

| 文档 | 用途 |
|------|------|
| [QUICK_START.md](QUICK_START.md) | **新会话必读** - 快速启动指南 |
| [WORK_SUMMARY.md](WORK_SUMMARY.md) | 完整工作总结 |
| [AF3_RUN_GUIDE.md](AF3_RUN_GUIDE.md) | AF3运行详细说明 |

---

## 项目状态

### 已完成 ✅
1. 论文修改 (v2 PDF, 11页, 358KB)
2. 独立验证集创建 (n=100)
3. 复杂度统计分析
4. GlyLES对比分析
5. AF3输入文件准备
6. 运行脚本创建

### 待完成 ⏳
1. 运行AF3预测 (需在外部终端执行)
2. 分析预测结果
3. 更新论文数据

---

## 核心文件结构

```
AF3_polysaccharides/
├── QUICK_START.md          # 快速启动指南
├── WORK_SUMMARY.md         # 工作总结
├── AF3_RUN_GUIDE.md        # AF3运行指南
├── setup_env.sh            # 环境设置脚本
├── run_predictions.sh      # 预测运行脚本
│
├── bioinformatics_template/
│   └── glycosmiles2bap_complete_v2.pdf  # 论文PDF
│
├── results/
│   ├── af3_validation/     # AF3输入文件
│   │   ├── sialyllactose_bap.json
│   │   ├── lactose_bap.json
│   │   └── sialyllactose_smiles.json
│   ├── af3_output/         # AF3输出 (预测后)
│   └── EXPERIMENT_RESULTS_SUMMARY.md
│
├── memory/
│   ├── experiment-memory.md
│   └── af3_validation_status.md
│
├── scripts/
│   └── analyze_af3_results.py
│
└── alphafold3/            # AF3源码
```

---

## 新会话启动流程

1. 读取 [QUICK_START.md](QUICK_START.md)
2. 检查 `results/af3_output/` 是否有预测结果
3. 如果有结果 → 运行分析
4. 如果无结果 → 在外部运行 `bash setup_env.sh && bash run_predictions.sh`

---

## 关键验证点

| 测试 | 文件 | 验证目标 |
|------|------|----------|
| V003 | sialyllactose_bap.json | **C2 anomeric** (酮糖特性) |
| V001 | lactose_bap.json | Beta连接基线 |
| SMILES对比 | sialyllactose_smiles.json | 立体化学错误预期 |

---

## 联系信息

- 作者: Qiang Xia (夏强)
- 单位: Zhejiang Xinghe Tea Technology Co., Ltd.
- 目标期刊: Bioinformatics (Oxford)
