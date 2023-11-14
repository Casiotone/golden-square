from lib.report_length import *

def test_report_length_is_ten():
    expected_result = "This string was 10 characters long."
    actual_result = report_length('1234567890')
    assert actual_result == expected_result
