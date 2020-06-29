import pytest
from special_string import special_string

def test_exists():
    assert special_string

def test_simple1():
    s = 'asasd'
    expected = 7
    actual = special_string(s)
    assert expected == actual

def test_simple2():
    s = 'abcbaba'
    expected = 10
    actual = special_string(s)
    assert expected == actual

def test_edge1():
    s = 'aaaa'
    expected = 10
    actual = special_string(s)
    assert expected == actual

def test_edge_short1():
    s = 'bb'
    expected = 3
    actual = special_string(s)
    assert expected == actual

def test_edge_short2():
    s = 'ab'
    expected = 2
    actual = special_string(s)
    assert expected == actual
