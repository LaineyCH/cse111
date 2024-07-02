from address import extract_city, extract_state, extract_zipcode
import pytest


def test_extract_city():
    """
    Checks the extract_city function to ensure it functions correctly and gives the correct return.
    Parameters: none
    Return: none
    """
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
    assert extract_city("132 My Street, Kingston, NY 12401") == "Kingston"
    assert extract_city("132 My Street, New York, NY 12401") == "New York"
    assert extract_city("132 My Street, Dover-Foxcroft, ME 12401") == "Dover-Foxcroft"
    assert extract_city("525 S Center St, , ID 83460") == ""


def test_extract_state():
    """
    Checks the extract_state function to ensure it functions correctly and gives the correct return.
    Parameters: none
    Return: none
    """
    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
    assert extract_state("132 My Street, Kingston, NY 12401") == "NY"
    assert extract_state("132 My Street, New York, NY 12401") == "NY"
    assert extract_state("132 My Street, Dover-Foxcroft, ME 12401") == "ME"
    assert extract_state("525 S Center St, Rexburg, 83460") == ""


def test_extract_zipcode():
    """
    Checks the extract_zipcode function to ensure it functions correctly and gives the correct return.
    Parameters: none
    Return: none
    """
    assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"
    assert extract_zipcode("132 My Street, Kingston, NY 12401") == "12401"
    assert extract_zipcode("132 My Street, New York, NY 12401") == "12401"
    assert extract_zipcode("132 My Street, Dover-Foxcroft, ME 12401") == "12401"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])