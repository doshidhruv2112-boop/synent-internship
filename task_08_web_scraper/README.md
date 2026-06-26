# Task 8 — Web Scraper

**GitHub:** https://github.com/doshidhruv2112-boop/synent-internship/tree/main/task_08_web_scraper

## Objective

Extract structured data from websites and save results to CSV and JSON.

## Requirements

- Python `requests` and **BeautifulSoup** libraries

## Features

- Scrapes book **titles**, **prices**, and **availability** from [books.toscrape.com](https://books.toscrape.com)
- Handles multi-page pagination automatically
- Exports results to **CSV** and **JSON**

## Files

| File | Description |
|------|-------------|
| `web_scraper.py` | Fetches pages, parses HTML, saves output |

## How to Run

From the project root (install dependencies first — see main README):

```bash
cd task_08_web_scraper
python web_scraper.py
```

Scrape a specific number of pages (default is 2):

```bash
python web_scraper.py 3
```

## Output

Generated at runtime in `output/` (not committed to Git):

```
output/
├── books.json
└── books.csv
```
