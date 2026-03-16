---
name: character-bible
description: Builds a complete character bible from all scene files — backstory, arcs, appearance, motivation, voice, relationships. Reads scenes/ recursively (including subdirectories). Writes analytics/characters.md.
---

You build a comprehensive character bible for the entire project. Work autonomously — read everything, analyze, write the file.

---

## Step 1 — Gather data

Read CLAUDE.md — get project type, title, genre, character table.

Read ALL .md files from scenes/ recursively (including subdirectories like серия_01/, серия_02/, etc.). Sort by filename.

For each file, extract:
- Character names (lines that are plain CAPS, 3–40 chars, no period)
- Their dialogue (lines after character name until next blank line)
- Action lines mentioning them
- Parentheticals
- First and last appearance (scene number)

---

## Step 2 — Identify characters

Split into tiers:
- MAIN: appear in 5+ scenes or listed in CLAUDE.md character table
- SUPPORTING: appear in 2–4 scenes
- EPISODIC: appear in 1 scene (list names only, no full sheet)

---

## Step 3 — Build bible

For each MAIN and SUPPORTING character, build a sheet:

```
## CHARACTER NAME (age if known)

Tier: main / supporting

### Role
Who they are in the story. One sentence.

### First appearance
Scene NN — how introduced, what they do, first impression.

### Last appearance
Scene NN — how they exit the story.

### Backstory
What we learn about their past — from dialogue, action, exposition. Only what is in the text, not invented.

### External goal
What they are pursuing through actions.

### Inner need
What they must change or accept. If unknown from text — say so.

### Arc
Entry state → pressure → exit state. Which axis shifts: safety/danger, hope/despair, connection/isolation, truth/lie, power/powerlessness.

### Appearance and props
All mentions of clothing, objects, physical details. Scene references.

### Voice portrait
- Typical phrases (direct quotes from scenes)
- Speech manner: long/short, formal/informal, pauses, interruptions
- Language: Russian/Kazakh/mixed, accent, slang
- How they address others

### Voice distinctiveness
Can you tell their lines apart from other characters without the name? What makes their voice unique? If indistinguishable from another character — flag it.

### Relationships
| Character | Relationship | Dynamic |
|-----------|-------------|---------|

### Scene map
| Scene | What they do | State |
|-------|-------------|-------|

### Problems
- Contradictions between scenes
- Scenes where they appear but serve no purpose
- Missing motivation for key decisions
- Says = Wants = Needs (no subtext)
```

For EPISODIC characters — one table at the end:

```
## Episodic characters

| Name | Scene | Function |
|------|-------|----------|
```

---

## Step 4 — Cross-character analysis

After all individual sheets, add a section:

```
## Cross-character analysis

### Voice overlap
Which characters sound alike? Specific examples.

### Relationship web
Who drives conflict with whom? Who has no conflict?

### Missing arcs
Characters who enter and exit in the same state.

### Screen time balance
| Character | Scenes | Dialogue lines | % of total |
|-----------|--------|---------------|------------|
```

---

## Step 5 — Write file

Write the complete bible to `analytics/characters.md`.

Format: plain text, no bold in examples. Section headers use ##/###.

Report to user:
```
Character bible written to analytics/characters.md

Main characters: N
Supporting characters: N
Episodic characters: N
Total scenes analyzed: N
```
