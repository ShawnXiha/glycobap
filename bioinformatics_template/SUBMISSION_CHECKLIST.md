# Bioinformatics 期刊投稿清单

## 作者信息
- **作者**: 夏强 (Qiang Xia)
- **单位**: 浙江兴合茶业科技有限公司 (Zhejiang Xinghe Tea Technology Co., Ltd.)
- **邮箱**: xiaqiang@xinghetea.com

---

## 投稿文件清单

### 必需文件
- [x] `paper.tex` - 主LaTeX文件 (已更新作者信息)
- [x] `references.bib` - BibTeX参考文献
- [x] `tables.tex` - LaTeX表格文件
- [x] `cover_letter.tex` - 投稿cover letter
- [x] `compile.sh` - 编译脚本

### 图表文件
- [x] `figures/figure1_pipeline.svg` - 管道架构图
- [x] `figures/figure2_accuracy.svg` - 准确率比较图
- [x] `figures/figure3_timing.svg` - 处理时间比较图

### 投稿前需要完成
- [ ] 将SVG图表转换为TIFF或EPS格式 (300 DPI)
- [ ] 编译LaTeX生成PDF
- [ ] 检查PDF格式和内容
- [ ] 准备Graphical Abstract (可选)
- [ ] 准备作者声明表格

---

## 图表转换说明

### 方法1: 使用Inkscape (推荐)
```bash
# 安装Inkscape
sudo apt-get install inkscape

# 转换为EPS
inkscape figure1_pipeline.svg --export-type=eps --export-filename=figure1_pipeline.eps

# 转换为TIFF (300 DPI)
inkscape figure1_pipeline.svg --export-type=tiff --export-dpi=300 --export-filename=figure1_pipeline.tiff
```

### 方法2: 使用rsvg-convert
```bash
# 安装
sudo apt-get install librsvg2-bin

# 转换
rsvg-convert -f eps -o figure1_pipeline.eps figure1_pipeline.svg
rsvg-convert -f tiff -d 300 -o figure1_pipeline.tiff figure1_pipeline.svg
```

### 方法3: 使用ImageMagick
```bash
# 安装
sudo apt-get install imagemagick

# 转换
convert -density 300 figure1_pipeline.svg figure1_pipeline.eps
convert -density 300 figure1_pipeline.svg figure1_pipeline.tiff
```

---

## LaTeX编译说明

### 编译命令
```bash
cd bioinformatics_template
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
```

### 或使用提供的脚本
```bash
chmod +x compile.sh
./compile.sh
```

---

## 投稿步骤

1. **登录OUP投稿系统**: https://academic.oup.com/bioinformatics
2. **选择文章类型**: Original Paper 或 Application Note
3. **上传文件**:
   - 主文稿PDF
   - LaTeX源文件
   - 图表文件 (TIFF/EPS)
   - Cover Letter
   - 补充材料
4. **填写元数据**:
   - 标题
   - 作者信息
   - 关键词
   - 简介
5. **确认并提交**

---

## 文件状态

| 文件 | 状态 | 说明 |
|------|------|------|
| paper.tex | ✅ 完成 | 作者信息已更新 |
| references.bib | ✅ 完成 | 12条引用 |
| tables.tex | ✅ 完成 | 3个表格 |
| figures/*.svg | ✅ 完成 | 3个SVG图表 |
| cover_letter.tex | ✅ 完成 | 投稿信 |
| compile.sh | ✅ 完成 | 编译脚本 |

---

## 注意事项

1. Bioinformatics要求图表分辨率至少300 DPI
2. 推荐使用矢量格式 (EPS/PDF) 或高质量TIFF
3. LaTeX模板需使用OUP官方模板
4. 补充材料需单独上传

---

生成时间: 2025-01
