# 验证方案状态总结

## 当前状态：方案1 (AlphaFold Server) 已准备就绪

---

## 方案1: AlphaFold Server 在线验证

### 状态：✅ 准备完成，等待执行

### 已准备的文件

| 文件 | 路径 | 用途 |
|------|------|------|
| `STEP_BY_STEP_GUIDE.md` | `results/alphafold_server_validation/` | 详细操作指南 |
| `AF_SERVER_GUIDE.md` | `results/alphafold_server_validation/` | Server使用说明 |
| `DEBUG_LOG.md` | `results/alphafold_server_validation/` | 调试记录 |
| `af_server_input_sialyllactose.json` | `results/alphafold_server_validation/` | CRITICAL测试输入 |
| `af_server_input_lactose.json` | `results/alphafold_server_validation/` | 基线测试输入 |

### 执行步骤

```bash
# Step 1: 访问 AlphaFold Server
# 打开浏览器访问: https://alphafoldserver.com

# Step 2: 登录/注册账户（免费）

# Step 3: 创建新预测
# - 选择 "Ligand" 类型
# - 上传或输入CCD codes: SIA, GAL, GLC (sialyllactose)
# - 或使用: GAL, GLC (lactose)

# Step 4: 等待预测完成（通常几分钟到几小时）

# Step 5: 下载结果
# - model.cif (预测结构)
# - confidence_scores.json (置信度)

# Step 6: 验证stereochemistry
# python scripts/alternative_validation.py --input downloaded_model.cif
```

### 验证要点

#### Sialyllactose (CRITICAL)
- [ ] Neu5Ac anomeric carbon 位置：**C2** (酮糖特性)
- [ ] SIA-GAL 连接：Alpha(2-3)
- [ ] GAL-GLC 连接：Beta(1-4)
- [ ] Ring oxygen：O6 (not O5)

#### Lactose (Baseline)
- [ ] GAL anomeric：C1
- [ ] GAL-GLC 连接：Beta(1-4)
- [ ] Galactose C4 hydroxyl：axial (区分于glucose)

---

## 方案2: Privateer 结构验证

### 状态：✅ 脚本已准备

### 执行方式
```bash
# 需要已有PDB/CIF结构文件
python scripts/privateer_validation.py --input structure.cif
```

### 验证内容
- Anomeric configuration (α/β)
- Absolute configuration (D/L)
- Ring puckering
- Linkage geometry

---

## 方案3: PDB已知结构对比

### 推荐参考结构

| PDB ID | Glycan类型 | 说明 |
|--------|-----------|------|
| 5NSC | Fucosylated | 文献报道错误案例 |
| 5K65 | N-glycan | 缺失linkage案例 |
| 4BYH | Sialyllactose | 已知正确结构 |

### 对比方法
1. 从PDB下载参考结构
2. 使用工具生成对应的输入
3. 比较结构参数

---

## Evo-Memory 记录

### 新增记录文件
- `memory/ALTERNATIVE_VALIDATION_DEBUG.md` - 方案1调试记录
- `memory/VALIDATION_ALTERNATIVE_STATUS.md` - 替代验证状态

### 关键发现
1. AF3模型参数未获批，需要使用替代方案
2. AlphaFold Server是最佳替代方案（免费、官方、支持glycan）
3. Privateer可用于结构验证补充

---

## 下一步行动

1. **立即执行**：通过AlphaFold Server提交预测
2. **等待结果**：预测完成后下载结构
3. **分析验证**：使用脚本验证stereochemistry
4. **记录结果**：更新论文和memory

---

## 预期时间线

| 阶段 | 时间 | 任务 |
|------|------|------|
| 提交预测 | Day 0 | 上传到AF Server |
| 等待结果 | Day 0-2 | 等待队列处理 |
| 分析结果 | Day 2 | 下载并分析 |
| 更新论文 | Day 3 | 整合验证