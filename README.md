# Synent Technologies — Python Internship Tasks

Python projects completed during internship at **Synent Technologies**.

## Tasks

| Task | Name | Folder |
|------|------|--------|
| 5 | File Organizer | `task_05_file_organizer/` |
| 7 | Student Management System | `task_07_student_management/` |
| 8 | Web Scraper | `task_08_web_scraper/` |

## Setup

```bash
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

## Task 5 — File Organizer

Automatically sorts files into folders by type (Images, Docs, Videos).

```bash
cd task_05_file_organizer
python create_sample_files.py   # creates test files in sample_downloads/
python file_organizer.py        # organizes them into Images, Docs, Videos, Others
```

Pass a custom directory:

```bash
python file_organizer.py "C:\path\to\your\folder"
```

> `sample_downloads/` is generated when you run the scripts and is not committed to Git.

## Task 7 — Student Management System

CLI to add, view, update, and delete student records. Data is stored in `data/students.json`.

```bash
cd task_07_student_management
python main.py
```

## Task 8 — Web Scraper

Scrapes book titles and prices from [books.toscrape.com](https://books.toscrape.com) and saves results to CSV and JSON.

```bash
cd task_08_web_scraper
python web_scraper.py
```

Output files are written to `task_08_web_scraper/output/` (generated at runtime, not committed to Git).

## Author

Internship project — Synent Technologies
