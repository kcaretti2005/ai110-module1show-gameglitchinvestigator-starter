from logic_utils import check_guess

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    
def test_large_guess_vs_small_secret():
    outcome, message = check_guess(100, 4)
    assert outcome == "Too High"
    assert "LOWER" in message