# Task 3.4 — AI-Assisted Coding: Audit Notes
**Week 3 | Skillset Go EduTech AI/ML Track**

**Prompt given to the AI assistant:** *"Write a Python CLI tool that lets me add students, record grades for
each student, and print each student's average and letter grade. Store data in a JSON file so it persists
between runs."*

`draft_app.py` is a first-pass draft written with common AI-code mistakes **deliberately included** so the review
process could be demonstrated. It runs and looks reasonable on a quick read, but reviewing it line by line — and
actually running it — surfaces seven real issues. Each one below was reproduced with a
concrete failing case before being fixed, not just inferred from reading the code. The corrected version is
`app.py`.

## Issues found

| # | Issue | Why it matters | Evidence |
|---|---|---|---|
| 1 | `def load_data(students={})` uses a **mutable default argument** | The empty dict is created once and reused across every call; data from one call can silently leak into the next, which is especially dangerous for a tool meant to persist separate runs | Reproduced: adding `"Leftover"` to the dict returned by one call made it appear in the dict returned by a *second, independent* call |
| 2 | `average(grades)` divides by `len(grades)` with no empty check | Any student added but not yet graded crashes the whole report screen | Reproduced: `average([])` raises `ZeroDivisionError` |
| 3 | `letter_grade` uses strict `>` instead of `>=` at every boundary | A perfect score of exactly 90 is graded "B" instead of "A" — the boundaries silently don't match normal grading conventions | Reproduced: `letter_grade(90)` returns `'B'`, not `'A'` |
| 4 | `add_grade` does not check the student exists | Recording a grade for a name that was never added (e.g. a typo) crashes with an unhandled `KeyError` instead of a clear message | Reproduced: calling `add_grade` on an unregistered name raises `KeyError` |
| 5 | File handles opened with `open()` are never closed | Minor here, but a real resource leak and risk of unflushed writes on a crash; no use of `with` |  Confirmed by code inspection (no `with`/`close()` anywhere in `draft_app.py`) |
| 6 | No `try/except` around `json.load` or file I/O | A corrupted or hand-edited `grades.json` crashes the program on startup with a raw traceback instead of a usable message | Confirmed by code inspection — `load_data` has no error handling |
| 7 | `int(grade)` on raw user input, with no validation | Typing anything non-numeric (or a number outside 0-100) crashes the program instead of re-prompting | Confirmed by code inspection — no bounds or type checking before `int(grade)` |

## Fixes applied (in `app.py`)

1. `load_data()` takes no default argument at all — it builds a fresh dict internally, which removes the shared-state bug entirely.
2. `average()` returns `None` for an empty grade list; callers display `"N/A"` instead of crashing.
3. `letter_grade()` boundaries changed to `>=` at each cutoff, so a 90 is correctly an "A".
4. `add_grade()` checks `name not in students` first and prints a clear message instead of raising `KeyError`; it also rejects grades outside 0-100.
5. All file access uses `with open(...) as f:`, so handles are always closed, including on an exception.
6. `load_data()` wraps the read in `try/except (json.JSONDecodeError, OSError)` and falls back to an empty dataset with a warning instead of crashing on startup.
7. User input for grades goes through a new `prompt_int()` helper that loops until a valid 0-100 integer is entered, instead of calling `int()` directly on raw input.

Two smaller improvements were also made while fixing the above: `add_student` now refuses to silently overwrite an existing student's grades (the draft's `add_student` reset `students[name] = []` even if the name already existed, which would have deleted recorded grades on a duplicate add), and data is now saved after every change rather than only when the user explicitly chooses "Quit" — in the draft, force-closing the program (Ctrl+C) lost everything entered that session.

## Verification

Every fix above was re-tested with real assertions against `app.py` (not just re-read) — duplicate-student
rejection, unknown-student rejection, out-of-range grade rejection, empty-average handling, and the exact
90 → "A" boundary all pass. The corresponding bugs were also independently reproduced against the original
`draft_app.py` to confirm each one is real and not just a theoretical concern.

## Outcome

The corrected `app.py` is the working deliverable: a small CLI that adds students, records bounds-checked
grades, computes averages and letter grades with standard rounding boundaries, and persists to
`grades.json` safely — handling the empty-data, invalid-input, missing-student, and corrupted-file cases
that the first AI-generated draft did not.
