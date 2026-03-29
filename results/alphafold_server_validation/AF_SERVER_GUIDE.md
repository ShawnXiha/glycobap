# AlphaFold Server 使用指南

## 概述

AlphaFold Server (https://alphafoldserver.com) 是DeepMind提供的免费在线结构预测服务，支持glycan输入。

---

## Step 1: 访问服务器

1. 打开浏览器，访问: https://alphafoldserver.com
2. 使用Google账户登录（免费）
3. 每日有限制预测数量

---

## Step 2: 准备输入

### 2.1 Glycan输入格式

AlphaFold Server支持以下glycan输入方式：

#### 方式A: 通过Glycan Builder
- 使用内置的glycan builder工具
- 选择单糖类型和连接方式
- 适合简单结构

#### 方式B: 通过CCD Codes
- 直接输入CCD codes列表
- 指定连接关系
- 更适合我们的测试

### 2.2 我们测试结构的输入

#### 测试1: Sialyllactose
```
结构: Neu5Ac(a2-3)Gal(b1-4)Glc
输入方式: 使用CCD codes
CCD codes: SIA, GAL, GLC
连接:
- SIA C2 → GAL O3 (alpha)
- GAL C1 → GLC O4 (beta)
```

#### 测试2: Lactose
```
结构: Gal(b1-4)Glc
输入方式: 使用CCD codes
CCD codes: GAL, GLC
连接:
- GAL C1 → GLC O4 (beta)
```

#### 测试3: M3 N-glycan
```
结构: Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc
输入方式: 使用CCD codes
CCD codes: MAN, MAN, BMA, NAG, NAG
连接:
- MAN(1) C1 → BMA O3 (alpha)
- MAN(2) C1 → BMA O6 (alpha)
- BMA C1 → NAG(4) O4 (beta)
- NAG(4) C1 → NAG(5) O4 (beta)
```

---

## Step 3: 提交预测

1. 点击 "New Prediction"
2. 选择 "Ligand" 类型
3. 输入CCD codes或使用glycan builder
4. 提交预测
5. 等待结果（可能需要几分钟到几小时）

---

## Step 4: 下载结果

预测完成后，可以下载：
- `predicted_structure.pdb` 或 `.cif`
- `confidence_scores.json`

---

## Step 5: 验证结果

### 关键验证点

#### Sialyllactose (CRITICAL):
- [ ] 检查Neu5Ac的anomeric bond是否在C2位置
- [ ] 检查ring oxygen是否在O6
- [ ] 检查SIA-GAL连接几何（alpha配置）
- [ ] 检查GAL-GLC连接几何（beta配置）

#### Lactose:
- [ ] 检查GAL的C4羟基方向（axial）
- [ ] 检查GAL-GLC连接几何（beta配置）

#### M3 N-glycan:
- [ ] 检查分支拓扑是否正确
- [ ] 检查两个MAN分支的连接

### 使用Privateer验证

下载结构后，可以使用Privateer验证：

```python
# 使用CCP4的Privateer
# 或使用我们的脚本
python scripts/privateer_validation.py --input downloaded_structure.cif
```

---

## 故障排除

### 问题1: Glycan格式不被识别
- 解决方案: 使用简化的glycan builder
- 或联系服务器支持

### 问题2: 预测失败
- 可能原因: 结构过于复杂
- 解决方案: 使用更小的测试结构

### 问题3: 排队时间过长
- AlphaFold Server有每日限制
- 可以分多天完成测试

---

## 记录结果

完成预测后，将结果记录到：
- `results/alphafold_server_validation/prediction_results.md`
- 更新 `memory/VALIDATION_ALTERNATIVE_STATUS.md`
