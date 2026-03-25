# AF3验证实验准备总结

## 完成日期
2026-03-24

---

## 1. AF3安装检查

### 发现的AF3资源
- **位置**: `/alphafold3/`
- **主要脚本**: `run_alphafold.py`
- **文档**: `docs/input.md`, `docs/installation.md`
- **Docker支持**: `docker/Dockerfile`

### AF3运行要求
- **操作系统**: Linux (Ubuntu 22.04 LTS推荐)
- **GPU**: NVIDIA Compute Capability 8.0+ (A100/H100)
- **内存**: 建议64GB+ RAM
- **磁盘**: 最高1TB (数据库)
- **CUDA**: 12.6
- **Docker**: 支持rootless模式

---

## 2. AF3输入格式分析

### Glycan定义方式
根据`docs/input.md`，AF3支持以下glycan输入格式：

### 方式1: CCD Codes + bondedAtomPairs (GlycoSMILES2BAP方式)
```json
{
  "ligand": {
    "id": "G",
    "ccdCodes": ["GAL", "BGC"]
  }
}
```

### 方式2: SMILES (已知问题 - 立体化学错误)
```json
{
  "ligand": {
    "id": "G",
    "smiles": "OC[C@H]1O[C@@H](O)[C@H](O)[C@@H](O)[C@@H]1O"
  }
}
```

### BondedAtomPairs格式
```json
"bondedAtomPairs": [
  [["A", 145, "SG"], ["L", 1, "C04"]],  // 蛋白质-配体键
  [["J", 1, "O6"], ["J", 2, "C1"]]      // 配体内部键 (glycan)
]
```

**关键参数**:
- `[entity_id, residue_index, atom_name]`
- residue_index: 1-based
- atom_name: CCD中定义的原子名

---

## 3. 创建的验证文件

### 文件位置
`/results/af3_validation/`

### V003: Sialyllactose (CRITICAL - C2 anomeric测试)

**文件**: `sialyllactose_bap.json`

```json
{
  "name": "sialyllactose_bap",
  "modelSeeds": [1],
  "sequences": [
    {
      "ligand": {
        "id": "G",
        "ccdCodes": ["SIA", "GAL", "BGC"]
      }
    }
  ],
  "bondedAtomPairs": [
    [["G", 1, "C2"], ["G", 2, "O3"]],
    [["G", 2, "C1"], ["G", 3, "O4"]]
  ],
  "dialect": "alphafold3",
  "version": 1
}
```

**验证要点**:
- SIA的anomeric carbon在C2 (酮糖特性)
- C2-O3键正确连接
- Alpha (Sia-Gal) + Beta (Gal-Glc) 构型

### V001: Lactose (基线测试)

**文件**: `lactose_bap.json`

```json
{
  "name": "lactose_bap",
  "modelSeeds": [1],
  "sequences": [
    {
      "ligand": {
        "id": "G",
        "ccdCodes": ["GAL", "BGC"]
      }
    }
  ],
  "bondedAtomPairs": [
    [["G", 1, "C1"], ["G", 2, "O4"]]
  ],
  "dialect": "alphafold3",
  "version": 1
}
```

---

## 4. 验证策略

### Paired Comparison Design
| 实验 | 输入格式 | 预期结果 |
|------|---------|----------|
| BAP格式 | CCD + bondedAtomPairs | >98% 立体化学正确 |
| SMILES格式 | SMILES string | ~60% 立体化学错误 |
| 对比 | 差值 | >35% 改进 |

### 关键验证点

1. **Sialic Acid C2 Anomeric (CRITICAL)**
   - BAP: 强制C2位置
   - SMILES: