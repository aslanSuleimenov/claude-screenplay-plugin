Merge two scenes/blocks into one. Argument: $ARGUMENTS (two numbers, e.g. `05 06`).

## Step 1 — Read both scenes

1. Read CLAUDE.md — determine project type
2. Find both files in scenes/ by number
3. Read the full contents of both files
4. Show the user a brief summary of both and ask for confirmation

## Step 2 — Merge

The first file (lower number) becomes the merged file:

### Fiction
- Keep the first scene's heading (or suggest a new one)
- Merge action and dialogue: the second scene's content is added after the first
- If the second scene has a different location — add a new slug line inside the file

### Documentary
- Keep the first block's heading (or suggest a new one)
- Merge the tables: rows from the second table are added after the first
- If different topics — add a visual divider `---` between them

## Step 3 — Delete the second file

Delete the file with the higher number.

## Step 4 — Renumber following files

If there are files with numbers higher than the deleted one — renumber:
- Two-phase rename using temp names
- Update headings inside the files

## Step 5 — Update CLAUDE.md

- Update the scenes table (merged row + renumbering)
- Add an entry to "Change log"

## Step 6 — Summary

Output the result: what was merged, which files were renumbered.
