# Paper Planning: F12 & F3 - Timeline & Handoff

## 四、Timeline

### 4周实施计划

| 周次 | F12任务 | F3任务 | 交付物 |
|------|---------|--------|--------|
| **Week 1** | 文献调研，收集10+错误案例 | GlyTouCan数据导出，子集选择 | 案例列表，1000糖链清单 |
| **Week 2** | 错误纠正验证，计算纠正率 | 批量处理，性能测试 | 纠正率数据，性能统计 |
| **Week 3** | 撰写F12章节草稿 | 数据库构建，撰写F3草稿 | 两个章节初稿 |
| **Week 4** | 整合到论文，审阅修改 | 整合到论文，审阅修改 | 完整论文更新 |

### 关键里程碑

```
Day 7: 完成10+文献案例收集
Day 14: 完成F12纠正验证 + F3批量处理
Day 21: 完成两个章节初稿
Day 28: 完成论文整合和审阅
```

---

## 五、Handoff Checklist

### 传递给paper-writing的artifacts

| Artifact | 来源 | 用途 |
|----------|------|------|
| Story summary (F12) | Section 1 | Case Study 3写作 |
| Story summary (F3) | Section 1 | Case Study 4写作 |
| Experiment plan | Section 2 | Experiments章节扩展 |
| Figure sketches | Section 3 | 图表制作 |
| Claim statements | Section 1 | Abstract/Introduction更新 |
| Rejection-risk table | Section 1 | 自我审查参考 |

---

## 六、论文结构更新

### 更新后的论文结构

```
Title: GlycoSMILES2BAP: Automated Conversion of Glycan Notations 
       to AlphaFold 3-Compatible Format

Abstract [更新]
- 添加应用价值声明

1. Introduction [更新]
- 添加应用场景段落

2. Methods [保持]
- 已完整

3. Results [扩展]
- 3.1 Benchmark Results [已有]
- 3.2 Ablation Study [已有]
- 3.3 Case Studies [扩展]
  - 3.3.1 Case Study 1: Linear N-Glycan [已有]
  - 3.3.2 Case Study 2: Branched N-Glycan [已有]
  - 3.3.3 Case Study 3: Error Correction Examples [新增F12]
  - 3.3.4 Case Study 4: GlyTouCan Database [新增F3]

4. Discussion [更新]
- 添加应用价值讨论
- 添加局限性更新

5. Conclusion [更新]
- 添加应用贡献总结

Supplementary Materials [新增]
- S1: Complete Error Correction Cases
- S2: GlyTouCan Database Documentation
```

---

## 七、资源需求评估

### F12资源需求

| 资源类型 | 需求 | 可获得性 |
|----------|------|----------|
| 文献访问 | PubMed/Google Scholar | ✓ 已有 |
| 计算资源 | CPU，<1小时 | ✓ 已有 |
| 时间投入 | 约40小时 | ✓ 可行 |

### F3资源需求

| 资源类型 | 需求 | 可获得性 |
|----------|------|----------|
| 数据来源 | GlyTouCan公开数据 | ✓ 已有 |
| 计算资源 | CPU，约2小时(1000结构) | ✓ 已有 |
| 存储空间 | 约100MB | ✓ 已有 |
| 时间投入 | 约30小时 | ✓ 可行 |

---

## 八、风险评估

| 风险 | 可能性 | 影响 | 缓解措施 |
|------|--------|------|----------|
| 文献案例收集不足 | 中 | 高 | 扩展搜索范围，包括用户手册错误 |
| 批量处理失败率高 | 低 | 中 | 先测试100个，再扩展到1000 |
| 审稿人认为贡献不足 | 中 | 高 | 强调应用价值而非方法创新 |

---

## 九、成功标准

### F12成功标准

- [ ] 收集≥10个文献报告的错误案例
- [ ] 错误纠正率≥80%
- [ ] 覆盖所有3类错误类型
- [ ] 有置信区间估计

### F3成功标准

- [ ] 成功处理≥950个糖链(95%成功率)
- [ ] 平均处理时间<1s/结构
