import pytest

@pytest.mark.demo
def test_one():
    assert 2*6 == 12

@pytest.mark.demo
def test_two():
    assert 45-12 == 33