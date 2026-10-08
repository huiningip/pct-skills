🌐 简体中文 · 繁體中文 · English · Français · Español · العربية · 日本語 · Русский

# PCT Skills · PCT 專利實務技能集

> *「一句話問清程序，拿回一份能直接用的 PCT 實務方案。」*
> *"Ask once. Get a filing-ready PCT practice answer."*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Agent-Agnostic](https://img.shields.io/badge/Agent-Agnostic-blue.svg)](https://github.com/huiningip/PCT-SKILLS)

一個面向**涉外專利代理師、企業 IPR 與涉外申請人**的 PCT 國際申請全流程實務技能集（母技能 + 5 個子技能）。不是科普問答，而是：流程與期限的檢查路徑、逐條可核的法源依據、檢索與審查結論的解讀方法、國家階段進入與恢復的手續方案。

技能遵循通用 Agent Skills 格式（`<skill-name>/SKILL.md`），支援 skills 的 agent 均可使用。

## 裝上就能用

### 方式一：同步腳本（推薦）

```bash
# Windows
py -3 scripts/sync_to_local.py

# macOS / Linux
python3 scripts/sync_to_local.py

# 常用參數
py -3 scripts/sync_to_local.py --dry-run                    # 預演，不寫入
py -3 scripts/sync_to_local.py --target D:/path/to/skills   # 指定技能目錄
```

腳本會把 `skills/` 下的 6 個技能單向同步到本機技能目錄（預設 `~/.workbuddy/skills`）：新增／變更的檔案會覆寫、過時檔案會清除，**本機中繼資料（`_user_meta.json` 等）自動保留**。

### 方式二：手動複製

把 `skills/` 下需要的技能目錄整份複製到你的技能目錄（如 `~/.workbuddy/skills/`），然後重新啟動或重新載入應用程式。

> ⚠️ 這是多檔案技能集：`references/` 下的大部頭原文（條約、實施細則、行政規程、檢索審查標準等）由 `SKILL.md` 以 `@` 相對路徑引用，**缺一即斷鏈**——請整目錄複製，勿只取 `SKILL.md`。

## 能做什麼

| 技能 | 定位 | 說明 |
|------|------|------|
| [`pct-guide`](skills/pct-guide) | 母技能 | 路由中樞：按問題自動分派五大實務領域，跨技能協調 |
| [`pct-treaty`](skills/pct-treaty) | 法源層 | 條約與實施細則、費用標準、聲明保留——全族法源基準 |
| [`pct-international-phase`](skills/pct-international-phase) | 國際階段 | 提交、受理、檢索、公布、第 19 條修改、第 II 章初審 |
| [`pct-national-phase`](skills/pct-national-phase) | 國家階段 | 進入期限與手續、權利恢復、PPH 與後續程序 |
| [`pct-search-examination`](skills/pct-search-examination) | 檢索審查 | ISR／書面意見／IPER 解讀、最低文獻、發明單一性 |
| [`pct-administrative`](skills/pct-administrative) | 操作規範 | 行政規程（AI）、受理局指南、ePCT 與表格 |

## 核心機制

1. **母技能路由**：任意入口提問，`pct-guide` 先判定領域，再呼叫對應子技能；
2. **法源單點維護**：條約、細則、費用等動態資料統一收斂在 `pct-treaty`，避免多處口徑漂移；
3. **漸進式披露**：大部頭原文放在 `references/`，按需載入，不撐上下文；
4. **查不到就回「無」**：無把握的資訊直接標註，不編造條款、期限與費用數字。

## 倉庫結構

```text
PCT-SKILLS/
├── skills/                    # 6 個技能（母 + 5 子）
│   ├── pct-guide/             #   母技能：路由中樞
│   ├── pct-treaty/            #   法源層
│   ├── pct-international-phase/
│   ├── pct-national-phase/
│   ├── pct-search-examination/
│   └── pct-administrative/
├── scripts/
│   └── sync_to_local.py       # 一鍵同步到本機技能目錄
├── README.md
└── LICENSE
```

- 技能目錄嚴格 **2 級**（`SKILL.md` + `references/`），符合 WorkBuddy 官方技能結構規範；
- 技能檔案約定：**CRLF、UTF-8 無 BOM**。

## 資料與時效

- 法源以 **WIPO / CNIPA 官方現行版本**為準，各技能內標註法源基準日；
- 易變資料（費用、期限）請以官方最新公告複核後再用於案卷；
- 輸出為實務參考，**不構成法律意見**。

## 能力邊界

- 不替代官方與個案判斷：期限、費用與程序結論以受理局通知與官方公告為準；
- 不做編造：查不到的資料直接回「無」；
- 法源聚焦 PCT 條約與規程層面；各指定局本國實體法與審查實務以其官方口徑為準。

## License

[MIT](LICENSE) © 2026 輝寧知識產權（Hui Ning IP）。

- 技能自身內容（`SKILL.md`、`references/` 內的整理與註解）適用 MIT；
- `references/` 中收錄／轉引的 WIPO 官方文本（條約、實施細則、行政規程等）版權歸 WIPO 所有，不受本協議覆蓋。

## 聯絡

- 問題與建議：歡迎在倉庫提 Issue；
- 由 輝寧知識產權（中國專利代理師團隊）構建與維護。
