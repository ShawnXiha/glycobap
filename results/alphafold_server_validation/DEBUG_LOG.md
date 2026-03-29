# AlphaFold Server Validation Debug Log

## Date: 2026-03-26

## Objective
使用AlphaFold Server在线服务验证GlycoSMILES2BAP生成的glycan结构的stereochemistry正确性。

---

## Step 1: 理解AlphaFold Server输入格式

### AlphaFold Server支持的输入格式
根据官方文档，AlphaFold Server (alphafoldserver.com) 支持：
1. **蛋白质序列** + ligands (glycans作为ligands)
2. Glycan通过CCD codes指定
3. 支持covalent bonds定义

### 关键发现
- AlphaFold Server有自己的JSON格式（与本地AF3不同）
- 需要指定蛋白质序列（至少一个氨基酸）
- Glycan作为ligand，通过ccdCodes指定
- 使用bondedAtomPairs定义glycosidic bonds

---

## Step 2: 准备测试案例

### 测试案例选择

#### Case 1: Sialyllactose (CRITICAL)
**测试目标**: 验证sialic acid的C2 anomeric位置

**IUPAC**: Neu5Ac(a2-3)Gal(b1-4)Glc

**CCD Codes**: ["SIA", "GAL", "GLC"]

**关键验证点**:
- Neu5Ac的anomeric carbon在C2（酮糖特性）
- SIA-GAL连接: Alpha(2-3)
- GAL-GLC连接: Beta(1-4)

#### Case 2: Lactose (Baseline)
**测试目标**: 基本beta连接验证

**IUPAC**: Gal(b1-4)Glc

**CCD Codes**: ["GAL", "GLC"]

**关键验证点**:
- Beta(1-4)连接几何
- Galactose C4羟基轴向

#### Case 3: M3 N-glycan Core (Branch)
**测试目标**: 分支处理验证

**IUPAC**: Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc

**CCD Codes**: ["MAN", "MAN", "BMA", "NAG", "NAG"]

**关键验证点**:
- 分支拓扑正确
- Alpha(1-3)和Alpha(1-6)连接

---

## Step 3: AlphaFold Server提交问题排查

### 问题1: 需要蛋白质序列
**发现**: AlphaFold Server要求至少一个蛋白质序列
**解决**: 使用短肽序列（如GS linker）作为载体

### 问题2: Glycan输入格式
**发现**: AlphaFold Server的glycan格式与本地AF3不同
**解决**: 需要转换为Server兼容格式

### 问题3: BondedAtomPairs格式
**发现**: Server格式的bondedAtomPairs需要调整
**解决**: 参考Server文档调整格式

---

## Step 4: 替代方案

### 方案A: 使用N-glycosylated蛋白质
- 使用已知有glycan的蛋白质结构
- 只预测glycan部分
- 比较stereochemistry

### 方案B: 使用GlycoTorchViz
- 独立的glycan可视化工具
- 可验证3D结构合理性

### 方案C: 直接使用Privateer
- 验证已知PDB结构
- 与文献报道对比

---

## Step 5: 当前状态

### 已完成
- [x] 分析AlphaFold Server输入要求
- [x] 准备测试案例定义
- [x] 创建初步输入JSON文件

### 待解决
- [ ] 确认AlphaFold Server是否支持standalone glycan预测
- [ ] 如果不支持，准备替代验证方案
- [ ] 完成Privateer验证脚本

---

## Notes
- AlphaFold Server可能有glycan预测限制
- 建议同时准备Privateer验证作为补充
- 考虑使用已有PDB结构进行对比验证
