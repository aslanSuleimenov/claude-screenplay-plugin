# Claude Screenplay Template

A [Claude Code](https://claude.ai/code) template for writing professional screenplays — fiction films, series, and documentary AV-scripts. One template, two formats.

---

## What it does

- **Two project types** from one template: fiction screenplay (one-column) and documentary AV-script (two-column VIDEO/AUDIO table)
- **16 slash commands** — from `/startproject` to `/compile` — all auto-detect project type
- **Format validation hook** — checks scene files on every save (slug lines, character names, AI writing patterns)
- **MD → DOCX converter** — outputs production-ready files: Courier New 12pt for fiction, landscape A4 table for documentary
- **Genre compass system** — research-backed reference files for thriller, drama, documentary portrait, verité, and more
- **Anti-AI-writing checker** — built-in rules against emotional placeholders, rule-of-three patterns, on-the-nose dialogue

---

## Quick start

**Requirements:** [Claude Code](https://claude.ai/code), Python 3, `pip install python-docx`

```bash
# 1. Copy this template to your project folder
cp -r claude-screenplay-template my-film
cd my-film

# 2. Open in Claude Code
claude

# 3. Initialize your project
/startproject
```

Claude will ask 12 questions (project type, title, genre, logline, format, theme, audience, location, period, currency/setting, runtime, structure) and configure `CLAUDE.md` accordingly.

**Windows users:** Make sure `.claude/` folder is copied — it's hidden. In Explorer: View → Show → Hidden items.

---

## Project types

| | Fiction (screenplay) | Documentary (AV-script) |
|---|---|---|
| Unit | Scene (`# Scene NN:`) | Block (`# Block NN:`) |
| Format | Slug line → action → dialogue | Two-column `\| VIDEO \| AUDIO \|` table |
| DOCX | A4 portrait, Courier New 12pt | A4 landscape, 55%/45% columns |
| Markers | `**INT./EXT.**`, `**CHARACTER**` | `**V/O:**`, `**SOT NAME:**`, `*(NAT SOUND:)*`, `**SUPER:**` |

---

## Commands

All commands auto-detect project type from `CLAUDE.md`.

### Start
| Command | What it does |
|---------|-------------|
| `/startproject` | Initialize: type + 11 questions → fills CLAUDE.md |
| `/split [file]` | Split a draft into scenes/blocks → scenes/ + character tables |
| `/compass [genre — logline]` | Build genre reference from web research → analytics/ |

### Write & analyze
| Command | Fiction | Documentary |
|---------|---------|-------------|
| `/new-scene 05 Bar` | Creates scene: slug line + action + dialogue | Creates block: VIDEO ↔ AUDIO table |
| `/rewrite 05 notes` | Rewrites scene by notes | Rewrites block by notes |
| `/analyze 05` | Analysis through compass systems | Analysis through compass systems |
| `/character-sheet Name` | Character card: arc, speech, contradictions | Hero card: appearances, quotes (SOT) |
| `/continuity` | Time, geography, props, character knowledge | Facts, chronology, names, supers |
| `/research topic` | Web research → analytics/ | Web research → analytics/ |

### Structure
| Command | What it does |
|---------|-------------|
| `/outline` | Show/create beat sheet, placeholder scenes |
| `/renumber` | Renumber scenes (two-phase rename, safe on Windows) |
| `/delete-scene NN` | Delete scene + renumber |
| `/merge NN NN` | Merge two scenes |

### Output
| Command | Fiction | Documentary |
|---------|---------|-------------|
| `/stats` | Scenes + runtime + dialogue/action ratio | Blocks + V/O word count + SOT count |
| `/compile` | One-column DOCX (screenplay) | Two-column DOCX (AV-script, landscape) |

### Agents
| Agent | What it does |
|-------|-------------|
| `/pitch` | Pitch document for investors/producers → analytics/pitch.md |
| `/unico` | UNICO starter pack (passport + character bible + presentation) |
| `/proofread [NN\|all]` | Proofreading: spelling, logic, chronology, anachronisms |

---

## Hooks (automatic)

| Hook | Trigger | Checks |
|------|---------|--------|
| Format validation | After every Edit/Write in scenes/ | **Fiction:** slug line, names, indentation. **Doc:** table, V/O, SOT, SUPER. **Both:** AI writing patterns |
| Session report | On session end | Writes changed scene files to memory/session_log.md |

---

## Genre compass

The `compass/` folder contains genre theory reference files — no project-specific content, pure craft systems and benchmarks. Use from any project as `./compass/` or move one level up for multi-project sharing (`../compass/`).

```
compass/
├── INDEX.md
├── fiction/
│   ├── thriller.md
│   ├── drama.md
│   ├── black-comedy.md
│   ├── coming-of-age.md
│   └── sci-drama.md
├── doc/
│   ├── portrait.md       (documentary portrait)
│   └── verite.md         (cinema verité)
└── format/
    ├── miniseries.md
    └── vertical-microdrama.md
```

Each project gets its own `analytics/compass_artifact.md` — the application of genre theory to that specific project. The compass files stay generic.

---

## Folder structure

```
my-project/
  README.md
  CLAUDE.md                     ← filled by /startproject (includes project type)
  НАЧНИ_ЗДЕСЬ.md                ← full guide in Russian
  setup.py                      ← terminal alternative to /startproject
  scenes/                       ← scenes/blocks (filled by /split or /new-scene)
  analytics/
    compass_artifact.md         ← created by /compass
    avoid-ai-writing-tells.md   ← forbidden AI writing patterns
    pitch.md                    ← created by /pitch agent
  versions/                     ← DOCX output (created by /compile)
  converter_MD_DOCX/
    md_to_docx.py               ← converter (auto-detects project type)
    README.md                   ← full format specification (both types)
  memory/
    session_log.md              ← written by hook automatically
  compass/                      ← genre reference (can be moved one level up)
  .claude/
    settings.json               ← hooks configuration
    commands/                   ← 16 commands
    hooks/
      session_report.py
    agents/                     ← pitch, unico, proofread
```

---

## Language

The template works in any language — Claude responds in whatever language is set in `CLAUDE.md`:

```markdown
Working language: **English**. All responses and comments in English.
```

Default is Russian. Change this line during `/startproject` or manually in `CLAUDE.md`.

---

## Contributing

Improvements to commands, hooks, compass files, or the converter are welcome. The template is kept intentionally minimal — one copy per project, no dependencies beyond `python-docx`.

---

---

## На русском

Это шаблон Claude Code для написания профессиональных сценариев — художественных фильмов, сериалов и документальных AV-сценариев.

**Быстрый старт:** скопируй папку → открой в Claude Code → `/startproject`

Подробная инструкция — в файле **`НАЧНИ_ЗДЕСЬ.md`** внутри шаблона.

**Два типа проектов:**
- **Художественный** — одноколоночный screenplay (slug line → действие → диалог)
- **Документальный** — двухколоночный AV-script (таблица VIDEO | AUDIO)

Тип выбирается при `/startproject` и влияет на все команды, хуки и конвертер.
