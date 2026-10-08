🌐 简体中文 · 繁體中文 · English · Français · Español · العربية · 日本語 · Русский

# PCT Skills · Práctica de patentes PCT

> *«Una sola pregunta. Una respuesta de práctica PCT lista para el expediente.»*
> *"Ask once. Get a filing-ready PCT practice answer."*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Agent-Agnostic](https://img.shields.io/badge/Agent-Agnostic-blue.svg)](https://github.com/huiningip/PCT-SKILLS)

Un conjunto de habilidades prácticas que cubre todo el ciclo de la solicitud internacional PCT — **una habilidad principal + 5 habilidades secundarias** — para **agentes de patentes, equipos de PI de empresa y solicitantes en el extranjero**. No es una explicación divulgativa: ofrece rutas de verificación de trámites y plazos, fuentes jurídicas verificables cláusula por cláusula, un método para leer las conclusiones de búsqueda y examen, y los trámites de entrada y restablecimiento de derechos en la fase nacional.

Basado en el formato universal Agent Skills (`<skill-name>/SKILL.md`); funciona con cualquier agente compatible con skills.

## Instalación

### Opción 1: script de sincronización (recomendado)

```bash
# Windows
py -3 scripts/sync_to_local.py

# macOS / Linux
python3 scripts/sync_to_local.py

# Opciones habituales
py -3 scripts/sync_to_local.py --dry-run                    # simulación, sin escrituras
py -3 scripts/sync_to_local.py --target D:/path/to/skills   # directorio de skills personalizado
```

El script sincroniza las 6 habilidades de `skills/` hacia tu directorio local de skills (por defecto `~/.workbuddy/skills`), en un solo sentido: los archivos nuevos o modificados se sobrescriben, los obsoletos se eliminan y **los metadatos locales (`_user_meta.json`, etc.) se conservan**.

### Opción 2: copia manual

Copia los directorios de habilidades que necesites desde `skills/` a tu directorio de skills (p. ej. `~/.workbuddy/skills/`) y, a continuación, reinicia o recarga la aplicación.

> ⚠️ Es un conjunto de varios archivos: los textos extensos de `references/` (tratado, Reglamento, Instrucciones administrativas, normas de búsqueda y examen, etc.) se referencian desde `SKILL.md` mediante rutas relativas `@` — **si falta un archivo, se rompe la cadena**. Copia los directorios completos; no tomes solo `SKILL.md`.

## Qué hace

| Habilidad | Rol | Descripción |
|------|------|------|
| [`pct-guide`](skills/pct-guide) | Habilidad principal | Centro de enrutamiento: dirige cada consulta a uno de los cinco ámbitos y coordina las habilidades |
| [`pct-treaty`](skills/pct-treaty) | Capa de fuentes jurídicas | Tratado y Reglamento, tablas de tasas, declaraciones y reservas — la base jurídica de la familia |
| [`pct-international-phase`](skills/pct-international-phase) | Fase internacional | Presentación, tramitación, búsqueda, publicación, modificaciones del artículo 19, examen preliminar del capítulo II |
| [`pct-national-phase`](skills/pct-national-phase) | Fase nacional | Plazos y trámites de entrada, restablecimiento de derechos, PPH y procedimientos posteriores |
| [`pct-search-examination`](skills/pct-search-examination) | Búsqueda y examen | Lectura del ISR / la opinión escrita / el IPER, documentación mínima, unidad de invención |
| [`pct-administrative`](skills/pct-administrative) | Trámites | Instrucciones administrativas (AI), guía de la oficina receptora, ePCT y formularios |

## Mecanismos clave

1. **Enrutamiento por la habilidad principal**: pregunta desde cualquier punto de entrada — `pct-guide` determina primero el ámbito y luego llama a la habilidad secundaria correspondiente;
2. **Fuente jurídica de punto único**: los datos dinámicos (disposiciones del tratado, Reglamento, tasas) se concentran en `pct-treaty`, evitando cifras divergentes en varios lugares;
3. **Divulgación progresiva**: los textos extensos viven en `references/` y se cargan a demanda, sin saturar el contexto;
4. **«Ninguno» antes que inventar**: la información dudosa se marca tal cual — sin disposiciones, plazos ni importes inventados.

## Estructura del repositorio

```text
PCT-SKILLS/
├── skills/                    # 6 habilidades (1 principal + 5 secundarias)
│   ├── pct-guide/             #   habilidad principal: centro de enrutamiento
│   ├── pct-treaty/            #   capa de fuentes jurídicas
│   ├── pct-international-phase/
│   ├── pct-national-phase/
│   ├── pct-search-examination/
│   └── pct-administrative/
├── scripts/
│   └── sync_to_local.py       # sincronización en un comando a tu directorio local de skills
├── README.md
└── LICENSE
```

- Los directorios de habilidades tienen estrictamente **2 niveles** (`SKILL.md` + `references/`), conforme a la estructura oficial de skills de WorkBuddy;
- Archivos de habilidades: **CRLF, UTF-8 sin BOM**.

## Datos y procedencia

- Las fuentes jurídicas siguen las **versiones oficiales vigentes de la OMPI / CNIPA**; cada habilidad indica su fecha de corte;
- Para datos volátiles (tasas, plazos), reverifica los anuncios oficiales más recientes antes de usarlos en el expediente;
- La salida es referencia práctica — **no constituye asesoramiento jurídico**.

## Limitaciones

- No sustituye a las instancias oficiales ni al criterio caso por caso: los plazos, las tasas y las conclusiones procedimentales se rigen por las notificaciones de la oficina receptora y los anuncios oficiales;
- Sin invención: los datos que no se encuentran se responden como «ninguno»;
- La cobertura jurídica se centra en el tratado PCT y la capa procedimental; el derecho sustantivo y la práctica de examen de cada oficina designada se rigen por las posiciones oficiales de esa oficina.

## License

[MIT](LICENSE) © 2026 Hui Ning IP（辉宁知识产权）.

- El contenido propio de las habilidades (organización y anotaciones en `SKILL.md` y `references/`) está bajo MIT;
- Los textos oficiales de la OMPI reproducidos o citados en `references/` (tratado, Reglamento, Instrucciones administrativas, etc.) siguen siendo propiedad de la OMPI y no están cubiertos por esta licencia.

## Contacto

- Preguntas y sugerencias: abre un Issue en este repositorio;
- Creado y mantenido por Hui Ning IP (un equipo chino de agentes de patentes).
