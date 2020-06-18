import pytest
from anagrams import make_anagram

def test_exists():
    assert make_anagram

def test_simple1():
    a = 'cde'
    b = 'dcf'
    actual = make_anagram(a, b)
    expected = 2
    assert actual == expected

def test_simple2():
    a = 'cde'
    b = 'abc'
    actual = make_anagram(a, b)
    expected = 4
    assert actual == expected

def test_anagrammed():
    a = 'tacocat'
    b = 'cattaco'
    actual = make_anagram(a, b)
    expected = 0
    assert actual == expected

def test_num_mismatch():
    a = 'aabcde'
    b = 'abbcde'
    actual = make_anagram(a, b)
    expected = 2
    assert actual == expected

def test_length_mismatch():
    a = 'aaaa'
    b = 'aaa'
    actual = make_anagram(a, b)
    expected = 1
    assert actual == expected