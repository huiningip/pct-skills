---
name: pct-guide
display_name: PCT全流程实务
display_name_en: PCT Full-Process Practice
description: PCT（专利合作条约）全流程实务母技能。统一入口，智能路由至5个子技能（treaty/international-phase/national-phase/search-examination/administrative），覆盖条约法律框架、国际阶段、国家阶段、检索审查标准、行政规程全流程。触发词：PCT、专利合作条约、PCT申请、PCT流程、PCT全流程、PCT费用、PCT期限、进入国家阶段、国际检索、国际公布、PCT子技能
description_zh: PCT 实务统一入口。以 PCT 国际阶段程序为主体、各缔约国通用，中国衔接为可选环节；按「条约 → 实施细则 → 行政规程」三层级与「国际阶段 → 国家阶段 → 行政程序」三流程做智能路由，分发至 pct-treaty / pct-international-phase / pct-national-phase / pct-search-examination / pct-administrative 五个子技能，并协调跨子技能调用链；涉及 PCT 进入中国国家阶段（可选环节）时联动 patent-exam-pct-national。母技能自身不深度展开任何单一法规文件。
description_en: Unified entry point for PCT practice, centred on the international phase and common to all Contracting States, with the Chinese national phase handled as an optional link. Routes a query by legal hierarchy (Treaty → Regulations → Administrative Instructions) and by procedural stage (international phase → national phase → administrative procedures) to five sub-skills, and coordinates cross-skill chains; escalates to patent-exam-pct-national when entry into the Chinese national phase (optional link) is involved. The parent skill itself does not expand any single legal instrument in depth.
category: legal
version: "2.6.1"
author: 辉宁知识产权
# allowed-tools：（选填）本技能为路由中枢，运行期需读取各子技能 SKILL.md 并可能转发至 patseek / iphouse 等 MCP 工具；
#   按官方开发文档，设白名单会切断未列出的工具调用（同 hague-design-system / trademark-infringement-analysis 处置），故不启用。
agent_created: true
tags: [pct, guide, router, wipo, full-process]
parent-skill: null
related-skills:
  - pct-treaty: 条约与实施细则法律基础层（法源支撑）
  - pct-international-phase: 国际阶段实务（提交/检索/公布/第II章）
  - pct-national-phase: 国家阶段实务（进入手续与后续程序）
  - pct-search-examination: ISPE 检索审查标准
  - pct-administrative: 行政规程与受理局实务
  - patent-exam-pct-national: 进入中国国家阶段的审查标准（中国审查指南第三部分）
  - patent-examination-guide: 中国审查指南全流程母技能（关联家族，含 PCT 国家阶段审查子技能）
  - ip-management-compliance: ISO 56005 IP 管理体系层面的 PCT 布局决策
update-log: |
  2.6.1 (2026-09-28) 版本号家族统一：由 2.1.5 统一至 **2.6.1**（全家族 6 技能同版本号，对齐 pct-treaty 基准，
    便于技能包整体发布与同步维护）；本次不涉及内容修订，历史修订见下方条目。
  2.1.5 (2026-09-28) 国际化定位改造（对标 madrid-trademark 模式）：角色段增设「主体｜国际阶段通用（各缔约国
    一致）／可选｜中国衔接环节」双板块声明；规则第 7 条由「必联动」改为「可选环节（按需联动）」并新增第 10 条
    「缔约国中立（office-neutral）」；「使用方式总则」原「自动联动中国审查指南」改为「按需联动（可选环节）」；
    双语 description 补入「以国际阶段程序为主体、各缔约国通用，中国衔接为可选环节」。
  2.1.4 (2026-09-27) 表述精度修正（跨家族定位）：删除对 patent-examination-guide 的三处「上位」定位
    （related-skills／「上下文·外部联动」段／「外部技能联动」表）——审查指南属中国国内法体系，并非
    PCT 审查标准的「上位」（PCT 标准法源上位为条约/细则），且对方已明确不覆盖国际阶段程序；
    三处统一改为「关联家族（其子技能 patent-exam-pct-national 负责进入中国国家阶段的审查）」。
  2.1.3 (2026-09-26) 跨家族联动修正（IP 管理家族方向）：
    - 「典型联动场景」"PCT国际布局策略"链路由直接引用对方子技能（ip-mgmt-strategy → ip-mgmt-innovation）
      统一为母技能层级：pct-guide → ip-management-compliance（其内部路由再分派 ip-mgmt-strategy／
      ip-mgmt-innovation）；同时在对方 linkage-rules.yaml 新增 CL-009 规则（ip-mgmt-innovation → pct-guide，
      PCT 国际阶段程序），双向引用闭合。
  2.1.2 (2026-09-26) 第二轮复查（族内一致性，对齐子技能权威表述）：
    - ★ 数字口径统一：「快速参考卡片」发明单一性判断删除无据的「50+」前缀，统一为
      「48个示例（2026版ISPE/14 Ch.10，编号1–48）」，与 pct-search-examination 2.3.2 保持一致；
    - ★ 路由补词：「路由关键词映射」新增「ISA 协议、IPEA 协议、EPO 试点、中欧 PCT 试点」条目
      （指向 pct-international-phase 附录B／附录D）；「国际检索」行补英文触发词 written opinion，
      与 pct-search-examination 触发词对齐。
  2.1.1 (2026-09-21) 移除非官方的跨技能伪语法（原 2 处，字面写法全文清零）：
    - 官方技能开发文档仅定义 `@references/` 作为文件引用语法（且仅限引用技能目录内文件），原使用的
      「以 @ 前缀调用技能」写法不在其定义范围内；
      「使用方式总则」第 4 条改为「以技能名显式调用子技能」，「失败模式与恢复」兜底行的建议调用说明同步改为
      技能名形式；跨技能调用一律以技能名显式发起，不使用任何伪语法；
    - 同类语法尚存于 patent-examination-guide / us-trademark-law，经用户确认由其自行修改，本技能不代改。
  2.1.0 (2026-09-21) 按官方技能开发文档（open.workbuddy.cn/docs/skill）合规化：
    - frontmatter 补齐文档列明的字段：display_name / display_name_en / description_zh / description_en / category，并补 related-skills 联动声明；
    - 载明 allowed-tools 未启用的理由（路由中枢须保留子技能加载与 MCP 工具调用能力）；
    - 标题层级修正：原「技能知识库」误用同级 H1（全文出现两个 H1），降为 H2 并同步下移各级子标题；
    - 失同步条目修复（对齐子技能权威表述）：
      ★★「快速参考卡片」发明单一性判断原写"43个案例指南"→更正为"50+示例（2026版 ISPE/14 Ch.10 含 48 个 Example，编号 1–48）"，与 pct-search-examination 2.2.0 的全局修正保持一致；
      ★「细则结构映射」Part 6 原写"各章通用细则"→更正为"有关条约各章的细则"（pct-treaty 2.4.0 已订正）；
      ★「PCT时限计算器」补明其为 WIPO ePCT 在线工具（pct-treaty 已载明链接与免责声明）；
      ★ PATENTSCOPE 路由补双通道：工具操作指南在 pct-international-phase（附录C 速查版），检索标准/策略在 pct-search-examination，修正原单一指向。
  2.0.0 (2026-08-22) 家族重构：确立「母技能 + 5 子技能」架构，母技能退化为纯路由层。
---

# PCT全流程实务（母技能）

## 角色

本技能是 **PCT（专利合作条约）全流程实务**的统一入口，采用「母技能 + 5 个独立子技能」架构。母技能承担**智能路由**与**跨子技能协调**职责，自身不深度展开任何单一法规文件，而是将查询精准分发到对应子技能。

**国际化定位（双板块）**：
- **主体｜国际阶段通用（各缔约国一致）**：PCT 是服务全体缔约国的国际条约体系——条约与实施细则、国际阶段程序（提交／检索／公布／第II章）、行政规程与 ISPE 审查标准，**对任一缔约国的从业者一律通用**，不因申请人国籍、代理人所在地或受理局而异；境外知识产权律师与专利工作者可直接使用，无需中国语境。
- **可选｜中国衔接环节**：涉及 PCT 进入中国国家阶段（中国审查指南适用）时，**按需**联动 `patent-exam-pct-national`——该环节为**可选分支而非主线**，非中国业务可整体跳过；进入其他缔约国国家阶段由 `pct-national-phase` 按国别通用处理。

## 任务

- 解析用户 PCT 相关问题，判定所属流程阶段与法规层级。
- 按路由关键词映射将查询分发至 5 个子技能之一（或跨技能协调链）。
- 复核法规层级完整性（条约 → 细则 → 行政规程，不可跳跃）。
- 子技能不可用时执行降级兜底，以母技能自身知识回答。
- 向用户交付**符合输出格式规范**的结构化分析结论。

## 上下文（背景数据）

本技能所依托的法规文件体系（各子技能分别管辖）：

- 《专利合作条约》(PCT) 69条 — 基本条约 → `pct-treaty`
- 《PCT实施细则》96条 + 费用表 — 次级立法 → `pct-treaty`
- 《PCT行政规程》8部分 + 8附件 — 操作规范 → `pct-administrative`
- 《PCT国际检索和初步审查指南》(ISPE) 8部分22章 — 检索审查标准 → `pct-search-examination`
- 《PCT申请人指南-国际阶段》 — 国际阶段实务 → `pct-international-phase`
- 《PCT申请人指南-国家阶段》 — 国家阶段实务 → `pct-national-phase`
- 《PCT受理局指南》19章 — 受理局操作 → `pct-administrative`

**法规层级（最高准据原则）**：

```
PCT条约（基本法）
   ↓ Art.58 授权
PCT实施细则（次级立法）
   ↓ Art.58(4)+Rule 89.2 授权
PCT行政规程（操作规范）
```

层级不可跳跃引用：输出引用链必须为「条约第X条 → 细则第X条 → 行政规程第XXX节（如适用）」。

**外部联动**：
- `patent-exam-pct-national`：PCT 进入中国国家阶段的审查标准（细则 + 审查指南第三部分双重适用）。
- `patent-examination-guide`：中国专利审查指南全流程母技能（关联家族，含 PCT 国家阶段审查子技能）。
- `ip-management-compliance`：ISO 56005 IP 管理体系层面的 PCT 布局决策。

## 流程（步骤）

处理用户请求按以下步骤执行：

1. **解析请求**：确定①涉及 PCT 哪个流程阶段（国际阶段/国家阶段/行政程序）②是否需要法条引用 ③是否涉及检索审查标准。
2. **路由匹配**：对照「路由关键词映射」确定目标子技能。
3. **加载子技能**：加载目标子技能 SKILL.md 获取详细规则。
4. **法规层级验证**：补充完整引用链（条约条文 + 实施细则条文 + 行政规程节号），确认版本适用（以生效日为准）。
5. **输出组装**：按输出格式规范组织交付文本（法规依据 → 实务标准 → 操作要点 → 版本提示）。
6. **降级兜底**：子技能不可用 → 母技能自身知识回答 + 列出可用子技能。

> 🔴 **CHECKPOINT 1**：请求能否匹配路由关键词？匹配 → 加载对应子技能；模糊 → 输出 2-3 个候选子技能让用户确认；不匹配 → 降级兜底。
> 🔴 **CHECKPOINT 2**：输出前是否完成法规层级验证（引用链完整、版本适用明确）？

## 规则（约束/边界）

1. **法规层级不可跳跃**：引用必须按「条约 → 细则 → 行政规程」顺序，禁止跳过条约直接引用细则/行政规程。
2. **PCT 体系与中国专利法不可混用**：PCT 是独立国际条约体系；涉及进入中国国家阶段时才联动 `patent-exam-pct-national`。
3. **PCT 国际阶段不授权**：国际检索/初步审查仅提供意见，对各国无约束力，不得表述为"国际授权"。
4. **版本适用确认**：2026 年 1 月 1 日生效的版本（PCT/AI/26、ISPE/14）适用于该日及之后的申请和操作；引用前确认生效日期。
5. **无优先权日不输出具体日期**：用户未提供优先权日时，仅输出期限长度与起算规则，不输出具体日历日；必要时提示补充。
6. **跨技能冲突处理**：子技能结论冲突时以《PCT条约》+《实施细则》为最高准据对齐。
7. **中国国家阶段为可选环节（按需联动）**：涉及 PCT 进入中国国家阶段（中国审查指南适用）时，显式转 `patent-exam-pct-national`；非中国国家阶段事务不触发该联动。
8. **输出硬约束（对用户交付文本）**：
   - **严禁输出任何 Markdown 表格**；
   - **如果找不到数据，直接回复"无"，严禁编造**。
9. 本技能内部知识库（参考/指引内容）不受第 8 条"禁表格"约束，可保留 Markdown 表格作为知识载体。
10. **缔约国中立（office-neutral）**：本家族以国际阶段程序为主体，表述保持缔约国中立——除明确标注「中国 / CNIPA」的（可选）内容外，其余内容适用于任一缔约国的从业者（含境外律师与专利工作者）。

## 输出格式

向用户交付的分析结论**严禁使用 Markdown 表格**，须用标题 + 列表组织，标准结构如下：

```markdown
## [PCT阶段/主题] 分析结论

### 法规依据
- 《专利合作条约》第X条第Y款
- 《PCT实施细则》第X条
- 《PCT行政规程》第XXX节（如适用）

### 实务标准
[具体实务标准]

### 操作要点
[可执行步骤，用编号列表]

### 版本提示
[如适用，标注生效日期]

### 风险提示
[常见错误和注意事项]
```

**找不到数据时**：直接回复"无"，不得编造、推测或拼接无关内容。

---

## 技能知识库（内部参考，不受输出禁表格约束）

### 快速参考卡片（路由）

| 我想查询... | 应使用 | 一句话说明 |
|-----------|--------|----------|
| PCT条约条文 / 细则编号 | `pct-treaty` | 条约69条+细则96条完整框架 |
| 如何提交PCT国际申请 | `pct-international-phase` | 请求书填写、受理局、申请日 |
| 国际检索报告解读 | `pct-search-examination` | ISR、书面意见、引用分类(X/Y/A) |
| 进入国家阶段手续 | `pct-national-phase` | 30个月期限、译文、费用、特殊要求 |
| PCT表格 / ePCT系统 | `pct-administrative` | 表格体系、受理局操作、电子申请 |
| 国际初步审查 | `pct-search-examination` | 第II章、要求书、IPER |
| 发明单一性判断 | `pct-search-examination` | 48个示例（2026版ISPE/14 Ch.10，编号1–48） |
| 优先权恢复 | `pct-administrative` | 故意性标准/适当注意标准 |
| 序列表(ST.26) | `pct-administrative` | WIPO标准ST.26要求 |
| 补充国际检索 | `pct-international-phase` | SISA、可选检索 |
| 第三方观察 | `pct-administrative` | 第三方提交意见（法源：行政规程Part 8） |
| PCT时限计算 | `pct-treaty`（工具：WIPO ePCT 在线时限计算器） | 输入优先权日等自动计算各关键期限 |
| PATENTSCOPE检索 | `pct-international-phase`（用户指南速查·附录C）/ `pct-search-examination`（检索标准与策略） | 查询PCT公开文本、现有技术检索 |
| 中国PCT国家阶段 | `patent-exam-pct-national` | 进入中国国家阶段全流程(联动审查指南) |

### 法规结构映射

#### 条约(69条) → `pct-treaty`

- 绪则(1-2): 定义
- 第I章(3-30): 国际申请和国际检索
- 第II章(31-42): 国际初步审查
- 第III章(43-49): 共同规定
- 第IV-VIII章(50-69): 技术服务/行政/争议/修订/最后条款

#### 细则(96条) → `pct-treaty`

- Part 1(1-2): 绪则
- Part 2(3-52): 第I章细则
- Part 3(53-78): 第II章细则
- Part 4(79-83): 第III章细则
- Part 5(84-89): 第V章细则
- Part 6(89bis-96): 有关条约各章的细则

#### 国际阶段 → `pct-international-phase`

- 提交申请 → 受理局处理 → 国际检索 → 国际公布 →（可选）国际初步审查

#### 国家阶段 → `pct-national-phase`

- 进入期限 → 手续办理 → 特殊要求 → 后续程序

#### ISPE指南(8部分22章) → `pct-search-examination`

- Part I(1-3): 引言概述
- Part II(4-8): 申请内容
- Part III(9-14): 审查标准
- Part IV(15-16): 检索
- Part V(17): 书面意见/IPER
- Part VI(18-20): 初步审查程序
- Part VII(21): 质量框架
- Part VIII(22): 行政程序

#### 行政规程(8部分) + 受理局指南(19章) → `pct-administrative`

- 总则 → 国际申请 → 受理局 → 国际局 → ISA → IPEA → 电子申请 → 第三方观察

### 2026年版本更新要点

| 文件 | 版本变化 | 主要更新内容 |
|------|---------|-------------|
| PCT实施细则(2026) | 2026年1月1日生效（基于2023年7月+2024年7月修订） | 序列表免附加费、退款扩展等最新修改 |
| PCT行政规程(2026) | PCT/AI/25→PCT/AI/26 | 替代旧版，电子申请标准更新 |
| ISPE指南(2026) | PCT/GL/ISPE/13→PCT/GL/ISPE/14 | 替代旧版，审查标准更新 |

> **适用确认**：引用前须确认版本生效日期。2026 年 1 月 1 日生效的版本适用于该日及之后的 PCT 申请和操作。

### 外部技能联动

| 技能名称 | 定位 | 协作场景 |
|---------|------|---------|
| `patent-exam-pct-national` | 审查指南PCT国家阶段子技能 | PCT申请进入中国国家阶段的审查标准(细则+审查指南双重适用) |
| `patent-examination-guide` | 审查指南全流程母技能 | 关联家族：进入中国国家阶段的审查标准（经其子技能 patent-exam-pct-national） |
| `ip-management-compliance` | ISO 56005 IP管理体系 | PCT国际布局策略、IP战略层面的PCT决策 |

#### 典型联动场景

| 场景 | 调用链 |
|------|--------|
| PCT进入中国国家阶段+审查 | pct-national-phase → patent-exam-pct-national |
| PCT国际布局策略 | pct-guide → ip-management-compliance（由其对下分派 ip-mgmt-strategy／ip-mgmt-innovation） |

### 使用方式总则

1. **单独使用PCT技能**：直接问PCT相关问题，不触发联动。
2. **按需联动中国审查指南（可选环节）**：当问题涉及 PCT 进入中国国家阶段时，按需联动 `patent-exam-pct-national`；非中国事务不触发该联动。
3. **IP管理联动**：当问题涉及PCT国际布局策略时，联动 `ip-management-compliance`。
4. **手动联动**：以技能名显式调用 PCT 子技能（如 `pct-treaty`、`pct-national-phase`）。官方定义的 `@references/` 引用语法仅适用于引用技能目录内的文件，跨技能调用一律以技能名发起，不使用任何伪语法。

### 路由关键词映射

| 关键词/场景 | 子技能 |
|------------|--------|
| PCT条约、条约第X条、PCT第X条、巴黎公约、条约定义 | pct-treaty |
| 实施细则、细则第X条、Rule X、PCT费用、Schedule of Fees、费用表 | pct-treaty |
| PCT期限、优先权期限、30个月、20个月 | pct-treaty(基本原则)/pct-national-phase(具体进入) |
| 国际申请、PCT申请、提交申请、请求书、PCT/RO/101 | pct-international-phase |
| 受理局、RO、国际申请日、申请日确定、缺陷改正 | pct-international-phase |
| 国际检索、ISR、检索报告、书面意见、WO/ISA、written opinion | pct-search-examination |
| 国际公布、18个月公布、第19条修改 | pct-international-phase |
| 国际初步审查、第II章、要求书、IPEA、IPER | pct-search-examination |
| 补充检索、SISA、补充国际检索 | pct-international-phase |
| ISA 协议、IPEA 协议、EPO 试点、中欧 PCT 试点 | pct-international-phase(附录B/附录D) |
| 专利性国际初步报告、IPRP | pct-search-examination |
| 发明单一性、unity of invention | pct-search-examination(审查标准)/pct-international-phase(申请人视角) |
| 新颖性、创造性、实用性、三步法、问题解决法 | pct-search-examination |
| X/Y/A文献、引用分类、PCT最低文献 | pct-search-examination |
| 国家阶段、进入国家阶段、指定局、选定局 | pct-national-phase |
| 30个月期限、译文、进入费用、国家阶段手续 | pct-national-phase |
| 译文改正、优先权恢复(国家阶段)、援引加入 | pct-national-phase |
| 发明人声明、转让证明、代理委托 | pct-national-phase |
| 加快审查、PPH | pct-national-phase |
| 受理局指南、RO指南、RO操作、受理通知 | pct-administrative |
| 行政规程、Administrative Instructions、表格、PCT表格 | pct-administrative |
| ePCT、电子申请、电子提交、fee reduction | pct-administrative |
| 序列表、ST.26、核苷酸、氨基酸 | pct-administrative |
| 生物材料保藏、布达佩斯条约 | pct-international-phase(国际阶段)/pct-administrative(形式要求) |
| 优先权恢复(受理局)、优先权改正、优先权增加 | pct-administrative |
| 援引加入、missing parts、错误提交项目 | pct-administrative |
| 明显错误更正、Rule 91、更正 | pct-administrative |
| 撤回、withdrawal、撤回国际申请 | pct-administrative(程序)/pct-international-phase(申请人操作) |
| 第三方观察、third party observation | pct-administrative |
| 最低文献、minimum documentation | pct-search-examination |
| 费用减免、fee reduction、电子申请费减免 | pct-administrative |
| 传送费、国际申请费、检索费、初步审查费 | pct-treaty(费用表) |
| 代理人、agent、共同代表、变更 | pct-international-phase |
| 指定、determination、selected、elected | pct-treaty(概念)/pct-international-phase(操作) |
| 质量框架、quality、质量管理 | pct-search-examination |
| PCT时限计算、期限计算、时限倒推 | pct-treaty(借助 WIPO ePCT 在线时限计算器) |
| PATENTSCOPE、专利检索、现有技术检索、公开号查询 | pct-international-phase(用户指南速查)/pct-search-examination(检索标准) |

> **路由退化兜底**：无法匹配任何子技能关键词时，母技能以自身知识直接回答，同时提示可用的子技能范围。

### 跨子技能协调链

| 场景 | 调用链 |
|------|--------|
| PCT全流程入门 | treaty → international-phase → national-phase |
| 国际申请前准备 | treaty(费用/期限) → international-phase(提交) |
| 收到ISR后应对 | search-examination(解读ISR) → international-phase(修改/第II章) |
| 进入国家阶段准备 | international-phase(国际阶段文件) → national-phase(进入手续) |
| 国家阶段优先权恢复 | national-phase(概述) → administrative(受理局恢复标准) |
| 形式缺陷处理 | international-phase(申请人视角) → administrative(受理局操作规范) |
| PCT全流程+中国国家阶段 | pct体系 → patent-exam-pct-national(中国审查指南联动) |

### 使用示例

| # | 用户请求 | 路由目标 | 说明 |
|---|---------|---------|------|
| 1 | "PCT条约第22条规定的进入国家阶段期限是多少？" | pct-treaty | 条约条文查询 |
| 2 | "如何提交PCT国际申请？需要什么文件？" | pct-international-phase | 国际阶段流程 |
| 3 | "国际检索报告里的X类文献是什么意思？" | pct-search-examination | 引用分类解读 |
| 4 | "PCT申请进入美国国家阶段需要什么手续？" | pct-national-phase | 国家阶段实务 |
| 5 | "受理局发现优先权有问题怎么处理？" | pct-administrative | 受理局操作规范 |
| 6 | "PCT国际阶段怎么提第三方观察意见？" | pct-administrative | 第三方观察程序 |
| 7 | "国际初步审查的流程和期限是怎样的？" | pct-search-examination | 第II章程序 |
| 8 | "PCT申请费用一览" | pct-treaty | 费用详情 |
| 9 | "从PCT申请到中国授权全流程" | pct-national-phase → patent-exam-pct-national | 跨技能协调 |

### 失败模式与恢复

| 触发条件 | 一线修复 | 仍失败兜底 |
|---------|---------|-----------|
| 用户请求无法匹配任何路由关键词 | 按关键词权重排序→输出最匹配的2-3个子技能候选→让用户确认 | 以母技能自身知识直接回答，附"建议手动调用: PCT 子技能的技能名（如 pct-treaty、pct-national-phase）" |
| 目标子技能加载失败 | 尝试通过母技能重新加载 | 从母技能自身知识库直接回答，标注"子技能暂不可用，结论基于PCT通用知识" |
| 涉及版本更新但无法确定适用版本 | 同时输出新旧版本标准→标注适用时间条件 | 建议用户核实提交日期，以提交日所在时间版本为准 |
| 跨子技能协调场景 | 确定主场景→优先加载主场景子技能→按联动链加载关联子技能 | 一次输出全部相关子技能的分析，按逻辑顺序排列 |
| 子技能间结论冲突 | 以《PCT条约》+《实施细则》为准对齐，标注差异点让用户确认 | 同时输出两方依据，提示"以条约+细则为最高准据" |
| 路由模糊（命中多个子技能关键词） | 列出 2–3 个候选子技能及其适用边界，让用户确认目标阶段 | 以母技能自身知识回答并标注建议子技能 |
| 用户未提供优先权日却要求具体截止日期 | 仅输出期限长度与起算规则，不输出具体日历日 | 提示补充优先权日后再计算具体日期 |
| 是否联动中国审查指南判断不清 | 一旦涉及 PCT 进入中国国家阶段，显式转 `patent-exam-pct-national` | 标注"中国国家阶段审查标准见 patent-exam-pct-national" |
| 各子技能版本适用不一致 | 统一以 2026 年 1 月 1 日生效版本（PCT/AI/26、ISPE/14）为准 | 标注引用版本号与生效日，提示以最新版为准 |

### 禁止行为与反例

| # | 禁止行为 | 原因 | 正确做法 |
|---|---|---|---|
| 1 | 跳过条约直接引用实施细则 | PCT条约→细则→行政规程三层级不可跳跃 | 引用格式：条约第X条→细则第X条→行政规程第XXX节(如适用) |
| 2 | 将PCT体系与中国专利法混用 | PCT是独立国际条约体系，与中国专利法适用不同规则 | PCT实务引用PCT法规；涉及中国国家阶段时再联动 patent-exam-pct-national |
| 3 | 忽略版本更新 | 生效的版本对旧版有修改 | 引用前确认文件生效日期和适用情形 |
| 4 | 将PCT初步审查等同于中国实质审查 | PCT第II章为国际初步审查(非授权性)，中国实审为国家阶段审查 | PCT阶段的分析注明"国际初步审查"而非"实质审查" |
| 5 | 向不存在或不匹配的子技能路由 | 路由错误将导致用户无法获得专业子技能的深度分析 | 严格按路由关键词映射表匹配，不确定时输出候选子技能让用户选择 |
| 6 | 交付文本使用 Markdown 表格 | 违反输出格式硬约束 | 用标题 + 列表组织交付文本 |
| 7 | 数据缺失时编造或推测 | 违反"无数据回'无'"硬约束 | 直接回复"无"，并提示可补充的检索途径 |

### 维护说明

- 版本号仅在本文件 frontmatter（`version`）维护，正文不写死技能版本。
- **家族版本治理（2026-09-28 起）**：6 个技能采用**统一版本号**（当前 **2.6.1**，以 pct-treaty 为基准）；任一技能修订时，全家族同步升版——避免版本号分散，便于技能包整体发布与安装对照。
- 法规文件版本（如 PCT/AI/26、ISPE/14 等）为知识内容，随法规更新同步修订，不视为技能版本。
- frontmatter 字段遵循官方技能开发文档（open.workbuddy.cn/docs/skill）：必填项 `description` / `description_zh` / `description_en` / `version` / `author`；展示项 `display_name` / `display_name_en` / `category`。自定义扩展字段与子技能族保持同构（`tags` / `parent-skill` / `related-skills` / `update-log`）。
- **不设 `references/` 目录**：本技能主体为路由元数据（关键词映射、协调链、失败模式），需常驻上下文才能完成路由判定，拆分入 `references/` 反而增加每次路由的读取开销；原始法规文本类参考资料由各子技能的 `references/` 承载。此为有意取舍，非遗漏。
- 更新日志：见 frontmatter `update-log`。
