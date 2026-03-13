Show or create the screenplay structure as a beat sheet. Argument: $ARGUMENTS (optional — "create" to generate placeholder scenes).

---

## Mode 1 — Show (default)

1. Read CLAUDE.md — project type, structural model, runtime, structural beats table
2. Read all files in scenes/ — extract headings and key events
3. Read analytics/compass_artifact.md (if present) — genre systems

### Beat map

Calculate expected beat positions based on runtime from CLAUDE.md (~1 min = 1 page = 1 scene-minute).

For **fiction** projects map against these beats:

| Beat | Position | What it does |
|------|----------|-------------|
| Opening image | ~1% | First impression — the world before change |
| Theme stated | ~5% | Someone (not the hero) says what the film is about |
| Set-up | 1–10% | Introduce hero, world, what needs fixing |
| Catalyst | ~10% | The event that disrupts the status quo |
| Debate | 10–20% | Hero resists — should I go? |
| Break into Two | ~20% | Hero chooses — enters new world |
| B Story | ~22% | Love story / mirror character introduced |
| Fun and games | 20–50% | The promise of the premise — what the trailer shows |
| Midpoint | ~50% | False victory or false defeat — stakes double |
| Bad guys close in | 50–75% | External pressure mounts, team falls apart |
| All is Lost | ~75% | Worst moment — the opposite of the opening |
| Dark night of the soul | 75–85% | Hero hits bottom, digs deep |
| Break into Three | ~85% | Hero finds the solution (A and B stories merge) |
| Finale | 85–99% | Hero executes the plan, world is changed |
| Final image | ~99% | Mirror of opening — transformation visible |

For **documentary** projects use a simpler frame:

| Beat | Position | What it does |
|------|----------|-------------|
| Hook | 1–5% | Strongest image or question — why watch? |
| World established | 5–15% | Who, where, what's at stake |
| Central conflict introduced | ~20% | The contradiction that drives the film |
| Complication | ~50% | Something makes the problem harder |
| Crisis point | ~75% | It gets worse before it gets better |
| Resolution / open question | 85–99% | Answer or deliberate non-answer |

4. Output the outline:

```
## Outline: TITLE
Runtime: N min | Scenes: N

### Act I  (scenes 01–NN, ~0–20%)
01. Title — key event [✓ written / ✗ empty]
    Beat: Set-up
...

### Act II  (scenes NN–NN, ~20–75%)
...

### Act III  (scenes NN–end, ~75–100%)
...

## Beat check
Opening image:     scene 01 ✓
Catalyst:          scene 03 ✓  (~10% — on target)
Break into Two:    — ✗  (expected ~scene 04)
Midpoint:          — ✗  (expected ~scene 10)
All is Lost:       — ✗  (expected ~scene 15)
Break into Three:  — ✗
Final image:       — ✗

## Gaps
- No connective tissue between scenes 08 and 09
- Midpoint missing — no false victory/defeat at the halfway point
```

5. Suggest what to add or rearrange based on missing beats.

---

## Mode 2 — Create placeholder scenes

If the argument contains "create" or a list of lines in the format:
```
01 Scene title
02 Another title
...
```

1. For each line create a file `scenes/NN_title.md` with minimal content:
   - Fiction: heading + empty slug line + comment `<!-- TODO -->`
   - Documentary: heading + empty VIDEO/AUDIO table + comment
2. Update the scenes table in CLAUDE.md (status: planned)
3. Add an entry to "Change log"

## Summary

Tell the user what to do next: `/new-scene NN Title` to write a specific scene.
