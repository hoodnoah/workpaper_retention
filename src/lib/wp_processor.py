# util
from dataclasses import dataclass
from datetime import date
from dateutil.relativedelta import relativedelta
from pathlib import Path

# types
from typing import Callable, Optional

# libs
from src.lib.date_extractor import get_report_date
from src.lib.client import get_client_name, get_fye

DESTRUCTION_DELTA = relativedelta(years=5)
LEAP_YEAR_DELTA = relativedelta(days=1)


@dataclass
class WorkPaper:
    ClientName: str
    FiscalYearEnd: date
    DestructionDate: date


def _is_leap_year(d: date) -> bool:
    return d.month == 2 and d.day == 29


def process_wp(
    report_path: Path,
    issue_date_fn: Callable[[Path], Optional[date]] = get_report_date,
    fye_fn: Callable[[Path], Optional[date]] = get_fye,
    name_fn: Callable[[Path], Optional[str]] = get_client_name,
) -> Optional[WorkPaper]:
    # calculate destruction date
    issue_date = issue_date_fn(report_path)
    if not issue_date:
        return None

    destruction_date: date
    if _is_leap_year(issue_date):
        destruction_date = issue_date + DESTRUCTION_DELTA + LEAP_YEAR_DELTA
    else:
        destruction_date = issue_date + DESTRUCTION_DELTA

    fye = fye_fn(report_path)
    if not fye:
        return None

    name = name_fn(report_path)
    if not name:
        return None

    return WorkPaper(
        ClientName=name, FiscalYearEnd=fye, DestructionDate=destruction_date
    )
