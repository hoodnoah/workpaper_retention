# testing
import pytest

# util
from pathlib import Path
from datetime import date

# module under test
from src.lib.client import get_client_name, get_fye

CLIENT_NAME_CASES = [
    (Path("Final Reports/CLIENT_1 013116 FINAL.PDF"), "CLIENT_1"),
    (Path("Final Reports/CLIENT_2 MASTER FINAL 013115.pdf"), "CLIENT_2"),
    (Path("Final Reports/CLIENT 30 Master Final 063017.pdf"), "CLIENT 30"),
    (Path("Final Reports/CLIENT #30 063014 FINAL.PDF"), "CLIENT #30"),
    (Path("Final Reports/CLIENT_5 FINAL FOR STATE 123120.pdf"), "CLIENT_5"),
    (Path("Final Reports/CLIENT_6 FINAL FOR STATE 12312021.pdf"), "CLIENT_6"),
]

CLIENT_FYE_CASES = [
    (Path("Final Reports/CLIENT_1 013116 FINAL.PDF"), date(2016, 1, 31)),
    (Path("Final Reports/CLIENT_2 MASTER FINAL 013115.pdf"), date(2015, 1, 31)),
    (Path("Final Reports/CLIENT 30 Master Final 063017.pdf"), date(2017, 6, 30)),
    (Path("Final Reports/CLIENT #30 063014 FINAL.PDF"), date(2014, 6, 30)),
    (Path("Final Reports/CLIENT_5 FINAL FOR STATE 123120.pdf"), date(2020, 12, 31)),
    (Path("Final Reports/CLIENT_6 FINAL FOR STATE 12312021.pdf"), date(2021, 12, 31)),
]


class TestClient:
    @pytest.mark.parametrize("path,expected_name", CLIENT_NAME_CASES)
    def test_name(self, path: Path, expected_name: str):
        # act
        result = get_client_name(path)

        # assert
        assert expected_name == result

    @pytest.mark.parametrize("path,expected_date", CLIENT_FYE_CASES)
    def test_fye(self, path: Path, expected_date: date):
        # act
        result = get_fye(path)

        # assert
        assert expected_date == result
