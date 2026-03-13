"""
Initialize a new screenplay project.
Run: python setup.py
"""
from pathlib import Path
from datetime import date
import sys

BASE = Path(__file__).parent


def check_template_protection():
    """Warn if running inside the master _template copy."""
    folder_name = BASE.name.lower()
    if folder_name == "_template":
        print("\n⚠  WARNING: You are running setup.py inside the master _template copy!")
        print("   Copy the _template folder to a new one (e.g. my_film) and run it there.")
        answer = input("   Continue anyway? (yes/no): ").strip().lower()
        if answer not in ("yes", "y"):
            print("Cancelled.")
            sys.exit(0)


def check_already_initialized(text):
    """Check whether the fields still contain dashes (not yet filled in)."""
    fields_with_dash = [
        "- **Type:** —",
        "- **Title:** —",
        "- **Genre:** —",
    ]
    filled = [f for f in fields_with_dash if f not in text]
    if filled:
        print("\n⚠  CLAUDE.md already contains project data.")
        answer = input("   Overwrite? (yes/no): ").strip().lower()
        if answer not in ("yes", "y"):
            print("Cancelled.")
            sys.exit(0)


def ask(question, default=None):
    prompt = f"{question}"
    if default:
        prompt += f" [{default}]"
    prompt += ": "
    answer = input(prompt).strip()
    return answer if answer else (default or "")


def ask_choice(question, options):
    print(f"\n{question}")
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")
    while True:
        answer = input("Number: ").strip()
        if answer.isdigit() and 1 <= int(answer) <= len(options):
            return options[int(answer) - 1]
        print("Enter a number from the list.")


# Formatting templates for CLAUDE.md
FICTION_FORMAT = """Strictly per `converter_MD_DOCX/README.md`. Quick rules:

```markdown
# Scene 01: Title

**INT./EXT. LOCATION — TIME OF DAY**

Action description. Present tense, third person. Max 4 lines per paragraph.

**CHARACTER NAME**
*(parenthetical)*
Dialogue text.
```

- ONE blank line between blocks; ZERO between name and dialogue
- Names — **bold caps**: `**NAME**`
- Slug line — **bold**: `**INT. LOCATION — DAY**`
- First appearance: `NAME (age)` in caps within action text
- Do not use: `FADE OUT.`, `CUT TO:`, `CLOSE ON:`
- Numbers in dialogue — written out as words
- `---` — location change within a scene (converter skips it)
- `> **PALETTE:** ...` — visual note"""

DOC_FORMAT = """Strictly per `converter_MD_DOCX/README.md`, section "Documentary format". Quick rules:

```markdown
# Block 01: Title

| VIDEO | AUDIO |
|-------|-------|
| WS. Mountains, dawn. | *(NAT SOUND: wind)* |
| MS. Shepherd leads the flock. | **V/O:** Voice-over text. |
| CU. Subject's face. | **SOT AIBEK:** "Direct quote." |
| **SUPER:** Aibek, shepherd, 43 | |
| B-ROLL: yurts, smoke, kettle. | *(MUSIC: komuz, low)* |
```

- Each block = one file `scenes/NN_name.md`
- Table `| VIDEO | AUDIO |` — mandatory format
- Labels: **V/O** (voice-over), **SOT** (sync/interview), **SUPER** (title card), **NAT SOUND**, **SFX**, **B-ROLL**
- Shot sizes: WS, MS, CU, ECU, AERIAL
- `> **NOTE:** ...` — director's note (not included in DOCX)"""


def ask_int(question, default=None):
    """Ask for an integer with validation."""
    while True:
        answer = ask(question, default)
        if not answer:
            return default or ""
        try:
            int(answer)
            return answer
        except ValueError:
            print("  Enter a number.")


def main():
    print("\n=== New screenplay project ===\n")

    check_template_protection()

    claude_md = BASE / "CLAUDE.md"
    text = claude_md.read_text(encoding="utf-8")
    check_already_initialized(text)

    proj_type  = ask_choice("Project type:", ["fiction", "documentary"])
    title      = ask("Project title")
    genre      = ask("Genre (black comedy / thriller / drama / other)")
    logline    = ask("Logline (one sentence about what the film is)")
    fmt        = ask("Format (feature / short / pilot / series)", "feature")
    theme      = ask("Theme (what it's about at a deeper level)")
    audience   = ask("Target audience")
    location   = ask("Setting (country, city, environment)")
    period     = ask("Period (month, era, season)")
    currency   = ask("Currency and locale (names, toponyms, cultural context)")
    runtime    = ask_int("Target runtime in minutes", "90")
    structure  = ask("Story structure", "three-act")

    print("\nCharacters (name, age, role — one per line, blank line to finish):")
    characters = []
    while True:
        line = input("  > ").strip()
        if not line:
            break
        characters.append(line)

    today = date.today().strftime("%d.%m.%Y")

    claude_md = BASE / "CLAUDE.md"
    text = claude_md.read_text(encoding="utf-8")

    replacements = {
        "- **Type:** —":               f"- **Type:** {proj_type}",
        "- **Title:** —":              f"- **Title:** {title}",
        "- **Genre:** —":              f"- **Genre:** {genre}",
        "- **Logline:** —":            f"- **Logline:** {logline}",
        "- **Format:** —":             f"- **Format:** {fmt}",
        "- **Theme:** —":              f"- **Theme:** {theme}",
        "- **Target audience:** —":    f"- **Target audience:** {audience}",
        "- **Setting:** —":            f"- **Setting:** {location}",
        "- **Period:** —":             f"- **Period:** {period}",
        "- **Currency and locale:** —": f"- **Currency and locale:** {currency}",
        "- **Runtime:** —":            f"- **Runtime:** {runtime} minutes",
        "- **Story structure:** —":    f"- **Story structure:** {structure}",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    format_block = DOC_FORMAT if proj_type == "documentary" else FICTION_FORMAT
    start_marker = "## Scene formatting"
    end_marker = "## Working rules"
    start_idx = text.find(start_marker)
    end_idx = text.find(end_marker)
    if start_idx != -1 and end_idx != -1:
        text = text[:start_idx] + f"## Scene formatting\n\n{format_block}\n\n" + text[end_idx:]

    if characters:
        char_rows = []
        for c in characters:
            parts = [p.strip() for p in c.split(",")]
            if len(parts) >= 4:
                char_rows.append(f"| {parts[0]} | {parts[1]} | {parts[2]} | {', '.join(parts[3:])} |")
            elif len(parts) == 3:
                char_rows.append(f"| {parts[0]} | {parts[1]} | {parts[2]} | — |")
            elif len(parts) == 2:
                char_rows.append(f"| {parts[0]} | — | {parts[1]} | — |")
            else:
                char_rows.append(f"| {parts[0]} | — | — | — |")
        text = text.replace(
            "| Name | Age | Role | Want / Need |\n|------|-----|------|-------------|\n",
            "| Name | Age | Role | Want / Need |\n|------|-----|------|-------------|\n" + "\n".join(char_rows) + "\n"
        )

    text = text.replace(
        "| Date | Change |\n|------|--------|",
        f"| Date | Change |\n|------|--------|\n| {today} | Project created: {title} ({proj_type}) |"
    )

    claude_md.write_text(text, encoding="utf-8")

    scenes_dir = BASE / "scenes"
    scenes_dir.mkdir(exist_ok=True)

    title_page = scenes_dir / "00_title.md"
    title_page.write_text(
        f"# {title.upper()}\n\n"
        f"**{genre.upper()}**\n\n"
        f"*{proj_type}*\n\n"
        f"{logline}\n\n"
        f"Written by: —\n\n"
        f"{date.today().year}\n",
        encoding="utf-8"
    )

    print(f"\n✓ CLAUDE.md filled in (type: {proj_type})")
    print(f"✓ scenes/00_title.md created")
    print(f"\nDone. Launch Claude Code:\n")
    print(f"  claude\n")
    print(f"First command in Claude: /compass {genre} — {logline}\n")


if __name__ == "__main__":
    main()
