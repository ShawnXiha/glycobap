# AlphaFold Server Web界面使用指南

## 重要发现

**AlphaFold Server (alphafoldserver.com) 不支持直接提交Glycan结构！**

根据AF3文档：
> "If the JSON in `alphafoldserver` format specifies glycans, the converter will raise an error."

这意味着：
- AlphaFold Server Web界面无法直接处理glycan
- Glycan需要通过`alphafold3`格式（本地AF3）处理
- 需要找到其他验证方法

---

## 替代验证方案

### 方案A: 使用已有的PDB Glycan结构

从PDB数据库中查找已解析的glycan结构进行对比验证。

**步骤：**
1. 查找PDB中包含glycan的结构
2. 提取glycan的stereochemistry信息
3. 与GlycoSMILES2BAP输出对比

**推荐PDB结构：**
| PDB ID | Glycan类型 | 说明 |
|--------|-----------|------|
| 5NSC | Fucosylated | 文献中报道有错误的案例 |
| 5K65 | N-glycan | 缺失linkage案例 |
| 1JND | N-glycan | 高质量N-glycan结构 |
| 2WMF | O-glycan | O-glycan参考结构 |

### 方案B: 使用Privateer进行结构验证

Privateer是专门验证glycan stereochemistry的工具。

**安装：**
```bash
# 通过pip安装
pip install privateer

# 或通过conda
conda install -c ccdc ccdc-privateer
```

**验证内容：**
- Anomeric configuration (α/β)
- Absolute configuration (D/L)
- Ring puckering
- Linkage geometry

### 方案C: 使用已知正确结构进行对比

**数据来源：**
- GlyTouCan数据库
- Glycosciences.de
- PDB中已验证的glycan结构

---

## 下一步行动

1. **立即可行**: 从PDB下载已知glycan结构
2. **使用Privateer**: 验证这些结构的stereochemistry
3. **对比**: 与GlycoSMILES2BAP的预期输出对比

---

## 执行脚本

```bash
# 下载PDB结构
cd /home/qiang/project/foodsci/polysaccharides/AF3_polysaccharides
mkdir -p data/pdb_structures

# 下载关键PDB文件
wget -P data/pdb_structures https://files.rcsb.org/download/5NSC.pdb
wget -P data/pdb_structures https://files.rcsb.org/download/5K65.pdb
wget -P data/pdb_structures https://files.rcsb.org/download/1JND.pdb

# 运行Privateer验证
python scripts/privateer_validation.py --input data/pdb_structures/
```
