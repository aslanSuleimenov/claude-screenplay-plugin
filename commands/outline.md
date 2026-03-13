Show or create the screenplay structure as a beat sheet. Argument: $ARGUMENTS (optional — "create" to generate placeholder scenes).

## Mode 1 — Show (default)

1. Read CLAUDE.md — project type, structural model, structural beats
2. Read all files in scenes/ — extract headings and key events
3. Read analytics/compass_artifact.md (if present) — genre systems
4. Output the outline:

```
## Outline: TITLE

### Act I (scenes 01-05)
01. Title — key event [✓ written / ✗ empty]
02. Title — key event [✓]
...

### Act II (scenes 06-15)
...

### Act III (scenes 16-20)
...

## Structural beats
- Inciting incident: scene 03 ✓
- Turn 1: scene 05 ✓
- Midpoint: — ✗
- Turn 2: — ✗
- Climax: — ✗

## Gaps
- No connective tissue between scenes 08 and 09
- No scene for [structural beat]
```

5. Suggest what to add or rearrange

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
