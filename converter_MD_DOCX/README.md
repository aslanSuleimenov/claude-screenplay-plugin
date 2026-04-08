# MD → DOCX Screenplay Converter

## What it does

Reads all `.md` files from the `scenes/` folder in alphabetical order, concatenates them on the fly, and converts to `.docx`.

Automatically detects the project type from CLAUDE.md (`- **Тип:** художественный` or `документальный`) and applies the corresponding format.

## Usage

```bash
pip install python-docx
python converter_MD_DOCX/md_to_docx.py
```

Output: `versions/<project_folder_name>_vNN.docx`

You can specify the filename explicitly:

```bash
python converter_MD_DOCX/md_to_docx.py MyScreenplay_v2
```

## Project folders

| Folder | Purpose |
|--------|---------|
| `scenes/` | Scenes/blocks in markdown (two-digit numbering: 01, 02, ...) |
| `versions/` | Output DOCX files (created automatically) |
| `analytics/` | Analytics, compass_artifact.md |
| `converter_MD_DOCX/` | Converter and this documentation |

## Dependencies

- Python 3.8+
- python-docx

---

# Fiction format (screenplay)

Standard single-column screenplay format.

## Scene file structure

```markdown
# Scene XX: Scene Title

INT./EXT. LOCATION — TIME OF DAY

Action description. Present tense. Short paragraphs, 4 lines max.

CHARACTER NAME
*(parenthetical)*
Dialogue text.

ANOTHER CHARACTER
Dialogue text without parenthetical.

Next action block.
```

## Elements and how to write them

### Scene heading
```
# Scene 12: Closing the Teahouse
```
- Always `#` (H1)
- Converter applies UPPERCASE automatically

### Slug line
```
INT. CAFE — DAY
```
- Plain text, no formatting
- INT. or EXT. required
- Time: DAY, NIGHT, MORNING, EVENING
- For moving vehicles: `INT./EXT. CAR — NIGHT (MOVING)`

### Action description
```
Mariam stands behind the counter. Hands in flour. Apron.
```
- Plain text, no formatting
- Present tense, third person
- 4 lines max per paragraph
- First appearance of a character — name in CAPS: `MARIAM (45) pours tea`
- DO NOT use camera directions (CLOSE-UP, MEDIUM SHOT, etc.)

### Character name before dialogue
```
MARIAM
```
- Plain text, ALL CAPS
- On a separate line

### Name with parenthetical
```
MARIAM (quietly)
```
or
```
MARIAM
*(quietly)*
```
Both formats work. Parenthetical — keep short (1-3 words): quietly, whispered, aside, V.O., O.S.

### Dialogue
```
Character's dialogue text.
```
- Plain text immediately after the name (or parenthetical)
- Converter auto-detects: if a line follows a name → it's dialogue → applies indent
- NO blank line between name and dialogue

### On-screen text / title card
```
## "THREE WEEKS LATER"
```
- `##` (H2) — centered, bold, larger

or italic:
```
*Mariam Tashmatova died two hours after the verdict was announced.*
```
- `*...*` — centered, italic

### Voice-over / phone
```
MARAT (V.O.)
Dialogue text.
```
Parentheticals: V.O. (voice over), O.S. (off screen), on phone, off camera.

### Palette / director's notes
```
> **PALETTE:** Monochrome — black, graphite, steel.
```
- Blockquote `>` — converter renders as small italic (10pt)
- Use sparingly, only for visual direction

### Location change within a scene
```
---
```
- Horizontal rule — converter skips it, for readability in the editor only

## Spacing between blocks

### Correct:
```
Action description.

CHARACTER
Dialogue.

ANOTHER CHARACTER
*(parenthetical)*
Dialogue.

Next action description.
```

### Incorrect:
```
Action description.


CHARACTER

Dialogue.
```

Rules:
- ONE blank line between blocks
- NO blank line between name and dialogue
- NO blank line between name and parenthetical
- NO double/triple blank lines

## What NOT to write in MD files

- `FADE OUT.` — not needed
- `CUT TO:` — not needed
- `CLOSE-UP:` — describe the action instead
- `CAMERA MOVES` — do not use
- Numerals in dialogue — spell out: "fifteen", not "15"

## Fiction DOCX output format

| Parameter | Value |
|-----------|-------|
| Font | Courier New 12pt |
| Page | A4 |
| Margins | top 1", bottom 0.5", left 1.5", right 1" |
| Spacing | single |
| Character name | 2" left indent, bold |
| Parenthetical | 1.5" left indent, italic |
| Dialogue | 1" left indent |
| Slug line | uppercase |
| Scene heading | bold, uppercase |

---

# Documentary format (AV-script)

Two-column format: VIDEO on the left, AUDIO on the right.

## Block file structure

```markdown
# Block 01: Block Title

| VIDEO | AUDIO |
|-------|-------|
| WS. Mountains, sunrise. | *(NAT SOUND: wind, birds)* |
| MS. Shepherd leads the flock along the trail. | **V/O:** In the Suusamyr valley, shepherds head out before dawn. |
| CU. Aibek's face. Wrinkles, sun-weathered skin. | **SOT AIBEK:** "My father brought me here when I was seven." |
| **SUPER:** Aibek Turgunov, shepherd, 43 years old | |
| B-ROLL: yurts, smoke from the tunduk, boiling kazan. | *(MUSIC: komuz, soft)* |
| | *(SFX: crackling fire)* |

Author's commentary or transition between themes — plain text outside the table.
```

## Elements and labels

### Block heading
```
# Block 01: Shepherds of Suusamyr
```
- `#` (H1), converter applies UPPERCASE
- "Block" instead of "Scene" — documentary is not tied to locations

### VIDEO | AUDIO table
```
| VIDEO | AUDIO |
|-------|-------|
| shot description | sound description |
```
- **Required** format for all block content
- Each row = one shot or editing element
- Left column — what the viewer **sees**
- Right column — what the viewer **hears**

### Video column (VIDEO)

**Shot sizes:**
| Abbreviation | Meaning |
|-------------|---------|
| ECU | Extreme close-up (eyes, hands) |
| CU | Close-up (face) |
| MS | Medium shot (waist up) |
| WS | Wide shot (full figure + surroundings) |
| EWS | Extreme wide shot (landscape) |
| AERIAL | Aerial shot |

**Content types in video column:**
- `CU. Aibek's face.` — shot description with size
- `B-ROLL: yurts, smoke, kazan.` — cutaway footage
- `**SUPER:** Aibek, 43 years old` — text overlay on video (bold)
- `ARCHIVE: 1970s footage, herd on the mountain pass.` — archival footage
- `GRAPHICS: route map.` — infographics, animation
- Empty cell `|  |` — audio continues over the same video

### Audio column (AUDIO)

**Content types:**
- `**V/O:** Voice-over narration text.` — narrator/author voice-over (bold label)
- `**SOT NAME:** "Direct quote."` — sync sound, interview (bold label + name)
- `*(NAT SOUND: wind, birds)*` — natural sound (italic in parentheses)
- `*(SFX: gunshot)*` — sound effect (italic in parentheses)
- `*(MUSIC: komuz, soft)*` — music (italic in parentheses)
- Empty cell `|  |` — silence or video without sound

### Text outside the table
```
Author's commentary between table blocks.
```
- Plain text between tables — author's notes, transitions
- Not part of the AV-script, used for organization

### Director's notes
```
> **NOTE:** Shoot at sunrise, natural light.
```
- Blockquote `>` — not included in the final DOCX
- For technical notes, not for the viewer

### On-screen text
```
## "THREE YEARS LATER"
```
- `##` (H2) — title card separator, centered

## Documentary DOCX output format

| Parameter | Value |
|-----------|-------|
| Font | Courier New 12pt |
| Page | A4, landscape orientation |
| Margins | top 1", bottom 0.5", left 1", right 1" |
| Table | two columns, VIDEO 55%, AUDIO 45% |
| Block heading | bold, uppercase, before the table |
| V/O, SOT | bold label, regular text |
| NAT SOUND, SFX, MUSIC | italic |
| SUPER | bold in video column |
