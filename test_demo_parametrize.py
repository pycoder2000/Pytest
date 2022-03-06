import pytest

@pytest.mark.parametrize("input, expected",[(1,2),(3,4)])

def test_values(input,expected):
    assert input + 1 == expected