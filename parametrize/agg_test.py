import pytest
import agg

@pytest.mark.skip("This is a sample skipped test")
def test_add():
    assert agg.add(3,4) == 7

@pytest.mark.xfail
def test_subtract():
    assert agg.subtract(3,4) == -1

@pytest.mark.xfail
def test_multiply():
    assert agg.multiply(3,4) == 15

check = 0
@pytest.mark.skipif(check < 1,reason = "Skipped because check < 1")
def test_divide():
    assert agg.divide(3,4) == 0.75