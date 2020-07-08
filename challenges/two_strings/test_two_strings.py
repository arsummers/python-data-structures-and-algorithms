import pytest
from two_strings import two_strings

def test_exists():
    assert two_strings

def test_yes():
    s1 = 'hello'
    s2 = 'hi'
    assert two_strings(s1, s2) == 'YES'

def test_no():
    s1 = 'help'
    s2 = 'no'
    assert two_strings(s1, s2) == 'NO'
