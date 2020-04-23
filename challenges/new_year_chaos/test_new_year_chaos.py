import pytest
from new_year_chaos import minimum_bribe

def test_exists():
    assert minimum_bribe

def test_sample_one():
    q = [2, 1, 5, 3, 4]
    expected = 3
    actual = minimum_bribe(q)
    assert expected == actual

def test_sample_chaotic():
    q = [2, 5, 1, 3, 4]
    expected = 'Too chaotic'
    actual = minimum_bribe(q)
    assert expected == actual

def sample_three_a():
    q = [5, 1, 2, 3, 7, 8, 6, 4]
    expected = 'Too chaotic'
    actual = minimum_bribe(q)
    assert expected == actual

def test_sample_three_b():
    q = [1, 2, 5, 3, 7, 8, 6, 4]
    expected = 7
    actual = minimum_bribe(q)
    assert expected == actual
