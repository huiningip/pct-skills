# pct-administrative 版本历史（完整）

> 本文件为 `pct-administrative` 技能的**完整版本历史**。依据官方技能开发文档的渐进式披露原则，`SKILL.md` 的 frontmatter `update-log` 仅保留最近三版，更早版本的历史归档于此。
> 版本号唯一权威来源：`SKILL.md` frontmatter 的 `version` 字段。
>
> ⚠️ **归档说明**：本技能 2.3.2 之前的 `update-log` 采用**日期条目制**而非版本号制，版本号与各日期条目的对应关系未在原档留存。为避免编造，本文件**保持日期条目原样归档，不回填版本号**。

---

## 2.3.2（2026-09-21）开发文档合规化 + 法源订正

依据 <https://open.workbuddy.cn/docs/skill> 对 frontmatter 与文件结构做合规化改造，并订正三类法源错误（共 6 处）。

**frontmatter**

- 补齐文档列明的展示字段：`display_name`（PCT行政规程与受理局实务）、`display_name_en`（PCT Administrative Instructions & Receiving Office Practice）、`description_zh`、`description_en`、`category: legal`。
- 新增 `related-skills` 联动声明（pct-guide / pct-treaty / pct-search-examination / pct-international-phase / pct-national-phase）。
- 新增 `allowed-tools` 注释，载明未启用的理由。
- `update-log` 精简为最近三版，更早历史迁入本文件。

**结构**

- 标题层级修正：原「技能知识库（内部参考，不受输出禁表格约束）」误用**同级 H1**（全文出现两个 H1），降为 H2，其下 35 个各级子标题同步下移一级。

**法源订正（★★★）— 申请日要件（规则第 10 条）**

原表述：

> **申请日三条件**（Art.11）：①明确或暗示指明国家 ②指定申请人 ③包含说明书 + 权利要求 + **费用缴纳**。

经 `references/PCT_TREATY_2026.md` 条约第 11 条(1) 原文核验，存在三项错误：

1. **费用缴纳并非申请日要件**——费用属 Art.14 及细则 Rules 14–16 的范围；未按期缴纳的后果是该申请**视为撤回**，既不影响国际申请日的给予，也不导致申请日后移。
2. **遗漏「说明是作为国际申请提出的」**——此为 Art.11(1)(iii)(a) 的第一项最低内容要求。
3. **遗漏语言要求与申请人资格**——Art.11(1)(i) 申请人不得因居所或国籍明显缺乏提出国际申请的权利；Art.11(1)(ii) 须使用规定语言撰写。

已按 Art.11(1)(i)–(iii) 重写为**三组要件**（①申请人资格 ②语言 ③最低内容五项 a–e），并补 Art.11(2) 的改正机制（以收到必要改正之日为国际申请日）。

**法源订正（★★）— 第三方观察窗口（规则第 7 条）**

原表述「仅限国际公布后**至国家阶段启动前**」与《PCT行政规程》Section 802(a)(ii) 不符。原文：

> be submitted **between the date of international publication and 28 months from the priority date** of the international application indicated

已更正为「自国际公布日起至**优先权日起 28 个月**止」，并补：内容限与新颖性和／或创造性相关的现有技术（Section 802(a)(v)、(vii)）；IB 通知申请人后，申请人可在**优先权日起 30 个月**内提交回应意见（Section 804(b)）。

**法源订正（★★）— 电子申请病毒检测（共 4 处）**

原表述（模板 B、规则第 6 条、失败模式表、禁止行为表各 1 处）称「**AI Sections 709-710** 要求电子提交文件须通过病毒检测」。经 `references/ADMIN_INSTRUCTIONS_2026.md` 原文核验：

- **Section 709** — *Means of Communication with the Applicant*（与申请人通信的方式）；
- **Section 710** — *Notification and Publication of Receiving Offices' Requirements and Practices*（受理局要求的通知与公布）；

**两者均与病毒检测无关**。正确的法源为：

- **Section 703(b)(v)** — 电子形式的国际申请须「*free of viruses and other forms of malicious logic*」，依 Annex F 或基本通用标准；
- **Section 708(b)** — 受理局收到电子形式申请后应即时核查病毒感染，并据此决定是否接收（Section 703(e)）、是否给予申请日，以及自制本／登记本／检索本的制备基础；
- （另见 **Section 802(a)(vi)** — 第三方观察文件同样须无病毒。）

**计数精确化（★）**

- 《PCT受理局指南》结构描述原写「19 章（**含**第 XIV 章**已删除**、第 VIIbis 章国家要求声明）+ 2 附录（**Annex A 已删除**、Annex B 典型缺陷示例）」——「19 章」与「含已删除的 XIV 章」自相矛盾，「2 附录」亦把已删除的 ANNEX A 计入。经 `references/RO_GUIDE_2026.md` 的 TOC 锚点核验，更正为：**章号 CHAPTER I–XIX + CHAPTER VIIbis（共 20 个章号，其中 CHAPTER XIV 已删除，现行 19 章）＋ 附录 ANNEX B（ANNEX A 已删除，现行 1 个）**。
- 第 4 级小节标题「受理局指南（19章+2附录）」同步精确化为「受理局指南（CHAPTER I–XIX + VIIbis；现行 19 章 + ANNEX B）」。
- 典型提问示例中「Art.11 三要件」改为「Art.11(1) 三组要件」。

**引用语法标准化**

`references/` 引用由反引号路径改为官方文档规定的 `@references/` 语法（4 处）。

---

## 2026-08-26

第 11 章费用补引 CNIPA 2026 年 9 月标准指针：交叉引用 `pct-treaty` 费用体系章节「CNIPA 受理 PCT 国际阶段费用标准（2026年9月生效 · 当前标准，将不定期调整）」；本技能第 11 章费用表保持受理局处理层面的**期限与流转框架**，具体金额以 `pct-treaty` 该（动态）标准为准；该标准非永久，CNIPA 将因汇率波动不定期调整，引用指针已同步标注「以 CNIPA 最新公布为准」。

## 2026-08-23（一）收录《PCT行政规程》原文结构化转换

- 新增 `references/ADMIN_INSTRUCTIONS_2026.md`（WIPO *PCT/AI/26*，as in force 2026-01-01）：105 页 / 8 Part / 180 Section（含 18 个 bis·ter·quater 变体）/ 8 Annex / 105 个逐页溯源标记 / 零乱码。
- 重写「行政规程（8 部分）」结构表，以与官方原文标题**逐一对应**。

## 2026-08-23（二）修复行政规程结构表系统性偏差

- **Part 1**（101–116）原归类错误：107–111 原标「期限计算」→ 实为主管局标识／通信／日期／Rule 82quater 宽免；112–114 原标「文件格式」→ 实为效力终止／特别费／费用转付。
- **Part 2**（201–218）补 204bis、210 `[Deleted]`、202 `[Deleted]`。
- **Part 3**（301–337）纠正三处：「310–315 援引加入」→ 实为后交页与优先权改正（314）；「316–317 Rule 91」→ 实为 325／327；「323–327 国家安全审查」→ 实属 RO Guide 第 3 章。
- **Part 4** 补 426–429 官方空号说明。
- **Part 5** 补 501／506 `[Deleted]`。
- **Part 7** 补 705bis／ter／quater。

## 2026-08-22（一）收录《PCT受理局指南》原文结构化转换

- 新增 `references/RO_GUIDE_2026.md`（WIPO *PCT/GL/RO/22*，as in force 2025-07-01）：93 页 / 333 个段落锚点 / 86 个逐页溯源标记 / 零乱码。
- 知识库首部加原文指针。

## 2026-08-22（二）修复「受理局指南（19章+2附录）」结构表遗漏

- 补第 14 章 `[Deleted]` 标注、第 16 章（申请人／发明人／代理人变更）、第 18 章（传送他局事项）。
- 第 19 章概括补全：Rule 9 不当表述（Form PCT/RO/112）／Rule 48.2(l) 信息／Rule 93.1 档案保存年限。
- 上下文 RO Guide 描述同步。

## 2026-08-22（三）交叉引用补充

适用边界段补引 WIPO《声明保留和不兼容》页面及 `pct-treaty` 对应章节，覆盖各缔约国就细则／行政规程条款（如 Rule 20.8、49ter、4.9(b)）作出的不兼容通知溯源。

## 2026-08-13

新增「提问指引与预期管理」小节（典型提问示例 + 操作模板／样例 + 边界与降级回应），回应 SkillHub TRACE 评测在 R／A／C 三项的能力短板（缺示例与预期管理）；并补本 update-log。

---

## 2.0.0 及更早

早期版本记录未留存于本技能档案（2.0.0 前的迭代在家族重构时并入 `pct-guide` 母技能体系）。如需追溯，参见 `pct-guide` 的对应版本记录。
