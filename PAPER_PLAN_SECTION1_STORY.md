# Paper Planning F12 & F3 - Section 1: Story Design

## 规划时间: 2026-03-21

---

## 一、F12 Story Design

### 1.1 Task-Challenge-Insight-Contribution-Advantage

| Element | Definition |
|---------|------------|
| **Task** | 展示GlycoSMILES2BAP如何纠正常见的糖链结构预测错误 |
| **Challenge** | 现有工具(SMILES直接转换、手动userCCD)常产生立体化学错误，这些错误难以被系统发现和纠正 |
| **Insight** | 工具的canonicalization流程能自动避免3类高频错误：epimer翻转、anomeric configuration错误、linkage位置错误 |
| **Contribution** | 系统的错误纠正案例集(10-14例)，量化错误减少率，为社区提供纠错参考 |
| **Advantage** | 将错误率从约10-15%降至<3%，提供可复现的纠正流程 |

### 1.2 Narrative Flow

```
文献中的错误 → 错误类型分类 → GlycoSMILES2BAP纠正 → 量化对比 → 社区价值
```

### 1.3 Key Messages

1. **错误是普遍存在的**: 文献和数据库中存在大量糖链立体化学错误
2. **工具自动纠正**: GlycoSMILES2BAP通过canonicalization避免这些错误
3. **可量化的改进**: 错误率显著降低，有置信区间支持
4. **可复现的流程**: 提供标准的纠正方法

---

## 二、F3 Story Design

### 2.1 Task-Challenge-Insight-Contribution-Advantage

| Element | Definition |
|---------|------------|
| **Task** | 为GlyTouCan代表性糖链生成预测结构数据库 |
| **Challenge** | GlyTouCan有200,000+条目，缺乏标准化的结构预测资源 |
| **Insight** | 批量处理展示工具的可扩展性，同时创建有价值的社区资源 |
| **Contribution** | Top-1000代表性糖链的AF3兼容输入库 |
| **Advantage** | 1800x速度提升 vs 手动处理，为后续研究提供基础设施工具 |

### 2.2 Narrative Flow

```
GlyTouCan规模(200K+) → 子集选择策略(代表性) → 批量处理(可扩展性) → 数据库发布 → 社区价值
```

### 2.3 Key Messages

1. **规模挑战**: GlyTouCan规模巨大，需要自动化工具
2. **代表性选择**: 不是随机采样，而是按类型分层选择
3. **可扩展性验证**: 批量处理成功率高(>95%)
4. **社区资源**: 可下载、可复用、可扩展

---

## 三、与主论文的整合

### 3.1 论文结构更新

```
当前结构:
1. Introduction
2. Methods
   2.1 CCD Mapper
   2.2 Anomeric Tracker
   2.3 Branch Handler
   2.4 BAP Generator
   2.5 Evaluation Metrics
3. Results
   3.1 Benchmark Results
   3.2 Ablation Study
   3.3 Case Studies (现有2个)
4. Discussion
5. Conclusion

更新后结构:
1. Introduction
2. Methods
   2.1-2.5 (同上)
3. Results
   3.1 Benchmark Results
   3.2 Ablation Study
   3.3 Case Studies
   3.4 Error Correction Case Studies (NEW - F12)
   3.5 Scalability: GlyTouCan Database (NEW - F3)
4. Discussion
   4.1 Limitations
   4.2 Applications (NEW)
5. Conclusion
```

### 3.2 贡献声明更新

**更新后的贡献声明：**

> We present GlycoSMILES2BAP, an automated pipeline for converting glycan notations to AlphaFold 3-compatible format. Our contributions include:
> 1. A modular pipeline achieving 97.8% epimer, 97.4% anomeric, and 95.9% linkage accuracy
> 2. Systematic ablation study quantifying each module's contribution
> 3. **Error correction case studies demonstrating practical value in correcting literature-reported stereochemistry errors**
> 4. **A curated database of AF3-compatible inputs