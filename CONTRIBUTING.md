# Contributing

欢迎改进这个 Skill，但请遵守以下原则。

## 内容原则

- 保留教练教育定位。
- 优先补充讲师原创解释、案例、测验、学习路径和教练话术。
- 涉及疾病、补剂、特殊人群时，必须保留安全边界。
- 不提交 ACSM 原书 PDF、扫描件、视频、音频或长段教材原文。

## Skill 文件原则

- `skills/acsm-sports-nutrition-coach/SKILL.md` 保持简洁，只放核心工作流。
- 大段课程资料放在 `references/`。
- 可重复、确定性的操作放在 `scripts/`。
- 不在 Skill 目录里新增无关说明文件。

## 验证

提交前至少运行：

```bash
cd skills/acsm-sports-nutrition-coach
python3 scripts/search_course.py --limit 5 碳水
python3 scripts/search_course.py --limit 5 蛋白质
```
