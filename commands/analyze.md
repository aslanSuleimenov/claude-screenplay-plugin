Analyze a scene or the full screenplay. Argument: $ARGUMENTS (scene number, title, or empty).

---

## Mode A — No argument: full screenplay analysis

If `$ARGUMENTS` is empty — analyze the entire screenplay.

1. Read CLAUDE.md — type, title, structure table, characters
2. Read all files in scenes/ in order
3. Check analytics/compass_artifact.md if it exists

### What to check:

**Logic and continuity:**
- Timeline and dates — contradictions, jumps that don't make sense
- Character knowledge — does a character know something they couldn't know yet?
- Location and prop continuity — object appears/disappears, location changes without explanation
- Character motivation gaps — actions without a clear reason

**Structure:**
- Scenes that contribute nothing (no new information, no change)
- Structural beats — are they present and in the right place?
- Opening and closing — does the ending answer the question raised at the start?

**Format (check against CLAUDE.md scene formatting rules):**
- Heading format violations
- Missing slug lines (fiction) or missing VIDEO/AUDIO table (documentary)
- Character name formatting errors

**AI writing patterns** (check against `${CLAUDE_PLUGIN_ROOT}/analytics/avoid-ai-writing-tells.md`):
- Rule of threes, emotional placeholders, dialogue that explains feelings

### Output format:

```
FULL ANALYSIS — [Title]
Scenes: N | Est. runtime: N min

LOGIC / CONTINUITY
[issue] → Scene NN: description
...
If none: ✓ No issues found

STRUCTURE
[issue or observation]
...

FORMAT ERRORS
Scene NN: description
...
If none: ✓ Format clean

AI PATTERNS
Scene NN: quoted problem line → suggested fix
...
If none: ✓ No AI patterns detected
```

Save nothing. Output only.

---

## Mode B — With argument: single scene analysis

If `$ARGUMENTS` is not empty:

1. Find the file in scenes/ by number or title
2. Read the scene in full
3. Check analytics/compass_artifact.md:
   - If exists — read it (genre systems)
   - If not — warn: "compass_artifact.md not found. Run /compass [genre — logline]. Analysis will continue without genre systems."
4. Score each system from compass (1–10), if compass_artifact.md exists:
   - Charge reversal (+ → - or - → +)?
   - Stakes rising?
   - Visual image without words?
   - Story engine running?
5. Check against `${CLAUDE_PLUGIN_ROOT}/analytics/avoid-ai-writing-tells.md` — forbidden patterns?
6. Point out specific problem lines
7. Suggest fixes in BEFORE → AFTER format
8. Answer: can this scene be cut without losing anything? If yes — what exactly would be lost, and can it be conveyed another way?

Save nothing. Analysis and recommendations only.
