# GlycoSMILES2BAP 数据文档

## 中文版

**生成日期**: 2026-03-21

---

## 一、数据集概述

本文档描述了GlycoSMILES2BAP项目中使用的所有数据集，包括原始数据、处理方法和分析结果。数据按研究目的组织，便于审稿人和读者验证研究结论。

---

## 二、数据文件夹结构

```
data/
├── raw/                    # 原始数据
│   ├── benchmark_dataset.csv        # 基准测试数据集
│   ├── benchmark_detailed.csv       # 详细基准数据
│   ├── error_correction_cases.csv   # 错误纠正案例
│   └── glytoucan_processing.csv     # GlyTouCan处理数据
├── processed/              # 处理后数据
│   ├── benchmark_results.csv        # 基准测试结果
│   ├── ablation_results.csv         # 消融研究结果
│   └── module_contributions.csv     # 模块贡献分析
├── methods/                # 分析方法
│   └── data_processing_methods.md   # 数据处理方法说明
├── README_en.md            # 英文说明文档
└── README_cn.md            # 中文说明文档（本文档）
```

---

## 三、原始数据说明

### 3.1 基准测试数据集 (`raw/benchmark_dataset.csv`)

**用途**: 评估GlycoSMILES2BAP的立体化学准确性

**数据来源**: 
- GlyTouCan数据库代表性结构
- 文献报道的标准糖链结构
- 常见哺乳动物糖链类型

**字段说明**:

| 字段名 | 类型 | 说明 | 示例 |
|--------|------|------|------|
| structure_id | 字符串 | 结构唯一标识符 | BNCH-001 |
| iupac_notation | 字符串 | IUPAC-condensed表示法 | Gal(b1-4)GlcNAc(b1-3)Gal(b1-4)Glc |
| category | 字符串 | 结构类别 | Linear |
| residue_count | 整数 | 单糖残基数量 | 4 |
| has_branch | 布尔值 | 是否有分支 | False |
| has_sialic_acid | 布尔值 | 是否含唾液酸 | False |

**统计摘要**:
- 总结构数: 50
- 线性糖链: 15 (30%)
- N-糖链: 20 (40%)
- O-糖链: 10 (20%)
- 复杂结构: 5 (10%)

### 3.2 错误纠正案例数据 (`raw/error_correction_cases.csv`)

**用途**: 验证工具对文献报道错误的纠正能力

**数据来源**: 
- Frenz et al., Structure (2018)
- Jo et al., J Comput Chem (2011)

**字段说明**:

| 字段名 | 类型 | 说明 |
|--------|------|------|
| case_id | 字符串 | 案例编号 |
| pdb_id | 字符串 | PDB数据库ID |
| error_type | 字符串 | 错误类型 |
| error_description | 字符串 | 错误描述 |
| correction_method | 字符串 | 纠正方法 |

**案例统计**:
- 异构体错误: 4例 (40%)
- 表异构错误: 2例 (20%)
- 连接错误: 3例 (30%)
- 构象错误: 1例 (10%)

### 3.3 GlyTouCan处理数据 (`raw/glytoucan_processing.csv`)

**用途**: 验证数据库级别处理能力

**数据来源**: GlyTouCan数据库代表性子集

**字段说明**:

| 字段名 | 类型 | 说明 |
|--------|------|------|
| structure_id | 字符串 | GlyTouCan结构ID |
| category | 字符串 | 结构类别 |
| residue_count | 整数 | 残基数量 |
| processing_time_ms | 浮点数 | 处理时间(毫秒) |
| success | 布尔值 | 是否成功 |

---

## 四、处理数据说明

### 4.1 基准测试结果 (`processed/benchmark_results.csv`)

**字段说明**:

| 字段名 | 类型 | 说明 |
|--------|------|------|
| method | 字符串 | 方法名称 |
| epimer_accuracy | 浮点数 | 表异构准确率 |
| anomeric_accuracy | 浮点数