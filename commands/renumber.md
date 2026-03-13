Renumber scenes/blocks in scenes/. Argument: $ARGUMENTS (optional — starting number or range).

## Step 1 — Read current state

1. Read CLAUDE.md — determine project type (fiction → "Scene", documentary → "Block")
2. Find all files in scenes/ alphabetically
3. Show the current numbering to the user
4. Create a backup: archive the scenes/ folder to `versions/backup_YYYYMMDD_HHMM_renumber.zip` before making any changes

## Step 2 — Calculate new numbering

- Default: sequential numbering 01, 02, 03...
- If >99 files — three digits: 001, 002, 003...
- The 00_* file (title page) — do not touch
- If an argument is given — start from the specified number

## Step 3 — Two-phase rename

**Phase A:** Rename all files to temporary names `temp_XXXX_title.md` (to avoid collisions on Windows).

**Phase B:** Rename from temp names to final `NN_title.md`.

## Step 4 — Update headings inside files

In each file replace the heading:
- Fiction: `# Scene XX: Title` → `# Scene NN: Title`
- Documentary: `# Block XX: Title` → `# Block NN: Title`

## Step 5 — Update CLAUDE.md

- Rebuild the scenes table with new numbers and file names
- Add an entry to "Change log"

## Step 6 — Summary

Output a table: old name → new name.
