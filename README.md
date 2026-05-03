# ACSM Sports Nutrition Coach Skill

张珊老师的ACSM运动营养学完整课程（100+节课），做成AI助教，一字不落地还原讲课内容。

## 适合谁

- 想完整学习张珊老师ACSM运动营养学课程的学员
- 需要按照100多节课的原始顺序系统学习的人
- 希望听到老师原话、书中内容、讲师纠偏的完整讲解
- 减脂教练、健身从业者想系统学习运动营养学

## 能做什么

- **完整讲课**：一字不落地输出张珊老师的100多节课内容，包括【讲师原话】【书中内容】【讲师解释/纠偏】【讲师补充】
- **按课程顺序学习**：从第01课开始，逐课学习，不跳过任何内容
- **答疑解惑**：根据课程内容回答具体问题，引用老师的原话和纠偏
- **生成测验**：基于已学课程生成复习题
- **安全边界提醒**：涉及疾病、用药、特殊人群时提醒转介

## 安装

Skill 目录位于：

```text
skills/acsm-sports-nutrition-coach
```

如果你的 Codex/Agent 客户端支持从本地目录安装 Skill，可以选择这个目录。

如果使用支持 GitHub 安装的 skill-installer，可以安装仓库中的：

```text
skills/acsm-sports-nutrition-coach
```

## 使用示例

```text
用 $acsm-sports-nutrition-coach 给一个零基础减脂教练安排 30 天学习计划。
```

```text
用 $acsm-sports-nutrition-coach 解释一下碳水和减脂的关系，并生成 5 道复习题。
```

```text
用 $acsm-sports-nutrition-coach 帮我把蛋白质摄入讲成客户能听懂的话。
```

```text
用 $acsm-sports-nutrition-coach 讲讲补剂，但要标出哪些不能给客户承诺。
```

## 本地检索

Skill 内置了一个简单检索脚本：

```bash
cd skills/acsm-sports-nutrition-coach
python3 scripts/search_course.py 碳水 糖原
python3 scripts/search_course.py --limit 20 蛋白质 减脂
```

## 边界声明

本 Skill 是学习资料和教练教育工具，不提供医学诊断、医学治疗或个体化临床营养治疗。

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
