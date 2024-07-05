from datetime import date, datetime
from pathlib import Path
import re

import fitz

# types
from typing import Optional

MAX_NUM_SEARCH_PAGES = 3

DATE_REGEX = re.compile(
    r"\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}\b"
)


def _parse_date_string(date_string: str) -> Optional[date]:
    date = datetime.strptime(date_string, "%B %d, %Y").date()
    return date


def get_report_date(filepath: Path) -> Optional[date]:
    # open file

    # read text from first 3 pages
    text = ""
    with fitz.open(filepath) as file:
        for page_num in range(min(3, len(file))):
            text += file.get_page_text(page_num)

    dates_text = re.findall(DATE_REGEX, text)
    print(dates_text)
    dates_parsed = [_parse_date_string(text) for text in dates_text]
    dates_parsed_not_none = [
        parsed_date for parsed_date in dates_parsed if parsed_date is not None
    ]

    if dates_parsed_not_none and len(dates_parsed_not_none) > 0:
        return max(dates_parsed_not_none)
    else:
        return None
