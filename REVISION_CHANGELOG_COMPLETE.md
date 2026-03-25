# 论文修改记录 (Revision Changelog)

## 文档信息
- **论文标题**: GlycoSMILES2BAP: An Automated Pipeline for Stereochemistry-Preserving Glycan Structure Prediction with AlphaFold 3
- **作者**: Qiang Xia
- **单位**: Zhejiang Xinghe Tea Technology Co., Ltd., Hangzhou, Zhejiang, China
- **修改日期**: 2025年3月21日
- **目标期刊**: Bioinformatics (Oxford)

---

## 修改总览

| Task | 修改内容 | 状态 |
|------|----------|------|
| Task 1 | 修复数据矛盾与补充公式 | ✅ 完成 |
| Task 2 | 补充算法与硬件细节 | ✅ 完成 |
| Task 3 | 优化Case Studies与局限性说明 | ✅ 完成 |
| Task 4 | 强化3D结构预测的讨论 | ✅ 完成 |

---

## Task 1: 修复数据矛盾与补充公式

### 修改位置
- `part3_methods.tex` - Methods部分
- `part4_results.tex` - Results部分

### 修改内容

#### 1.1 新增 "Evaluation Metrics" 子章节 (Methods)

**新增内容摘要:**
- 明确定义三个评价指标的计算方式
- **关键澄清**: 所有指标基于**单糖残基/单个糖苷键级别**计算，而非整个分子结构级别

**Epimer accuracy 定义:**
```
Epimer Accuracy = 正确识别的单糖残基数 / 基准集中的单糖残基总数
```

**Anomeric accuracy 定义:**
```
Anomeric Accuracy = 异头碳正确的糖苷键数 / 基准集中的糖苷键总数
```

**Linkage accuracy 定义:**
```
Linkage Accuracy = BAP规范正确的糖苷键数 / 基准集中的糖苷键总数
```

#### 1.2 修复数据逻辑冲突 (Results)

**原问题:**
- 文中提到 2/50 (4%) 结构需人工干预
- Table 2 显示 Overall stereochemistry >98%
- 数据逻辑存在矛盾

**解决方案:**
- 明确说明 Table 2 准确率基于**48个成功处理样本**
- 新增 Table 3: Sample Disposition and Error Breakdown
- 提供两组准确率数据:
  - 成功样本准确率 (用于公平比较)
  - 整体准确率 (考虑所有50样本)

**新增表格数据:**

| 类别 | 数量 | 百分比 |
|------|------|--------|
| Total benchmark structures | 50 | 100% |
| Successfully processed (automated) | 48 | 96% |
| Manual intervention required | 2 | 4% |
| -- Unsupported CCD (GlcN, GalN) | 2 | 4% |
| -- Algorithmic errors | 0 | 0% |

---

## Task 2: 补充算法与硬件细节

### 修改位置
- `part3_methods.tex` - BAP Generator Module部分

### 修改内容

#### 2.1 新增分支结构拓扑解析算法

**新增段落:** "Branch Topology Resolution"

**核心内容:**
- 明确使用**深度优先搜索 (DFS)** 遍历AST
- 从还原端向非还原端遍历
- 递归处理每个子分支
- 保证多触角结构的正确表示

**算法复杂度:**
- 时间复杂度: O(n)
- 空间复杂度: O(d), d为最大深度

#### 2.2 新增硬件环境说明

**新增子章节:** "Computational Environment"

**硬件配置:**
- CPU: Intel Core i7-10700 @ 2.90GHz (8 cores)
- RAM: 16GB DDR4
- OS: Ubuntu 20.04 LTS
- 执行模式: 单线程执行，无GPU加速
- 测量方法: 每结构3次运行取平均

---

## Task 3: 优化Case Studies与局限性说明

### 修改位置
- `part4_results.tex` - Case Studies部分
- `part5_discussion.tex` - Limitations部分

### 修改内容

#### 3.1 新增 Case Study 2: Complex Branched N-Glycan

**新增案例:**
```
Input: Neu5Ac(a2-6)Gal(b1-4)GlcNAc(b1-2)Man(a1-6)[Neu5Ac(a2-3)Gal(b1-4)GlcNAc(b1-2)Man(a1-3)]Man