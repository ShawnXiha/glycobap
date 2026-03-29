# AlphaFold Server 验证 - 分步操作指南

## 背景
由于AF3模型参数未获得审批，使用AlphaFold Server在线服务作为替代验证方案。

---

## 前置准备

### 1. 确认账户
- 访问 https://alphafoldserver.com
- 使用Google账户登录
- 确认有预测额度（每日免费额度有限）

### 2. 准备输入文件
已准备的文件位于 `results/alphafold_server_validation/`:
- `af_server_input_sialyllactose.json` - 关键测试（C2 anomeric）
- `af_server_input_lactose.json` - 基线测试

---

## Step 1: 提交Sialyllactose预测

### 1.1 登录AlphaFold Server
1. 打开 https://alphafoldserver.com
2. 点击 "Sign in with Google"

### 1.2 创建新预测
1. 点击 "New Prediction"
2. 选择 "Ligand" 类型
3. 输入方式选择:
   - **方式A**: 上传JSON文件
   - **方式B**: 手动输入CCD codes

### 1.3 输入结构信息

#### 方式A: JSON上传
直接上传 `af_server_input_sialyllactose.json`

#### 方式B: 手动输入
```
Name: Sialyllactose_GlycoSMILES2BAP_Validation
Ligand CCD Codes: SIA, GAL, BGC
```

### 1.4 提交预测
1. 点击 "Submit"
2. 记录Job ID
3. 等待预测完成（可能需要数分钟到数小时）

---

## Step 2: 下载和分析结果

### 2.1 下载预测文件
预测完成后，下载以下文件:
- `predicted_structure.pdb` 或 `.cif`
- `confidence_scores.json`

### 2.2 保存到项目目录
```bash
# 创建输出目录
mkdir -p results/alphafold_server_output/sialyllactose

# 移动下载的文件
mv ~/Downloads/predicted_structure.cif results/alphafold_server_output/sialyllactose/
mv ~/Downloads/confidence_scores.json results/alphafold_server_output/sialyllactose/
```

### 2.3 分析stereochemistry

#### 手动检查
使用PyMOL或ChimeraX:
```python
# PyMOL命令
load results/alphafold_server_output/sialyllactose/predicted_structure.cif

# 检查Neu5Ac的C2位置
# C2应该是anomeric carbon，连接到Gal的O3
# 检查键几何形状
```

#### 使用Privateer
```bash
# 在CCP4环境中
privateer results/alphafold_server_output/sialyllactose/predicted_structure.cif
```

---

## Step 3: 关键验证点检查清单

### Sialyllactose验证清单

#### ✅ C2 Anomeric位置（CRITICAL）
- [ ] Neu5Ac的anomeric carbon在C2（不是C1）
- [ ] C2-O3键存在且几何正确
- [ ] 键角约110-115°（glycosidic bond典型值）

#### ✅ Ring Oxygen
- [ ] Neu5Ac的ring oxygen在O6位置
- [ ] 6-membered ring形成正确

#### ✅ 连接几何
- [ ] SIA-GAL: Alpha(2-3)连接
- [ ] GAL-GLC: Beta(1-4)连接

#### ✅ 置信度
- [ ] pLDDT > 70（置信区域）
- [ ] Glycan区域有合理的置信度分数

---

## Step 4: 记录结果

### 4.1 创建结果报告
在 `results/alphafold_server_output/sialyllactose/` 创建:
- `validation_report.md` - 验证报告
- 截图保存关键几何特征

### 4.2 更新memory
将结果记录到 `memory/ALTERNATIVE_VALIDATION_DEBUG.md`

---

## 故障排除

### 问题1: 上传JSON失败
**原因**: AlphaFold Server可能使用不同的JSON格式

**解决方案**:
1. 使用Web界面手动输入
2. 或使用CCD codes直接输入
3