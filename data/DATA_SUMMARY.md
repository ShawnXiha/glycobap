# GlycoSMILES2BAP 数据存档总结
## Data Archive Summary

**生成日期 / Generated**: 2026-03-22
**版本 / Version**: v1.0
**用途 / Purpose**: 出版数据存档 / Publication Data Archive

---

## 一、数据文件夹结构 / Data Folder Structure

```
data/
├── README_en.md              # 英文数据说明 / English Data Documentation
├── README_cn.md              # 中文数据说明 / Chinese Data Documentation
├── METHODOLOGY_en.md         # 英文方法论文档 / English Methodology
├── METHODOLOGY_cn.md         # 中文方法论文档 / Chinese Methodology
├── DATA_INDEX.md             # 数据索引文件 / Data Index
├── DATA_SUMMARY.md           # 数据总结报告 / This File
│
├── raw/                      # 原始数据 / Raw Data
│   ├── benchmark_dataset.csv         # 基准测试数据集 (17行)
│   ├── benchmark_detailed.csv        # 详细基准数据 (10行)
│   ├── error_correction_cases.csv    # 错误纠正案例 (11行)
│   └── glytoucan_processing.csv      # GlyTouCan处理数据 (18行)
│
└── processed/                # 处理后数据 / Processed Data
    ├── benchmark_results.csv         # 基准测试结果 (26行)
    ├── ablation_results.csv          # 消融研究结果 (6行)
    └── module_contributions.csv      # 模块贡献分析 (5行)
```

---

## 二、数据文件详情 / Data File Details

### 2.1 原始数据文件 / Raw Data Files

| 文件名 | 行数 | 内容描述 | 列数 |
|--------|------|----------|------|
| benchmark_dataset.csv | 17 | 基准测试数据集元数据 | 7列 |
| benchmark_detailed.csv | 10 | 扩展基准数据详情 | 9列 |
| error_correction_cases.csv | 11 | 文献错误纠正案例 | 8列 |
| glytoucan_processing.csv | 18 | GlyTouCan数据库处理记录 | 6列 |

### 2.2 处理后数据文件 / Processed Data Files

| 文件名 | 行数 | 内容描述 | 列数 |
|--------|------|----------|------|
| benchmark_results.csv | 26 | 基准测试性能结果 | 7列 |
| ablation_results.csv | 6 | 消融研究详细数据 | 5列 |
| module_contributions.csv | 5 | 模块贡献量化分析 | 5列 |

---

## 三、数据集概览 / Dataset Overview

### 3.1 基准测试数据集 (Benchmark Dataset)

- **总数 / Total**: 50个糖链结构
- **分类 / Categories**:
  - 线性糖链 (Linear): 15个
  - N-糖链 (N-glycans): 20个
  - O-糖链 (O-glycans): 10个
  - 复杂结构 (Complex): 5个

### 3.2 错误纠正案例 (Error Correction Cases)

- **总数 / Total**: 10个文献报道案例
- **来源 / Sources**: Frenz et al. (2018), Jo et al. (2011)
- **分类 / Categories**:
  - 异构体错误 (Anomeric): 4例
  - 差向异构错误 (Epimer): 2例
  - 连接错误 (Linkage): 3例
  - 构象错误 (Conformation): 1例
- **纠正率 / Correction Rate**: 100%

### 3.3 GlyTouCan数据库处理 (Database Processing)

- **总数 / Total**: 100个代表性结构
- **成功转换 / Success**: 94个
- **成功率 / Success Rate**: 94%
- **平均处理时间 / Avg Time**: 0.82ms
- **失败原因分析 / Failures**:
  - 不支持的CCD代码: 3个
  - 特殊连接方式: 2个
  - 输入格式错误: 1个

---

## 四、性能指标摘要 / Performance Metrics Summary

### 4.1 主要准确率指标 / Main Accuracy Metrics

| 指标 | GlycoSMILES2BAP | SMILES | userCCD | Manual BAP |
|------|-----------------|