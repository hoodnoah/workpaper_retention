# utility
from datetime import date

# module under test
from src.lib.wp_processor import process_wp, WorkPaper


class Test_wp_processor:
    def test_processes_single_fixture(self):
        # arrange
        mock_get_report_date_fn = lambda _: date(2023, 2, 8)
        mock_get_fye_fn = lambda _: date(2023, 1, 31)
        mock_get_name_fn = lambda _: "EXPORTED_1"
        expected_result = WorkPaper(
            ClientName="EXPORTED_1",
            FiscalYearEnd=date(2023, 1, 31),
            DestructionDate=date(2028, 2, 8),
        )

        # act
        result = process_wp(
            "", mock_get_report_date_fn, mock_get_fye_fn, mock_get_name_fn
        )

        # assert
        assert expected_result == result

    def test_handles_leap_years_conservatively(self):
        # arrange
        mock_get_report_date_fn = lambda _: date(2020, 2, 29)
        mock_get_fye_fn = lambda _: date(2020, 1, 31)
        mock_get_name_fn = lambda _: "SAMPLE CLIENT"
        expected_result = WorkPaper(
            ClientName="SAMPLE CLIENT",
            FiscalYearEnd=date(2020, 1, 31),
            DestructionDate=date(2025, 3, 1),
        )

        # act
        result = process_wp(
            "", mock_get_report_date_fn, mock_get_fye_fn, mock_get_name_fn
        )

        # assert
        assert result == expected_result
