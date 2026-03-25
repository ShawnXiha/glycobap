# F12: 文献糖链结构错误案例收集

## 收集日期: 2026-03-21
## Stage: 1 - Initial Implementation

---

## 案例收集策略

### 选择标准
1. 文献明确报告的立体化学错误
2. 有已知的正确结构作为参照
3. 错误类型可被GlycoSMILES2BAP预防

### 错误类型分类
- **Epimer错误**: 立体构型翻转 (D/L, Gal/Glc等)
- **Anomeric错误**: α/β配置错误
- **Linkage错误**: 糖苷键位置错误
- **Ring Conformation错误**: 高能环构象

---

## 收集案例列表

### Case-01: Fucose Anomeric Error (PDB: 5NSC)
- **来源**: Frenz et al., Structure, 2018 (PMID: 30344107)
- **错误类型**: Anomeric错误
- **错误结构**: β-Fuc (Fucose 507)
- **正确结构**: α-Fuc
- **分辨率**: 2.3Å
- **GlycoSMILES2BAP预防机制**: Anomeric Tracker模块自动识别Fuc为α-L构型

### Case-02: High-Energy Boat Conformation (PDB: 5K65)
- **来源**: Frenz et al., Structure, 2018 (PMID: 30344107)
- **错误类型**: Ring Conformation错误
- **错误结构**: Fucose 507 - boat构象
- **正确结构**: ¹C₄ chair构象
- **分辨率**: 2.5Å
- **GlycoSMILES2BAP预防机制**: CCD Mapper使用标准chair构型

### Case-03: Missing N-Glycosidic Bond (PDB: 5K65)
- **来源**: Frenz et al., Structure, 2018 (PMID: 30344107)
- **错误类型**: Linkage错误
- **错误结构**: Asn 297与GlcNAc缺失连接
- **正确结构**: Asn297-GlcNAc N-糖苷键
- **分辨率**: 2.5Å
- **GlycoSMILES2BAP预防机制**: BAP Generator显式生成所有连接

### Case-04: Multiple Stereochemistry Errors (PDB: 1C1Z)
- **来源**: Frenz et al., Structure, 2018 (PMID: 30344107)
- **错误类型**: 混合错误 (2 anomeric + 2 ring)
- **错误结构**: 11个糖残基中4个有错误
- **正确结构**: 经Rosetta精修后修正
- **分辨率**: 2.87Å
- **GlycoSMILES2BAP预防机制**: 多模块协同防止

### Case-05: Maximum High-Energy Conformations (PDB: 5H9Y)
- **来源**: Frenz et al., Structure, 2018 (PMID: 30344107)
- **错误类型**: Ring Conformation错误
- **错误结构**: 15个糖残基中8个高能构象
- **正确结构**: 全部修正为chair
- **分辨率**: 1.97Å
- **GlycoSMILES2BAP预防机制**: CCD Mapper使用标准构象库

### Case-06: High Error Rate (PDB: 5WBE)
- **来源**: Frenz et al., Structure, 2018 (PMID: 30344107)
- **错误类型**: Ring Conformation错误
- **错误结构**: 21个糖残基中6个高能构象
- **正确结构**: 全部修正
- **分辨率**: 2.75Å
- **GlycoSMILES2BAP预防机制**: CCD构象约束

### Case-07: Incorrect Bond Connectivity (PDB: 1Q5C)
- **来源**: Jo et al., J Comput Chem, 2011 (PMID: 21815173)
- **错误类型**: Linkage错误
- **错误结构**: 糖苷键氧与环氧形成额外键
- **正确结构**: 正常糖苷键连接
- **GlycoSMILES2BAP预防机制**: BAP Generator精确原子配对

### Case-08: Incorrect C-C Bond (PDB: 1BCR)
- **来源**: Jo et al., J Comput Chem, 2011 (PM