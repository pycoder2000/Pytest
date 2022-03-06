import pytest

def test_three():
    assert 2+6 == 8

def test_four():
    assert 45/5 == 9

@pytest.mark.fun
def test_fun1():
    assert 8*4 == 32

@pytest.mark.fun
def test_function():
    assert "apple" == "apple"