""""""

from names import make_full_name, extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    """
    Checks the make_full_name function to ensure it functions correctly and gives the correct return.
    Parameters: none
    Return: none
    """
    assert make_full_name("Elaine", "Henson") == "Henson; Elaine"
    assert make_full_name("", "Henson") == "Henson; "
    assert make_full_name("Elaine", "") == "; Elaine"
    assert make_full_name("E", "Henson") == "Henson; E"
    assert make_full_name("Elaine", "Henson-Smith") == "Henson-Smith; Elaine"
    assert make_full_name("Elaine Cassandra", "Henson") == "Henson; Elaine Cassandra"


def test_extract_family_name():
    """
    Checks the extract_family_name function to ensure it functions correctly and gives the correct return.
    Parameters: none
    Return: none
    """
    assert extract_family_name("Henson; Elaine") == "Henson"
    assert extract_family_name("Henson; ") == "Henson"
    assert extract_family_name("; Elaine") == ""
    assert extract_family_name("Henson; E") == "Henson"
    assert extract_family_name("Henson-Smith; Elaine") == "Henson-Smith"
    assert extract_family_name("Henson; Elaine Cassandra") == "Henson"

def test_extract_given_name():
    """
    Checks the extract_given_name function to ensure it functions correctly and gives the correct return.
    Parameters: none
    Return: none
    """
    assert extract_given_name("Henson; Elaine") == "Elaine"
    assert extract_given_name("Henson; ") == ""
    assert extract_given_name("; Elaine") == "Elaine"
    assert extract_given_name("Henson; E") == "E"
    assert extract_given_name("Henson-Smith; Elaine") == "Elaine"
    assert extract_given_name("Henson; Elaine Cassandra") == "Elaine Cassandra"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])