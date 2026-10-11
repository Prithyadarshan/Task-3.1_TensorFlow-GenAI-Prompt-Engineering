"""
Student Grade Manager — CORRECTED (after audit of the AI-generated draft)
See audit_notes.md for the full list of issues found in draft_app.py and
how each one was fixed below.
"""
import json
import os

DATA_FILE = "grades.json"


def load_data():
    """Load student->grades data from DATA_FILE, or start empty if missing/corrupt."""
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"Warning: could not read {DATA_FILE} ({e}); starting with empty data.")
        return {}


def save_data(students):
    """Persist student->grades data to DATA_FILE."""
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(students, f, indent=2)
    except OSError as e:
        print(f"Warning: could not save data ({e}).")


def add_student(students, name):
    """Add a new student. Returns False (and does nothing) if the name already exists,
    so re-adding a student never silently wipes their recorded grades."""
    name = name.strip()
    if not name:
        print("Student name cannot be empty.")
        return False
    if name in students:
        print(f"'{name}' already exists — not overwriting their grades.")
        return False
    students[name] = []
    return True


def add_grade(students, name, grade):
    """Add a grade (0-100) for an existing student. Returns False on any invalid input."""
    if name not in students:
        print(f"No such student: '{name}'. Add them first.")
        return False
    if not (0 <= grade <= 100):
        print("Grade must be between 0 and 100.")
        return False
    students[name].append(grade)
    return True


def average(grades):
    """Average of a grade list. Returns None for a student with no grades yet,
    instead of raising ZeroDivisionError."""
    if not grades:
        return None
    return sum(grades) / len(grades)


def letter_grade(avg):
    """Standard letter-grade boundaries (inclusive lower bound, matching common
    grading conventions: 90+ is A, 80-89 is B, and so on)."""
    if avg is None:
        return "N/A"
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def prompt_int(prompt_text, lo=0, hi=100):
    """Repeatedly prompt until a valid integer in [lo, hi] is entered."""
    while True:
        raw = input(prompt_text)
        try:
            value = int(raw)
        except ValueError:
            print(f"Please enter a whole number between {lo} and {hi}.")
            continue
        if not (lo <= value <= hi):
            print(f"Please enter a number between {lo} and {hi}.")
            continue
        return value


def report(students):
    if not students:
        print("No students yet.")
        return
    for name, grades in students.items():
        avg = average(grades)
        avg_display = f"{avg:.1f}" if avg is not None else "N/A"
        print(f"{name:<15} avg={avg_display:<6} grade={letter_grade(avg)}  (n={len(grades)})")


def main():
    students = load_data()
    menu = "\n1. Add student  2. Add grade  3. Show report  4. Quit\n> "
    while True:
        choice = input(menu).strip()
        if choice == "1":
            name = input("Student name: ")
            if add_student(students, name):
                save_data(students)
        elif choice == "2":
            name = input("Student name: ")
            grade = prompt_int("Grade (0-100): ")
            if add_grade(students, name, grade):
                save_data(students)
        elif choice == "3":
            report(students)
        elif choice == "4":
            save_data(students)
            print("Saved. Goodbye.")
            break
        else:
            print("Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
