# PM Expert Skills · 专家分析级产品实战工具包

<p align="center">
  <b>产品经理的 AI 时代工具包</b><br>
  深度分析 + 质量控制 + 项目管理 + 认知校准
</p>

<p align="center">
  <a href="#-快速开始"><b>快速开始</b></a> •
  <a href="#-四个-skill"><b>四个 Skill</b></a> •
  <a href="#-适用场景"><b>适用场景</b></a> •
  <a href="#-为什么值得收藏"><b>为什么值得收藏</b></a> •
  <a href="#-安装"><b>安装</b></a>
</p>

---

## 🎯 这个项目解决什么问题

AI 生成内容越来越普遍，但产品经理面临三个核心痛点：

| 痛点 | 表现 | 这个工具包怎么解决 |
|------|------|------------------|
| **分析没有深度** | AI 输出的报告堆数据、没有判断、像模板填空 | `deep-analysis-report` 提供 30 项质量门禁 + 四层结构方法论 |
| **质量不可衡量** | 你觉得不好，但说不清哪里不好，架构师不知道改什么 | `ai-quality-checker` 提供 26 项门禁 + 评分标准 + 团队校准机制 |
| **AI agent 管理没流程** | 需求、开发、验收、迭代一团乱，PM 不知道自己的角色 | `pm-practice-management` 提供全流程管理工具 + 验收模板 |
| **输入未经校准** | AI 很快开始产出，但目标、证据和边界还没说清 | `cognitive-lead` 先核对材料，再给带置信度和反例的判断 |

**一句话：把输入、分析、管理和质量检查连成一套可复用的 PM 工作工具。**

---

## 📦 四个 Skill

### 1. deep-analysis-report · 深度分析报告

> 把原始材料和数据，转化为面向决策者的分析产品。

从商业分析、行业研究到战略咨询、竞争分析——任何需要"先判断、后数据、证据可审计"的场景。抽象自高级咨询分析师方法论，去除了特定领域术语，保留完整的判断框架。

**核心能力：**
- 四层结构（决策层 → 分析层 → 监测层 → 审计层）
- 产品基线六问闭环
- 30 项质量门禁覆盖全流程
- 自循环审查顺序

```text
定位是否准确 → 产品基线是否闭环 → 章节是否服务决策
  → 强判断是否有支撑 → 风险是否越界 → 表达是否专业 → 附录是否可审计
```

→ [查看详情](skills/deep-analysis-report/SKILL.md)

---

### 2. ai-quality-checker · 质量检查器

> 让 AI 输出可衡量、可验收、可复现。

专为产品经理设计的内容质量检查工具。覆盖 PRD、策略文档、分析报告、决策文档等 PM 全场景输出。

**核心能力：**
- 7 层 26 项 PM 专用质量门禁
- 3 档检查深度（快速 2min / 标准 5min / 完整 15min）
- 团队一致性机制（校准会议、分歧仲裁、质量追踪）
- 集成行业最佳实践（NIST AI RMF、Anthropic Evaluation Framework）

→ [查看详情](skills/ai-quality-checker/SKILL.md)

---

### 3. pm-practice-management · 实战管理方法论

> 产品经理的 AI Agent 开发管理手册。

不是技术文档，而是 PM 的实操手册——管理 AI 产品从定义到交付的全过程。

**核心能力：**
- Skill 开发全流程（需求 → 开发 → 验证 → 发布 → 迭代）
- 5 套实战工具（PRD 模板、测试用例、版本日志、验收标准、团队校准）
- 三层结构方法论（产品本体 + 管理文档 + 质量闸门）
- 常见陷阱和避坑指南

→ [查看详情](skills/pm-practice-management/SKILL.md)

---

### 4. cognitive-lead · 认知校准

> 在开始产出前，先把目标、证据、边界和反例说清楚。

适用于需要做决定、设计方案或准备对外表达的任务。它先核对材料，再给出带置信度、依据和反例的判断，并把输入改写成可观察的验收标准。

**核心能力：**
- 把事实、推断和未知分开，并为材料结论标出来源
- 用置信度与可观察的反例校准判断
- 通过开放式提问补齐真实例子、代价、边界和验收条件
- 可选的决策日志工具，支持到期复查与 Brier 分计算

→ [查看详情](skills/cognitive-lead/SKILL.md)

---

## 🔗 四个 Skill 的关系

```text
需求和证据
    │
    ▼
cognitive-lead ── 明确目标与验收标准
    │
    ├── pm-practice-management ── 管理交付流程
    ├── deep-analysis-report ──── 生成分析内容
    └── ai-quality-checker ────── 检查输出质量
```

四个 skill 可独立使用，也可按任务组合：先用 `cognitive-lead` 明确目标与证据，再由 `pm-practice-management` 管理交付过程，使用 `deep-analysis-report` 产出分析，最后交给 `ai-quality-checker` 检查质量。

---

## 🚀 快速开始

### 前提

- Claude Code（命令行版本）
- macOS 或 Linux（Windows 用户可在 WSL 中使用）

### 安装单个 Skill

```bash
# 安装深度分析报告 skill
cp -r skills/deep-analysis-report ~/.claude/skills/deep-analysis-report

# 安装质量检查器
cp -r skills/ai-quality-checker ~/.claude/skills/ai-quality-checker

# 安装实战管理方法论
cp -r skills/pm-practice-management ~/.claude/skills/pm-practice-management

# 安装认知校准
cp -r skills/cognitive-lead ~/.claude/skills/cognitive-lead
```

### 使用

重启 Claude Code 后，通过 slash command 调用：

```bash
# 生成深度分析报告
/deep-analysis-report 分析新能源车市场竞争格局

# 检查 PM 文档质量
/ai-quality-checker 帮我检查这份 PRD

# 查看管理方法论
/pm-practice-management 如何开始一个新 skill 项目？

# 校准目标、依据与边界
/cognitive-lead 帮我判断这个产品方向是否值得做
```

---

## 🎬 适用场景

| 场景 | 用什么 skill | 效果 |
|------|------------|------|
| 写 PRD / 产品需求文档 | ai-quality-checker | 检查问题定义、scope 纪律、metrics、风险 |
| 做竞品分析 / 市场研究 | deep-analysis-report | 结构化分析框架，从数据到判断闭环 |
| 管理 AI agent 开发项目 | pm-practice-management | 从需求到验收的完整流程 |
| 团队统一输出标准 | ai-quality-checker + 校准会议 | 消除评分差异，统一质量标准 |
| 向高管汇报分析结论 | deep-analysis-report | 先判断后数据，读者一眼看到核心结论 |
| 任务目标和证据还不清楚 | cognitive-lead | 先核实材料、明确反例和可观察的验收标准 |

---

## ⭐ 为什么值得收藏

- **实战验证**：非理论框架，来自真实产品团队的经验提炼
- **可立即落地**：安装即用，每个 skill 有完整参考文件和示例
- **工程化就绪**：验收标准模板、测试用例格式、版本日志规范——直接给架构师用
- **行业最佳实践**：融合 NIST AI RMF、Anthropic Evaluation Framework 等权威来源
- **团队一致性保障**：校准会议、分歧仲裁、质量追踪机制，解决"标准不统一"问题

---

## 📁 项目结构

```text
pm-expert-skills/
├── README.md
├── LICENSE
│
├── skills/
│   ├── deep-analysis-report/          # 深度分析报告方法论
│   │   ├── SKILL.md
│   │   ├── references/                # 设计原则、质量门禁、分析规则等
│   │   └── agents/                    # 跨平台配置
│   │
│   ├── ai-quality-checker/            # PM 质量检查器
│   │   ├── SKILL.md
│   │   └── references/                # 门禁详解、写作规范、团队校准等
│   │
│   ├── pm-practice-management/       # PM 实战管理方法论
│   │   ├── SKILL.md
│   │   └── references/                # 模板和示例
│   │
│   └── cognitive-lead/               # 认知校准与决策记录
│       ├── SKILL.md
│       ├── references/
│       └── scripts/                  # 决策日志与校准分工具
│
└── docs/                              # 通用文档
    └── acceptance-standard-template.md # 验收标准填空模板
```

---

## 🤝 如何贡献

1. Fork 这个仓库
2. 创建你的分支（`git checkout -b feature/xxx`）
3. 提交你的修改（`git commit -m 'feat: xxx'`）
4. 推送到分支（`git push origin feature/xxx`）
5. 创建一个 Pull Request

---

## 📄 License

MIT © you

---

<p align="center">
  <b>如果这个项目对你有帮助，点个 ⭐ 让更多人看到</b>
</p>
