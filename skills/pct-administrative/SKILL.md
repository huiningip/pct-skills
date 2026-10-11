---
name: pct-administrative
display_name: PCT行政规程与受理局实务
display_name_en: PCT Administrative Instructions & Receiving Office Practice
description: PCT行政规程与受理局实务子技能。覆盖《PCT行政规程》(PCT/AI/26, 2026年1月1日生效)+《PCT受理局指南》(PCT/GL/RO/22, 2025年7月1日生效)。包含：受理局全流程操作(申请日确定/第14条检查/优先权处理/援引加入/序列表ST.26/费用/副本传送/更正/撤回)、行政规程(8部分180节表格体系/通信/期限/费用/电子申请ePCT/第三方观察/最低文献/8个附件)。触发词：受理局、RO、受理局指南、行政规程、Administrative Instructions、表格、PCT表格、ePCT、电子申请、ST.26、序列表、援引加入、明显错误更正、撤回、第三方观察、缺陷改正、形式审查、费用催缴、登记本、最低文献、PCT/RO/101、PCT/IPEA/401
description_zh: "PCT 体系最细粒度的操作规范层。合并覆盖《PCT行政规程》（PCT/AI/26，8 部分 Sections 101–805 + 8 附件）与《PCT受理局指南》（PCT/GL/RO/22，现行 19 章 + ANNEX B），按节号／章号给出受理局全流程操作（申请日 Art.11(1) 核查、语言检查、第14条形式检查、优先权、援引加入、序列表 ST.26、费用催缴、副本传送、明显错误更正、撤回）、标准化表格体系、ePCT 电子申请标准与第三方观察系统。两份原文全文见 @references/。
"
description_en: "The most granular operational layer of the PCT system. Jointly covers the PCT Administrative Instructions (PCT/AI/26: 8 Parts, Sections 101 to 805, plus 8 Annexes) and the PCT Receiving Office Guidelines (PCT/GL/RO/22: 19 chapters in force plus Annex B). Returns article- and section-anchored guidance on the full receiving-office workflow (Article 11(1) filing-date check, language check, Article 14 formalities check, priority claims, incorporation by reference, ST.26 sequence listings, fee invitations, transmittal of copies, rectification of obvious mistakes, withdrawal), the standard forms system, the ePCT electronic filing standards and the third party observation system.
"
category: legal
version: "2.6.1"
author: 辉宁知识产权
# allowed-tools：（选填）本技能答复前可能需检索 ima 知识库并可能经 WebFetch 核对 WIPO 表格／声明保留页；
#   设白名单会切断未列出的工具调用，故不启用。
agent_created: true
tags: [pct, administrative-instructions, receiving-office, ePCT, ST26, forms, formalities]
parent-skill: pct-guide
related-skills:
  - pct-guide: 上位母技能（路由与跨技能协调）
  - pct-treaty: 条约与实施细则法源（行政规程的上位依据）
  - pct-search-examination: ISPE 检索审查标准（最低文献、第三方意见对审查的影响）
  - pct-international-phase: 申请人视角的国际阶段操作
  - pct-national-phase: 国家阶段进入手续
update-log: |
  2.6.1 (2026-09-28) 版本号家族统一：由 2.3.5 统一至 **2.6.1**（全家族 6 技能同版本号，对齐 pct-treaty 基准，
    便于技能包整体发布与同步维护）；本次不涉及内容修订，历史修订见下方条目。
  2.3.5 (2026-09-28) 国际化定位改造（对标 madrid-trademark 模式）：角色段注明「规则对各受理局通用
    （缔约国中立）」及 CNIPA 数据为可选补充（指向 pct-treaty 费用章节）。
  2.3.4 (2026-09-26) 第二轮复查修复（3 处，含《PCT行政规程》Section 802 原文核验）：
    - ★★ 失败模式失同步（一处）：「第三方观察」条目原写「仅保留专利性意见(新颖性/创造性/实用性)」，
      与 Section 802(a)(vii) 原文（仅限 novelty or inventive step）及规则第 7 条矛盾；更正为
      「仅保留与新颖性/创造性相关的现有技术（Section 802(a)(v)、(vii)）」，触发条件列同步修正；
    - ★ 章节重排：「受理局指南（CHAPTER I–XIX）」章节原为 14→16→18→15→17→19，第 15 章（明显错误
      更正）误置于第 16/18 章之后；重排为 14→15→16→17→18→19；
    - ★ 笔误订正：第 14 章 [Deleted] 注「（已删除，不含量）」→「（已删除，不含内容）」。
  2.3.3 (2026-09-26) 全量回扫 2.3.2 订正口径：修复 6 处未同步引用点 + 1 处回扫新发现的引用偏差（族内一致性校验）：
    - ★★★ 申请日要件失同步（两处）：「快速参考卡片」与「第4章：第11条(1)检查」表仍含「费用」
      并保留旧「指明国家／指定申请人」框架，与规则第 10 条已订正的三组要件（Art.11(1)(i)–(iii)）矛盾；
      两处均改按「申请人资格＋规定语言＋最低内容五项」重写，并加注费用非申请日要件（费用属
      Art.14 与细则 Rules 14–16，未缴后果为视为撤回）；
    - ★★ 第三方观察窗口失同步（三处）：「快速参考卡片」「实务要点第 6 条」「禁止行为第 6 条」仍写
      「国际公布后至国家阶段启动前」，与规则第 7 条已订正的「自国际公布日至优先权日起 28 个月」
      （《PCT行政规程》Section 802(a)(ii)）矛盾；三处统一为 28 个月口径并补申请人回应期（Section 804(b)）；
    - ★ 援引加入法源失同步（一处）：「快速参考卡片」原引「AI Section 310-315」，与第 296 行注
      （援引加入实在细则 Rules 20.5/20.6 及 RO Guide 第 8 章，AI 仅涉后交页 310–310ter）矛盾；
      更正为「RO Guide 第8章 + 细则 Rules 20.5/20.6」；
    - ★ 费用催缴引用偏差（一处，回扫新发现）：「快速参考卡片」原引「AI Section 305-306」，经
      references/ADMIN_INSTRUCTIONS_2026.md 原文核验，Section 305 为「Identifying the Copies of the
      International Application」、Section 306 为「Delayed Transmittal of Search Copy」，均与费用催缴
      无关；费用催缴的正确节号为 Section 304（Invitation to Pay Fees before Date on Which They Are
      Due）；已更正，并注 Rule 16bis 延期缴费情形见 Section 320。
  2.3.2 (2026-09-21) 按官方技能开发文档（open.workbuddy.cn/docs/skill）合规化 + 法源订正：
    - frontmatter 补齐 display_name / display_name_en / description_zh / description_en / category，并补
      related-skills 与 allowed-tools 未启用理由；update-log 精简为最近三版；
    - 标题层级修正：原「技能知识库」误用同级 H1（全文出现两个 H1），降为 H2 并同步下移各级子标题；
    - ★★★ 法源订正（规则第 10 条）：「申请日三条件（Art.11）」原写「①明确或暗示指明国家 ②指定申请人
      ③包含说明书 + 权利要求 + 费用缴纳」，与条约第 11 条(1) 原文不符——**费用缴纳并非申请日条件**（费用
      属 Art.14 及细则 Rules 14–16，未按期缴纳的后果是视为撤回），且遗漏「说明是作为国际申请提出的」及
      语言、申请人资格两组要件；已按 Art.11(1)(i)–(iii) 重写为三组要件；
    - ★★ 法源订正（规则第 7 条）：第三方观察窗口原写「国际公布后至国家阶段启动前」，与《PCT行政规程》
      Section 802(a)(ii)「自国际公布日至优先权日起 28 个月」不符，已更正并补申请人回应期（Section 804(b)）；
    - ★★ 法源订正（两处）：电子申请病毒检测原引「AI Sections 709-710」，经原文核验 Section 709 为「与申请人
      通信的方式」、Section 710 为「受理局要求的通知与公布」，均与病毒检测无关；更正为 Section 703(b)(v)
      （电子形式申请须无病毒及恶意逻辑）+ Section 708(b)（受理局核查感染的程序与后果）；
    - ★ 计数精确化：《PCT受理局指南》结构描述原写「19 章（含第 XIV 章已删除…）+ 2 附录（Annex A 已删除…）」，
      计数与「已删除」自相矛盾；更正为「章号 CHAPTER I–XIX + CHAPTER VIIbis（共 20 个章号，其中 CHAPTER XIV
      已删除，现行 19 章）+ 附录 ANNEX B（ANNEX A 已删除，现行 1 个）」；
    - references 引用语法标准化：反引号路径改为官方文档规定的 @references/ 语法（4 处）。
  2026-08-26 第 11 章费用补引 CNIPA 2026 年 9 月标准指针：交叉引用 pct-treaty 费用体系章节「CNIPA 受理 PCT 国际阶段费用标准（2026年9月生效 · 当前标准，将不定期调整）」；本技能第 11 章保持受理局处理层面的期限与流转框架，具体金额以 pct-treaty 该（动态）标准为准，并标注「以 CNIPA 最新公布为准」。
  2026-08-23 收录《PCT行政规程》原文结构化转换（references/ADMIN_INSTRUCTIONS_2026.md，WIPO PCT/AI/26 as in force 2026-01-01，105 页 / 8 Part / 180 Section[含 18 变体] / 8 Annex / 零乱码），重写「行政规程（8 部分）」结构表以与官方原文标题逐一对应；并修复结构表系统性偏差（Part 1/2/3/4/5/7 的节号归类与 [Deleted] 标注）。
---

# PCT行政规程与受理局实务

## 角色

本技能是 **PCT 行政规程与受理局实务子技能**，隶属 `pct-guide` 母技能。合并覆盖《PCT行政规程》（Administrative Instructions, AI）与《PCT受理局指南》（RO Guide），是 PCT 体系中最细粒度的操作规范和受理局处理指南，面向受理局操作、表格使用、电子申请与行政程序。**规则对各受理局通用（缔约国中立）**；CNIPA 等特定受理局的具体费用数据为可选补充（见 `pct-treaty` 费用章节）。

## 任务

- 提供受理局全流程操作指引（申请日确定、语言检查、第14条形式检查、优先权、缺失部分/援引加入、序列表、生物材料、费用、副本传送、更正、撤回）。
- 提供行政规程（AI）各节操作规范（总则、国际申请、受理局、国际局、ISA、IPEA、电子申请、第三方观察）。
- 提供标准化表格体系（PCT/RO/101 请求书、PCT/IPEA/401 要求书等）的编号、用途与填写指引。
- 提供 ePCT 电子申请标准与费用减免信息。
- 提供最低文献范围与附件（Annex A-H）说明。
- 向用户交付**符合输出格式规范**的分析结论。

## 上下文（背景数据）

- **PCT行政规程**：PCT/AI/26（2026 年 1 月 1 日起生效，替代 PCT/AI/25）；8 部分（第 101-805 节）+ 8 附件（Annex A-H）。
- **PCT受理局指南**：PCT/GL/RO/22（2025 年 7 月 1 日起生效）；章号 **CHAPTER I–XIX + CHAPTER VIIbis**（共 20 个章号，其中 **CHAPTER XIV 已删除**；**现行 19 章**，第 VIIbis 章为国家要求声明）+ 附录 **ANNEX B**（请求书典型缺陷示例；**ANNEX A 已删除**，现行 1 个）。完整原文见 @references/RO_GUIDE_2026.md。
- **法规层级定位**：

```
PCT条约 (Art.58)
    ↓
PCT实施细则 (Rule 89.2)
    ↓
PCT行政规程 (Administrative Instructions) ← 本技能覆盖
    +
PCT受理局指南 (RO Guidelines) ← 本技能覆盖
```

- **受理局核心操作链**：申请日确定（Art.11 检查）→ 语言检查（第5章）→ 第14条形式检查（第6章）→ 优先权（第7章）→ 缺失部分/援引加入（第8章）→ 费用（第11章）→ 副本传送（第12-13章）→ 更正（第15章）→ 撤回（第17章）。
- **ePCT 系统**：电子申请标准 + Basic 通用标准（Part VII, Sections 701-716）；EFiling 服务器入口：https://pct.wipo.int/ePCTExternal/pages/EFilingServers.xhtml
- **表格体系**：一套标准化表格（PCT/RO/101 请求书、PCT/IPEA/401 要求书等数十种），最新版从 WIPO 官网下载：https://www.wipo.int/pct/zh/forms/
- **联动**：`pct-international-phase`（申请人视角操作）；`pct-search-examination`（WO/ISA 栏目、最低文献操作要求）；`pct-treaty`（费用表框架）。

## 流程（步骤）

1. **确定操作类型**：受理局操作 / 表格使用 / 电子申请 / 第三方观察等。
2. **定位规范来源**：行政规程第 XXX 节 / 受理局指南第 X 章。
3. **查找表格/模板**：对应 PCT 表格编号和填写规范。
4. **确认适用版本**：AI/26 或 RO/22 版本下的具体要求。
5. **输出格式化**：按输出格式规范组织交付文本（法规依据 → 操作规范 → 表格指引 → 版本提示）。

> 🔴 **CHECKPOINT 1**：用户请求涉及受理局操作（RO Guide）还是行政规程操作（AI）？RO Guide 针对受理局处理程序，AI 针对国际局/ISA/IPEA 操作规范。确定规范来源（第X节/第X章）后再输出。
> 🔴 **CHECKPOINT 2**：所查找的表格/PCT 编号是否对应正确的现行版本？确认版本生效日期及对应操作要求。
> 🔴 **CHECKPOINT 3（受理局指南前）**：RO Guide 偏重受理局实操（申请日/缺陷/费用/副本传送），AI 偏重国际局/ISA/IPEA 操作规范（表格/公布/检索/审查）。用户问"受理局如何处理"→RO Guide；用户问"标准表格/公布格式"→AI。

## 提问指引与预期管理

本小节帮助用户判断"我的问题是否适用本技能"并管理交付预期。本小节属技能内部指引，不受输出格式"禁表格"硬约束（第 11 条仅针对向用户交付的文本）。

### 典型提问示例（可直接触发本技能）

- "PCT 申请提交后，受理局怎么确定申请日？缺说明书会怎样？"（→ RO Guide 第4章，Art.11(1) 三组要件）
- "PCT/RO/101 请求书每个栏目怎么填？哪里下载最新版？"（→ AI Section 102 + Annex A）
- "国际申请漏了说明书某几页，怎么援引加入？期限怎么算？"（→ RO Guide 第8章 + PCT/RO/106）
- "序列表现在用什么格式？ST.25 还能用吗？要不要另交附加费？"（→ AI Section 207-208 + Annex C）
- "通过 ePCT 提交能省多少费用？文件有什么安全要求？"（→ AI Part VII Sections 701-716）
- "受理局发了费用催缴通知（PCT/RO/103），不补会怎样？"（→ RO Guide 第11章）
- "第三方观察什么时候能提？能写什么内容？"（→ AI Part VIII Sections 801-805）
- "明显错误（Rule 91）怎么更正？要在什么时间前提？"（→ RO Guide 第15章）

> 以上示例覆盖本技能八类核心场景（受理局操作 / 表格使用 / 电子申请 / 援引加入 / 序列表 / 费用催缴 / 第三方观察 / 明显错误）。用户问题落入这些主题即适用本技能。

### 操作模板 / 样例

**模板 A — 援引加入请求（PCT/RO/106）要点**
- 提交表格：PCT/RO/106
- 必要内容：引用在先申请号 + 具体引用位置（段号 / 行号 / 图号）+ 补交部分说明
- 期限：申请日后的规定期限内（超期不能再援引）
- 效果：申请日不后移

**模板 B — ePCT 电子提交标准动作**
1. 准备符合 Basic 通用标准的电子申请文件（PDF 推荐）
2. 对所有附件执行病毒扫描（AI **Section 703(b)(v)**：电子形式申请须无病毒及其他恶意逻辑；受理局的核查程序见 **Section 708(b)**）
3. 通过 ePCT EFiling 服务器提交：https://pct.wipo.int/ePCTExternal/pages/EFilingServers.xhtml
4. 确认享受国际申请费减免并保存提交回执

**模板 C — 费用催缴（Form PCT/RO/103）响应**
- 在催缴通知载明的期限内补足差额
- 补缴后主动联系受理局确认到账状态并索取收据（受理局不单独通知到账）
- 逾期未补 → 视为撤回 → 启动权利恢复程序

### 边界与降级回应

- **适用边界**：本技能覆盖 PCT 受理局操作、行政规程（AI）、受理局指南（RO Guide）、标准化表格、ePCT 电子申请、第三方观察、最低文献；各缔约国就细则/行政规程条款作出的不兼容通知（如 Rule 20.8 优先权文件、49ter 期限/费用、4.9(b) 全部指定）以 WIPO《声明保留和不兼容》页面(https://www.wipo.int/zh/web/pct-system/texts/reservations/res_incomp)及 pct-treaty 对应章节为准。
- **不适用 / 未覆盖情形**：国家阶段实体审查、国际检索与初步审查的专利性判断、具体国家国内法细节、非 PCT 体系事务——超出本技能范围。
- **降级回应标准话术**：当问题超出本技能覆盖范围或所需数据不可得时，直接回复"无"，并指明可转向的技能或权威来源（如 `pct-national-phase`、`pct-search-examination`、WIPO 表格页 https://www.wipo.int/pct/zh/forms/），不编造、不推测。

## 规则（约束/边界）

1. **RO Guide vs AI 分工**：受理局实操（申请日/缺陷/费用/副本传送）→ RO Guide；国际局/ISA/IPEA 操作（表格/公布/检索/审查）→ AI。禁止混用。
2. **表格必须标准化**：行政规程 Section 102 强制要求使用标准化表格体系（PCT/RO/101 等），从 WIPO 网站下载最新版填写。
3. **援引加入时效**：务必在申请日后的规定期限内提交援引加入请求，超过期限则不能再援引；须明确引用在先申请的具体部分（段号/行号等）。
4. **序列表 ST.26**：自 2022-07-01 起 ST.25 不再接受，必须使用 ST.26 XML 格式；2026 年起序列表不计入计费页数（免附加费）。
5. **优先权恢复双标准**：受理局可选择"适当注意标准"或"故意性标准"，须先确认目标受理局适用标准再准备恢复理由和证据。
6. **电子文件安全**：电子形式的国际申请须**无病毒及其他形式的恶意逻辑**（AI **Section 703(b)(v)**，依 Annex F 或基本通用标准）；受理局收到电子形式的申请后应即时核查感染情况，并据此决定是否接收、是否给予申请日（AI **Section 708(b)**）。
   - ⚠️ 注意：Section 709 为「与申请人通信的方式」、Section 710 为「受理局要求的通知与公布」，**均与病毒检测无关**，不得误引；Section 802(a)(vi) 另要求第三方观察文件同样须无病毒。
7. **第三方观察窗口**：自**国际公布日**起至**优先权日起 28 个月**止（《PCT行政规程》Section 802(a)(ii)）；内容仅限与**新颖性和／或创造性**相关的现有技术，不得含其他评论（Section 802(a)(v)、(vii)）。IB 收到后通知申请人，申请人可在**优先权日起 30 个月**内提交回应意见（Section 804(b)）。
8. **费用催缴**：催缴后须主动确认费用到账状态，索取缴费收据；受理局不单独通知到账。
9. **Rule 91 明显错误更正**：错误须"明显"（非申请人真实意图 + 正确内容明确），且尽量在国际公布前提出。
10. **申请日要件**（Art.11(1)，三组）：①**申请人资格**——申请人并不因居所或国籍的原因而明显缺乏向该受理局提出国际申请的权利；②**语言**——国际申请是用规定的语言撰写；③**最低内容五项**——(a) 说明是作为国际申请提出的、(b) 至少指定一个缔约国、(c) 按规定方式写明的申请人姓名或名称、(d) 有一部分表面上看像是说明书、(e) 有一部分表面上看像是一项或几项权利要求。
    - ⚠️ **费用缴纳不是申请日要件**：传送费／国际申请费／检索费的缴纳属 Art.14 与细则 Rules 14–16 的范围；未在允许期限内缴纳的后果是该申请**视为撤回**，既不影响国际申请日的给予，也不导致申请日后移。不得将其列为 Art.11 的申请日条件。
    - 不符合上述要件时，受理局按细则要求申请人改正；**以收到必要改正之日为国际申请日**（Art.11(2)）。
11. **输出硬约束（对用户交付文本）**：
    - **严禁输出任何 Markdown 表格**；
    - **如果找不到数据，直接回复"无"，严禁编造**。
12. 本技能内部知识库（参考/指引内容）不受第 11 条"禁表格"约束，可保留 Markdown 表格作为知识载体。

## 输出格式

向用户交付的分析结论**严禁使用 Markdown 表格**，须用标题 + 列表组织：

```markdown
### [操作事项名称]

**法规依据**
- PCT行政规程Section XXX
- PCT受理局指南 第X章
- (如适用) PCT表格编号

**操作规范**
[具体操作步骤，用编号列表]

**表格/工具指引**
- 表格编号：[PCT/RO/XXX]
- 提交方式：[ePCT/书面/传真]

**版本提示**
- 适用版本：PCT/AI/26（2026年1月1日起生效）
- 适用版本：PCT/GL/RO/22（2025年7月1日起生效）
```

**找不到数据时**：直接回复"无"，不得编造、推测或拼接无关内容。

---

## 技能知识库（内部参考，不受输出禁表格约束）

> **完整原文结构化转换**：
> - @references/RO_GUIDE_2026.md（WIPO *PCT/GL/RO/22*，as in force 2025-07-01，93 页；19 章 + Annex B 共 333 个段落号 `### N.` 锚定、86 个逐页溯源标记）。
> - @references/ADMIN_INSTRUCTIONS_2026.md（WIPO *PCT/AI/26*，as in force 2026-01-01，105 页；8 Part（按 Section 百位动态插入）+ 180 个 `### Section NNN` 锚定（含 18 个 bis/ter/quater 变体）+ 8 个 Annex（A/F 为官方未复制占位，B/C/D/E/G/H 含正文）+ 105 个逐页溯源标记，零乱码）。
> 本技能速查内容如与原文冲突，以上述两文件为准。

### 快速参考卡片

| 我想查询... | 应查看章节 | 一句话说明 |
|------------|----------|----------|
| 受理局确定申请日条件 | RO Guide 第4章 | Art.11(1) 三组要件：申请人资格+规定语言+最低内容五项（**不含费用**；费用属 Art.14 与细则 Rules 14–16，未缴后果为视为撤回） |
| 标准表格PCT/RO/101填写 | AI Section 102 + Annex A | 10个栏目填写规范+标准化表格体系 |
| 援引加入操作流程 | RO Guide 第8章 + 细则 Rules 20.5/20.6 | 提交PCT/RO/106表格+引用在先申请对应部分+在规定期限内（AI Section 310–310ter 仅为后交页处理，非援引加入法源） |
| 序列表ST.26格式要求 | AI Section 207-208 + Annex C | WIPO标准ST.26 XML格式(2022年起替代ST.25) |
| 费用催缴处理 | RO Guide 第11章 + AI Section 304（Rule 16bis 延期缴费另见 Section 320） | 受理局发催缴通知(Form PCT/RO/103)→期限内补缴 |
| ePCT电子申请操作 | AI Part VII Sections 701-716 | 电子提交享费用减免→Basic通用标准+病毒扫描要求→EFiling服务器: https://pct.wipo.int/ePCTExternal/pages/EFilingServers.xhtml |
| 第三方观察提交规范 | AI Part VIII Sections 801-805 | 自国际公布日起至优先权日起28个月止（Section 802(a)(ii)）→内容仅限新颖性/创造性相关现有技术 |

### 行政规程（8部分，Sections 101-805 + 8 Annexes）

#### PART I: 总则（Sections 101-116）

| 节号 | 内容（WIPO PCT/AI/26 原文标题）|
|------|------|
| 101 | Abbreviated Expressions and Interpretation（缩略语与解释）|
| 102 | Use of the Forms（表格使用）|
| 103 | Languages of the Forms Used by International Authorities（国际局用表格语言）|
| 104 | Language of Correspondence（通信语言）|
| 105 | Identification of International Application with Two or More Applicants（多申请人国际申请标识）|
| 106 | Change of Common Representative（共同代表变更）|
| 107 | Identification of International Authorities and of Designated and Elected Offices（国际局/指定局/选定局标识）|
| 108 | Correspondence Intended for the Applicant（致申请人的通信）|
| 109 | File Reference（档案引用号）|
| 110 | Dates（日期）|
| 111 | Excuse of Delay in Meeting Time Limits and Extension under Rule 82quater（期限延误宽免/延长）|
| 112 | Ceasing of Effect under Arts 24(1)(iii)/39(2), Review under Art 25(2), Maintaining of Effect（效力终止/审查/维持）|
| 113 | Special Fees Payable to the International Bureau（国际局特别费）|
| 114 | Notification and Transfer of Fees（费用通知与转付）|
| 115 | Indications of States, Territories and Intergovernmental Organizations（国家/地区/组织标识）|
| 116 | Minimum Documentation（最低文献）|

#### PART II: 国际申请相关（Sections 201-218）

| 节号 | 内容（WIPO PCT/AI/26 原文标题）|
|------|------|
| 201 | Language of the International Application（国际申请语言）|
| 202 | **[Deleted]**（已删除）|
| 203 | Different Applicants for Different Designated States（不同指定国不同申请人）|
| 204 | Headings of the Parts of the Description（说明书各部分标题）|
| 204bis | Numbering of Claims（权利要求编号）|
| 205 | Numbering and Identification of Claims upon Amendment（修改后权利要求编号标识）|
| 206 | Unity of Invention（发明单一性，Annex B 细化）|
| 207 | Arrangement of Elements and Numbering of Sheets（申请文件要素排列与页码）|
| 208 | Sequence Listings（序列表 ST.26，Annex C）|
| 209 | Indications as to Deposited Biological Material（生物材料保藏标注）|
| 210 | **[Deleted]**（已删除）|
| 211 | Declaration as to the Identity of the Inventor（发明人身份声明）|
| 212 | Declaration as to the Applicant's Entitlement to Apply (Art.5) |
| 213 | Declaration as to the Applicant's Entitlement to Priority (Rule 4.17) |
| 214 | Declaration of Inventorship（发明人声明）|
| 215 | Declaration as to Non-Prejudicial Disclosures（新颖性宽限期声明）|
| 216 | Notice of Correction or Addition of a Declaration under Rule 26ter |
| 217 | Corrections Concerning Expressions under Rule 9.2（不当表述更正）|
| 218 | Processing of a Request for Omission under Rules 48.2(l)/94.1(e) |

#### PART III: 受理局相关（Sections 301-337）

| 节号 | 内容（WIPO PCT/AI/26 原文标题）|
|------|------|
| 301 | Notification of Receipt of Purported International Application（受理通知 Form PCT/RO/105）|
| 302 | Priority Claim Considered Not to Have Been Made（视为未提出优先权声明）|
| 303 | Deletion of Additional Matter in the Request（请求书中额外事项删除）|
| 304 | Invitation to Pay Fees before Date on Which They Are Due（费用催缴 Form PCT/RO/103）|
| 305 | Identifying the Copies of the International Application（申请副本标识）|
| 305bis | Preparation/Identification/Transmittal of Translation Copies（Rule 12.3/12.4/26.3ter）|
| 305ter | Identification and Transmittal of Translation of Earlier Application（Rule 20.6(a)(iii)）|
| 306 | Delayed Transmittal of Search Copy（检索本迟延传送）|
| 307 | System of Numbering International Applications（国际申请编号系统）|
| 308 | Marking of the Sheets（申请文件页码标记）|
| 308bis | Marking of Later Submitted Sheets（后交页标记）|
| 309 | Procedure in Case of Later Submitted Sheets（后交页处理 Rule 20.5(c)/(d)）|
| 310 / 310bis / 310ter | Procedure in Case of Later Submitted Sheets（后交页各类情形处理）|
| 311 | Renumbering（重新编号）|
| 312 | Notification of Decision Not to Issue Declaration（不发声明通知）|
| 313 | Documents Filed with the International Application, Manner of Filing（文件提交方式）|
| 314 | Correction or Addition of a Priority Claim under Rule 26bis（优先权改正/增加）|
| 315 | Processing of Documents by the Receiving Office under Rule 26ter |
| 316 | Procedure Where International Application Lacks Elements（申请缺乏要素处理）|
| 317 / 317bis | Transmittal of a Notice of Correction or Addition（更正/补充通知传送）|
| 318 | Cancellation of Designations of Non-Contracting States（非缔约方指定取消）|
| 319 | Procedure under Rule 4.9(b)（全部指定程序）|
| 320 | Invitation to Pay Fees under Rule 16bis.1(a) |
| 321 | Application of Moneys Received by the Receiving Office（费用应用）|
| 322 | Invitation to Submit a Request for Refund of the Search Fee（检索费退款请求）|
| 323 | Transmittal of Priority Documents to International Bureau（优先权文件传送 IB）|
| 324 | Copy of Notification of the International Application Number（申请号通知副本）|
| 325 | Corrections of Defects under Rule 26.4 and Rectifications of Obvious Mistakes（**Rule 91 明显错误更正在此**）|
| 326 | Withdrawal by Applicant under Rule 90bis（申请人撤回）|
| 327 | Ex Officio Correction of Request by the Receiving Office（受理局职权改正，**Rule 91 在此**）|
| 328 | Notifications Concerning Representation（代理相关通知）|
| 329 | Correction of Indications Concerning the Applicant's Residence/Nationality（申请人居所/国籍改正）|
| 330 | Transmittal of Record Copy Prevented or Delayed（登记本传送受阻）|
| 331 | Receipt of Confirmation Copy（确认本收到）|
| 332 | Notification of Languages Accepted by the Receiving Office（受理局接受语言通知）|
| 333 | Transmittal of International Application to the International Bureau（国际申请传送 IB）|
| 334 | Notification to Applicant of Submission of Demand after Expiration of Time Limit |
| 335 | Procedures Relating to Sequence Listings（序列表程序）|
| 336 | Waivers under Rules 90.4(d) and 90.5(c) |
| 337 | **[Deleted]**（已删除）|

> 注：国家安全审查不属行政规程 Part 3，而属《PCT受理局指南》第 3 章（见 @references/RO_GUIDE_2026.md）。援引加入程序实际规定于细则 Rule 20.5/20.6 及 RO Guide 第 8 章，行政规程 Part 3 仅涉及后交页（310–310ter）与优先权改正（314）。

#### PART IV: 国际局相关（Sections 401-436）

| 节号 | 内容（WIPO PCT/AI/26 原文标题）|
|------|------|
| 401 | Marking of the Sheets of the Record Copy（登记本页码标记）|
| 402 | Correction or Addition of a Priority Claim under Rule 26bis（优先权改正/增加）|
| 403 | Transmittal of Protest against Payment of Additional Fees（附加费异议传送）|
| 404 | International Publication Number（国际公布号）|
| 405 | Publication of Notifications of Languages Accepted（接受语言通知公布）|
| 406 | Publication of International Applications（国际申请公布 Form PCT/IB/306）|
| 406bis | Suggested English Translation of the Title of the Invention |
| 407 | The Gazette（PCT 公报）|
| 408 | Priority Application Number |
| 409 | Priority Claim Considered Not to Have Been Made |
| 410 | Numbering of Sheets for the Purposes of International Publication |
| 411 | Receipt of Priority Document（优先权文件收到）|
| 411bis | Receipt of Translation of Earlier Application under Rule 20.6(a)(ii) |
| 412 | Notification of Lack of Transmittal of Search Copy |
| 413 | Incorporations by Reference under Rule 20.6, Corrections |
| 413bis | Rectifications of Obvious Mistakes under Rule 91（明显错误更正）|
| 414 | Notification to the International Preliminary Examining Authority |
| 415 | Notification of Withdrawal under Rule 90bis（撤回通知）|
| 416 | Correction of Request in Record Copy |
| 417 | Processing of Amendments under Article 19（Art.19 修改处理）|
| 418 | Notifications to Elected Offices Where the Demand Is Considered Withdrawn |
| 419 | Processing of a Declaration under Rule 26ter |
| 419bis | Processing of Corrections or Additions under Rule 26quater |
| 420 | Copy of International Application, International Search Report, etc. |
| 420bis | Communication of Other Documents to Elected Offices |
| 421 | Invitation to Furnish a Copy of the Priority Document |
| 422 | Notifications Concerning Changes Recorded under Rule 92bis |
| 422bis | Objections Concerning Changes in the Person of the Applicant |
| 423 | Cancellation of Designations and Elections |
| 424 | Procedure under Rule 4.9(b) |
| 425 | Notifications Concerning Representation |
| 430 | Notification of Designations under Rule 32 |
| 431 | Publication of Notice of Submission of Demand |
| 432 | Notification to Applicant of Submission of Demand after Expiration of Time Limit |
| 433 | Waivers under Rule 90.4(d) |
| 434 | Publication of Information Concerning Waivers |
| 435 | Communication of Publications and Documents |
| 436 | Preparation, Identification and Transmittal of the Copies of the International Application |

> 注：426–429 为官方空号（目录列 423–436 但实际跳号，原文不存在）。

#### PART V: 国际检索单位相关（Sections 501-521）

| 节号 | 内容（WIPO PCT/AI/26 原文标题）|
|------|------|
| 501 | **[Deleted]**（已删除）|
| 502 | Transmittal of Protest against Payment of Additional Fees（附加费异议传送）|
| 503 | Method of Identifying Documents Cited in the International Search Report（引用文献标识）|
| 504 | Classification of the Subject Matter（IPC 分类）|
| 505 | Indication of Citations of Particular Relevance（特别相关文献指示）|
| 506 | **[Deleted]**（已删除）|
| 507 | Manner of Indicating Certain Special Categories of Documents |
| 508 | Manner of Indicating the Claims to Which the Documents Cited Relate |
| 509 | International Search and Written Opinion of the International Searching Authority（检索与书面意见，ISPE 联动）|
| 510 | Refund of Search Fee in Case of Withdrawal of International Application |
| 511 | Rectifications of Obvious Mistakes under Rule 91（明显错误更正）|
| 512 | Notifications Concerning Representation |
| 513 | Sequence Listings（序列表）|
| 514 | Authorized Officer（授权官员）|
| 515 | Modification of Abstract in Response to Applicant's Comments |
| 516 | Notification to Applicant of Submission of Demand after Expiration of Time Limit |
| 517 | Waivers under Rules 90.4(d) and 90.5(c) |
| 518 | Guidelines for Explanations Contained in the Written Opinion（书面意见解释指南，ISPE 联动）|
| 519 | Notification of Receipt of Copy of International Application |
| 520 | Withdrawal by Applicant under Rule 90bis.3bis |
| 521 | Minimum Documentation（最低文献操作要求，Annex H）|

#### PART VI: 国际初步审查单位相关（Sections 601-617）

| 节号 | 内容（WIPO PCT/AI/26 原文标题）|
|------|------|
| 601 | Notification to Applicant of Submission of Demand after Expiration of Time Limit |
| 602 | Processing of Amendments by the International Preliminary Examining Authority（Art.34 修改处理）|
| 602bis | Transmittal of Other Documents to the International Bureau |
| 603 | Transmittal of Protest against Payment of Additional Fees |
| 604 | Guidelines for Explanations Contained in the International Preliminary Examination Report（IPER 指南）|
| 605 | File to Be Used for International Preliminary Examination |
| 606 | Cancellation of Elections（选定取消）|
| 607 | Rectifications of Obvious Mistakes under Rule 91（明显错误更正）|
| 608 | Notifications Concerning Representation |
| 609 | Withdrawal by Applicant under Rule 90bis（申请人撤回）|
| 610 | Sequence Listings（序列表）|
| 611 | Method of Identification of Documents in the International Preliminary Examination Report |
| 612 | Authorized Officer（授权官员）|
| 613 | Invitation to Submit a Request for Refund of Fees under Rule 57.4 |
| 614 | Evidence of Right to File Demand |
| 615 | Invitation to Pay Fees before Date on Which They Are Due |
| 616 | International Preliminary Examination on the Basis of a Translation |
| 617 | Waivers under Rules 90.4(d) and 90.5(c) |

#### PART VII: 电子形式申请和处理（Sections 701-716）

| 节号 | 内容（WIPO PCT/AI/26 原文标题）|
|------|------|
| 701 | Abbreviated Expressions（缩略语）|
| 702 | Filing, Processing and Communication in Electronic Form（电子形式提交/处理/通信）|
| 703 | Filing Requirements; Basic Common Standard（提交要求与 Basic 通用标准）|
| 704 | Receipt; International Filing Date; Signature; Physical Requirements（接收/申请日/签名/物理要求）|
| 705 | Home Copy, Record Copy and Search Copy Where International Application Filed in Electronic Form |
| 705bis | Processing in Electronic Form of International Applications（电子形式处理）|
| 705ter | Processing of International Applications Filed in or Scanned in a Pre-Conversion Format |
| 705quater | International Applications Resubmitted in Electronic Form（电子形式重新提交）|
| 706 | Documents in Pre-Conversion Format（转换前格式文件）|
| 707 | Calculation of International Filing Fee and Fee Reduction（国际申请费计算与减免）|
| 708 | Special Provisions Concerning Legibility（可读性特别规定）|
| 709 | Means of Communication with the Applicant（与申请人通信方式）|
| 710 | Notification and Publication of Receiving Offices' Requirements and Practices（受理局要求通知与公布）|
| 711 | Electronic Records Management（电子记录管理）|
| 712 | Access to Electronic Records（电子记录访问）|
| 713 | Application of Provisions to International Authorities and the International Bureau（规定适用）|
| 714 | Furnishing by the International Bureau of Copies of Documents Kept in Electronic Form（IB 提供电子文件副本）|
| 715 | Availability of Priority Documents from Digital Libraries（数字图书馆优先权文件获取）|
| 716 | Request that Priority Document Be Obtained from a Digital Library under Rule 17.1(b-bis) |

#### PART VIII: 第三方观察（Sections 801-805）

| 节号 | 内容（WIPO PCT/AI/26 原文标题）|
|------|------|
| 801 | Third Party Observation System（第三方观察制度）|
| 802 | Filing of a Third Party Observation（提交方式：书面/电子）|
| 803 | Availability of an Observation and Related Information（观察及信息可用性）|
| 804 | Notification of Receipt of an Observation to the Applicant（通知申请人收到观察）|
| 805 | Communication of Observations and Comments to International Authorities and Designated Offices（向国际局/指定局传送观察与意见）|

#### 附件一览

| 附件 | 内容 | 备注 |
|------|------|------|
| Annex A | 标准表格 | 官方未复制，从 WIPO 网站下载：https://www.wipo.int/pct/zh/forms/ |
| Annex B | **发明单一性指南**（Unity of Invention）| 详细判断指南，正文已收录 |
| Annex C | **核苷酸/氨基酸序列表**（ST.26 展示规范）| 正文已收录 |
| Annex D | 公报内容-公告信息（Rule 86.1(i)）| 正文已收录 |
| Annex E | 公报内容-其他信息（Rule 86.1(v)）| 正文已收录 |
| Annex F | ePCT 电子申请标准 | 官方未复制，从 WIPO 网站下载 |
| Annex G | 费用收讫和转付通知（Notification of Receipt and Transfer of Fees）| 正文已收录 |
| Annex H | **最低文献**（Minimum Documentation 技术与可获取性要求）| 正文已收录 |

### 受理局指南（CHAPTER I–XIX + VIIbis；现行 19 章 + ANNEX B）

#### 第1-3章：引言与总则

| 章节 | 内容 |
|------|------|
| 第1章 | 引言 |
| 第2章 | 总则：通信方式、期限计算、邮寄异常宽免 |
| 第3章 | 国家安全审查：受理局须进行国家安全审查 |

#### 第4章：第11条(1)检查与国际申请日（核心）

| 要件组（Art.11(1)） | 检查内容 |
|------|---------|
| ① 申请人资格（Art.11(1)(i)） | 申请人是否不因居所或国籍的原因而明显缺乏向该受理局提出国际申请的权利 |
| ② 语言（Art.11(1)(ii)） | 国际申请是否用规定的语言撰写 |
| ③ 最低内容五项（Art.11(1)(iii)） | (a) 说明是作为国际申请提出的；(b) 至少指定一个缔约国；(c) 按规定方式写明的申请人姓名或名称；(d) 有一部分表面上看像是说明书；(e) 有一部分表面上看像是一项或几项权利要求 |

> ⚠️ **费用缴纳不是申请日要件**：传送费／国际申请费／检索费的缴纳属 Art.14 与细则 Rules 14–16；未在允许期限内缴纳的后果是**视为撤回**（Art.14(3)(a)），不影响国际申请日的给予，也不导致申请日后移。

| 缺陷处理 | 说明 |
|---------|------|
| 缺少说明书或权利要求 | 给予期限补交→以收到日为申请日 |
| 引用并入已有申请 | 依细则Rule 20.5(b)处理 |
| 援引加入 | 依细则Rule 20.6→申请日不后移 |
| 确定申请日 | 满足条件→通知申请人(Form PCT/RO/105) |

#### 第5章：语言检查

| 检查内容 | 说明 |
|---------|------|
| 请求书语言 | 须为受理局接受的语言 |
| 说明书/权利要求语言 | 须与ISA语言要求一致 |
| 摘要/附图文字 | 语言要求 |
| 译文提交 | 如原文不符合语言要求→要求提交译文 |

#### 第6章：第14条检查与形式要求（最详细章节）

| 检查项目 | 说明 |
|---------|------|
| **请求书各栏目** | 申请人/发明人/代理人/指定/签字 |
| **申请人信息** | 姓名/名称+地址+国籍+居所 |
| **发明人信息** | 姓名+地址 |
| **签字** | 申请人或代理人（签字要求） |
| **物理要求** | 纸张/字体/边距/页码 |
| **缺陷改正** | 给予期限补正→通知申请人 |
| **职权改正** | 受理局自行改正(轻微形式缺陷) |
| **视为撤回** | 重大缺陷未在规定期限内改正 |

#### 第7章：优先权

| 事项 | 说明 |
|------|------|
| **优先权声明** | 在先申请日/号/国+在先申请全文 |
| **优先权恢复** | 双标准："适当注意标准"+"故意性标准"(受理局选择适用) |
| **优先权改正** | Rule 26bis.1: 改正优先权声明 |
| **优先权增加** | Rule 26bis.2: 申请日后增加优先权声明 |

#### 第7章之二：国家要求声明(Rule 4.17)

| 声明类型 | 说明 |
|---------|------|
| 发明人身份声明 | 对应美国要求 |
| 申请人资格声明 | 证明有权申请 |
| 优先权资格声明 | 证明有权要求优先权 |
| 新颖性宽限期声明 | 如适用 |

#### 第8章：缺失部分/错误提交项目/援引加入

| 情形 | 处理方式 |
|------|---------|
| **缺失部分** | 申请文件中缺少说明书/权利要求/附图→援引加入 |
| **错误提交项目** | 提交了不完整的部分→替换 |
| **替换页** | 要求提交替换页+说明 |
| **援引加入请求** | 须引用在先申请的对应部分 |

#### 第9章：序列表

| 要求 | 说明 |
|------|------|
| **ST.26格式** | WIPO标准ST.26 XML格式(2022年7月1日起替代ST.25) |
| 提交时限 | 国际申请日时或后续规定期限 |
| 附加费 | 2026年起序列表不计页数(免附加费) |

#### 第10章：生物材料保藏

| 事项 | 说明 |
|------|------|
| 保藏要求 | 布达佩斯条约认可的保藏单位 |
| 说明内容 | 保藏单位+保藏号+保藏日期 |
| 提交期限 | 国际申请日前或同时 |

#### 第11章：费用

| 费用项目 | 期限 | 处理 |
|---------|------|------|
| 传送费 | 国际申请提交时 | 由受理局收取/保留 |
| 国际申请费 | 国际申请提交时 | 由受理局代收→转付国际局 |
| 检索费 | 国际申请提交时 | 由受理局代收→转付ISA |
| 费用不足 | 给予期限补缴→视为撤回(如仍未缴) |

> **CNIPA 受理 PCT 国际阶段具体费用金额（2026年9月标准 · 当前生效，非永久）**：见 `pct-treaty` 费用体系章节「CNIPA 受理 PCT 国际阶段费用标准（2026年9月生效 · 当前标准，将不定期调整）」。该标准非永久性，CNIPA 将因汇率波动等原因不定期调整并另行公布，实际金额以 CNIPA PCT 专栏最新公布为准。本表为受理局处理层面的期限与流转框架，具体金额以该动态标准为准。

#### 第12-13章：副本传送

| 副本 | 接收方 | 时限 |
|------|--------|------|
| 登记本(copy for record) | 国际局(IB) | 受理局在收到申请后尽快传送 |
| 检索本(copy for search) | ISA | 与登记本同时发送 |
| Home副本 | 申请人/受理局 | 由受理局存档 |

#### 第14章：[Deleted]（已删除，不含内容）

#### 第15章：明显错误更正(Rule 91)

| 条件 | 说明 |
|------|------|
| 错误明显 | 明显非申请人的真实意图+明显正确内容 |
| 更正及时 | 在国际公布前提出(公布后更正可能) |
| 更正程序 | 提交更正请求+说明原因+缴纳费用 |

#### 第16章：申请人/发明人/代理人/共同代表变更（Ch.XVI）

| 事项 | 说明 |
|------|------|
| 变更申请人/发明人 | 依 Rule 92bis 提交变更请求（PCT/RO/122 等） |
| 代理人/共同代表变更 | 委任/撤换代理人或指定共同代表 |
| 传送他局更正请求 | 变更请求副本须传送国际局/ISA（段落 307 起） |

#### 第17章：撤回

| 可撤回内容 | 说明 |
|-----------|------|
| 国际申请 | 全部撤回 |
| 指定 | 撤回某个国家的指定 |
| 选定 | 在第II章撤回选定 |
| 优先权要求 | 撤回某个优先权 |

#### 第18章：传送他局事项（Ch.XVIII, Items to Be Transmitted to Another Authority）

| 事项 | 说明 |
|------|------|
| 检索本已传送后的通知 | 若检索本已送 ISA 且发生效力通知，须传送相关文件（段落 323 起） |
| 副本/通知的后续传送 | 受理局向国际局/ISA 补送因后续事件产生的文件 |

#### 第19章：杂项（Ch.XIX, Miscellaneous）

| 事项 | 说明 |
|------|------|
| 不当表述处理（Rule 9） | 申请含贬损性表述/ drawings/statements→依 Rule 9.2 处理，使用 Form PCT/RO/112（抄送 IB 与 ISA） |
| Rule 48.2(l) 信息 | 满足 Rule 48.2(l) 标准的信息记录与处理 |
| ePCT系统 | 电子提交/接收/管理 |
| 国际公布技术准备 | 受理局为国际公布准备的技术工作 |
| 档案保存 | 受理局保存国际申请档案至少10年（Rule 93.1，自国际申请日起算） |

#### 附录B: 11个典型缺陷及改正示例

| # | 缺陷类型 | 改正方法 |
|---|---------|---------|
| 1 | 缺少申请人信息 | 补交申请人姓名/名称 |
| 2 | 缺少发明人信息 | 补交发明人姓名 |
| 3 | 缺少签字 | 补签 |
| 4 | 优先权声明错误 | 改正优先权声明 |
| 5 | 费用不足 | 补缴费用 |
| 6 | 语言不合规 | 提交译文 |
| 7 | 缺少附图 | 援引加入/后补 |
| 8 | 序列表格式错误 | 提交ST.26格式 |
| 9 | 请求书栏目填写错误 | 改正请求书 |
| 10 | 代理人委托书缺失 | 补交委托书 |
| 11 | 物理形式缺陷(纸张等) | 重制文件 |

> 🔴 **CHECKPOINT（表格查询前）**：输出表格信息前确认：①用户所需表格编号（如 PCT/RO/101）②表格用途（请求书/撤回通知/费用催缴等）③适用版本。表格内容以 WIPO 网站最新版本为准。

### 关键表格速查

| 表格编号 | 名称 | 用途 |
|---------|------|------|
| PCT/RO/101 | 国际申请请求书 | 提交PCT国际申请 |
| PCT/RO/102 | 撤回通知 | 撤回国际申请/指定/选定 |
| PCT/RO/103 | 费用催缴通知 | 受理局催缴费用 |
| PCT/RO/105 | 国际申请日确认 | 通知申请人申请日 |
| PCT/RO/106 | 援引加入请求 | 补交遗漏部分 |
| PCT/IB/301 | 国际局通知 | 国际局各种通知 |
| PCT/IB/304 | 优先权文件 | 优先权文件请求 |
| PCT/IB/306 | 国际公布 | 公布通知 |
| PCT/IPEA/401 | 国际初步审查要求书 | 请求第II章审查 |
| PCT/IPEA/402 | 修改附页 | Art.34修改 |

> 所有表格最新版本从WIPO官网下载：https://www.wipo.int/pct/zh/forms/
> ePCT在线提交入口：https://pct.wipo.int/ePCTExternal/pages/EFilingServers.xhtml

### 实务要点

1. **电子申请优先**：通过 ePCT 电子提交可享受国际申请费减免，且简化流程。ePCT EFiling 服务器入口：https://pct.wipo.int/ePCTExternal/pages/EFilingServers.xhtml
2. **援引加入的时效性**：务必在申请日后的规定期限内提交援引加入请求，超过期限则不能再援引。
3. **优先权恢复双标准**：务必确认目标受理局适用"适当注意标准"还是"故意性标准"，不同标准下恢复成功率和策略差异大。
4. **序列表ST.26转换**：自 2022 年 7 月 1 日起 ST.25 格式已不再接受，必须使用 ST.26 XML 格式；2026 年起序列表不另收附加费。
5. **形式缺陷避免**：最常见的缺陷包括：签字缺失/申请人信息不全/优先权声明错误，建议在提交前使用自查清单逐项核对。
6. **第三方观察窗口**：自国际公布日起至优先权日起 28 个月止（《PCT行政规程》Section 802(a)(ii)），可提交第三方观察意见——内容仅限与新颖性和／或创造性相关的现有技术；申请人回应期为优先权日起 30 个月内（Section 804(b)）。

### 失败模式与恢复

| 触发条件 | 一线修复 | 仍失败兜底 |
|---------|---------|-----------|
| 受理局确定申请日时发现缺少说明书或权利要求 | 给予期限补交(以收到日为申请日)→或申请援引加入(申请日不后移) | 引用并入已有申请(Rule 20.5(b))→重新计算申请日 |
| 费用不足导致受理局发出催缴通知(Form PCT/RO/103) | 在催缴期限内补足差额→避免被视为撤回 | 如已视为撤回→申请权利恢复程序 |
| 国际申请提交后漏传送登记本至国际局 | 受理局立即补传→附说明函 | 若登记本已超过国际公布准备时间→紧急联系国际局协调补正 |
| 优先权声明错误(日期/号/国别不一致) | 提交优先权改正请求(Rule 26bis.1)→附优先权证明 | 改正超期→优先权丧失→考虑优先权恢复 |
| 援引加入请求未在规定期限内提交 | 检查是否有宽限规则→尽快补交援引加入请求(PCT/RO/106) | 无法补救→以实际收到补充部分日期为申请日 |
| 第三方观察内容超出允许范围（含与新颖性/创造性无关的评论） | 将超出部分删除→仅保留与新颖性/创造性相关的现有技术（Section 802(a)(v)、(vii)） | 超出部分视为无效→仅处理有效部分 |
| 国家安全审查未通过 | 向受理局反馈→确认是否需要保密处理或修改申请内容 | 保密处理期间暂停国际公布→按国家安全法规定执行 |
| 明显错误更正(Rule 91)请求被驳回 | 确认错误是否"明显"(非申请人真实意图+正确内容明确)→补充更正理由 | 无法更正→保留原文→在国家阶段以修改方式处理 |
| ePCT电子提交文件被系统拒收(格式/病毒/大小超标) | 检查文件格式(推荐PDF)+病毒扫描(AI Section 703(b)(v))+文件大小限制 | 转为书面提交→附电子拒收记录→确保不超期限 |
| 优先权改正请求(Rule 26bis.1)超期提交 | 检查是否有宽限规则→附迟交理由证明 | 超期不可改正→优先权丧失→评估对后续国家阶段的影响 |
| 受理局发现请求书物理形式缺陷(纸张/字体/边距) | 在收到缺陷通知后规定期限内补正缺陷→重新提交符合要求的文件 | 未能在期限内补正→申请视为撤回→申请权利恢复(Rule 49ter) |

### 禁止行为与反例

| # | 禁止行为 | 原因 | 正确做法 |
|---|---|---|---|
| 1 | 提交PCT国际申请时不使用标准表格 | 行政规程Section 102强制要求使用标准化表格体系(PCT/RO/101等) | 从WIPO网站下载最新版标准化表格→按AI Section 102-104填写 |
| 2 | 援引加入的申请部分引用来源不清晰 | 援引加入须明确引用在先申请的具体部分(段号/行号等) | 提交PCT/RO/106表格→详细注明在先申请号+对应部分位置→附在先申请副本 |
| 3 | 序列表仍使用ST.25旧格式 | 自2022年7月1日起ST.25已不被接受，需用ST.26 XML格式 | 将序列表转换为ST.26 XML格式→通过ePCT提交→2026年起可享免附加费 |
| 4 | 优先权恢复未确认受理局适用标准 | 不同受理局选择"适当注意标准"或"故意性标准"，成功率差异大 | 先确认受理局适用标准→针对性地准备恢复理由和证据 |
| 5 | ePCT电子申请不检查文件安全(病毒/恶意代码) | AI Section 703(b)(v)要求电子形式的国际申请须无病毒及其他形式的恶意逻辑；受理局核查程序见 Section 708(b)（原引 709-710 有误：709 为与申请人通信方式、710 为受理局要求通知，均与病毒无关） | 提交前对所有附件进行病毒扫描→确保文件符合安全要求 |
| 6 | 第三方观察在窗口期外提交 | 第三方观察窗口为国际公布日起至优先权日起28个月止（Section 802(a)(ii)） | 确认国际公布日(优先权日起18个月)与优先权日起28个月的窗口期→在窗口期内经ePCT提交 |
| 7 | 受理局发出催缴通知后仅补缴费用但未确认费用到账 | 费用是否到账影响申请状态(如视为撤回)，受理局不单独通知到账 | 补缴后主动联系受理局确认费用到账状态→索取缴费收据 |
| 8 | 明显错误更正(Rule 91)申请理由不充分且超期提交 | Rule 91要求错误"明显"且在公布前提出，理由不充分或超期均会被驳回 | 确认错误的"明显性"(客观标准)→尽快在公布前提交更正请求→附充分理由 |
| 9 | 交付文本使用 Markdown 表格 | 违反输出格式硬约束 | 用标题 + 列表组织交付文本 |
| 10 | 数据缺失时编造或推测 | 违反"无数据回'无'"硬约束 | 直接回复"无"，并提示可补充的检索途径 |
