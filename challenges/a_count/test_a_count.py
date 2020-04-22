import pytest
from a_count import a_count

def test_short_cut():
    n = 3
    s = 'ba'
    expected = 1
    actual = a_count(s, n)
    assert expected == actual

def test_aba():
    n = 10
    s = 'aba'
    expected = 7
    actual = a_count(s, n)
    assert expected == actual

def test_only_a():
    n = 5
    s = 'a'
    expected = 5
    actual = a_count(s, n)
    assert expected == actual

def test_no_a_in_string():
    n = 3
    s = 'bcd'
    expected = 0
    actual = a_count(s, n)
    assert expected == actual

def test_no_a_in_slice():
    n = 4
    s = 'bdcgha'
    expected = 0
    actual = a_count(s, n)
    assert expected == actual