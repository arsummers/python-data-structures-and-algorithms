import pytest
from easy import stickers_for

def test_exists():
    assert stickers_for

def test_tiara():
    phrase = 'tiara'
    actual = stickers_for(phrase)
    expected = 1

    assert expected == actual

def test_six_a():
    phrase = 'aaaaaa'
    actual = stickers_for(phrase)
    expected = 3

    assert expected == actual

def test_five_a():
    phrase = 'aaaaa'
    actual = stickers_for(phrase)
    expected = 3

    assert expected == actual

def test_taming_giant_gnats():
    phrase = 'taming giant gnats'
    actual = stickers_for(phrase)
    expected = 3

    assert expected == actual

def test_artisan_martians():
    phrase = 'artisan martians'
    actual = stickers_for(phrase)
    expected = 2

    assert expected == actual

def test_triple_instagram():
    phrase = 'instagram instagram instagram'
    actual = stickers_for(phrase)
    expected = 3

    assert expected == actual

def test_double_instagram():
    phrase = 'instagram instagram'
    actual = stickers_for(phrase)
    expected = 2

    assert expected == actual

