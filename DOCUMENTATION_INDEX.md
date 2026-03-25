# GlycoSMILES2BAP 项目文档索引

## 生成时间: 2026-03-21

---

## 一、核心记忆文件 (Memory Files)

### 1.1 Ideation Memory (M_I)
**文件路径**: `/memory/ideation-memory.md`
**状态**: ✅ 完整 (131行)

**用途说明**:
- 记录所有可行的研究方向
- 跟踪方向状态（feasible/validated/failed）
- 为未来研究提供起点

**内容概览**:
- Direction 1-4: 原有方向（包括已验证的GlycoSMILES2BAP）
- Direction 5: Antibody Fc Glycan Optimization (Elo 1620) - 最高排名
- Direction 6: Error Correction Cases (Elo 1595) - 最高新颖性
- Direction 7: GlyTouCan Database (Elo 1585) - 可扩展性展示

**如何使用**:
1. 启动新研究时，检查M_I中的可行方向
2. 选择与当前目标匹配的方向
3. 查看相关条目的Validation Plan
4. 检索标签快速定位相关内容

---

### 1.2 Experiment Memory (M_E)
**文件路径**: `/memory/experiment-memory.md`
**状态**: ✅ 已修复 (352行)

**用途说明**:
- 记录经过验证的实验策略
- 为重复实验提供参考
- 记录失败教训

**内容概览**:
- **ABL策略** (ABL-1 至 ABL-5): 消融实验方法论
- **IDEA策略** (IDEA-1 至 IDEA-3): 想法生成方法
- **Top Ideas**: F5, F12, F3的详细实施计划
- **Code Quality Metrics**: 模块代码质量指标

**如何使用**:
1. 设计新实验时，检索相关策略
2. 参考已验证的参数范围
3. 避免重复已知的失败路径
4. 使用策略的Generality字段判断适用范围

---

### 1.3 Evolution Reports
**文件路径**: `/memory/evolution-reports/`

**用途说明**:
- 记录记忆演化的详细过程
- 追踪ESE/IDE/IVE周期

**关键文件**:
| 文件 | 类型 | 说明 |
|------|------|------|
| ESE_CYCLE2_SUMMARY.md | ESE | 消融实验成功 |
| ESE_F12_F3_SUMMARY.md | ESE | F12/F3实验成功 |
| cycle_3_ide_tournament_round2.md | IDE | 第二轮想法竞赛 |

**如何使用**:
1. 了解某个方向如何被验证
2. 学习记忆演化的模式
3. 回溯决策过程

---

## 二、论文手稿文件

### 2.1 Markdown完整版
**文件路径**: `/manuscript_final.md`
**状态**: ✅ 完整 (478行)

**章节结构**:
```
1. Title & Authors
2. Abstract (含F12/F3验证)
3. Introduction
   - 背景
   - 立体化学问题
   - 贡献
4. Methods
   - Pipeline Architecture
   - Input Parsing Module
   - CCD Mapper Module
   - BAP Generator Module
   - Error Handling Strategy
   - Evaluation Metrics (新增)
5. Results
   - Benchmark Dataset
   - Stereochemistry Accuracy
   - Statistical Analysis
   - Ablation Study (Table 3)
   - Case Studies (含新增的Case Study 3 & 4)
6. Discussion
   - Key Findings
   - Strengths
   - Limitations
   - Comparison with Existing Tools
   - Community Impact
7. Conclusions
8. Acknowledgments
9. Author Contributions
10. References (11篇)
```

**如何使用**:
- 这是主要的工作版本
- 可直接用于内容编辑
- 支持版本控制

---

### 2.2 LaTeX版本
**文件路径**: `/bioinformatics_template/submission_final.pdf`
**状态**: ✅ 已生成 (169 KB, 2页)

**包含图表**:
- Figure 3: Error correction validation (figure_case_study3.pdf)
- Figure 4: GlyTouCan database processing (figure_case_study4.pdf)

**相关文件**:
- `submission_final.tex` - LaTeX源文件
- `references_complete.bib` - 完整参考文献

**如何使用**:
- 用于正式投稿
-