"""PostToolUse hook: validate scene files after Edit/Write."""
import json
import os
import re
import sys


def main():
    file_path = os.environ.get("CLAUDE_FILE_PATH", "")

    # Only check files in scenes/
    if "/scenes/" not in file_path.replace("\\", "/"):
        print(json.dumps({"ok": True}))
        return

    if not os.path.isfile(file_path):
        print(json.dumps({"ok": True}))
        return

    with open(file_path, encoding="utf-8") as f:
        content = f.read()
    lines = content.split("\n")

    # Determine type from heading
    is_fiction = True
    for line in lines:
        if line.startswith("# "):
            low = line.lower()
            if "block" in low or "блок" in low:
                is_fiction = False
            break

    errors = []

    # Check: no bold (**) in fiction scene files
    if is_fiction:
        for i, line in enumerate(lines, 1):
            if "**" in line:
                errors.append(f"Line {i}: bold markers (**) found. Fiction scenes must be plain text, no bold.")
                break

    # Check: one slug per file (fiction)
    if is_fiction:
        slug_prefixes = ("INT.", "EXT.", "ИНТ.", "НАТ.", "INT./EXT.", "ИНТ./НАТ.")
        slug_count = 0
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("#"):
                continue
            if any(stripped.upper().startswith(p) for p in slug_prefixes):
                slug_count += 1
        if slug_count > 1:
            errors.append(
                "Multiple slug lines detected. Split this file now: "
                "each slug becomes its own scene file. Renumber subsequent scenes."
            )

    # Check: no two blank lines before character name
    if is_fiction:
        for i in range(2, len(lines)):
            stripped = lines[i].strip()
            if (
                stripped
                and stripped.isupper()
                and len(stripped) > 2
                and not stripped.startswith("#")
                and not any(stripped.startswith(p) for p in ("INT.", "EXT.", "ИНТ.", "НАТ."))
                and lines[i - 1].strip() == ""
                and lines[i - 2].strip() == ""
            ):
                errors.append(f"Line {i + 1}: two blank lines before character name '{stripped}'. Use exactly one.")
                break

    if errors:
        print(json.dumps({"ok": False, "reason": errors[0]}))
    else:
        print(json.dumps({"ok": True}))


if __name__ == "__main__":
    main()
