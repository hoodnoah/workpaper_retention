import fitz  # pymupdf
from pathlib import Path

FINAL_REPORT_PATH = Path("./Final Reports")


def main():
    # List all report files
    pdf_files_iterator = FINAL_REPORT_PATH.glob("*.pdf")

    num_files = 0
    for _ in pdf_files_iterator:
        num_files += 1

    print(f"Number of reports: {num_files}")


if __name__ == "__main__":
    main()
