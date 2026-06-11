"""
Task 7: Student Management System
Add, update, and delete student records with JSON/CSV file storage.
"""

import student_manager as sm


def print_students(students: list) -> None:
    if not students:
        print("  No students found.")
        return

    print(f"\n  {'ID':<5} {'Name':<20} {'Age':<5} {'Course':<15} {'Email'}")
    print("  " + "-" * 65)
    for s in students:
        print(f"  {s['id']:<5} {s['name']:<20} {s['age']:<5} {s['course']:<15} {s['email']}")
    print()


def prompt_int(message: str) -> int:
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("  Please enter a valid number.")


def handle_add() -> None:
    print("\n--- Add Student ---")
    name = input("  Name: ").strip()
    age = prompt_int("  Age: ")
    course = input("  Course: ").strip()
    email = input("  Email: ").strip()

    if not name or not course or not email:
        print("  Error: Name, course, and email are required.")
        return

    student = sm.add_student(name, age, course, email)
    print(f"\n  Student added successfully (ID: {student['id']}).")


def handle_update() -> None:
    print("\n--- Update Student ---")
    student_id = prompt_int("  Enter student ID: ")
    student = sm.get_student(student_id)

    if not student:
        print(f"  Student with ID {student_id} not found.")
        return

    print(f"  Current: {student['name']}, {student['age']}, {student['course']}, {student['email']}")
    print("  Press Enter to keep current value.\n")

    name = input(f"  Name [{student['name']}]: ").strip() or None
    age_str = input(f"  Age [{student['age']}]: ").strip()
    age = int(age_str) if age_str else None
    course = input(f"  Course [{student['course']}]: ").strip() or None
    email = input(f"  Email [{student['email']}]: ").strip() or None

    updated = sm.update_student(student_id, name=name, age=age, course=course, email=email)
    print(f"\n  Student updated: {updated['name']} (ID: {updated['id']}).")


def handle_delete() -> None:
    print("\n--- Delete Student ---")
    student_id = prompt_int("  Enter student ID: ")

    if sm.delete_student(student_id):
        print(f"  Student ID {student_id} deleted.")
    else:
        print(f"  Student with ID {student_id} not found.")


def main() -> None:
    menu = {
        "1": ("View all students", lambda: print_students(sm.list_students())),
        "2": ("Add student", handle_add),
        "3": ("Update student", handle_update),
        "4": ("Delete student", handle_delete),
        "5": ("Exit", None),
    }

    print("=" * 40)
    print("  Student Management System")
    print("=" * 40)

    while True:
        print("\nMenu:")
        for key, (label, _) in menu.items():
            print(f"  {key}. {label}")

        choice = input("\nSelect option: ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        action = menu.get(choice)
        if action:
            action[1]()
        else:
            print("  Invalid option. Try again.")


if __name__ == "__main__":
    main()
