import pytest
from common_child import commonChild

def test_exists():
    assert commonChild

def test_harry():
    s1 = 'HARRY'
    s2 = 'SALLY'
    expected = 2
    actual = commonChild(s1, s2)
    assert expected == actual
    # AY

def test_none():
    s1 = 'AA'
    s2 = 'BB'
    expected = 0
    actual = commonChild(s1, s2)
    assert expected == actual

def test_shinchan():
    s1 = 'SHINCHAN'
    s2 = 'NOHARAAA'
    expected = 3
    actual = commonChild(s1, s2)
    assert expected == actual
    # NHA

def test_abcdf():
    s1 = 'ABCDEF'
    s2 = 'FBDAMN'
    expected = 2
    actual = commonChild(s1, s2)
    assert expected == actual
    # BD