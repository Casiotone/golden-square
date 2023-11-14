from lib.check_codeword import *

def test_check_codeword_is_horse():
    expected_result = "Correct! Come in."
    actual_result = check_codeword('horse')
    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
