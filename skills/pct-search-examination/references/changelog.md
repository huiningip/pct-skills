# pct-search-examination 版本历史（完整）

> 本文件为 `pct-search-examination` 技能的**完整版本历史**。依据官方技能开发文档的渐进式披露原则，`SKILL.md` 的 frontmatter `update-log` 仅保留最近三个版本，更早版本的历史归档于此。
> 版本号唯一权威来源：`SKILL.md` frontmatter 的 `version` 字段。

---

## 2.3.0（2026-09-21）开发文档合规化 + 法源订正

依据 <https://open.workbuddy.cn/docs/skill> 对 frontmatter 与文件结构做合规化改造，并订正一处引用已删除节号的错误法源、两处内部不一致。

**frontmatter**

- 补齐文档列明的展示字段：`display_name`（PCT国际检索与初步审查指南）、`display_name_en`（PCT International Search & Preliminary Examination (ISPE)）、`description_zh`、`description_en`、`category: legal`。
- 新增 `related-skills` 联动声明（pct-guide / pct-treaty / pct-administrative / pct-international-phase / patent-exam-pct-national / patent-exam-substantive）。
- 新增 `allowed-tools` 注释，载明未启用的理由。
- `update-log` 精简为最近三版，完整历史迁入本文件。

**结构**

- 标题层级修正：原「技能知识库（内部参考，不受输出禁表格约束）」误用**同级 H1**（全文出现两个 H1），降为 H2，其下 20 个各级子标题同步下移一级。

**法源订正（★★）**

规则第 4 条原将引文分类的法源写为「Admin Instructions 505/506/507」。经 `references/ADMIN_INSTRUCTIONS_2026.md`（PCT/AI/26）原文核验：

- **Section 505** — Indication of Citations of Particular Relevance in the International Search Report；
- **Section 506** — **`[Deleted]`（现行版已删除）**；
- **Section 507** — Manner of Indicating Certain Special Categories of Documents Cited in the International Search Report。

原表述引用了**已删除的节号**。经 **ISPE §16.65** 与 `references/ADMIN_INSTRUCTIONS_2026.md` **双向交叉验证**后细化更正为：

- **Section 505** — Indication of Citations of Particular Relevance（特别相关文献：X／Y）；
- **Section 507** — Manner of Indicating Certain Special Categories of Documents Cited in the International Search Report，其子项与类别对应关系为 **507(a) O ／ 507(b) E ／ 507(c) A ／ 507(d) P ／ 507(e) T ／ 507(f) L**；
- **Section 503** — Method of Identifying Documents Cited in the International Search Report（引用文献的标识方式）；
- **Section 506 已删除**（`[Deleted]`），不得再引。

旁证：ISPE §16.65 原文「…details of which are given in **Administrative Instructions 505 and 507**」，与上述结论一致。

**内部不一致订正（★，两处）**

- 「任务」栏引文分类原列「X/Y/A/P/O/T/E/&」共 **7 类**，与本文档规则第 4 条、快速参考卡片及 PART IV 引文分类表的 **9 类**不符（2.2.0 引入 D、L 时遗漏此处），补齐为 10 个符号 / 9 类。
- 快速参考卡片「WO/ISA 栏目填写规范」仅列栏 I–III，与 PART V 的栏 I–VIII 不符，补全至栏 VIII 并标注各栏适用阶段。

**引用语法标准化**

`references/ISPE_2026.md` 引用由反引号路径改为官方文档规定的 `@references/` 语法。

---

## 2.2.1（2026-08-23）发明单一性示例数二次订正

- 复查发现 ISPE Ch.10 发明单一性示例数描述与官方不符（原写「54 个 Example」）。
- 经核验官方 MD 实际为 **48 个独立 Example**（编号 1–48，全文出现 63 次含重复引用）；
- 全局 **7 处**修正为「48个Example（2026版 ISPE/14 Ch.10 编号 1–48）」。
- ISPE 章节归属／第三方意见法源／Ch.18 标题等其余写进技能的内容，经复查与官方一致。

---

## 2.2.0（2026-08-22）依据 ISPE 原文逐章对照核查，修复 7 项错漏

- **★★★** 发明单一性「43 个案例」过时数字全局更正为「50+ 示例（2026 版 ISPE/14 Ch.10 含 48 个 Example，编号 1–48）」（**11 处**）。
- **★★★** PART VI 第 18 章误标「语言要求」→ 改为「收到要求书后的初步程序（Preliminary Procedure on Receipt of the Demand），语言／译文要求散见其中」（Part VI 无语言要求专章）。
- **★★** 第三方意见小节从 PART VIII 移至 PART V（Ch.17）之下，并明确 ISPE 第 22 章不讨论此主题、真实法源 = 行政规程 Part 8（801–805）；PART VIII 改为交叉引用。
- **★★** 引文分类补 D（申请中已引证）、L（其他理由／质疑优先权）两类，共 9 类（Ch.16.65–16.75）。
- **★** WO/ISA / IPER 栏位补 Box VIII（Certain Observations），原栏 I–VII → I–VIII。
- **★** IPER 时限改精确：「原则上优先权日起 28 个月，以三者最晚届满为准（Rule 69.2：①28 月 ②审查启动后 6 月 ③译文收到后 6 月）」。
- **★** 补充国际检索（SISA）归位至 Ch.15（§15.75–15.97），非第 16 章（PART IV 结构表与说明同步）。

---

## 2.1.0（2026-08-22）补第三方意见（Third Party Observations）章节

- 澄清 PCT 国际阶段**无「protest／异议」程序**（前次 TRACE 自测所记 Rule 40.2(c) / 68.3(e) 为**误判，已更正**）。
- 正确法源为 **PCT 行政规程 Part 8（第 801–805 节）**，含提交窗口（公布后至 28 个月）、ePCT 匿名提交、对 ISR/IPER 影响、申请人 30 个月评论期、GL/ISPE 15.68 / 16.57 / 17.69 指引。
- 在 PART V（书面意见／IPER）与 PART VIII（行政程序）两处交叉引用。

---

## 2.0.0 及更早

早期版本记录未留存于本技能档案（2.0.0 前的迭代在家族重构时并入 `pct-guide` 母技能体系）。如需追溯，参见 `pct-guide` 的对应版本记录。
