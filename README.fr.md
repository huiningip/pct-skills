🌐 简体中文 · 繁體中文 · English · Français · Español · العربية · 日本語 · Русский

# PCT Skills · Pratique des brevets PCT

> *« Une question. Une réponse de pratique PCT directement exploitable. »*
> *"Ask once. Get a filing-ready PCT practice answer."*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Agent-Agnostic](https://img.shields.io/badge/Agent-Agnostic-blue.svg)](https://github.com/huiningip/PCT-SKILLS)

Un ensemble de compétences pratiques couvrant tout le cycle de la demande internationale PCT — **une compétence parente + 5 compétences filles** — pour les **conseils en brevets, les équipes PI d'entreprise et les déposants à l'étranger**. Pas une vulgarisation : des parcours de vérification des procédures et des délais, des sources juridiques vérifiables clause par clause, une méthode de lecture des conclusions de recherche et d'examen, et les formalités d'entrée en phase nationale et de rétablissement des droits.

Basé sur le format universel Agent Skills (`<skill-name>/SKILL.md`) ; compatible avec tout agent prenant en charge les skills.

## Installation

### Méthode 1 : script de synchronisation (recommandé)

```bash
# Windows
py -3 scripts/sync_to_local.py

# macOS / Linux
python3 scripts/sync_to_local.py

# Options courantes
py -3 scripts/sync_to_local.py --dry-run                    # simulation, aucune écriture
py -3 scripts/sync_to_local.py --target D:/path/to/skills   # répertoire de skills personnalisé
```

Le script synchronise les 6 skills de `skills/` vers votre répertoire local de skills (par défaut `~/.workbuddy/skills`), en sens unique : les fichiers nouveaux ou modifiés sont écrasés, les fichiers obsolètes supprimés, et **les métadonnées locales (`_user_meta.json`, etc.) sont préservées**.

### Méthode 2 : copie manuelle

Copiez les répertoires de skills nécessaires depuis `skills/` vers votre répertoire de skills (p. ex. `~/.workbuddy/skills/`), puis redémarrez ou rechargez l'application.

> ⚠️ Il s'agit d'un ensemble multi-fichiers : les textes longs sous `references/` (traité, Règlement d'exécution, Instructions administratives, normes de recherche et d'examen, etc.) sont référencés depuis `SKILL.md` par des chemins relatifs `@` — **un fichier manquant casse la chaîne**. Copiez les répertoires en entier ; ne prenez pas seulement `SKILL.md`.

## Ce que cela fait

| Skill | Rôle | Description |
|------|------|------|
| [`pct-guide`](skills/pct-guide) | Compétence parente | Hub de routage : oriente chaque question vers l'un des cinq domaines et coordonne les skills |
| [`pct-treaty`](skills/pct-treaty) | Couche des sources juridiques | Traité et Règlement d'exécution, barèmes de taxes, déclarations et réserves — la base juridique de la famille |
| [`pct-international-phase`](skills/pct-international-phase) | Phase internationale | Dépôt, traitement, recherche, publication, modifications de l'article 19, examen préliminaire du chapitre II |
| [`pct-national-phase`](skills/pct-national-phase) | Phase nationale | Délais et formalités d'entrée, rétablissement des droits, PPH et procédures ultérieures |
| [`pct-search-examination`](skills/pct-search-examination) | Recherche et examen | Lecture du ISR / de l'opinion écrite / du IPER, documentation minimale, unité d'invention |
| [`pct-administrative`](skills/pct-administrative) | Formalités | Instructions administratives (AI), guide de l'office récepteur, ePCT et formulaires |

## Mécanismes clés

1. **Routage par la compétence parente** : posez la question depuis n'importe quel point d'entrée — `pct-guide` détermine d'abord le domaine, puis appelle la compétence fille correspondante ;
2. **Source juridique à point unique** : les données dynamiques (dispositions du traité, Règlement, taxes) sont regroupées dans `pct-treaty`, évitant toute divergence de chiffres entre plusieurs endroits ;
3. **Divulgation progressive** : les textes longs vivent dans `references/` et se chargent à la demande, sans saturer le contexte ;
4. **« Aucun » plutôt qu'inventer** : toute information incertaine est signalée telle quelle — aucune disposition, aucun délai, aucun montant inventé.

## Structure du dépôt

```text
PCT-SKILLS/
├── skills/                    # 6 skills (1 parente + 5 filles)
│   ├── pct-guide/             #   compétence parente : hub de routage
│   ├── pct-treaty/            #   couche des sources juridiques
│   ├── pct-international-phase/
│   ├── pct-national-phase/
│   ├── pct-search-examination/
│   └── pct-administrative/
├── scripts/
│   └── sync_to_local.py       # synchronisation en une commande vers vos skills locaux
├── README.md
└── LICENSE
```

- Répertoires de skills strictement sur **2 niveaux** (`SKILL.md` + `references/`), conformes à la structure officielle des skills WorkBuddy ;
- Fichiers de skills : **CRLF, UTF-8 sans BOM**.

## Données et provenance

- Les sources juridiques suivent les **versions officielles en vigueur de l'OMPI / CNIPA** ; chaque skill indique sa date d'arrêté ;
- Pour les données volatiles (taxes, délais), revérifiez les annonces officielles les plus récentes avant tout usage au dossier ;
- La sortie est une référence pratique — **elle ne constitue pas un avis juridique**.

## Limites

- Ne remplace ni les instances officielles ni l'appréciation au cas par cas : délais, taxes et conclusions procédurales relèvent des notifications de l'office récepteur et des annonces officielles ;
- Aucune invention : les données introuvables sont rendues par « aucune » ;
- La couverture juridique porte sur le traité PCT et l'étage procédural ; le droit matériel et la pratique d'examen de chaque office désigné relèvent des positions officielles de cet office.

## License

[MIT](LICENSE) © 2026 Hui Ning IP（辉宁知识产权）.

- Le contenu propre des skills (organisation et annotations dans `SKILL.md` et `references/`) est sous licence MIT ;
- Les textes officiels de l'OMPI reproduits ou cités dans `references/` (traité, Règlement d'exécution, Instructions administratives, etc.) restent la propriété de l'OMPI et ne sont pas couverts par cette licence.

## Contact

- Questions et suggestions : ouvrez une Issue dans ce dépôt ;
- Construit et maintenu par Hui Ning IP (une équipe chinoise de conseils en brevets).
