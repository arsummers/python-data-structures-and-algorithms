import pytest
from abs_minimum import abs_minimum

def test_exists():
    assert abs_minimum

def test_simple():
    arr = [3, -7, 0]
    expected = 3
    actual = abs_minimum(arr)
    assert expected == actual

def test_mostly_negative():
    arr = [-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]
    expected = 1
    actual = abs_minimum(arr)
    assert expected == actual

def test_medium():
    arr = [1, -3, 71, 68, 17]
    expected = 3
    actual = abs_minimum(arr)
    assert expected == actual