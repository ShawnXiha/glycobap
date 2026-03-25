# F3: GlyTouCan Subset Selection

## Stage 1: Initial Implementation

### 实验目标
选择1000个代表性糖链用于批量处理验证

### 数据来源
- GlyTouCan数据库 (https://glytoucan.org)
- 已有数据文件: `/data/glytoucan_representative_structures.json`

---

## 子集选择策略

### 类别分布设计

| 类别 | 目标数量 | 选择标准 |
|------|----------|----------|
| Mammalian N-glycans | 300 | 高质量，完整注释 |
| Mammalian O-glycans | 150 | 常见Core结构 |
| Glycolipid glycans | 150 | 结构多样性 |
| GAGs (糖胺聚糖) | 100 | 药物相关 |
| Microbial glycans | 100 | 新兴研究领域 |
| Plant glycans | 100 | 结构独特性 |
| Other/Mixed | 100 | 剩余类型覆盖 |
| **Total** | **1000** | - |

---

## 已有数据检查

### 现有数据文件: `/data/glytoucan_representative_structures.json`
- 当前结构数: 100个
- 需要扩展: 900个

### 扩展策略
1. 从GlyTouCan API获取更多条目
2. 按类别分层采样
3. 确保IUPAC/WURCS注释完整
4. 验证结构唯一性

---

## 实际可用数据 (从现有文件)

### Mammalian N-glycans (25个)

| GlyTouCan ID | IUPAC Notation | Name |
|--------------|----------------|------|
| G00001MO | Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc | Man3 core |
| G00002MO | Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)[Fuc(a1-6)]GlcNAc | Man3F core |
| G00003MO | Man(a1-2)Man(a1-3)[Man(a1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc | Man5 |
| G00004MO | Man(a1-2)Man(a1-2)Man(a1-3)[Man(a1-2)Man(a1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc | Man6 |
| G00005MO | Man(a1-2)Man(a1-2)Man(a1-3)[Man(a1-2)Man(a1-2)Man(a1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc | Man7 |
| G00006MO | Gal(b1-4)GlcNAc(b1-2)Man(a1-3)[Gal(b1-4)GlcNAc(b1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc | NA2 |
| G00007MO | Neu5Ac(a2-6)Gal(b1-4)GlcNAc(b1-2)Man(a1-3)[Neu5Ac(a2-6)Gal(b1-4)GlcNAc(b1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc | A2 |
| G00008MO | Neu5Ac(a2-6)Gal(b1-4)GlcNAc(b1-2)Man(a1-3)[Gal(b1-4)GlcNAc(b1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc | A1 |
| G00009MO | Gal(b1-4)GlcNAc(b1-2)Man(a1-3)[Gal(b1-4)GlcNAc(b1-2)Man(a1-6)]Man(b1-4)GlcNAc(b1-4)[Fuc(a1-6)]GlcNAc | NA2F |
| G00010