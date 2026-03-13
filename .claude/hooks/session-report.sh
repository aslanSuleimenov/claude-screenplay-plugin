#!/bin/bash
# Хук Stop: записывает отчёт о сессии в memory/session_log.md
# Находит файлы сцен, изменённые за последние 2 часа

PROJ_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
SCENES_DIR="$PROJ_DIR/scenes"
LOG_FILE="$PROJ_DIR/memory/session_log.md"

mkdir -p "$PROJ_DIR/memory"

TIMESTAMP=$(date "+%Y-%m-%d %H:%M")

# POSIX-совместимый вариант (без -printf)
MODIFIED=""
if [ -d "$SCENES_DIR" ]; then
  for f in $(find "$SCENES_DIR" -name "*.md" -mmin -120 2>/dev/null); do
    name=$(basename "$f")
    if [ -z "$MODIFIED" ]; then
      MODIFIED="$name"
    else
      MODIFIED="$MODIFIED
$name"
    fi
  done
  MODIFIED=$(echo "$MODIFIED" | sort)
fi

if [ -z "$MODIFIED" ]; then
  exit 0
fi

# Записать в лог
{
  echo ""
  echo "## Сессия $TIMESTAMP"
  echo ""
  echo "Изменённые файлы:"
  echo "$MODIFIED" | while read f; do
    echo "- $f"
  done
} >> "$LOG_FILE"

exit 0
