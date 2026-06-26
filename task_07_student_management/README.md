# Task 7 — Student Management System

## Objective

Manage student records through a command-line interface with persistent file storage.

## Requirements

- Add, update, and delete student data
- Store records in **JSON** and **CSV** files

## Features

- Add new students
- View all students in a formatted table
- Update existing student details
- Delete students by ID
- Dual storage: `data/students.json` and `data/students.csv`

## Files

| File | Description |
|------|-------------|
| `main.py` | Interactive CLI menu |
| `student_manager.py` | CRUD operations (add, read, update, delete) |
| `storage.py` | Load/save logic for JSON and CSV |
| `data/students.json` | Sample student data (JSON) |
| `data/students.csv` | Sample student data (CSV) |

## How to Run

From the project root (after setup in main README):

```bash
cd task_07_student_management
python main.py
```

## Menu Options

1. View all students
2. Add student
3. Update student
4. Delete student
5. Exit
