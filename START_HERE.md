# Screenplay Plugin — How to use

## Step 0 — Install the plugin

In Claude Code (any project):

```
/plugin marketplace add aslanSuleimenov/claude-screenplay-template
/plugin install screenplay@claude-screenplay-template
/reload-plugins
```

One-time install. The plugin is then available in all your projects.

**Update later:**
```
/plugin update screenplay
```

---

## Step 1 — Create a project folder and open it

```bash
mkdir "X:/scenarii/my-film"
cd "X:/scenarii/my-film"
claude
```

Any empty folder works. No template copying needed.

---

## Step 2 — /startproject

```
/startproject
```

Or, if you already have a draft file:

```
/startproject path/to/draft.md
```

Claude reads the file, extracts what it can (title, type, genre, characters, logline), and only asks about what's missing. Without a file — asks all 12 questions one at a time.

**Project types:**

| Type | When to use | DOCX output |
|------|-------------|-------------|
| **Fiction** | Feature film, series, short film | Single-column, Courier New 12pt |
| **Documentary** | Documentary, corporate video, AV-script | Two-column VIDEO/AUDIO, landscape A4 |

`/startproject` creates the full project structure:
- `CLAUDE.md` — project metadata and formatting rules
- `scenes/00_title.md` — title page
- `analytics/avoid-ai-writing-tells.md` — AI pattern checklist
- `memory/` — session logs (written by hook automatically)
- `START_HERE.md` — this file

Genre compass files stay in the plugin and are read directly. To get local editable copies: `/sync-plugin-files`

---

## Step 3 — /split (if you have a draft)

```
/split path/to/draft.md
```

Splits a raw text into scenes/blocks, places them in `scenes/`, extracts characters, fills the tables in `CLAUDE.md`.

If you have no draft — write from scratch with `/new-scene`.

---

## Step 4 — /compass

```
/compass genre — logline
```

Searches the web, builds a genre reference at `analytics/compass_artifact.md`. Used by `/analyze` and `/new-scene`.

---

## All commands

Commands automatically detect project type from `CLAUDE.md`.

### Setup

| Command | What it does |
|---------|-------------|
| `/startproject [file]` | Initialize project. Reads file if provided, asks only about missing fields |
| `/split [file]` | Split a draft into scenes/blocks → scenes/ + character tables |
| `/compass [genre — logline]` | Build genre reference from web → analytics/ |
| `/sync-plugin-files` | Update local compass and avoid-ai-writing-tells from plugin (after plugin update) |

### Writing and analysis

| Command | Fiction | Documentary |
|---------|---------|-------------|
| `/new-scene 05 Bar` | Scene: slug line + action + dialogue | Block: VIDEO/AUDIO table |
| `/rewrite 05 notes` | Rewrite scene by notes | Rewrite block by notes |
| `/analyze 05` | Analysis via compass systems | Analysis via compass systems |
| `/character-sheet Name` | Character card: arc, voice, contradictions | Subject card: appearances, SOT quotes |
| `/continuity` | Time, geography, props, character knowledge | Facts, timeline, names, title cards |
| `/research topic` | Web research → analytics/ | Web research → analytics/ |

### Structure

| Command | What it does |
|---------|-------------|
| `/outline` | Show/create beat sheet, placeholder scenes |
| `/renumber` | Renumber scenes (two-phase rename) |
| `/delete-scene NN` | Delete scene + renumber |
| `/merge NN NN` | Merge two scenes |

### Output

| Command | Fiction | Documentary |
|---------|---------|-------------|
| `/stats` | Scenes + runtime + dialogue/action ratio | Blocks + V/O word count + SOT count |
| `/compile` | Single-column DOCX | Two-column DOCX (landscape) |

### Agents

| Agent | What it does | Output |
|-------|-------------|--------|
| `draft-polish` | Full draft pipeline: analysis → scenes → logic → spelling → AI patterns | scenes/ |
| `pitch` | Pitch document for investor/producer | analytics/pitch.md |
| `unico` | UNICO starter pack (passport + character bible + presentation) | analytics/unico_package.md |
| `proofread [NN\|all]` | Spelling, logic, timeline, anachronisms | console only |

### Diagnostics

| Command | What it does |
|---------|-------------|
| `/type-check` | Project status: type set? compass? how many scenes? |

---

## Hooks (automatic)

| Hook | When | What it does |
|------|------|-------------|
| Format check | After every Edit/Write in scenes/ | Validates slug lines, character names, AI patterns |
| Compass check | Session start | Warns if compass_artifact.md is missing |
| Session report | Session end | Writes changed files to memory/session_log.md |

---

## Folder structure (after /startproject)

```
my-film/
  CLAUDE.md                     ← project metadata + formatting rules
  START_HERE.md                 ← this file
  scenes/
    00_title.md                 ← title page
  analytics/
    avoid-ai-writing-tells.md   ← AI pattern checklist (from plugin)
    compass_artifact.md         ← created by /compass
    pitch.md                    ← created by pitch agent
    unico_package.md            ← created by unico agent
  versions/                     ← DOCX output (created by /compile)
  memory/
    session_log.md              ← written by hook automatically
```

Genre compass lives in the plugin — no local copy by default. Commands and agents read it via `${CLAUDE_PLUGIN_ROOT}/compass/`. To get local editable copies: `/sync-plugin-files`.
