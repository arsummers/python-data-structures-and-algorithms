import pytest
from odd_one_out import odd_one_out

def test_exists():
    assert odd_one_out

def test_single():
    expected = 5
    actual = odd_one_out([3, 3, 2, 2, 5, 4, 4, 4, 4])
    assert expected == actual

def test_triple():
    expected = 2
    actual = odd_one_out([33, 33, 2, 2, 2, 4, 4, 4, 4, 5, 5, 5, 5])
    assert expected == actual
