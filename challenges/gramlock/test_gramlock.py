import pytest
from gramlock import gramlock

def test_exists():
    assert gramlock

def test_yes_1():
    s = 'abba'
    expected = 4
    actual = gramlock(s)
    assert expected == actual

def test_no_1():
    s = 'abcd'
    expected = 0
    actual = gramlock(s)
    assert expected == actual

def test_yes_2():
    s = 'ifailuhkqq'
    expected = 3
    actual = gramlock(s)
    assert expected == actual

def test_yes_3():
    s = 'bbbb'
    expected = 10
    actual = gramlock(s)
    assert expected == actual

def test_yes_4():
    s = 'cdcd'
    expected = 5
    actual = gramlock(s)
    assert expected == actual