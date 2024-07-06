from pathlib import Path
import re

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
