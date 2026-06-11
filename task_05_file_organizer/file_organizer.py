"""
Task 5: File Organizer
Automatically organizes files into folders by type (Images, Docs, Videos).
Uses os and shutil modules.
"""

import os
import shutil
import sys

# File extensions grouped by category
CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".ico"},
    "Docs": {".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"},
    "Videos": {".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"},
}


def get_category(filename: str) -> str:
    """Return the folder name for a file based on its extension."""
    _, ext = os.path.splitext(filename)
    ext = ext.lower()

    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category

    return "Others"


def organize_directory(target_dir: str) -> dict[str, int]:
    """
    Sort files in target_dir into subfolders by type.
    Returns a count of files moved per category.
    """
    if not os.path.isdir(target_dir):
        raise NotADirectoryError(f"Directory not found: {target_dir}")

    moved: dict[str, int] = {cat: 0 for cat in CATEGORIES}
    moved["Others"] = 0

    for item in os.listdir(target_dir):
        item_path = os.path.join(target_dir, item)

        # Skip directories (including category folders we create)
        if not os.path.isfile(item_path):
            continue

        category = get_category(item)
        dest_folder = os.path.join(target_dir, category)
        os.makedirs(dest_folder, exist_ok=True)

        dest_path = os.path.join(dest_folder, item)

        # Avoid overwriting — append a number if file already exists
        if os.path.exists(dest_path):
            base, ext = os.path.splitext(item)
            counter = 1
            while os.path.exists(dest_path):
                dest_path = os.path.join(dest_folder, f"{base}_{counter}{ext}")
                counter += 1

        shutil.move(item_path, dest_path)
        moved[category] += 1
        print(f"  Moved: {item} -> {category}/")

    return moved


def main() -> None:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    target = sys.argv[1] if len(sys.argv) > 1 else os.path.join(script_dir, "sample_downloads")

    print(f"Organizing files in: {target}\n")

    try:
        results = organize_directory(target)
    except NotADirectoryError as e:
        print(f"Error: {e}")
        sys.exit(1)

    print("\n--- Summary ---")
    total = 0
    for category, count in results.items():
        if count > 0:
            print(f"  {category}: {count} file(s)")
            total += count

    if total == 0:
        print("  No files to organize.")
    else:
        print(f"\n  Total: {total} file(s) organized.")


if __name__ == "__main__":
    main()
