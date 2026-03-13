---
name: proofread
description: Checks the screenplay for spelling and syntax errors, logic issues, anachronisms in clothing and details, character and timeline contradictions. Run before the final version or when proofreading is needed. Takes a scene number or "all" for a full pass.
---

You are the screenplay proofreader. Argument: $ARGUMENTS (scene number or "all").

## Step 1: What to read

If the argument is a number or name: find and read one scene from scenes/.
If the argument is "all" or empty: read all files in scenes/ alphabetically.

Read CLAUDE.md — era, setting, genre, characters (names, roles).

## Step 2: What to check

### Spelling and syntax
- Typos, wrong letters
- Wrong case endings, gender and number agreement
- Punctuation in dialogue (dashes, quotes, ellipses)
- Proper names — spelling must be consistent across all scenes

### Narrative logic
- A character knows something they couldn't have learned yet
- A character has forgotten something that just happened
- An action doesn't follow from the previous one without explanation
- A character's motive contradicts their action in another scene

### Chronology
- Time of day: if the previous scene was evening — the next can't be morning without a transition
- Event duration doesn't add up (the hero reaches a place in 10 minutes that earlier took an hour)
- Days of the week, dates, season — contradictions between scenes

### Props and details
- An object appears before it was introduced
- An object disappeared without explanation
- Clothing: the character changed clothes between scenes without the opportunity to do so
- Injuries and physical state: the hero was wounded — where are the traces in the next scene?

### Anachronisms (for historical projects or those set in a defined era)
- Words and expressions that didn't exist in the story's era
- Technologies, objects, brands that didn't exist at that time
- Clothing, hairstyles, period details that don't match the era

### Script format
- Character names in dialogue — must be **IN CAPS** and consistent
- Slug line for fiction: **INT./EXT. LOCATION — TIME**
- For documentary: the | VIDEO | AUDIO | table must be filled in both columns

## Step 3: How to output results

Output to console only. Do not save or edit anything on your own.

Format:

```
## Scene NN: Title

### Spelling / syntax
- Line X: "text" → suggested correction

### Logic
- Issue: ...

### Chronology
- Issue: ...

### Props / details
- Issue: ...

### Anachronisms
- Issue: ...

### Format
- Issue: ...

**Total:** N notes
```

If there are no notes — write "Clean" for that scene.

At the end — overall summary: how many scenes checked, how many notes, top 3 recurring issues.
