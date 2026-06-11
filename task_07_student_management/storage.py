"""File-based storage for student records (JSON and CSV)."""

import csv
import json
import os
from typing import Any

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
JSON_FILE = os.path.join(DATA_DIR, "students.json")
CSV_FILE = os.path.join(DATA_DIR, "students.csv")

FIELDNAMES = ["id", "name", "age", "course", "email"]


def _ensure_data_dir() -> None:
    os.makedirs(DATA_DIR, exist_ok=True)


def load_students() -> list[dict[str, Any]]:
    """Load students from JSON file. Returns empty list if file doesn't exist."""
    _ensure_data_dir()

    if not os.path.exists(JSON_FILE):
        return []

    with open(JSON_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_students(students: list[dict[str, Any]]) -> None:
    """Persist students to both JSON and CSV files."""
    _ensure_data_dir()

    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(students, f, indent=2)

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(students)


def next_id(students: list[dict[str, Any]]) -> int:
    """Generate the next available student ID."""
    if not students:
        return 1
    return max(s["id"] for s in students) + 1
