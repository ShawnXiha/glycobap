# 数据处理与分析方法说明

## 概述

本文档详细说明GlycoSMILES2BAP项目中使用的数据处理和分析方法，供出版方和审稿人参考。

---

## 一、数据收集方法

### 1.1 基准测试数据集

**来源**:
- GlyTouCan数据库 (https://glytoucan.org/)
- 文献中的标准糖链结构
- PDB数据库中的糖蛋白结构

**选择标准**:
1. 覆盖常见哺乳动物糖链类型
2. 包含不同复杂度（线性、分支、唾液酸化）
3. 代表性单糖种类
4. 可验证的立体化学信息

**收集过程**:
```
GlyTouCan数据库 → 筛选代表性结构 → 验证IUPAC注释 → 构建基准集
```

### 1.2 错误纠正案例

**来源文献**:
- Frenz et al., Structure (2018) - PMID: 30344107
- Jo et al., J Comput Chem (2011) - PMID: 21815173

**案例选择**:
- 文献明确报告的立体化学错误
- 有正确结构参考
- 可通过CCD映射验证

### 1.3 GlyTouCan规模处理数据

**数据来源**: GlyTouCan数据库代表性子集

**选择策略**:
- 哺乳动物N-糖链: 25个结构
- O-糖链: 20个结构
- 糖脂糖链: 20个结构
- 糖胺聚糖: 15个结构
- 微生物糖链: 20个结构

---

## 二、数据处理方法

### 2.1 糖链注释解析

**输入格式**: IUPAC-condensed, WURCS

**解析流程**:
```
输入字符串 → 语法验证 → AST构建 → 单糖识别 → 连接信息提取
```

**关键步骤**:
1. **词法分析**: 识别单糖名称、异头构型、连接位置
2. **语法分析**: 构建抽象语法树(AST)
3. **语义验证**: 检查生物学合理性

### 2.2 CCD映射算法

**映射规则**:

| 输入特征 | 映射逻辑 | 输出 |
|---------|---------|------|
| 单糖名称 | 标准化小写 → CCD查找表 | CCD代码 |
| 异头构型 (α/β) | 与单糖组合查询 | 完整CCD |
| 绝对构型 (D/L) | 嵌入CCD代码 | 立体化学定义 |

**特殊情况处理**:
- 唾液酸 (Neu5Ac, Neu5Gc): 异头位置C2
- 戊糖 (Xyl, Ara, Rib): 环氧位置O4
- 岩藻糖 (Fuc): L-构型

### 2.3 BAP生成算法

**核心算法**:

```python
def generate_bap(glycan_topology):
    """
    从糖链拓扑结构生成bondedAtomPairs
    
    参数:
        glycan_topology: 包含残基和连接信息的拓扑结构
    
    返回:
        list: BAP条目列表
    """
    bap_entries = []
    for linkage in glycan_topology.linkages:
        donor = linkage.donor
        acceptor = linkage.acceptor
        
        # 确定异头碳位置
        if donor.is_ketose():
            anomeric_c = "C2"  # 唾液酸等酮糖
        else:
            anomeric_c = "C1"  # 醛糖
        
        # 确定环氧位置
        if donor.is_pentose():
            ring_o = "O4"
        elif donor.is_sialic_acid():
            ring_o = "O6"
        else:
            ring_o = "O5"
        
        bap_entry = {
            "residue1": donor.id,
            "atom1": anomeric_c,
            "residue2": acceptor.id,
            "atom2": f"O{linkage.position}",
            "order": 1
        }
        bap_entries.append(bap_entry)
    
    return bap_entries
```

---

## 三、分析方法

### 3.1 准确率计算方法

**表位异构准确率** (Epimer Accuracy):
```
准确率 = 正确识别