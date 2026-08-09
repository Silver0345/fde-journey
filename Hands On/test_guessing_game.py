import pytest
from guessing_game import choose_difficulty, get_valid_range, guess_number, check_guess

def test_choose_difficulty():
    assert choose_difficulty("1-50") == (1, 50)
    assert choose_difficulty("50-1") == (50, 1)
    assert choose_difficulty("10-20") == (10, 20)
    assert choose_difficulty("20-10") == (20, 10)
   
def test_crash():
    with pytest.raises(ValueError):
        choose_difficulty("abc")
    

    
def test_check_guess():
    assert check_guess(11, 37) == "Too Low"
    assert check_guess(51, 23) == "Too High"
    assert check_guess(7,7) == "Correct"
    