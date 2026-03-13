Initialize a new project. Ask questions one at a time, wait for each answer.

## Questions

1. Project type: **fiction** or **documentary**?
2. Project title?
3. Genre (black comedy / thriller / drama / other)?
4. Logline — one sentence describing what the film is about?
5. Format (feature / short / pilot / series)?
6. Theme — what is it about at a deeper level?
7. Target audience?
8. Setting (country, city, environment)?
9. Season and time period?
10. Currency and cultural specifics (names, place names, language of characters)?
11. Target runtime (60 / 90 / 120 minutes)?
12. Structural model (three-act / five-loop / other)?

## After the answers

Fill in the "Project" section in CLAUDE.md — replace all dashes "—" with the real data.
Set the **Type** field to "fiction" or "documentary".
Add an entry to "Change log" with today's date.
Leave the characters and scenes tables empty — they will be filled via /split.

Create the `scenes/` directory (if it doesn't exist) and the file `scenes/00_title.md` with the title page:
```
# TITLE
**GENRE**
*project type*
Logline
Author: —
Year
```

### If type = documentary

Replace the "Scene Formatting" section in CLAUDE.md with the documentary format (two-column AV).
Format details are in `converter_MD_DOCX/README.md`, section "Documentary Format".

## Summary

Tell the user:

"Done. Now run:
/split [path to draft file]

Claude will read the text, cut it into scenes in scenes/ and fill in characters and structure in CLAUDE.md."
