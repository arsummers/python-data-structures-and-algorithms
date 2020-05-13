import pytest
from anagrams import is_anagram

def test_exists():
    assert is_anagram

def test_yes_anagram():
    arr = ['poke', 'ekop', 'kope', 'peok']
    expected = True
    actual = is_anagram(arr)
    assert expected == actual

def test_not_anagram_simple():
    arr = ['poke', 'code', 'lace']
    expected = False
    actual = is_anagram(arr)
    assert expected == actual

def test_not_anagram_hard():
    arr = ['poke', 'pokep', 'poker']
    expected = False
    actual = is_anagram(arr)
    assert expected == actual