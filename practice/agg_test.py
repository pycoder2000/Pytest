import pytest
import agg

def test_add():
    assert agg.add(3,4) == 7

def test_subtract():
    assert agg.subtract(3,4) == -1

def test_multiply():
    assert agg.multiply(3,4) == 12

def test_divide():
    assert agg.divide(3,4) == 0.75