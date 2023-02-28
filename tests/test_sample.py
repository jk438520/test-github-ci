# Sample Test passing with nose and pytest

def test_pass():
    assert True, "dummy sample test"

def test_for_python38():
    walrus = False
    assert (walrus := True)