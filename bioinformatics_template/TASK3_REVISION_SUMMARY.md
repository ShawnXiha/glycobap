# Task 3 修改总结：Case Studies 与局限性说明

## 修改日期：2025-01

---

## 修改内容

### 1. 新增 Case Study 2: Complex Branched N-Glycan

在 Results -> Case Studies 部分添加了详细的分支结构案例：

**输入示例：**
```
Neu5Ac(a2-6)Gal(b1-4)GlcNAc(b1-2)Man(a1-6)[Neu5Ac(a2-3)Gal(b1-4)GlcNAc(b1-2)Man(a1-3)]Man(b1-4)GlcNAc(b1-4)GlcNAc
```

**关键内容：**
- 双触角N-糖结构（11个残基）
- 15个CCD代码正确生成
- 详细展示分支点BAP生成逻辑：
  - α1-3臂：Man(α1-3) → C1→O3
  - α1-6臂：Man(α1-6) → C1→O6
- 方括号解析正确处理
- DFS遍历先完成α1-3分支再回溯处理α1-6分支
- 处理时间1.2s，展示线性复杂度

**案例顺序调整：**
- Case Study 1: LNnT (原有)
- Case Study 2: Complex Branched N-Glycan (新增)
- Case Study 3: Sialylated Structure (原Case 2顺延)
- Case Study 4: Rare Monosaccharides (原Case 3顺延)

---

### 2. 新增数据集规模局限性说明

在 Discussion -> Limitations 部分新增第一项：

**关键陈述：**
- 承认50个样本作为 **pilot validation** 的局限性
- 说明当前样本量足以检测大效应量 (Cohen's d > 2.0)
- 提出未来改进方向：
  - 扩展到GlyTouCan数据库的数千个代表性结构
  - 涵盖更广泛的分类多样性（细菌、植物、真菌糖）
  - 纳入罕见修饰以评估鲁棒性

---

## 文件修改

| 文件 | 修改内容 |
|------|----------|
| `part4_results.tex` | 新增Case Study 2，调整案例顺序 |
| `part5_discussion.tex` | 新增Limitations第1项 |

---

## 质量检查

- [x] Case Study 2提供完整IUPAC输入示例
- [x] 分支点BAP生成逻辑清晰描述
- [x] DFS遍历与Methods部分一致
- [x] 局限性陈述客观、专业
- [x] 未来方向具体可行
- [x] 引用格式正确 (\\citet{huang2025})
