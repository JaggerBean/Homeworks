from read_turbidity import calc_turbidity, time_till_safe
import pytest

def test_calc_turbidity():
    assert calc_turbidity(1.5,2.0) == 3.0
    assert calc_turbidity(4.6,15.0) == 69.0
    assert isinstance(calc_turbidity(1.6,23.5), float) == True

def test_calc_turbidity_exceptions():
    with pytest.raises(TypeError):
        calc_turbidity(1.3,'x')
    with pytest.raises(TypeError):
        calc_turbidity(15, {"num" : 24})




def test_time_till_safe():
    assert 23.263 < time_till_safe(1.6, .02, 1) < 23.2644
    assert 7.04 < time_till_safe(1.153, .02, 1) < 7.05
    assert 3.48 < time_till_safe(1.153, .04, 1) < 3.49
    assert isinstance(time_till_safe(1, .02, 1), float) == True 


def test_time_till_safe_exceptions():
    with pytest.raises(ValueError):
        time_till_safe(1.2134, 2.0, 1)
    with pytest.raises(TypeError):
        time_till_safe(1.5, {"num" : .024}, 1) 
