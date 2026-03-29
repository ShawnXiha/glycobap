# AlphaFold Server Validation - Correct Input Files

## 问题诊断

**原始问题**: "no job found in files"  
**原因**: AlphaFold Server要求输入JSON为数组格式，即使只有一个预测任务

## 正确的输入文件

### 文件列表
| 文件 | 测试结构 | 状态 |
|------|---------|------|
| `af_server_sialyllactose.json` | Sialyllactose (C2 anomeric测试) | ✅ 正确格式 |
| `af_server_lactose.json` | Lactose (基线测试) | ✅ 正确格式 |
| `af_server_m3_nglycan.json` | M3 N-glycan (分支测试) | ✅ 正确格式 |

## 文件格式说明

### AlphaFold Server JSON格式（数组）

```json
[
  {
    "name": "job_name",
    "modelSeeds": [1],
    "sequences": [
      {
        "ligand": {
          "id": "A",
          "ccdCodes": ["SIA", "GAL", "GLC"]
        }
      }
    ],
    "bondedAtomPairs": [
      [["A", 1, "C2"], ["A", 2, "O3"]],
      [["A", 2, "C1"], ["A", 3, "O4"]]
    ]
  }
]
```

### 关键点
1. **顶层是数组** `[...]`，即使只有一个任务
2. **每个任务包含**: name, modelSeeds, sequences, bondedAtomPairs
3. **不需要** `dialect` 和 `version` 字段（AF Server自动处理）

## 使用步骤

### 1. 访问 AlphaFold Server
```
https://alphafoldserver.com
```

### 2. 登录
- 使用Google账号登录

### 3. 上传文件
- 点击 "New Prediction"
- 选择上传JSON文件
- 选择: `af_server_sialyllactose.json` (推荐先测试这个)

### 4. 等待结果
- 预测时间: 数分钟到数小时
- 完成后下载结果

### 5. 分析结果
```bash
# 下载结果后，运行分析脚本
cd /home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides
python scripts/analyze_af3_results.py --input results/alphafold_server_output/
```

## 验证要点

### Sialyllactose (关键测试)
- [ ] Neu5Ac anomeric carbon 在 **C2** (不是C1)
- [ ] SIA-GAL 连接: Alpha(2-3)
- [ ] GAL-GLC 连接: Beta(1-4)

### Lactose (基线)
- [ ] GAL-GLC 连接: Beta(1-4)
- [ ] Galactose C4 hydroxyl axial

### M3 N-glycan (分支)
- [ ] 分支拓扑正确
- [ ] MAN-BMA: Alpha(1-3) 和 Alpha(1-6)
- [ ] BMA-NAG: Beta(1-4)
