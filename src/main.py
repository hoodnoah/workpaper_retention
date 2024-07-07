from pathlib import Path

FINAL_REPORT_PATH = Path("./Final Reports")


def main():
    reports_iterator = FINAL_REPORT_PATH.glob("**/*.pdf")


if __name__ == "__main__":
    main()
