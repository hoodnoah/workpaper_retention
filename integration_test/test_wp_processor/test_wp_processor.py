# testing
import pytest

# utility
from pathlib import Path
from datetime import date

# module under test
from src.lib.wp_processor import process_wp, WorkPaper

TEST_EXPORTED = [
    (
        Path("integration_test/test_fixtures/exported/exported_1 013123.pdf"),
        WorkPaper(
            ClientName="EXPORTED_1",
            FiscalYearEnd=date(2023, 1, 31),
            DestructionDate=date(2028, 2, 8),
        ),
    ),
    (
        Path("integration_test/test_fixtures/exported/exported_2 123122.pdf"),
        WorkPaper(
            ClientName="EXPORTED_2",
            FiscalYearEnd=date(2022, 12, 31),
            DestructionDate=date(2028, 4, 13),
        ),
    ),
    (
        Path("integration_test/test_fixtures/exported/exported_3 063021.pdf"),
        WorkPaper(
            ClientName="EXPORTED_3",
            FiscalYearEnd=date(2021, 6, 30),
            DestructionDate=date(2026, 9, 1),
        ),
    ),
    (
        Path("integration_test/test_fixtures/exported/exported_4 123122.pdf"),
        WorkPaper(
            ClientName="EXPORTED_4",
            FiscalYearEnd=date(2022, 12, 31),
            DestructionDate=date(2028, 1, 11),
        ),
    ),
    (
        Path("integration_test/test_fixtures/exported/exported_5 123122.pdf"),
        WorkPaper(
            ClientName="EXPORTED_5",
            FiscalYearEnd=date(2022, 12, 31),
            DestructionDate=date(2028, 3, 28),
        ),
    ),
]

TEST_SCANNED = [
    (
        Path("integration_test/test_fixtures/scanned/scanned_1 022916.PDF"),
        WorkPaper(
            ClientName="SCANNED_1",
            FiscalYearEnd=date(2016, 2, 29),
            DestructionDate=date(2021, 3, 22),
        ),
    ),
    (
        Path("integration_test/test_fixtures/scanned/scanned_2 022920.pdf"),
        WorkPaper(
            ClientName="SCANNED_2",
            FiscalYearEnd=date(2020, 2, 29),
            DestructionDate=date(2025, 4, 27),
        ),
    ),
    (
        Path("integration_test/test_fixtures/scanned/scanned_3 123112.PDF"),
        WorkPaper(
            ClientName="SCANNED_3",
            FiscalYearEnd=date(2012, 12, 31),
            DestructionDate=date(2020, 5, 6),
        ),
    ),
    (
        Path("integration_test/test_fixtures/scanned/scanned_4 063019.PDF"),
        WorkPaper(
            ClientName="SCANNED_4",
            FiscalYearEnd=date(2019, 6, 30),
            DestructionDate=date(2024, 8, 7),
        ),
    ),
    (
        Path("integration_test/test_fixtures/scanned/scanned_5 123120.pdf"),
        WorkPaper(
            ClientName="SCANNED_5",
            FiscalYearEnd=date(2020, 12, 31),
            DestructionDate=date(2026, 5, 6),
        ),
    ),
    (
        Path("integration_test/test_fixtures/scanned/scanned_6 063020.pdf"),
        WorkPaper(
            ClientName="SCANNED_6",
            FiscalYearEnd=date(2020, 6, 30),
            DestructionDate=date(2026, 1, 7),
        ),
    ),
    (
        Path("integration_test/test_fixtures/scanned/scanned_7 06302015.PDF"),
        WorkPaper(
            ClientName="SCANNED_7",
            FiscalYearEnd=date(2015, 6, 30),
            DestructionDate=date(2021, 2, 22),
        ),
    ),
    (
        Path("integration_test/test_fixtures/scanned/scanned_8 063020.pdf"),
        WorkPaper(
            ClientName="SCANNED_8",
            FiscalYearEnd=date(2020, 6, 30),
            DestructionDate=date(2025, 12, 18),
        ),
    ),
    (
        Path("integration_test/test_fixtures/scanned/scanned_9 123115.PDF"),
        WorkPaper(
            ClientName="SCANNED_9",
            FiscalYearEnd=date(2015, 12, 31),
            DestructionDate=date(2021, 3, 22),
        ),
    ),
    (
        Path("integration_test/test_fixtures/scanned/scanned_10 12312016.PDF"),
        WorkPaper(
            ClientName="SCANNED_10",
            FiscalYearEnd=date(2016, 12, 31),
            DestructionDate=date(2022, 3, 16),
        ),
    ),
]


class TestGetReportDate:
    @pytest.mark.parametrize("input_path,expected_result", TEST_EXPORTED)
    def test_finds_correct_date_on_exported_pdf(
        self, input_path: Path, expected_result: WorkPaper
    ):
        # act
        result = process_wp(input_path)

        # assert
        assert expected_result == result

    @pytest.mark.parametrize("input_path,expected_result", TEST_SCANNED)
    def test_finds_correct_date_on_scanned_pdf(
        self, input_path: Path, expected_result: WorkPaper
    ):
        # act
        result = process_wp(input_path)

        # assert
        assert expected_result == result
