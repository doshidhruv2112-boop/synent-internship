"""CRUD operations for student records."""

from typing import Any

from storage import load_students, next_id, save_students


def list_students() -> list[dict[str, Any]]:
    return load_students()


def get_student(student_id: int) -> dict[str, Any] | None:
    for student in load_students():
        if student["id"] == student_id:
            return student
    return None


def add_student(name: str, age: int, course: str, email: str) -> dict[str, Any]:
    students = load_students()
    student = {
        "id": next_id(students),
        "name": name.strip(),
        "age": age,
        "course": course.strip(),
        "email": email.strip(),
    }
    students.append(student)
    save_students(students)
    return student


def update_student(student_id: int, **fields: Any) -> dict[str, Any] | None:
    students = load_students()
    for student in students:
        if student["id"] == student_id:
            for key, value in fields.items():
                if key in student and value is not None:
                    student[key] = value.strip() if isinstance(value, str) else value
            save_students(students)
            return student
    return None


def delete_student(student_id: int) -> bool:
    students = load_students()
    original_len = len(students)
    students = [s for s in students if s["id"] != student_id]

    if len(students) == original_len:
        return False

    save_students(students)
    return True
