import pytest

@pytest.mark.demo
def test_one():
    assert 2*6 == 12

@pytest.mark.demo
def test_two():
    assert 45-12 == 33
    
@pytest.mark.fun
def test_fun1():
    assert 8*4 == 32

@pytest.mark.fun
def test_function():
    assert "apple" == "apple"