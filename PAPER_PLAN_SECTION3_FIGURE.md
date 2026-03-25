# Paper Planning Section 3: Figure Design

## 规划时间: 2026-03-21

---

## 一、Figure Design for F12

### 1.1 Figure F12-1: Error Correction Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│                 Error Correction Workflow                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐  │
│  │ Literature│    │ Error    │    │ GlycoSMILES│    │ Corrected│  │
│  │  Error    │───>│ Analysis │───>│  2BAP     │───>│ Structure│  │
│  │  Report   │    │          │    │ Processing│    │          │  │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘  │
│       │               │               │               │         │
│       v               v               v               v         │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐  │
│  │ Original  │    │ Error    │    │ Automated │    │ Validated│  │
│  │  Symbol   │    │  Type    │    │ Correction│    │  Output  │  │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘  │
│                                                                  │
│  Example Case:                                                   │
│  Input: Gal(b1-4)Glc (wrong epimer)                             │
│  Error: D-Galactose should be D-Glucose                         │
│  Output: Glc(b1-4)Glc (corrected)                               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**设计原则：**
- 突出错误检测 → 纠正流程
- 展示具体案例
- 量化结果标注

### 1.2 Figure F12-2: Error Type Distribution

```
┌─────────────────────────────────────────────────────────────────┐
│           Error Type Distribution (n=12 cases)                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Error Type          │ Before    │ After     │ Reduction        │
│  ────────────────────┼───────────┼───────────┼───────────────── │
│  Epimer flip         │ 5 cases   │ 0 cases  │ 100% correction  │
│  Anomeric config     │ 4 cases   │ 0 cases  │ 100% correction  │
│  Linkage position    │ 3 cases   │ 0 cases  │ 100% correction  │
│  ────────────────────┼───────────┼───────────┼───────────────── │
│  TOTAL               │ 12 cases  │ 0 cases  │ 100% correction  │
│                                                                  │
│  [Bar Chart: Before vs After for each error type]               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 二、Figure Design for F3

### 2.1 Figure F3-1: GlyTouCan Database Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│              GlyTouCan Structure Database Pipeline               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────┐                                                │
│  │ GlyTouCan   │  200,000+ entries                              │
│  │ Database    │                                                │
│  └──────┬──────┘                                                │
│         │                                                        │
│         v                                                        │
│  ┌─────────────┐                                                │
│  │ Selection   │  Stratified sampling by category               │
│  │ Strategy    │  - N-glycans (300)                             │
│  │             │  - O-glycans (200)                             │
│  │             │  - Glycolipids (150)                           │
│  │             │  - GAGs (100)                                  │
│  │             │