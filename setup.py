"""
Инициализация нового проекта сценария.
Запусти: python setup.py
"""
from pathlib import Path
from datetime import date
import sys

BASE = Path(__file__).parent


def check_template_protection():
    """Предупредить если запуск в мастер-копии _template."""
    folder_name = BASE.name.lower()
    if folder_name == "_template":
        print("\n⚠  ВНИМАНИЕ: Ты запускаешь setup.py в мастер-копии _template!")
        print("   Скопируй папку _template в новую (например: мой_фильм) и запусти там.")
        answer = input("   Продолжить всё равно? (да/нет): ").strip().lower()
        if answer not in ("да", "yes", "y", "д"):
            print("Отменено.")
            sys.exit(0)


def check_already_initialized(text):
    """Проверить что поля ещё содержат прочерки (не заполнены)."""
    fields_with_dash = [
        "- **Тип:** —",
        "- **Название:** —",
        "- **Жанр:** —",
    ]
    filled = [f for f in fields_with_dash if f not in text]
    if filled:
        print("\n⚠  CLAUDE.md уже содержит данные проекта.")
        answer = input("   Перезаписать? (да/нет): ").strip().lower()
        if answer not in ("да", "yes", "y", "д"):
            print("Отменено.")
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
        answer = input("Номер: ").strip()
        if answer.isdigit() and 1 <= int(answer) <= len(options):
            return options[int(answer) - 1]
        print("Введи номер из списка.")


# Шаблоны форматирования для CLAUDE.md
FICTION_FORMAT = """Строго по `converter_MD_DOCX/README.md`. Краткие правила:

```markdown
# Сцена 01: Название

**ИНТ./НАТ. ЛОКАЦИЯ — ВРЕМЯ СУТОК**

Описание действия. Настоящее время, третье лицо. Максимум 4 строки в абзаце.

**ИМЯ ПЕРСОНАЖА**
*(ремарка)*
Текст диалога.
```

- ОДНА пустая строка между блоками; НОЛЬ между именем и диалогом
- Имена — **жирными заглавными**: `**ИМЯ**`
- Slug line — **жирным**: `**ИНТ. ЛОКАЦИЯ — ДЕНЬ**`
- Первое появление: `ИМЯ (возраст)` заглавными в тексте действия
- Не использовать: `ЗАТЕМНЕНИЕ.`, `CUT TO:`, `КРУПНЫЙ ПЛАН:`
- Числа в диалогах — словами
- `---` — смена локации внутри сцены (конвертер пропускает)
- `> **ПАЛИТРА:** ...` — визуальная заметка"""

DOC_FORMAT = """Строго по `converter_MD_DOCX/README.md`, раздел «Документальный формат». Краткие правила:

```markdown
# Блок 01: Название

| VIDEO | AUDIO |
|-------|-------|
| WS. Горы, рассвет. | *(NAT SOUND: ветер)* |
| MS. Пастух ведёт стадо. | **V/O:** Текст закадрового голоса. |
| CU. Лицо героя. | **SOT АЙБЕК:** «Прямая речь героя.» |
| **SUPER:** Айбек, пастух, 43 года | |
| B-ROLL: юрты, дым, казан. | *(МУЗЫКА: комуз, тихо)* |
```

- Каждый блок = один файл `scenes/NN_название.md`
- Таблица `| VIDEO | AUDIO |` — обязательный формат
- Обозначения: **V/O** (закадр), **SOT** (синхрон/интервью), **SUPER** (титр), **NAT SOUND**, **SFX**, **B-ROLL**
- Размеры планов: WS, MS, CU, ECU, AERIAL
- `> **ЗАМЕТКА:** ...` — режиссёрская заметка (не попадает в DOCX)"""


def ask_int(question, default=None):
    """Запросить целое число с валидацией."""
    while True:
        answer = ask(question, default)
        if not answer:
            return default or ""
        try:
            int(answer)
            return answer
        except ValueError:
            print("  Введи число.")


def main():
    print("\n=== Новый проект сценария ===\n")

    check_template_protection()

    # Проверить что CLAUDE.md ещё не заполнен
    claude_md = BASE / "CLAUDE.md"
    text = claude_md.read_text(encoding="utf-8")
    check_already_initialized(text)

    proj_type  = ask_choice("Тип проекта:", ["художественный", "документальный"])
    title      = ask("Название проекта")
    genre      = ask("Жанр (чёрная комедия / триллер / драма / другое)")
    logline    = ask("Логлайн (одно предложение о чём фильм)")
    fmt        = ask("Формат (полный метр / короткометражка / пилот / сериал)", "полный метр")
    theme      = ask("Тема (о чём на глубинном уровне)")
    audience   = ask("Целевая аудитория")
    location   = ask("Место действия (страна, город, среда)")
    period     = ask("Время года и период (месяц, эпоха)")
    currency   = ask("Валюта и культурные реалии (имена, топонимы)")
    runtime    = ask_int("Целевой хронометраж в минутах", "90")
    structure  = ask("Структурная модель", "трёхактная")

    print("\nПерсонажи (имя, возраст, роль — по одному на строку, пустая строка для завершения):")
    characters = []
    while True:
        line = input("  > ").strip()
        if not line:
            break
        characters.append(line)

    today = date.today().strftime("%d.%m.%Y")

    # --- Заполнить CLAUDE.md ---
    claude_md = BASE / "CLAUDE.md"
    text = claude_md.read_text(encoding="utf-8")

    replacements = {
        "- **Тип:** —":              f"- **Тип:** {proj_type}",
        "- **Название:** —":         f"- **Название:** {title}",
        "- **Жанр:** —":             f"- **Жанр:** {genre}",
        "- **Логлайн:** —":          f"- **Логлайн:** {logline}",
        "- **Формат:** —":           f"- **Формат:** {fmt}",
        "- **Тема:** —":             f"- **Тема:** {theme}",
        "- **Целевая аудитория:** —": f"- **Целевая аудитория:** {audience}",
        "- **Место действия:** —":   f"- **Место действия:** {location}",
        "- **Время:** —":            f"- **Время:** {period}",
        "- **Валюта и реалии:** —":  f"- **Валюта и реалии:** {currency}",
        "- **Хронометраж:** —":      f"- **Хронометраж:** {runtime} минут",
        "- **Структурная модель:** —": f"- **Структурная модель:** {structure}",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    # Заменить блок форматирования на нужный тип
    format_block = DOC_FORMAT if proj_type == "документальный" else FICTION_FORMAT
    # Убрать условные секции, оставить только нужный формат
    start_marker = "## Форматирование сцен"
    end_marker = "## Правила работы"
    start_idx = text.find(start_marker)
    end_idx = text.find(end_marker)
    if start_idx != -1 and end_idx != -1:
        text = text[:start_idx] + f"## Форматирование сцен\n\n{format_block}\n\n" + text[end_idx:]

    # Персонажи — парсить ввод "Имя, Возраст, Роль" в колонки таблицы
    if characters:
        char_rows = []
        for c in characters:
            parts = [p.strip() for p in c.split(",")]
            if len(parts) >= 4:
                # Имя, Возраст, Роль, Want/Need
                char_rows.append(f"| {parts[0]} | {parts[1]} | {parts[2]} | {', '.join(parts[3:])} |")
            elif len(parts) == 3:
                char_rows.append(f"| {parts[0]} | {parts[1]} | {parts[2]} | — |")
            elif len(parts) == 2:
                char_rows.append(f"| {parts[0]} | — | {parts[1]} | — |")
            else:
                char_rows.append(f"| {parts[0]} | — | — | — |")
        text = text.replace(
            "| Имя | Возраст | Роль | Want / Need |\n|-----|---------|------|-------------|\n",
            "| Имя | Возраст | Роль | Want / Need |\n|-----|---------|------|-------------|\n" + "\n".join(char_rows) + "\n"
        )

    # История изменений
    text = text.replace(
        "| Дата | Изменение |\n|------|-----------|",
        f"| Дата | Изменение |\n|------|-----------|\n| {today} | Создан проект: {title} ({proj_type}) |"
    )

    claude_md.write_text(text, encoding="utf-8")

    # --- Создать титульную страницу ---
    scenes_dir = BASE / "scenes"
    scenes_dir.mkdir(exist_ok=True)

    title_page = scenes_dir / "00_титульная.md"
    title_page.write_text(
        f"# {title.upper()}\n\n"
        f"**{genre.upper()}**\n\n"
        f"*{proj_type}*\n\n"
        f"{logline}\n\n"
        f"Автор: —\n\n"
        f"{date.today().year}\n",
        encoding="utf-8"
    )

    # --- Итог ---
    print(f"\n✓ CLAUDE.md заполнен (тип: {proj_type})")
    print(f"✓ scenes/00_титульная.md создан")
    print(f"\nГотово. Запусти Claude Code:\n")
    print(f"  claude\n")
    print(f"Первая команда в Claude: /compass {genre} — {logline}\n")


if __name__ == "__main__":
    main()
