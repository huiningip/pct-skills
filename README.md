<sub>🌐 <b>中文</b> · <a href="README.zh-Hant.md">繁體中文</a> · <a href="README.en.md">English</a> · <a href="README.fr.md">Français</a> · <a href="README.es.md">Español</a> · <a href="README.ar.md">العربية</a> · <a href="README.ja.md">日本語</a> · <a href="README.ru.md">Русский</a></sub>

<div align="center">

<img src="logo.png" alt="辉宁知识产权 Hui Ning IP" width="150">

# PCT Skills · PCT 专利实务技能集

> *「一句话问清程序，拿回一份能直接用的 PCT 实务方案。」*
> *"Ask once. Get a filing-ready PCT practice answer."*

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.6.1-blue.svg)](https://github.com/huiningip/PCT-SKILLS)
[![Agent-Agnostic](https://img.shields.io/badge/Agent-Agnostic-blueviolet)](#装上就能用)
[![PCT Members](https://img.shields.io/badge/PCT%20Members-159-green)](https://www.wipo.int/treaties/en/registration/pct/)
![No-Fabrication](https://img.shields.io/badge/Principle-No--Fabrication-orange)

<br>

**一个面向涉外专利代理师、企业 IPR 与涉外申请人的 PCT 国际申请全流程实务技能集（母技能 + 5 个子技能）。**

<br>

不是科普问答，而是：流程与期限的检查路径、逐条可核的法源依据、检索与审查结论的解读方法、国家阶段进入与恢复的手续方案。

技能遵循通用 Agent Skills 格式（`<skill-name>/SKILL.md`），支持 skills 的 agent 均可使用。

[能做什么](#能做什么) · [装上就能用](#装上就能用) · [核心机制](#核心机制) · [仓库结构](#仓库结构) · [能力边界](#能力边界)

</div>

---

## 装上就能用

### 方式一：同步脚本（推荐）

```bash
# Windows
py -3 scripts/sync_to_local.py

# macOS / Linux
python3 scripts/sync_to_local.py

# 常用参数
py -3 scripts/sync_to_local.py --dry-run                    # 预演，不写入
py -3 scripts/sync_to_local.py --target D:/path/to/skills   # 指定技能目录
```

脚本把 `skills/` 下 6 个技能单向同步到本地技能目录（默认 `~/.workbuddy/skills`）：新增/变更文件覆盖写入、陈旧文件清除，**本机元数据（`_user_meta.json` 等）自动保留**。

### 方式二：手动复制

把 `skills/` 下需要的技能目录整体复制到你的技能目录（如 `~/.workbuddy/skills/`），然后重启或重载应用。

> ⚠️ 这是多文件技能集：`references/` 下的大部头原文（条约、实施细则、行政规程、检索审查标准等）由 `SKILL.md` 以 `@` 相对路径引用，**缺一即断链**——请整目录复制，勿只取 `SKILL.md`。

## 能做什么

| 技能 | 定位 | 说明 |
|------|------|------|
| [`pct-guide`](skills/pct-guide) | 母技能 | 路由中枢：按问题自动分派五大实务领域，跨技能协调 |
| [`pct-treaty`](skills/pct-treaty) | 法源层 | 条约与实施细则、费用标准、声明保留——全族法源基准 |
| [`pct-international-phase`](skills/pct-international-phase) | 国际阶段 | 提交、受理、检索、公布、第 19 条修改、第 II 章初审 |
| [`pct-national-phase`](skills/pct-national-phase) | 国家阶段 | 进入期限与手续、权利恢复、PPH 与后续程序 |
| [`pct-search-examination`](skills/pct-search-examination) | 检索审查 | ISR／书面意见／IPER 解读、最低文献、发明单一性 |
| [`pct-administrative`](skills/pct-administrative) | 操作规范 | 行政规程（AI）、受理局指南、ePCT 与表格 |

## 核心机制

1. **母技能路由**：任意入口提问，`pct-guide` 先判定领域，再调用对应子技能；
2. **法源单点维护**：条约、细则、费用等动态数据统一收敛在 `pct-treaty`，避免多处口径漂移；
3. **渐进式披露**：大部头原文放在 `references/`，按需加载，不撑上下文；
4. **查不到就回「无」**：无把握的信息直接标注，不编造条款、期限与费用数字。

## 仓库结构

```text
PCT-SKILLS/
├── skills/                    # 6 个技能（母 + 5 子）
│   ├── pct-guide/             #   母技能：路由中枢
│   ├── pct-treaty/            #   法源层
│   ├── pct-international-phase/
│   ├── pct-national-phase/
│   ├── pct-search-examination/
│   └── pct-administrative/
├── scripts/
│   └── sync_to_local.py       # 一键同步到本地技能目录
├── README.md                        # 简体中文（本文件 · 默认）
├── README.zh-Hant.md                # 繁體中文
├── README.en.md                     # English
├── README.fr.md                     # Français
├── README.es.md                     # Español
├── README.ar.md                     # العربية（RTL）
├── README.ja.md                     # 日本語
├── README.ru.md                     # Русский
├── LICENSE                          # MIT 许可证
└── logo.png                         # 品牌标识（README 首屏）
```

- 技能目录严格 **2 级**（`SKILL.md` + `references/`），符合 WorkBuddy 官方技能结构规范；
- 技能文件约定：**CRLF、UTF-8 无 BOM**。

## 数据与时效

- 法源以 **WIPO / CNIPA 官方现行版本**为准，各技能内标注法源基准日；
- 易变数据（费用、期限）请以官方最新公告复核后再用于案卷；
- 输出为实务参考，**不构成法律意见**。

## 能力边界

- 不替代官方与个案判断：期限、费用与程序结论以受理局通知与官方公告为准；
- 不做编造：查不到的数据直接回「无」；
- 法源聚焦 PCT 条约与规程层面；各指定局本国实体法与审查实务以其官方口径为准。

## License

[MIT](LICENSE) © 2026 辉宁知识产权（Hui Ning IP）。

- 技能自身内容（`SKILL.md`、`references/` 内的整理与注释）适用 MIT；
- `references/` 中收录／转引的 WIPO 官方文本（条约、实施细则、行政规程等）版权归 WIPO 所有，不受本协议覆盖。

## 联系

- 问题与建议：欢迎在仓库提 Issue；
- 由 辉宁知识产权（中国专利代理师团队）构建与维护。
