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
| 1 | "F12只是案例分析，缺乏统计显著性" | 收集n≥10个文献案例，计算错误纠正率置信区间 |
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
- 如果移除Anomeric Tracker → anomeric错误无法纠正 ✓ 已在主论文验证
- 如果移除Branch Handler → linkage错误无法纠正 ✓ 已在主论文验证

**F3的"消融"思考：**
- F3不涉及新方法，是可扩展性验证，消融已在主论文完成

### 3.4 Fallback Narrative

**如果审稿人认为F12/F3贡献不足：**
- 主叙事：方法是核心，应用案例展示价值
- 备选叙事：工具论文的标准结构包含应用验证

---

## 四、Experiment Plan

### 4.1 F12: Error Correction Case Studies

#### 数据收集

| 来源 | 预期案例数 | 错误类型 |
|------|-----------|----------|
| 文献报告的立体化学错误 | 5-7 | epimer翻转 |
| 用户CCD手册错误案例 | 3-4 | anomeric configuration |
| 结构预测软件失败案例 | 2-3 | linkage位置 |
| **总计** | **10-14** | 混合 |

#### 评估指标

| 指标 | 定义 | 计算方式 |
|------|------|----------|
| 错误纠正率 | 工具成功纠正的案例比例 | n_corrected / n_total |
| 错误类型覆盖率 | 覆盖的错误类型数量 | 3类全覆盖为最优 |
| 与文献一致性 | 纠正后与正确结构一致 | binary per case |

#### 实验设计

```
实验F12-1: 文献错误案例收集
- 搜索关键词: "glycan structure error", "stereochemistry error glycan"
- 选择标准: 文献明确报告的错误案例
- 输出: 10-14个案例的详细记录

实验F12-2: 错误纠正验证
- 输入: 收集的错误案例的原始符号
- 处理: GlycoSMILES2BAP生成AF3输入
- 验证: 与正确结构对比
- 输出: 错误纠正率 + 置信区间

实验F12-3: 错误类型分析
- 分类: epimer / anomeric / linkage
- 统计: 每类错误的纠正成功率
- 输出: 按错误类型的量化结果
```

### 4.2 F3: GlyTouCan Structure Database

#### 数据选择策略

| 类别 | 数量 | 选择标准 |
|------|------|----------|
| 常见N-糖链 | 300 | 高质量, 完整注释 |
| 常见O-糖链 | 200 | 研究热点 |
| 糖脂糖链 | 150 | 结构多样性 |
| GAGs | 100 | 药物相关 |
| 微生物糖链 | 100 | 新兴领域 |
| 其他 | 150 | 覆盖剩余类型 |
| **总计** | **1000** | 代表性覆盖 |

#### 评估指标

| 指标 | 定义 | 目标值 |
|------|------|--------|
| 处理成功率 | 无错误生成的比例 | >95% |
| 平均处理时间 | 每结构处理时间 | <1s |
| 结构覆盖度 | 成功处理的类型数 | 全部主要类型 |

#### 实验设计

```
实验F3-1: GlyTouCan子集选择
- 来源: GlyTouCan数据库导出
- 筛选: 有完整WURCS/IUPAC注释
- 采样: 按类别分层采样
- 输出: 1000个代表性糖链列表

实验F3-2: 批量处理性能测试
- 输入: 1000个糖链符号
- 处理: 批量运行GlycoSMILES2BAP
- 记录: 处理时间、成功率、失败原因
- 输出: 性能统计数据

实验F3-3: 数据库构建
- 格式: JSON + 文档说明
- 内容: 每个糖链的AF3输入
- 发布: GitHub仓库
- 输出: 可下载的数据库文件
``
