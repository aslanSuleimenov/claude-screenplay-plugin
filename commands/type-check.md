Check project status and output diagnostics.

1. Read CLAUDE.md — extract:
   - The "Type" field (fiction / documentary)
   - Title, genre, logline
   - Number of rows in the scenes table

2. Count files in scenes/ (*.md, excluding 00_*)

3. Check for key files:
   - analytics/compass_artifact.md
   - analytics/avoid-ai-writing-tells.md
   - memory/session_log.md

4. Output the summary:

```
Project: [Title]
Type: [type]  ← if empty: ⚠ NOT SET → run /startproject
Genre: [genre]
Logline: [first 80 characters]

Scenes in scenes/: N
Compass: [present / missing → run /compass]
Session log: [present / missing]

Ready to work: YES / NO
```

If "Type" is empty or not set — that is the only reason to output "NO".
If compass_artifact.md is missing — warn, but do not block.
