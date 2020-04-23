import pytest
from ransom_dict import check_magazine

def test_exists():
    assert check_magazine

def test_easy_sample():
    magazine = ['give', 'me', 'one', 'grand', 'today', 'night']
    note = ['give', 'one', 'grand', 'today']
    expected = 'Yes'
    actual = check_magazine(magazine, note)
    assert expected == actual

def test_insufficient_repetition():
    magazine = ['two', 'times', 'three', 'is', 'not', 'four']
    note = ['two', 'times', 'two', 'is', 'four']
    expected = 'No'
    actual = check_magazine(magazine, note)
    assert expected == actual

def test_missing_word():
    magazine = ['ive', 'got', 'a', 'lovely', 'bunch', 'of', 'coconuts']
    note = ['ive', 'got', 'some', 'coconuts']
    expected = 'No'
    actual = check_magazine(magazine, note)
    assert expected == actual

def test_case_mismatch():
    magazine = ['Speak', 'to', 'me', 'your', 'murder', 'trial']
    note = ['speak', 'your', 'Murder', 'trial', 'to', 'Me']
    expected = 'No'
    actual = check_magazine(magazine, note)
    assert expected == actual