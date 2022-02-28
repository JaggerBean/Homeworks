
from ml_data_analysis import compute_average_mass
from ml_data_analysis import check_hemisphere
from ml_data_analysis import count_classes
import pytest

def test_compute_average_mass():
    
    assert compute_average_mass([{'a': 1}, {'a': 2}, {'a': 6}], 'a') == 3
    assert compute_average_mass([{'a': 10}, {'a': 1}, {'a': 190}], 'a') == 67
    
    assert isinstance(compute_average_mass([{'a': 1}, {'a': 1}], 'a'), float) == True


def test_compute_average_mass_exceptions():
    
    with pytest.raises(KeyError):
        compute_average_mass([{'a': 1}, {'a': 2}], 'b')
    with pytest.raises(KeyError):
        compute_average_mass([{'a': 1}, {'b': 1}], 'a')
    with pytest.raises(ValueError):
        compute_average_mass([{'a': 1}, {'a': 'b'}], 'a')
    with pytest.raises(ZeroDivisionError):
        compute_average_mass([], 'a')                                


def test_check_hemisphere():
    
    assert check_hemisphere(1,1) == 'Northern & Eastern'
    assert check_hemisphere(1,-1) == 'Northern & Western'
    assert check_hemisphere(-1,1) == 'Southern & Eastern'
    assert check_hemisphere(-1,-1) == 'Southern & Western'
    assert isinstance(check_hemisphere(1,-1), str) == True

def test_check_hemisphere_exceptions():
    
    with pytest.raises(ValueError):
        check_hemisphere(0, 1)
        
def test_count_classes():
    assert count_classes([],'') == {}
    assert count_classes([{'a': 'class1'}], 'a') == {'class1': 1}
    assert count_classes([{'a': 'class1'}, {'a': 'class1'}, {'a': 'class1'}], 'a') == {'class1': 3} 

def test_count_classes_exceptions():
    with pytest.raises(KeyError):
        count_classes([{'a': 'class1'}, {'b': 'class1'}], 'b')
    with pytest.raises(KeyError):
        compute_average_mass([{'a': 'class1'}, {'a': 'class2'}], 'b')
