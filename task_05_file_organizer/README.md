# Task 5 — File Organizer

**GitHub:** https://github.com/doshidhruv2112-boop/synent-internship/tree/main/task_05_file_organizer

## Objective

Automatically organize files into folders based on file type.

## Requirements

- Python `os` and `shutil` modules

## Features

- Sorts files into **Images**, **Docs**, **Videos**, and **Others**
- Creates category folders automatically
- Supports custom directory input via command line
- Includes sample file generator for testing

## Files

| File | Description |
|------|-------------|
| `file_organizer.py` | Main script — scans a folder and moves files by extension |
| `create_sample_files.py` | Creates test files in `sample_downloads/` |

## How to Run

From the project root (after setup in main README):

```bash
cd task_05_file_organizer
python create_sample_files.py
python file_organizer.py
```

Custom folder:

```bash
python file_organizer.py "C:\path\to\your\folder"
```

## Output

A clean directory structure with files grouped by type:

```
sample_downloads/
├── Images/
├── Docs/
├── Videos/
└── Others/
```
