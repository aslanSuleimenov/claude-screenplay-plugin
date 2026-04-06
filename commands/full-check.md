---
description: Comprehensive screenplay analysis. Runs all 14 analysis agents in optimal order (foundation → macro → continuity → characters → craft). Produces consolidated dashboard with priority fixes. Requires CLAUDE.md project setup.
---

# /full-check

Run complete screenplay quality audit using all 14 analysis agents.

## Usage

```
/full-check              # Analyze entire script
/full-check 1-20         # Analyze scenes 1-20 only
/full-check 45-72        # Analyze scenes 45-72 only
```

## What It Does

Orchestrates 14 specialized agents in 6 phases:

**Phase 1 — Foundation**
- `action-line-checker` — spec formatting, filmability
- `timeline-checker` — day/night, continuity, physical states

**Phase 2 — Macro Structure**
- `structure-checker` — beat positions (Save the Cat framework)
- `scene-balance-checker` — ACTION/DIALOGUE/EXPOSITION distribution
- `dialogue-ratio-checker` — cumulative pacing ratio vs genre

**Phase 3 — Continuity & Logic**
- `scene-continuity-checker` — props, costumes, positions
- `plot-thread-checker` — setup/payoff, dangling threads
- `tone-checker` — genre register consistency

**Phase 4 — Characters**
- `character-ooc-checker` — dialogue voice, behavior consistency

**Phase 5 — Scene-Level Craft**
- `value-shift-checker` — does each scene turn? (McKee)
- `scene-hook-checker` — YES-BUT / NO-AND momentum
- `scene-economy-checker` — enter late, exit early
- `subtext-checker` — on-the-nose dialogue
- `visual-storytelling-checker` — visual story independence

**Phase 6 — Synthesis**
- Consolidates all 14 reports into `analytics/full-check-dashboard.md`
- Prioritizes fixes by impact
- Flags critical issues

## Output

Creates 15 files in `analytics/`:

- `full-check-dashboard.md` — **main report** (start here)
- `action-line-report.md`
- `timeline-report.md`
- `structure-report.md`
- `balance-report.md`
- `ratio-report.md`
- `continuity-report.md`
- `plot-report.md`
- `tone-report.md`
- `ooc-report.md`
- `value-report.md`
- `hook-report.md`
- `economy-report.md`
- `subtext-report.md`
- `visual-report.md`

## Time

Full script: **~90 minutes**
Partial range: **~45-60 minutes** (depends on scene count)

## Requirements

- CLAUDE.md must exist (project metadata + genre)
- `chapters/` or `scenes/` directory with scene files
- `/outline` beat sheet helpful (optional, structure-checker will infer)

## Example Output

```
═══════════════════════════════════════════════════════════
FULL SCREENPLAY CHECK — DASHBOARD

Script: The Heist
Genre: Thriller
Length: 47 scenes
═══════════════════════════════════════════════════════════

⚠️  CRITICAL ISSUES
────────────────────────────────────────────────────────────
[None found]

🔴 PRIORITY FIXES
────────────────────────────────────────────────────────────
1. VALUE SHIFTS: 7 scenes with no clear turn (static)
   → Rewrite scenes 12, 18, 24, 31, 38, 41, 44 or cut them

2. STRUCTURE: Inciting incident at 16% (should be ~12%)
   → Minor — within tolerance, but could tighten Act I

3. DIALOGUE RATIO: 58% dialogue (expected 60% for thriller)
   → Slightly action-heavy; acceptable range

4. CONTINUITY: 3 prop inconsistencies (gun position, jacket)
   → Minor production issues, easy fixes

PHASE RESULTS
────────────────────────────────────────────────────────────
Phase 1 - Foundation: ✓ PASS
Phase 2 - Macro: ✓ PASS (minor structure variance)
Phase 3 - Continuity: ✓ PASS (3 minor prop issues)
Phase 4 - Characters: ✓ PASS
Phase 5 - Craft: ⚠️ ATTENTION (static scenes, weak hooks)

VERDICT
────────────────────────────────────────────────────────────
Screenplay is structurally sound and well-executed. Main issue:
7 scenes lack dramatic turn (value shift). These should be
rewritten for dramatic purpose or cut. Otherwise, strong
thriller fundamentals with solid character work.

Next steps:
1. Review value-report.md for specific static scenes
2. Fix those 7 scenes (rewrite or cut)
3. Light touch-ups to structure timing
4. Final pass on dialogue subtext
```

## Notes

- Agents run in **optimal dependency order** (foundation before details)
- Phase 1 is a **gate** — if foundation fails, subsequent phases abort
- Agents within same phase run **in parallel** for speed
- All reports are **permanent archive** in analytics/
- Dashboard links to detailed reports for investigation
- Command requires user confirmation for long runtime

## See Also

- `/analyze` — analyze single scene (quick check)
- `/check style` / `/check continuity` — specific agent runs
- `deep-check` agent — the orchestrator (runs behind `/full-check`)
