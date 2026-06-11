"""
Task 8: Web Scraper
Scrapes book titles and prices from books.toscrape.com
and saves results to CSV and JSON.
"""

import csv
import json
import os
import sys
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")


def fetch_page(url: str) -> BeautifulSoup:
    """Fetch a page and return parsed BeautifulSoup object."""
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def scrape_books(soup: BeautifulSoup) -> list[dict[str, str]]:
    """Extract book title, price, and availability from a catalog page."""
    books = []

    for article in soup.select("article.product_pod"):
        title = article.h3.a["title"] if article.h3 and article.h3.a else "N/A"
        price_tag = article.select_one(".price_color")
        price = price_tag.text.strip() if price_tag else "N/A"

        availability_tag = article.select_one(".instock.availability")
        availability = availability_tag.text.strip() if availability_tag else "N/A"

        books.append({
            "title": title,
            "price": price,
            "availability": availability,
        })

    return books


def get_next_page(soup: BeautifulSoup, current_url: str) -> str | None:
    """Return the URL of the next page, or None if on the last page."""
    next_btn = soup.select_one("li.next a")
    if next_btn and next_btn.get("href"):
        return urljoin(current_url, next_btn["href"])
    return None


def scrape_all_pages(max_pages: int | None = None) -> list[dict[str, str]]:
    """Scrape books from all catalog pages (or up to max_pages)."""
    all_books: list[dict[str, str]] = []
    url: str | None = BASE_URL
    page_num = 0

    while url:
        page_num += 1
        print(f"  Scraping page {page_num}: {url}")
        soup = fetch_page(url)
        books = scrape_books(soup)
        all_books.extend(books)
        print(f"    Found {len(books)} book(s)")

        if max_pages and page_num >= max_pages:
            break

        url = get_next_page(soup, url)

    return all_books


def save_to_json(books: list[dict[str, str]], filepath: str) -> None:
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(books, f, indent=2, ensure_ascii=False)
    print(f"  Saved JSON: {filepath}")


def save_to_csv(books: list[dict[str, str]], filepath: str) -> None:
    if not books:
        return

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "price", "availability"])
        writer.writeheader()
        writer.writerows(books)
    print(f"  Saved CSV:  {filepath}")


def main() -> None:
    max_pages = int(sys.argv[1]) if len(sys.argv) > 1 else 2

    print("Task 8: Web Scraper")
    print(f"Source: {BASE_URL}")
    print(f"Max pages: {max_pages}\n")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    try:
        books = scrape_all_pages(max_pages=max_pages)
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

    if not books:
        print("No books found.")
        return

    json_path = os.path.join(OUTPUT_DIR, "books.json")
    csv_path = os.path.join(OUTPUT_DIR, "books.csv")

    print(f"\nTotal books scraped: {len(books)}\n")
    save_to_json(books, json_path)
    save_to_csv(books, csv_path)
    print("\nDone!")


if __name__ == "__main__":
    main()
