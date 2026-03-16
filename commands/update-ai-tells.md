Search the web for new AI writing patterns and merge them into the canonical avoid-ai-writing-tells.md file.

---

## Step 1 — Read current file

Read `${CLAUDE_PLUGIN_ROOT}/analytics/avoid-ai-writing-tells.md`. Note all existing patterns — you will not duplicate them.

---

## Step 2 — Search the web

Search for recent sources (prioritize 2025–2026):

1. "signs of AI writing" Wikipedia
2. "AI writing detection patterns" NLP research
3. "how to detect AI generated text" 2026
4. "AI writing tells screenwriting"
5. "ChatGPT writing patterns avoid"
6. "LLM text detection markers linguistic"
7. "AI сгенерированный текст признаки" (Russian)

For each source found — extract specific patterns (words, constructions, structural habits). Skip vague advice like "AI text sounds generic."

---

## Step 3 — Filter and deduplicate

Compare found patterns against the existing file. Keep only patterns that:
- Are concrete (a specific word, phrase, or construction)
- Are not already in the file
- Apply to screenplay or general writing (not academic papers or SEO)

---

## Step 4 — Show results

Present new patterns to the user grouped by section:

```
Found N new patterns from M sources:

ENGLISH PATTERNS:
- [section name]: "pattern" — why it signals AI (source: URL)
- ...

RUSSIAN PATTERNS:
- [section name]: "pattern" — why it signals AI (source: URL)

SCREENPLAY-SPECIFIC:
- ...

SOURCES:
- [title](URL) — what was useful
- ...
```

Ask: "Add these to avoid-ai-writing-tells.md?"

---

## Step 5 — Merge

After confirmation, add new patterns to the appropriate sections in `${CLAUDE_PLUGIN_ROOT}/analytics/avoid-ai-writing-tells.md`.

Rules:
- Add to existing sections where they fit
- If a pattern doesn't fit any section — create a new numbered section
- Always add the source URL as a comment next to new patterns
- Update the Sources line at the top of the file with new sources
- Do not remove or rewrite existing patterns
- Do not change the structure or numbering of existing sections

---

## Step 6 — Report

```
Updated: ${CLAUDE_PLUGIN_ROOT}/analytics/avoid-ai-writing-tells.md

Added: N new patterns
Sources: M new sources
Sections modified: [list]

To sync to current project: /sync-plugin-files
```
