import pytest
from alternating_chars import alterating_chars

def test_exists():
    assert alterating_chars

def test_all_a():
    s = 'AAAA'
    expected = alterating_chars(s)
    actual = 3
    assert expected == actual

def test_all_b():
    s = 'BBBBB'
    expected = alterating_chars(s)
    actual = 4
    assert expected == actual

def test_abab():
    s = 'ABABABAB'
    expected = alterating_chars(s)
    actual = 0
    assert expected == actual

def test_all_baba():
    s = 'BABABA'
    expected = alterating_chars(s)
    actual = 0
    assert expected == actual

def test_all_aaabb():
    s = 'AAABBB'
    expected = alterating_chars(s)
    actual = 4
    assert expected == actual