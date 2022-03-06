import pytest

@pytest.fixture
def in_value():
    i =20
    return i

def test_sum_1(in_value):
    assert in_value + 12 == 32

def test_sum_2(in_value):
    assert in_value + 20 == 40