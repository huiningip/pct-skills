<sub>🌐 <a href="README.md">简体中文</a> · <a href="README.zh-Hant.md">繁體中文</a> · <b>English</b> · <a href="README.fr.md">Français</a> · <a href="README.es.md">Español</a> · <a href="README.ar.md">العربية</a> · <a href="README.ja.md">日本語</a> · <a href="README.ru.md">Русский</a></sub>

<div align="center">

<img src="logo.png" alt="Hui Ning IP" width="150">

# PCT Skills · PCT Patent Practice

> *"Ask once. Get a filing-ready PCT practice answer."*
> *「一句话问清程序，拿回一份能直接用的 PCT 实务方案。」*

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.6.1-blue.svg)](https://github.com/huiningip/PCT-SKILLS)
[![Agent-Agnostic](https://img.shields.io/badge/Agent-Agnostic-blueviolet)](#install)
[![PCT Members](https://img.shields.io/badge/PCT%20Members-159-green)](https://www.wipo.int/treaties/en/registration/pct/)
![No-Fabrication](https://img.shields.io/badge/Principle-No--Fabrication-orange)

<br>

**An end-to-end practical skill set for the PCT international application lifecycle — one parent skill plus five child skills — for patent attorneys, corporate IP teams and applicants working across borders.**

<br>

Not an explainer: it delivers check paths for procedures and deadlines, clause-by-clause verifiable legal sources, a method for reading search and examination conclusions, and formalities for entering the national phase and restoring rights.

Built on the universal Agent Skills format (`<skill-name>/SKILL.md`); works with any agent that supports skills.

[What it does](#what-it-does) · [Install](#install) · [Core mechanisms](#core-mechanisms) · [Repository layout](#repository-layout) · [Limitations](#limitations)

</div>

---

## Install

### Option 1: sync script (recommended)

```bash
# Windows
py -3 scripts/sync_to_local.py

# macOS / Linux
python3 scripts/sync_to_local.py

# Common options
py -3 scripts/sync_to_local.py --dry-run                    # preview, no writes
py -3 scripts/sync_to_local.py --target D:/path/to/skills   # custom skills directory
```

The script syncs the six skills under `skills/` into your local skills directory (default `~/.workbuddy/skills`), one way: new or changed files are overwritten, stale files are removed, and **local metadata such as `_user_meta.json` is preserved**.

### Option 2: manual copy

Copy the skill directories you need from `skills/` into your skills directory (e.g. `~/.workbuddy/skills/`), then restart or reload the app.

> ⚠️ This is a multi-file skill set: the long-form texts under `references/` (treaty, Regulations, Administrative Instructions, search and examination standards, etc.) are referenced from `SKILL.md` via relative `@` paths — **one missing file breaks the chain**. Copy whole directories; do not take `SKILL.md` alone.

## What it does

| Skill | Role | Description |
|------|------|------|
| [`pct-guide`](skills/pct-guide) | Parent skill | Routing hub: dispatches questions to the five practice areas and coordinates across skills |
| [`pct-treaty`](skills/pct-treaty) | Legal source layer | Treaty and Regulations, fee schedules, declarations and reservations — the family's legal baseline |
| [`pct-international-phase`](skills/pct-international-phase) | International phase | Filing, processing, search, publication, Article 19 amendments, Chapter II preliminary examination |
| [`pct-national-phase`](skills/pct-national-phase) | National phase | Entry deadlines and formalities, restoration of rights, PPH and follow-up procedures |
| [`pct-search-examination`](skills/pct-search-examination) | Search & examination | Reading the ISR / written opinion / IPER, minimum documentation, unity of invention |
| [`pct-administrative`](skills/pct-administrative) | Formalities | Administrative Instructions (AI), Receiving Office guide, ePCT and forms |

## Core mechanisms

1. **Parent-skill routing**: ask from any entry point — `pct-guide` first determines the domain, then calls the matching child skill;
2. **Single-point legal source**: dynamic data such as treaty provisions, Regulations and fees converge in `pct-treaty`, avoiding divergent figures across the set;
3. **Progressive disclosure**: long-form texts live in `references/` and load on demand, without blowing up the context window;
4. **"None" when not found**: uncertain information is flagged directly — no invented provisions, deadlines or fee figures.

## Repository layout

```text
PCT-SKILLS/
├── skills/                    # 6 skills (1 parent + 5 children)
│   ├── pct-guide/             #   parent skill: routing hub
│   ├── pct-treaty/            #   legal source layer
│   ├── pct-international-phase/
│   ├── pct-national-phase/
│   ├── pct-search-examination/
│   └── pct-administrative/
├── scripts/
│   └── sync_to_local.py       # one-command sync to your local skills directory
├── README.md                        # 简体中文 (default)
├── README.zh-Hant.md                # 繁體中文
├── README.en.md                     # English (this file)
├── README.fr.md                     # Français
├── README.es.md                     # Español
├── README.ar.md                     # العربية (RTL)
├── README.ja.md                     # 日本語
├── README.ru.md                     # Русский
├── LICENSE                          # MIT License
└── logo.png                         # Brand mark (README header)
```

- Skill directories are strictly **2 levels deep** (`SKILL.md` + `references/`), compliant with the official WorkBuddy skill structure;
- Skill files: **CRLF, UTF-8 without BOM**.

## Data and provenance

- Legal sources follow the **current official WIPO / CNIPA versions**; each skill records its legal-as-of date;
- For volatile data (fees, deadlines), re-check the latest official announcements before use in a case file;
- Output is practice reference only — **not legal advice**.

## Limitations

- No substitute for official or case-specific judgment: deadlines, fees and procedural conclusions are governed by the receiving Office's notices and official announcements;
- No fabrication: data that cannot be found is answered as "none";
- Legal coverage focuses on the PCT treaty and procedure layer; the substantive law and examination practice of each designated Office follow that Office's official positions.

## License

[MIT](LICENSE) © 2026 Hui Ning IP（辉宁知识产权）.

- The skill content itself (curation and annotations in `SKILL.md` and `references/`) is under MIT;
- Official WIPO texts reproduced or quoted in `references/` (Treaty, Regulations, Administrative Instructions, etc.) remain the property of WIPO and are not covered by this license.

## Contact

- Questions and suggestions: open an Issue in this repository;
- Built and maintained by Hui Ning IP (a Chinese patent attorney team).
