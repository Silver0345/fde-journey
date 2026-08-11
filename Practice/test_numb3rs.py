from numb3rs import validate

def test_valide():
    assert validate("1.2.3.0") is True
    assert validate("255.2.3.255") is True
    
def test_invalid():
    assert validate("1.2.3.999") is False
    assert validate("275.2.3.10") is False
    assert validate("1.2.3.4.5") is False
    assert validate("1.2.3") is False
    assert validate("1.2.3.abc") is False
    assert validate("hello word!") is False