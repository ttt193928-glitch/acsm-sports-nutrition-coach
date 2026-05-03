# ACSM Sports Nutrition Coach Skill

一个针对减脂教练小白的运动营养学学习助教技能。

这个仓库把整理的中文课程讲义做成可安装的AI技能，用于帮助学习者按路径学习ACSM运动营养学相关课程内容、做复习、生成表格、把专业概念翻译成作业能讲给客户的话。

## 适合谁

- 零基础或入门阶段的减脂教练
- 想系统学习运动营养学的健身从业者
- 想把课程内容转变成客户沟通话术的教练
- 需要按7天、30天、90天路径学习的人

## 能做什么

- 详细讲解《ACSM运动营养学》：一字不落地输出张珊老师的100多节课内容，包括【教师讲解】【书籍内容】【教师解释/纠偏】【教师补充】
- 制定运动营养学学习计划
- 按主题解释碳水、蛋白质、脂肪、能量、水分、运动代谢、补剂等内容
- 生成复习题、测验和案例题
- 把课程知识转成教练话术
- 提醒疾病、补剂、特殊人群等场景的专业边界

## 安装

技能目录位于：

```text
skills/acsm-sports-nutrition-coach
```

如果您的Codex/Agent客户端支持从本地目录安装技能，可以选择这个目录。

如果使用支持GitHub安装的skill-installer，可以安装仓库中的：

```text
skills/acsm-sports-nutrition-coach
```

## 使用示例

```text
用 $acsm-sports-nutrition-coach 从第01课开始，完整讲解ACSM运动营养学课程。
```

```text
用 $acsm-sports-nutrition-coach 客户问我晚上吃碳水会不会胖，我该怎么解释？
```

```text
用 $acsm-sports-nutrition-coach 帮我给一个70kg想每周减0.5kg的女性客户设计饮食方案。
```

```text
用 $acsm-sports-nutrition-coach 客户问左旋肉碱有没有用，我该怎么回答？
```

## 本地检索

技能内置了一个简单检索脚本：

```bash
cd skills/acsm-sports-nutrition-coach
python3 scripts/search_course.py 碳水 糖原
python3 scripts/search_course.py --limit 20 蛋白质 减脂
```

## 边界声明

本技能是学习资料和教练教育工具，不提供医学诊断、医学治疗或个体化临床营养治疗。

涉及疾病、用药、孕期、未成年人、进食障碍、极端减重、持续症状、特殊人群或补剂剂量时，应转介医生、注册营养师或其他合格专业人士。

## 版权说明

这个仓库开源的是讲师整理的学习路径、教学结构、讲义、测验和教练应用方式，不是 ACSM 原书 PDF，也不应包含原书长段复制内容。

请勿把受版权保护的教材 PDF 或大段教材原文提交到本仓库。

## 仓库结构

```text
.
├── README.md
├── LICENSE
└── skills/
    └── acsm-sports-nutrition-coach/
        ├── SKILL.md
        ├── agents/
        ├── references/
        └── scripts/
```
