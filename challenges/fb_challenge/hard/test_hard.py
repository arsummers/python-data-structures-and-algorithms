import pytest
from hard import anagram, anagram_oneliner

def test_exists():
    assert anagram
    assert anagram_oneliner

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

def test_base_case():
    text = ['code', 'doce', 'frame', 'edoc', 'framer', 'famer']
    expected = ['code', 'frame', 'framer']
    actual = anagram(text)
    assert expected == actual

def test_single():
    text = ['python']
    expected = ['python']
    actual = anagram(text)
    assert expected == actual

# TESTS FOR ONELINER

def test_simple_one():
    text = ['poke', 'ekop', 'kope', 'peok']
    expected = ['poke']
    actual = anagram_oneliner(text)
    assert expected == actual

def test_medium_one():
    text = ['code', 'doce', 'frame', 'edoc', 'framer']
    expected = ['code', 'frame', 'framer']
    actual = anagram_oneliner(text)
    assert expected == actual

def test_harder_one():
    text = ['duck', 'alice', 'ckud', 'ecila']
    expected = ['alice', 'duck']
    actual = anagram_oneliner(text)
    assert expected == actual

def test_base_case_one():
    text = ['code', 'doce', 'frame', 'edoc', 'framer', 'famer']
    expected = ['code', 'frame', 'framer']
    actual = anagram_oneliner(text)
    assert expected == actual

def test_single_one():
    text = ['python']
    expected = ['python']
    actual = anagram_oneliner(text)
    assert expected == actual
