from quilt_yardage import compute_yardage, read_csv
import pytest
from pytest import approx
from unittest.mock import mock_open, patch

def test_compute_yardage():
    """Verify that the compute_yardage function returns correct results.
    Parameters: none
    Return: nothing
    """
    yardage_list, yardage = compute_yardage(6, 100, 2, [0.55, 0.55])
    assert len(yardage_list) == 2
    assert yardage_list[0] == approx(45.00, abs=0.01)
    assert yardage_list[1] == approx(45.00, abs=0.01)
    assert yardage == approx(90.00, abs=0.01)

    yardage_list, yardage = compute_yardage(10, 36, 5, [0.1,0.39,0.39,0.41,0.41])
    assert len(yardage_list) == 5
    assert yardage_list[0] == approx(8.18, abs=0.01)
    assert yardage_list[1] == approx(31.91, abs=0.01)
    assert yardage_list[2] == approx(31.91, abs=0.01)
    assert yardage_list[3] == approx(33.55, abs=0.01)
    assert yardage_list[4] == approx(33.55, abs=0.01)
    assert yardage == approx(139.10, abs=0.01)


def test_read_csv():
    # create mock csv file (""" required, and the second and third lines may not have any indent)
    mock_csv = """Block Name,Image File Name,Number of Colours,List of proportion of each colour (relative to block area)
Log Cabin,log_cabin.png,5,0.1,0.39,0.39,0.41,0.41
Pinwheel,pinwheel.png,2,0.55,0.55"""

    # the patch function is used to replace the built-in open function with mock_open
    # when the read_csv function tries to open a file, it will read from mock_csv_content instead
    with patch("builtins.open", mock_open(read_data=mock_csv)):
        result = read_csv("mock_file.csv")

    # create expected output from the mock_csv file
    expected = {
        "Log Cabin": ["log_cabin.png", 5, ["0.1", "0.39", "0.39", "0.41", "0.41"]],
        "Pinwheel": ["pinwheel.png", 2, ["0.55", "0.55"]]
    }
    assert result == expected


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])


"""
from quilt_yardage import validate_int_entry, lbl_error
from unittest.mock import Mock
def test_validate_int_entry():"""
"""Verify that the validate_int_entry function returns correct results.
Parameters: none
Return: nothing
"""
"""
# create Mock of lbl_error
lbl_error.config = Mock()
# create Mock of entry lable, with get value of 10
mock_entry = Mock()
mock_entry.get.return_value = '10'

assert validate_int_entry(mock_entry, 1, 20, True) == True
assert validate_int_entry(mock_entry, 1, 20, False) == False
assert validate_int_entry(mock_entry, 1, 20, True) == False
"""