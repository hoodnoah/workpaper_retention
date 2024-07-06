from datetime import date, datetime
from pathlib import Path
import re

import fitz

# types
from typing import List, Optional

MAX_NUM_SEARCH_PAGES = 4

DATE_REGEX = re.compile(
    r"\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}\b"
)


def _parse_date_string(date_string: str) -> Optional[date]:
    date = datetime.strptime(date_string, "%B %d, %Y").date()
    return date


def is_scanned_file(doc: fitz.Document) -> bool:
    # try and locate any text on the first 3 pages
    for page_num in range(min(MAX_NUM_SEARCH_PAGES, len(doc))):
        if doc.get_page_text(page_num) == "":
            return True

    return False


def get_text(doc: fitz.Document) -> str:
    num_search_pages = min(MAX_NUM_SEARCH_PAGES, len(doc))

    text = ""
    if not is_scanned_file(doc):
        for page_num in range(num_search_pages):
            text += doc.get_page_text(page_num)
    else:
        for page_num in range(num_search_pages):
            page = doc.load_page(page_num).get_textpage_ocr(dpi=200, full=True)
            text += page.extractText()

    return text


def get_report_date(filepath: Path) -> Optional[date]:
    with fitz.open(filepath) as doc:
        text = get_text(doc)

        dates_text = re.findall(DATE_REGEX, text)
        dates_parsed = [_parse_date_string(text) for text in dates_text]

        # filter off dates which failed parsing
        dates_parsed = [
            parsed_date for parsed_date in dates_parsed if parsed_date is not None
        ]

        # filter off dates which are impossible
        dates_parsed = [
            parsed_date for parsed_date in dates_parsed if parsed_date.year <= 2023
        ]

        if dates_parsed and len(dates_parsed) > 0:
            return max(dates_parsed)
        else:
            return None
