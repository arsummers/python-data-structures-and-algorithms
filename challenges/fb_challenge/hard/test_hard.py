import pytest
from hard import anagram

def test_exists():
    assert anagram

def test_simple():
    text = ['poke', 'ekop', 'kope', 'peok']
    expected = ['poke']
    actual = anagram(text)
    assert expected == actual

def test_medium():
    text = ['code', 'doce', 'frame', 'edoc', 'framer']
    expected = ['code', 'frame', 'framer']
    actual = anagram(text)
    assert expected == actual

def test_harder():
    text = ['duck', 'alice', 'ckud', 'ecila']
    expected = ['alice', 'duck']
    actual = anagram(text)
    assert expected == actual