"""Verify that functions work correctly."""

from names import make_full_name, extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    """Verify that the make_full_name function returns correct results.

    Parameters: none
    Return: nothing
    """
    assert make_full_name("Elaine", "Henson") == "Henson; Elaine"
    assert make_full_name("E", "Henson") == "Henson; E"
    assert make_full_name("", "Henson") == "Henson; "
    assert make_full_name("Elaine", "") == "; Elaine"
    assert make_full_name("", "") == "; "


def test_extract_family_name():
    """Verify that the extract_family_name function returns correct results.

    Parameters: none
    Return: nothing
    """
    assert extract_family_name("Henson; Elaine") == "Henson"
    assert extract_family_name("Henson; E") == "Henson"
    assert extract_family_name("Henson; ") == "Henson"
    assert extract_family_name("; Elaine") == ""
    assert extract_family_name("; ") == ""

def test_extract_given_name():
    """Verify that the extract_given_name function returns correct results.

    Parameters: none
    Return: nothing
    """
    assert extract_given_name("Henson; Elaine") == "Elaine"
    assert extract_given_name("H; Elaine") == "Elaine"
    assert extract_given_name("Henosn; ") == ""
    assert extract_given_name("; ") == ""
    assert extract_given_name("Henson; E") == "E"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])