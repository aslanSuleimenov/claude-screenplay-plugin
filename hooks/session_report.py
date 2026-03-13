#!/usr/bin/env python3
"""
Stop hook: writes session report to memory/session_log.md
Finds scene files modified in the last 2 hours.
Works on Windows, macOS, Linux.
"""

import os
import sys
import time
from pathlib import Path
from datetime import datetime

def main():
    proj_dir = Path(os.environ.get("CLAUDE_PROJECT_DIR", Path.cwd()))
    scenes_dir = proj_dir / "scenes"
    log_file = proj_dir / "memory" / "session_log.md"

    if not scenes_dir.exists():
        sys.exit(0)

    now = time.time()
    two_hours = 120 * 60

    modified = []
    for f in sorted(scenes_dir.glob("*.md")):
        if (now - f.stat().st_mtime) <= two_hours:
            modified.append(f.name)

    if not modified:
        sys.exit(0)

    log_file.parent.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        "",
        f"## Session {timestamp}",
        "",
        "Modified files:",
    ]
    for name in modified:
        lines.append(f"- {name}")

    with open(log_file, "a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

if __name__ == "__main__":
    main()
