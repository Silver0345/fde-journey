from fuel import guage, convert
import pytest


def test_convert():
    assert convert("3/4") == (3, 4)
    assert convert("2/4") == (2, 4)
    
def test_faults():
    with pytest.raises(ValueError):
        convert("7/5")
    with pytest.raises(ZeroDivisionError):
        convert("5/0")
    with pytest.raises(ValueError):
        convert("abc")
        
        
def test_guage():
    assert guage(1, 100) == "E"
    assert guage(99, 100) == "F"
    assert guage(1,4) == "25%"