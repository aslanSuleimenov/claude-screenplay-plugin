#!/usr/bin/env python3
"""
Хук SessionStart: проверяет возраст файлов в compass/
Если какой-то файл старше THRESHOLD_DAYS — выводит напоминание.
Работает на Windows, macOS, Linux.
"""

import os
import sys
import time
from pathlib import Path
from datetime import datetime, timedelta

# ── Настройка ────────────────────────────────────────────────────────────────
THRESHOLD_DAYS = 30   # напоминать если файл не обновлялся дольше этого
# ─────────────────────────────────────────────────────────────────────────────

def main():
    proj_dir   = Path(__file__).resolve().parent.parent.parent
    compass_dir = proj_dir / "compass"

    if not compass_dir.exists():
        sys.exit(0)

    now       = time.time()
    threshold = THRESHOLD_DAYS * 24 * 3600
    stale     = []

    for md_file in sorted(compass_dir.rglob("*.md")):
        if md_file.name == "INDEX.md":
            continue
        # пропускаем незаполненные (содержат только _не заполнено_)
        text = md_file.read_text(encoding="utf-8", errors="ignore")
        if "_не заполнено_" in text and text.count("_не заполнено_") > 3:
            continue
        age_sec = now - md_file.stat().st_mtime
        if age_sec > threshold:
            age_days = int(age_sec // (24 * 3600))
            rel = md_file.relative_to(compass_dir)
            stale.append((rel, age_days))

    if not stale:
        sys.exit(0)

    print("\n─────────────────────────────────────────")
    print(f"  Compass: {len(stale)} файл(а) не обновлялись >{THRESHOLD_DAYS} дней")
    for rel, days in stale:
        print(f"  · {rel}  ({days} дн.)")
    print("  Запусти /update-compass чтобы обновить")
    print("─────────────────────────────────────────\n")

if __name__ == "__main__":
    main()
