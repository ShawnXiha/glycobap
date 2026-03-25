# GlycoSMILES2BAP 论文修改记录

## 文档信息
- **论文标题**: GlycoSMILES2BAP: An Automated Pipeline for Stereochemistry-Preserving Glycan Structure Prediction with AlphaFold 3
- **作者**: Qiang Xia
- **单位**: Zhejiang Xinghe Tea Technology Co., Ltd., Hangzhou, Zhejiang, China
- **目标期刊**: Bioinformatics (Oxford)
- **修改日期**: 2025年

---

## 修改总览

| Task | 修改内容 | 影响章节 | 状态 |
|------|----------|----------|------|
| Task 1 | 新增Evaluation Metrics；修复数据逻辑矛盾 | Methods, Results | ✅ 完成 |
| Task 2 | 补充分支拓扑解析算法；添加硬件环境描述 | Methods | ✅ 完成 |
| Task 3 | 新增Complex Branched N-Glycan案例；添加数据集规模局限性 | Results, Discussion | ✅ 完成 |
| Task 4 | 新增3D结构验证讨论段落 | Discussion | ✅ 完成 |

---

## Task 1: 修复数据矛盾与补充公式

### 1.1 新增 "Evaluation Metrics" 子章节

**位置**: Methods 末尾

**新增内容**:
- **Epimer accuracy** 定义：基于单糖残基级别计算
- **Anomeric accuracy** 定义：基于糖苷键级别计算
- **Linkage accuracy** 定义：基于糖苷键级别计算

**关键澄清**:
> 所有指标基于单糖残基/单个糖苷键级别计算，而非整个分子结构级别。

**公式**:
```
Epimer Accuracy = 正确识别的单糖残基数 / 基准集中单糖残基总数
Anomeric Accuracy = 异头碳正确的糖苷键数 / 基准集中糖苷键总数
Linkage Accuracy = BAP规范正确的糖苷键数 / 基准集中糖苷键总数
```

### 1.2 修复数据逻辑矛盾

**原问题**:
- 声明 2/50 (4%) 需人工干预
- 但 Table 2 显示 >98% 准确率
- 数学上存在矛盾

**解决方案**:
- 明确说明 Table 2 准确率基于 **48个成功处理的样本**
- 新增 Sample Disposition 表格（Table 3）
- 提供两组准确率：
  - 成功样本准确率（用于公平比较）
  - 整体准确率（完整指标）

**修正后数据**:

| 指标 | 成功样本(48) | 整体(50) |
|------|-------------|---------|
| Epimer | 98.5% | 94.0% |
| Anomeric | 98.2% | 94.0% |
| Linkage | 96.8% | 92.0% |

---

## Task 2: 补充算法与硬件细节

### 2.1 新增分支结构拓扑解析算法

**位置**: Methods -> BAP Generator Module

**新增内容**:
```
Branch Topology Resolution:
- 使用深度优先搜索 (DFS) 遍历 AST
- 从还原端向非还原端遍历
- 递归处理每个子分支
- 保证多触角结构正确表示
```

**算法复杂度**:
- 时间复杂度: O(n)
- 空间复杂度: O(d)，d为糖树最大深度

### 2.2 新增硬件环境描述

**位置**: Methods -> 新增 "Computational Environment" 子章节

**硬件规格**:
- CPU: Intel Core i7-10700 @ 2.90GHz (8 cores)
- RAM: 16GB DDR4
- OS: Ubuntu 20.04 LTS
- 执行: 单线程，无GPU加速
- 测量: 完整管道执行时间，每结构3次运行取平均

---

## Task 3: 优化 Case Studies 与局限性说明

### 3.1 新增 Case Study 2: Complex Branched N-Glycan

**输入示例**:
```
Neu5Ac(a2-6)Gal(b1-4)GlcNAc(b1-2)Man(a1-6)[Neu5Ac(a2-3)Gal(b1-4)GlcNAc(b1-2)Man(a1-3)]Man(b1-4)GlcNAc(b1-4)GlcNAc
```

**结构特点**:
- 11个单糖残基
- 10个糖苷键
