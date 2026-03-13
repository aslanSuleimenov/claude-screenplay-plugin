#!/usr/bin/env python3
"""
Хук Stop: записывает отчёт о сессии в memory/session_log.md
Находит файлы сцен, изменённые за последние 2 часа.
Работает на Windows, macOS, Linux.
"""

import os
import sys
import time
from pathlib import Path
from datetime import datetime

def main():
    # Путь к корню проекта — два уровня выше hooks/
    hook_dir  = Path(__file__).resolve().parent
    proj_dir  = hook_dir.parent.parent
    scenes_dir = proj_dir / "scenes"
    log_file   = proj_dir / "memory" / "session_log.md"

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
        f"## Сессия {timestamp}",
        "",
        "Изменённые файлы:",
    ]
    for name in modified:
        lines.append(f"- {name}")

    with open(log_file, "a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

if __name__ == "__main__":
    main()
