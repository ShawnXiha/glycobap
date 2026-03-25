# Paper Planning: F12 & F3 补充方案

## 规划时间: 2026-03-21

---

## 一、背景分析

### 当前论文状态
- **主要贡献**: GlycoSMILES2BAP工具 - 糖链结构预测输入生成
- **核心结果**: 97.8% epimer, 97.4% anomeric, 95.9% linkage准确率
- **已有内容**:
  - Ablation Study (Table 3)
  - Evaluation Metrics定义
  - Case Study 1 & 2
  - 完整的方法描述

### 补充目标
将F12(错误纠正案例)和F3(GlyTouCan数据库)作为新的应用章节添加到论文中，提升论文从"纯方法论文"到"方法+应用论文"。

---

## 二、Story Design

### F12: Glycan Structure Error Correction Case Studies

#### 核心故事线

| Element | Definition |
|---------|------------|
| **Task** | 展示GlycoSMILES2BAP如何纠正常见的糖链结构预测错误 |
| **Challenge** | 现有工具(SMILES直接转换、手动userCCD)常产生立体化学错误，但这些错误难以被系统发现和纠正 |
| **Insight** | 工具的canonicalization流程能自动避免3类高频错误：epimer翻转、anomeric configuration错误、linkage位置错误 |
| **Contribution** | 系统的错误纠正案例集，量化错误减少率，为社区提供纠错参考 |
| **Advantage** | 将错误率从约10-15%降至<3%，提供可复现的纠正流程 |

#### Story叙述逻辑
```
文献中的错误 → 错误类型分析 → GlycoSMILES2BAP纠正 → 量化对比
```

### F3: GlyTouCan Structure Prediction Database

#### 核心故事线

| Element | Definition |
|---------|------------|
| **Task** | 为GlyTouCan代表性糖链生成预测结构数据库 |
| **Challenge** | GlyTouCan有200,000+条目，但缺乏标准化的结构预测资源 |
| **Insight** | 批量处理展示工具的可扩展性，同时创建有价值的社区资源 |
| **Contribution** | Top-1000代表性糖链的AF3兼容输入库 |
| **Advantage** | 1800x速度提升 vs 手动处理，为后续研究提供基础设施工具 |

#### Story叙述逻辑
```
GlyTouCan规模 → 子集选择策略 → 批量处理 → 数据库发布 → 社区价值
```

---

## 三、Counterintuitive Planning

### 3.1 Pre-emptive Rejection Letter

**模拟审稿人可能的拒绝意见：**

| # | 可能的拒绝意见 | 预防措施 |
|---|---------------|----------|
| 1 | "F12只是案例分析，缺乏统计显著性" | 收集n>=10个文献案例，计算错误纠正率置信区间 |
| 2 | "F3只是批量处理，无方法创新" | 强调可扩展性验证+社区资源价值，不是方法创新claim |
| 3 | "案例集选择有cherry-picking嫌疑" | 明确选择标准：文献报告的错误案例，非人工挑选 |
| 4 | "数据库实际价值未验证" | 提供使用场景：研究者可直接下载使用，节省时间 |
| 5 | "与主论文贡献关联不明确" | 统一框架：都是展示工具实际应用价值 |

### 3.2 Narrow Claim First

**F12 最小可辩护声明：**
> "GlycoSMILES2BAP成功纠正了文献报告的糖链立体化学错误，错误类型包括epimer翻转、anomeric configuration错误和linkage位置错误。"

**F3 最小可辩护声明：**
> "GlycoSMILES2BAP可批量处理GlyTouCan代表性子集，生成AF3兼容输入，处理速度达<1s/结构。"

**扩展声明(需更多证据)：**
- F12: "工具可减少90%的常见错误" ← 需要大规模验证
- F3: "数据库已被X个研究组使用" ← 需要发布后统计

### 3.3 Ablation First

**F12的"消融"思考：**
- 如果移除CCD Mapper → epimer错误无法纠正 ✓ 已在主论文验证
- 如果移除Anomeric Tracker →