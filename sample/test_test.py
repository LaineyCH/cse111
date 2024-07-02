from test import pressure_loss_from_fittings, pressure_loss_from_fittings2

from pytest import approx
import pytest

def test_pressure_lost_from_fittings():
    """tests to make sure pressure_lost_from_fittings works.
    takes no perameters, returns no perameters"""
    assert pressure_loss_from_fittings(fluid_velocity=0.00, quantity_fittings=3) == approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(fluid_velocity=1.65, quantity_fittings=0) == approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(fluid_velocity=1.65, quantity_fittings=2) == approx(-0.109, abs=0.001)
    assert pressure_loss_from_fittings(fluid_velocity=1.75, quantity_fittings=2) == approx(-0.122, abs=0.001)
    assert pressure_loss_from_fittings(fluid_velocity=1.75, quantity_fittings=5) == approx(-0.306, abs=0.001)


def test_pressure_loss_from_fittings2():
    """Verify that the pressure_loss_from_fittings function returns correct results.

    Parameters: none
    Return: nothing
    """
    # Use approx with absolute tolerance
    assert pressure_loss_from_fittings(0.00, 3) == approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 0) == approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 2) == approx(-0.109, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 2) == approx(-0.122, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 5) == approx(-0.306, abs=0.001)


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])