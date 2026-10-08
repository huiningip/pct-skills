🌐 [简体中文](README.md) · [繁體中文](README.zh-Hant.md) · [English](README.en.md) · [Français](README.fr.md) · [Español](README.es.md) · [العربية](README.ar.md) · [日本語](README.ja.md) · [Русский](README.ru.md)

# PCT Skills · PCT 特許実務スキル集

> *「ひとこと聞けば、そのまま案件に使える PCT 実務の回答が返ってくる。」*
> *"Ask once. Get a filing-ready PCT practice answer."*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Agent-Agnostic](https://img.shields.io/badge/Agent-Agnostic-blue.svg)](https://github.com/huiningip/PCT-SKILLS)

PCT 国際出願の全工程をカバーする実務スキル集です（**親スキル 1 つ＋子スキル 5 つ**）。対象は**渉外特許代理師、企業の IP 担当、海外出願を行う出願人**。解説記事ではなく、手続と期限の確認手順、一条ずつ照合できる法源、サーチ・審査結論の読み解き方、国内段階への移行と権利回復の手続を提供します。

汎用の Agent Skills 形式（`<skill-name>/SKILL.md`）に準拠し、skills に対応する任意のエージェントで使用できます。

## インストール

### 方法1：同期スクリプト（推奨）

```bash
# Windows
py -3 scripts/sync_to_local.py

# macOS / Linux
python3 scripts/sync_to_local.py

# よく使うオプション
py -3 scripts/sync_to_local.py --dry-run                    # 事前確認のみ、書き込みなし
py -3 scripts/sync_to_local.py --target D:/path/to/skills   # 任意のスキルディレクトリを指定
```

スクリプトは `skills/` 配下の 6 つのスキルを、ローカルのスキルディレクトリ（既定：`~/.workbuddy/skills`）へ一方向に同期します。新規・変更ファイルは上書き、古いファイルは削除され、**本機のメタデータ（`_user_meta.json` など）は自動的に保持されます**。

### 方法2：手動コピー

`skills/` 配下の必要なスキルディレクトリを、お使いのスキルディレクトリ（例：`~/.workbuddy/skills/`）へ丸ごとコピーし、アプリを再起動または再読み込みしてください。

> ⚠️ これは複数ファイル構成のスキル集です。`references/` 配下の大部な原文（条約、実施細則、行政指針、サーチ・審査基準など）は `SKILL.md` から `@` の相対パスで参照されています——**1 ファイル欠けるだけで参照チェーンが切れます**。必ずディレクトリごとコピーし、`SKILL.md` だけを取らないでください。

## できること

| スキル | 位置づけ | 説明 |
|------|------|------|
| [`pct-guide`](skills/pct-guide) | 親スキル | ルーティングハブ：質問を 5 つの実務領域へ振り分け、スキル間を調整 |
| [`pct-treaty`](skills/pct-treaty) | 法源レイヤー | 条約と実施細則、費用基準、宣言・留保——一族の法源基盤 |
| [`pct-international-phase`](skills/pct-international-phase) | 国際段階 | 提出、受理、サーチ、公開、第 19 条補正、第 II 章予備審査 |
| [`pct-national-phase`](skills/pct-national-phase) | 国内段階 | 移行期限と手続、権利回復、PPH とその後の手続 |
| [`pct-search-examination`](skills/pct-search-examination) | サーチ・審査 | ISR／見解書／IPER の読み解き、最低限の文献、発明の単一性 |
| [`pct-administrative`](skills/pct-administrative) | 手続・様式 | 行政指針（AI）、受理官庁ガイド、ePCT と様式 |

## 中核メカニズム

1. **親スキルによるルーティング**：どの入口から質問しても、まず `pct-guide` が領域を判定し、対応する子スキルを呼び出します；
2. **法源の一点管理**：条約・細則・費用などの動的データは `pct-treaty` に集約し、箇所ごとの数値のずれを防ぎます；
3. **段階的開示**：大部な原文は `references/` に置き、必要時に読み込み、コンテキストを圧迫しません；
4. **見つからなければ「無」**：不確かな情報はそのまま明示し、条文・期限・費用の数字を捏造しません。

## リポジトリ構成

```text
PCT-SKILLS/
├── skills/                    # 6 スキル（親 1 + 子 5）
│   ├── pct-guide/             #   親スキル：ルーティングハブ
│   ├── pct-treaty/            #   法源レイヤー
│   ├── pct-international-phase/
│   ├── pct-national-phase/
│   ├── pct-search-examination/
│   └── pct-administrative/
├── scripts/
│   └── sync_to_local.py       # ワンコマンドでローカルのスキルディレクトリへ同期
├── README.md
└── LICENSE
```

- スキルのディレクトリは厳密に **2 階層**（`SKILL.md` ＋ `references/`）で、WorkBuddy 公式のスキル構造に準拠しています；
- スキルファイルの約束：**CRLF、UTF-8（BOM なし）**。

## データと出所

- 法源は **WIPO／CNIPA の現行公式版**に準拠し、各スキルに法源の基準日を記載しています；
- 変動データ（費用・期限）は、案件で使用する前に最新の公式公告で再確認してください；
- 出力は実務上の参考であり、**法的意見ではありません**。

## 適用範囲と限界

- 公式の判断や個別案件の判断を代替しません：期限・費用・手続の結論は受理官庁の通知と公式公告に従います；
- 捏造しません：見つからないデータは「無」とそのまま回答します；
- 法源は PCT 条約と手続層に焦点を当てています。各指定官庁の国内実体法と審査実務は、その官庁の公式見解に従います。

## License

[MIT](LICENSE) © 2026 Hui Ning IP（辉宁知识产权）.

- スキル自体の内容（`SKILL.md` と `references/` 内の整理・注記）には MIT が適用されます；
- `references/` に収録・引用した WIPO 公式テキスト（条約、実施細則、行政指針など）の著作権は WIPO に帰属し、本ライセンスの対象外です。

## 連絡先

- 質問・提案：本リポジトリの Issue へどうぞ；
- Hui Ning IP（中国の特許代理師チーム）が構築・維持しています。
