from pathlib import Path
import re
from datetime import datetime, date

# types
from typing import Optional

DATE_REGEX = re.compile(r"\d{6,8}")
CHAFF_REGEX = re.compile(r"\b(final|report|master|audit|for|state)\b")
MULTI_SPACE_REGEX = re.compile(r"\s{2}")


def get_client_name(filepath: Path) -> Optional[str]:
    client_name = filepath.stem.lower()

    # filter off dates
    client_name = re.sub(DATE_REGEX, "", client_name)

    # get rid of words like "audit," "report," "final," etc.
    client_name, _ = re.subn(CHAFF_REGEX, "", client_name)

    # remove double spaces
    client_name, _ = re.subn(MULTI_SPACE_REGEX, " ", client_name)

    # remove leading, trailing spaces
    client_name = client_name.strip()

    return client_name.upper()


def get_fye(path: Path) -> Optional[date]:
    match_result = re.search(DATE_REGEX, path.stem)

    if not match_result:
        return None

    date_str = match_result.group()

    if len(date_str) == 6:
        date = datetime.strptime(date_str, "%m%d%y").date()
        return date
    else:
        date = datetime.strptime(date_str, "%m%d%Y").date()
        return date
