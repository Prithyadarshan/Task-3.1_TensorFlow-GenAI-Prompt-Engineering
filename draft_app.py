"""
Student Grade Manager — DRAFT (AI-generated first pass)
Prompt given to the AI assistant:
  "Write a Python CLI tool that lets me add students, record grades for each
  student, and print each student's average and letter grade. Store data in
  a JSON file so it persists between runs."

This file is the assistant's first output, kept as-is for the audit in
Task 3.4. See audit_notes.md for the issues found and task4_app.py for the
corrected version.
"""
import json
import os

DATA_FILE = "grades.json"


def load_data(students={}):
    if os.path.exists(DATA_FILE):
        f = open(DATA_FILE, "r")
        students = json.load(f)
    return students


def save_data(students):
    f = open(DATA_FILE, "w")
    json.dump(students, f)


def add_student(students, name):
    students[name] = []


def add_grade(students, name, grade):
    students[name].append(grade)


def average(grades):
    return sum(grades) / len(grades)


def letter_grade(avg):
    if avg > 90:
        return "A"
    elif avg > 80:
        return "B"
    elif avg > 70:
        return "C"
    elif avg > 60:
        return "D"
    else:
        return "F"


def main():
    students = load_data()
    while True:
        print("1. Add student  2. Add grade  3. Show report  4. Quit")
        choice = input("> ")
        if choice == "1":
            name = input("Student name: ")
            add_student(students, name)
        elif choice == "2":
            name = input("Student name: ")
            grade = input("Grade (0-100): ")
            add_grade(students, name, int(grade))
        elif choice == "3":
            for name, grades in students.items():
                avg = average(grades)
                print(name, avg, letter_grade(avg))
        elif choice == "4":
            save_data(students)
            break


if __name__ == "__main__":
    main()
