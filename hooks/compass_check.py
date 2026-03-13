#!/usr/bin/env python3
"""
SessionStart hook: checks age of files in compass/
If any file hasn't been updated in THRESHOLD_DAYS — prints a reminder.
Works on Windows, macOS, Linux.
"""

import os
import sys
import time
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────────
THRESHOLD_DAYS = 30
# ─────────────────────────────────────────────────────────────────────────────

def main():
    plugin_root = Path(os.environ.get("CLAUDE_PLUGIN_ROOT", Path(__file__).resolve().parent.parent))
    compass_dir = plugin_root / "compass"

    if not compass_dir.exists():
        sys.exit(0)

    now = time.time()
    threshold = THRESHOLD_DAYS * 24 * 3600
    stale = []

    for md_file in sorted(compass_dir.rglob("*.md")):
        if md_file.name == "INDEX.md":
            continue
        text = md_file.read_text(encoding="utf-8", errors="ignore")
        if "_not filled_" in text and text.count("_not filled_") > 3:
            continue
        age_sec = now - md_file.stat().st_mtime
        if age_sec > threshold:
            age_days = int(age_sec // (24 * 3600))
            rel = md_file.relative_to(compass_dir)
            stale.append((rel, age_days))

    if not stale:
        sys.exit(0)

    print("\n─────────────────────────────────────────")
    print(f"  Compass: {len(stale)} file(s) not updated in >{THRESHOLD_DAYS} days")
    for rel, days in stale:
        print(f"  · {rel}  ({days}d)")
    print("  Run /compass to update")
    print("─────────────────────────────────────────\n")

if __name__ == "__main__":
    main()
