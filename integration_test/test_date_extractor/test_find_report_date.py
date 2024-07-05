from pathlib import Path
from datetime import date

# module under test
from src.lib.date_extractor import get_report_date


class TestGetReportDate:
    def test_finds_correct_date_on_exported_pdf(self):
        # arrange
        pdf_path = Path(
            "/integration_test/test_date_extractor/test_fixtures/test_exported_report_1.pdf"
        )
        expected_date = date(2023, 2, 8)

        # act
        pdf_date = get_report_date(pdf_path)
        assert expected_date == pdf_date

    def test_finds_correct_date_on_exported_pdf_2(self):
        # arrange
        pdf_path = Path(
            "integration_test/test_date_extractor/test_fixtures/test_exported_report_2.pdf"
        )
        expected_date = date(2023, 4, 13)

        # act
        pdf_date = get_report_date(pdf_path)
        assert expected_date == pdf_date
