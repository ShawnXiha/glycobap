# PDB结构验证方案

## 背景
AlphaFold Server不支持直接提交纯glycan结构。需要使用替代方案。

## 方案：使用已知PDB结构验证

### 方法
从PDB数据库中选择含有glycan的已知结构，验证我们的工具生成的BAP格式是否正确。

### 验证流程
1. 选择已知glycan结构的PDB条目
2. 使用我们的工具生成对应的BAP输入
3. 与原始结构对比验证

### 测试PDB结构

#### 1. Lactose (乳糖)
- PDB常见于乳糖结合蛋白
- 已知连接方式: Gal(b1-4)Glc

#### 2. Sialyllactose (唾液酸乳糖)
- PDB: 多种病毒/抗体复合物
- 已知连接方式: Neu5Ac(a2-3)Gal(b1-4)Glc
- 关键验证: C2 anomeric位置

#### 3. N-glycan核心
- PDB: 多种糖蛋白
- 已知连接方式: Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc-Asn

### 验证脚本
使用Privateer或其他结构验证工具验证生成的结构。

### 实施步骤

#### Step 1: 收集已知结构
```bash
# 从PDB下载含有glycan的结构
# 例如: 5NSC (有错误的fucosylated结构)
# 例如: 含有lactose的结构
```

#### Step 2: 使用GlycoSMILES2BAP生成BAP
```python
# 输入: IUPAC notation
# 输出: AF3格式的JSON
```

#### Step 3: 对比验证
- 检查anomeric carbon位置
- 检查连接位置
- 检查stereochemistry

## 具体验证案例

### Case 1: Sialyllactose验证
| 属性 | 已知正确值 | GlycoSMILES2BAP输出 | 验证方法 |
|------|-----------|---------------------|----------|
| SIA anomeric | C2 | C2 | 检查BAP |
| SIA-GAL linkage | a2-3 | a2-3 | 检查连接 |
| GAL-GLC linkage | b1-4 | b1-4 | 检查连接 |

### Case 2: Lactose验证
| 属性 | 已知正确值 | GlycoSMILES2BAP输出 | 验证方法 |
|------|-----------|---------------------|----------|
| GAL anomeric | C1 | C1 | 检查BAP |
| GAL-GLC linkage | b1-4 | b1-4 | 检查连接 |

## 验证结果记录

将结果记录到 `VALIDATION_RESULTS.md`
