# util
import csv
from pathlib import Path
from datetime import datetime

# types
from typing import Optional

# lib
from lib.wp_processor import process_wp, WorkPaper

FINAL_REPORT_PATH = Path("./Final Reports")


# processes a report; printing an error message and returning None
# when `process_wp` fails
def handle_report(report_path: Path) -> Optional[WorkPaper]:
    print(f"[INFO]: Processing {report_path.name}...")
    result = process_wp(report_path)
    if result is None:
        print(f"[ERROR]: Failed to process {str(report_path)}")
        return None

    return result


def main():
    start_time = datetime.now()
    reports_processed = 0

    reports_iterator = FINAL_REPORT_PATH.glob("*.[pP][dD][fF]")

    processed_reports = map(handle_report, reports_iterator)
    processed_reports = (
        wp for wp in processed_reports if wp is not None
    )  # filter off failures

    # sort by client name, then by DestructionDate
    processed_reports = sorted(
        processed_reports, key=lambda x: (x.ClientName, x.DestructionDate)
    )

    with open("destruction_manifest.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["client_name", "fiscal_year_end", "destruction_date"])

        for workpaper in processed_reports:
            writer.writerow(
                [
                    workpaper.ClientName,
                    workpaper.FiscalYearEnd,
                    workpaper.DestructionDate,
                ]
            )

            reports_processed += 1

    end_time = datetime.now()
    elapsed = end_time - start_time
    print(
        f"[INFO]: Done. Processed {reports_processed} reports in {elapsed.total_seconds()} seconds."
    )


if __name__ == "__main__":
    main()
