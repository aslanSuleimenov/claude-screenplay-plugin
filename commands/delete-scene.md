Delete a scene/block and renumber following ones. Argument: $ARGUMENTS (scene number).

## Step 1 — Find the file

1. Read CLAUDE.md — determine project type
2. Find the file in scenes/ by number (NN_*.md)
3. Show the user the file contents (first 10 lines) and ask for confirmation
4. Before deleting — create a backup in `versions/backup_YYYYMMDD_HHMM_delete_NN.md`

## Step 2 — Delete the file

After confirmation — delete the file.

## Step 3 — Renumber following files

If there are files with numbers higher than the deleted one — renumber them:
1. Two-phase rename using temp names (to avoid collisions on Windows)
2. Update headings inside the files:
   - Fiction: `# Scene XX:` → `# Scene NN:`
   - Documentary: `# Block XX:` → `# Block NN:`

## Step 4 — Update CLAUDE.md

- Remove the row from the scenes table
- Update numbers in remaining rows
- Add an entry to "Change log"

## Step 5 — Summary

Output what was deleted and which files were renumbered.
