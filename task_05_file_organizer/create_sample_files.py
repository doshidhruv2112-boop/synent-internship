"""Create sample files in sample_downloads/ for testing the file organizer."""

import os

SAMPLE_DIR = os.path.join(os.path.dirname(__file__), "sample_downloads")

SAMPLE_FILES = [
    "photo.jpg",
    "screenshot.png",
    "report.pdf",
    "notes.txt",
    "presentation.pptx",
    "clip.mp4",
    "demo.avi",
    "data.csv",
    "archive.zip",
]


def main() -> None:
    os.makedirs(SAMPLE_DIR, exist_ok=True)

    for name in SAMPLE_FILES:
        path = os.path.join(SAMPLE_DIR, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"Sample file: {name}\n")

    print(f"Created {len(SAMPLE_FILES)} sample files in {SAMPLE_DIR}")


if __name__ == "__main__":
    main()
