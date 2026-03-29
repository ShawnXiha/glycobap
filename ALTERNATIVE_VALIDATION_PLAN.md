# Alternative Validation Plan for GlycoSMILES2BAP

## 背景
由于AF3模型参数未获得审批，需要调整验证方向，采用替代方案验证工具的准确性。

---

## 当前已完成的验证

| 验证项 | 状态 | 说明 |
|--------|------|------|
| 输入格式验证 | ✅ 完成 | JSON格式符合AF3规范 |
| CCD Mapping逻辑 | ✅ 完成 | 28+配置正确映射 |
| BAP生成逻辑 | ✅ 完成 | 单元测试100%通过 |
| 文献对比分析 | ✅ 完成 | 与Huang et al. 2025对比 |
| GlyLES工具对比 | ✅ 完成 | 功能差异分析 |
| 独立验证集统计 | ✅ 完成 | 100结构复杂度分析 |

---

## 替代验证方案

### 方案1: AlphaFold Server在线服务 ⭐推荐

**网址**: https://alphafoldserver.com

**优势**:
- 免费使用，无需本地模型参数
- 支持glycan输入（CCD codes）
- 官方AF3服务
- 输出包含置信度分数

**限制**:
- 每日预测数量限制
- 需要排队等待
- 复杂结构可能失败

**验证步骤**:
```
1. 准备测试结构（选择3-5个关键案例）
2. 通过Web界面提交预测
3. 下载预测结果
4. 分析stereochemistry准确性
```

**关键测试案例**:
| 结构 | 测试目标 | 预期验证 |
|------|----------|----------|
| Sialyllactose | C2 anomeric位置 | Neu5Ac的C2-O键几何 |
| M3 N-glycan | Branch处理 | 分支拓扑正确性 |
| Fucosylated | L-config | Fucose L构型 |

---

### 方案2: Privateer结构验证

**工具**: Privateer (CCP4套件的一部分)

**用途**: 验证glycan结构的stereochemistry

**安装**: 
```bash
# 通过conda安装
conda install -c ccdc ccdc-privateer
# 或通过CCP4
```

**验证内容**:
- Anomeric configuration (α/β)
- Absolute configuration (D/L)
- Ring puckering
- Linkage geometry

**验证流程**:
```python
# 使用Privateer验证生成的结构
from privateer import validate_glycan

result = validate_glygan("predicted_structure.cif")
# 输出stereochemistry验证结果
```

---

### 方案3: 与PDB已知结构对比

**数据来源**: 
- PDB数据库中含glycan的结构
- GlyTouCan参考结构

**方法**:
1. 查找已知正确结构的glycan
2. 使用工具生成对应输入
3. 比较 correctness

**参考PDB结构**:
| PDB ID | Glycan类型 | 说明 |
|--------|-----------|------|
| 5NSC | Fucosylated | 文献报道有错误的案例 |
| 5K65 | N-glycan | 缺失linkage案例 |
| 已验证结构 | 多种 | 作为对照 |

**验证指标**:
- Epimer: 正确的单糖类型
- Anomer: 正确的α/β构型
- Linkage: 正确的连接位置

---

### 方案4: RDKit化学合理性验证

**用途**: 验证生成结构的化学合理性

**验证内容**:
```python
from rdkit import Chem
from rdkit.Chem import Descriptors, rdMolDescriptors

# 验证项目:
# 1. 键长范围合理性
# 2. 手性中心正确性
# 3. 分子描述符匹配
# 4. 3D构象合理性
```

---

### 方案5: 分子动力学验证

**用途**: 验证结构在MD模拟中的稳定性

**工具**: GROMACS + GLYCAM力场

**方法**:
1. 将生成的glycan结构进行短时间MD
2. 分析结构稳定性
3. 检查stereochemistry是否保持

---

## 推荐执行顺序

### Phase 1: AlphaFold Server验证 (最直接)
1. 准备3个关键测试案例JSON
2. 通过Web界面提交预测
3. 分析输出结构的stereochemistry

### Phase 2: Privateer验证 (补充)
1. 安装Privateer工具
2. 验