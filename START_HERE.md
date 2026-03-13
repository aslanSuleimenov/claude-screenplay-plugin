# How to start a new project

## Step 0 — Install dependencies

```bash
pip install python-docx
```

Required for `/compile` (conversion to DOCX). Make sure it's `python-docx`, not `docx` — they are different packages.

## Step 1 — Copy the folder

```
X:\scenarii\_template     ← do not touch, this is the master copy
X:\scenarii\my_project    ← copy everything here
```

**Windows:** when copying, make sure the `.claude/` folder is included. It is a hidden folder — in Explorer, enable "Show hidden items" (View → Show → Hidden items). Without `.claude/` the commands and hooks will not work.

## Step 2 — Open in Claude Code

```bash
cd "X:/scenarii/my_project"
claude
```

(Use forward slashes `/` in bash paths, even on Windows.)

## Step 3 — /startproject

```
/startproject
```

Claude will ask 12 questions. **The first question is the project type:**

| Type | When to choose | Page format |
|------|----------------|-------------|
| **Fiction** | Feature film, animation, series, short film | Single-column (screenplay): slug line → action → name → dialogue |
| **Documentary** | Documentary film, corporate video, advertising | Two-column (AV-script): VIDEO ↔ AUDIO table |

Remaining questions: title, genre, logline, format, theme, audience, setting, period, locale, runtime, structure.

The command will fill in `CLAUDE.md` and configure the format for the chosen type.

**Alternative:** `python setup.py` — same questions via terminal.

## Step 4 — /split (if you have a draft)

```
/split path/to/draft.md
```

Reads the file and splits it into:
- **Fiction** → scenes with slug lines and dialogue
- **Documentary** → blocks with VIDEO | AUDIO tables

Places files in `scenes/`, extracts characters/subjects, fills in the tables in `CLAUDE.md`.

If you have no draft — skip this, write from scratch with `/new-scene`.

## Step 5 — /compass

```
/compass genre — logline
```

Goes online, builds a genre reference guide at `analytics/compass_artifact.md`.

---

## All commands

Commands **automatically** detect the project type from CLAUDE.md and apply the correct format.

### Project setup

| Command | What it does |
|---------|-------------|
| `/startproject` | Initialization: type + 11 questions → fills CLAUDE.md |
| `/split [file]` | Splits a draft into scenes/blocks → scenes/ + tables |
| `/compass [genre — logline]` | Builds a genre reference from the web → analytics/ |

### Writing and analysis

| Command | Fiction | Documentary |
|---------|---------|-------------|
| `/new-scene 05 Bar` | Creates a scene: slug line + action + dialogue | Creates a block: VIDEO ↔ AUDIO table |
| `/rewrite 05 notes` | Rewrites the scene based on notes | Rewrites the block based on notes |
| `/analyze 05` | Analysis via compass systems | Analysis via compass systems |
| `/character-sheet Name` | Character card: arc, voice, contradictions | Subject card: appearances, quotes (SOT) |
| `/continuity` | Time, geography, props, character knowledge | Facts, timeline, names, title cards (SUPER) |
| `/research topic` | Web research → analytics/ | Web research → analytics/ |

### Structure and management

| Command | What it does |
|---------|-------------|
| `/outline` | Show/create beat sheet, placeholder scenes |
| `/renumber` | Renumber scenes (two-phase rename) |
| `/delete-scene NN` | Delete a scene + renumber |
| `/merge NN NN` | Merge two scenes into one |

### Review and export

| Command | Fiction | Documentary |
|---------|---------|-------------|
| `/stats` | Scenes + runtime + dialogue/action ratio | Blocks + V/O word count + SOT count |
| `/compile` | Single-column DOCX (screenplay) | Two-column DOCX (AV-script, landscape) |

### Agents (run manually)

| Agent | What it does | Output |
|-------|-------------|--------|
| `/pitch` | Pitch document for investor/producer | analytics/pitch.md |
| `/unico` | UNICO starter pack (passport + character bible + presentation) | analytics/unico_package.md |
| `/proofread [NN\|all]` | Proofread: spelling, logic, timeline, anachronisms | output only |

**When to use what:**

| Task | Tool |
|------|------|
| Genre system, hook, scene structure | `/analyze NN` |
| Spelling, logic, timeline, props | `/proofread NN` |
| Full check before final version | both in sequence |

### Diagnostics

| Command | What it does |
|---------|-------------|
| `/type-check` | Project status: type set? compass present? how many scenes? |

### Hooks (run automatically)

| Hook | When it fires | What it checks |
|------|--------------|----------------|
| Format check | After every Edit/Write in scenes/ | **Fiction:** slug line, names, indentation. **Doc:** table, V/O, SOT, SUPER. **Both:** AI patterns |
| Session report | When work session ends | Writes changed files to memory/session_log.md |

---

## Folder structure

```
my_project/
  START_HERE.md
  CLAUDE.md                       ← filled in by /startproject (including project type)
  setup.py                        ← alternative to /startproject via terminal
  scenes/                         ← scenes/blocks (filled by /split or /new-scene)
  analytics/
    compass_artifact.md           ← created by /compass
    avoid-ai-writing-tells.md     ← banned AI writing patterns
    pitch.md                      ← created by /pitch agent
    unico_package.md              ← created by /unico agent
  versions/                       ← DOCX output (created by /compile)
  converter_MD_DOCX/
    md_to_docx.py                 ← screenplay converter (auto-detects type)
    pitch_to_docx.py              ← pitch → DOCX converter
    README.md                     ← formatting rules (both types)
  memory/
    session_log.md                ← written automatically by hook
  .claude/
    settings.json                 ← MCP + hooks (format validation + session report)
    commands/                     ← 16 commands (work with both types)
    hooks/
      session_report.py           ← Python, works on Windows/macOS/Linux
    agents/                       ← pitch, unico, proofread
```
