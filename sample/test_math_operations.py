import pytest
from math_operations import power_calc
from pytest import approx
 
def test_power_calc():
    assert power_calc(4, 6, 3) == approx(8)
 

pytest.main(["-v", "--tb=line", "-rN", __file__])