import pytest
from sherlock import sherlock

def test_exists():
    assert sherlock

def test_simple_yes():
    s = 'abc'
    actual = sherlock(s)
    expected = 'YES'
    assert expected == actual

def test_yes():
    s = 'abcc'
    actual = sherlock(s)
    expected = 'YES'
    assert expected == actual

def test_yes():
    s = 'abcc'
    actual = sherlock(s)
    expected = 'YES'
    assert expected == actual

def test_simple_no():
    s = 'abccc'
    actual = sherlock(s)
    expected = 'NO'
    assert expected == actual

def test_no_2():
    s = 'aabbcd'
    actual = sherlock(s)
    expected = 'NO'
    assert expected == actual

def test_no_3():
    s = 'aaabbccddeefghi'
    actual = sherlock(s)
    expected = 'NO'
    assert expected == actual