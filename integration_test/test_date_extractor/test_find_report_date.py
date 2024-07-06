# testing
import pytest

# utility
from pathlib import Path
from datetime import date

# module under test
from src.lib.date_extractor import get_report_date

TEST_EXPORTED = [
    (
        "integration_test/test_date_extractor/test_fixtures/exported/exported_1.pdf",
        date(2023, 2, 8),
    ),
    (
        "integration_test/test_date_extractor/test_fixtures/exported/exported_2.pdf",
        date(2023, 4, 13),
    ),
    (
        "integration_test/test_date_extractor/test_fixtures/exported/exported_3.pdf",
        date(2021, 9, 1),
    ),
    (
        "integration_test/test_date_extractor/test_fixtures/exported/exported_4.pdf",
        date(2023, 1, 11),
    ),
    (
        "integration_test/test_date_extractor/test_fixtures/exported/exported_5.pdf",
        date(2023, 3, 28),
    ),
]

TEST_SCANNED = [
    (
        "integration_test/test_date_extractor/test_fixtures/scanned/scanned_1.PDF",
        date(2016, 3, 22),
    ),
    (
        "integration_test/test_date_extractor/test_fixtures/scanned/scanned_2.pdf",
        date(2020, 4, 27),
    ),
    (
        "integration_test/test_date_extractor/test_fixtures/scanned/scanned_3.PDF",
        date(2015, 5, 6),
    ),
]


class TestGetReportDate:
    @pytest.mark.parametrize("input_path,expected_date", TEST_EXPORTED)
    def test_finds_correct_date_on_exported_pdf(
        self, input_path: str, expected_date: date
    ):
        # act
        pdf_date = get_report_date(input_path)

        # assert
        assert expected_date == pdf_date

    @pytest.mark.parametrize("input_path,expected_date", TEST_SCANNED)
    def test_finds_correct_date_on_scanned_pdf(
        self, input_path: str, expected_date: date
    ):
        # act
        pdf_date = get_report_date(input_path)

        # assert
        assert expected_date == pdf_date
