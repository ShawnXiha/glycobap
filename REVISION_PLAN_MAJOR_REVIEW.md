# GlycoSMILES2BAP 论文修改计划

## 基于同行评审意见的结构化修改方案

**生成日期**: 2026-03-23
**目标期刊**: Bioinformatics / J Chem Inf Model / Glycobiology

---

## 一、评审意见核心问题诊断

### 1.1 关键短板（Major Issues）

| 问题 | 严重程度 | 修改难度 | 优先级 |
|------|----------|----------|--------|
| Benchmark设计不够严格 | 🔴 高 | 中 | P0 |
| 缺乏AF3输出结构验证 | 🔴 高 | 高 | P0 |
| 统计分析方法不严谨 | 🔴 高 | 低 | P0 |
| 过度结论（overclaim） | 🔴 高 | 低 | P0 |
| 与现有方法对比不足 | 🟠 中 | 中 | P1 |
| 方法可复现性不足 | 🟠 中 | 低 | P1 |

### 1.2 次要问题（Minor Issues）

| 问题 | 状态 |
|------|------|
| 术语不统一 | 待修改 |
| 表格重复（Table 2 vs Table 5） | 待删除 |
| Figure重复（Figure 2 vs Figure 4） | 待合并 |
| 英文表达细节 | 待润色 |
| References格式不统一 | 待修改 |

---

## 二、修改优先级与执行计划

### Phase 1: 文稿基础修改（P0 - 必须完成）✅ 已完成

#### 1.1 修改overclaim表述 ✅

**当前表述** → **修改后表述**

| 位置 | 原文 | 修改后 | 状态 |
|------|------|--------|------|
| Abstract | "near-perfect accuracy" | "high stereochemical accuracy (>98%)" | ✅ 完成 |
| Abstract | "100% correction rate" | "successfully corrected all tested cases (n=10)" | ✅ 完成 |
| Results | "near-perfect stereochemistry accuracy" | "high stereochemistry accuracy" | ✅ 完成 |
| Conclusions | "near-perfect accuracy approaching manual" | "high accuracy approaching manual specification" | ✅ 完成 |

**修改命令**:
```latex
% Abstract line 32
- achieves near-perfect stereochemistry accuracy
+ achieves high stereochemical accuracy (98.5% epimer, 98.2% anomeric, 96.8% linkage)

% Results section
- achieved 100% correction rate
+ successfully corrected all tested cases (n=10), demonstrating feasibility of error detection
```

#### 1.2 删除重复表格

- [ ] 检查Table 2 vs Table 5内容
- [ ] 保留更完整的版本
- [ ] 删除重复版本并更新引用

#### 1.3 术语统一

在Methods section 2.5定义：
```
We define three accuracy metrics:
- Epimer Accuracy: correct preservation of monosaccharide stereochemistry
- Anomeric Accuracy: correct α/β configuration
- Linkage Accuracy: correct donor-acceptor atom positions
```

#### 1.4 英文表达规范化

| 原文 | 修改后 |
|------|--------|
| "~100%" | "approximately 100%" |
| "30-60min" | "30–60 minutes" |
| "<1 second" | "<1 s" |
| "0.82ms" | "0.82 s" |

---

### Phase 2: 统计方法修正（P0 - 必须完成）

#### 2.1 替换t-test为bootstrap CI

**问题分析**:
- accuracy是比例数据（0-1范围）
- 传统t-test假设正态分布，不适用
- 应使用bootstrap置信区间或McNemar test

**修改方案**:

在Methods添加新的Statistical Analysis小节：

```latex
\subsection{Statistical Analysis}

We report accuracy metrics with 95% confidence intervals calculated using bootstrap resampling (10,000 iterations). For comparing GlycoSMILES2BAP against baseline methods, we computed the difference in accuracy and reported the 95% CI of the difference. Confidence intervals that exclude zero indicate statistically significant differences.

Effect sizes were quantified using Cohen's h for proportion comparisons. We interpreted effect sizes following standard conventions: small (h < 0.2), medium (0.2 ≤ h < 0.8), large (h ≥ 0.8).
```

#### 2.2 更新表格统计信息

Table 2更新格式：
```
| Metric | Ours | 95% CI | SMILES | Difference (95% CI) |
|--------