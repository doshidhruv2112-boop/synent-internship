# Synent Technologies — Python Internship Tasks

Python projects completed during internship at **Synent Technologies**.

## Submission Links

| Task | Project | GitHub Link |
|------|---------|-------------|
| **5** | File Organizer | https://github.com/doshidhruv2112-boop/synent-internship/tree/main/task_05_file_organizer |
| **7** | Student Management System | https://github.com/doshidhruv2112-boop/synent-internship/tree/main/task_07_student_management |
| **8** | Web Scraper | https://github.com/doshidhruv2112-boop/synent-internship/tree/main/task_08_web_scraper |

**Repository:** https://github.com/doshidhruv2112-boop/synent-internship

## Setup

```bash
git clone https://github.com/doshidhruv2112-boop/synent-internship.git
cd synent-internship
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

## Task 5 — File Organizer

Automatically sorts files into folders by type (Images, Docs, Videos, Others) using `os` and `shutil`.

**Link:** [task_05_file_organizer](https://github.com/doshidhruv2112-boop/synent-internship/tree/main/task_05_file_organizer)

```bash
cd task_05_file_organizer
python create_sample_files.py   # creates test files in sample_downloads/
python file_organizer.py        # organizes them into category folders
```

## Task 7 — Student Management System

CLI application with full CRUD (add, view, update, delete) for student records. Data persisted in JSON and CSV.

**Link:** [task_07_student_management](https://github.com/doshidhruv2112-boop/synent-internship/tree/main/task_07_student_management)

```bash
cd task_07_student_management
python main.py
```

## Task 8 — Web Scraper

Scrapes book titles, prices, and availability from [books.toscrape.com](https://books.toscrape.com) using `requests` and BeautifulSoup. Exports to CSV and JSON.

**Link:** [task_08_web_scraper](https://github.com/doshidhruv2112-boop/synent-internship/tree/main/task_08_web_scraper)

```bash
cd task_08_web_scraper
python web_scraper.py
```

## Author

Internship project — Synent Technologies
