import pytest
from escape_room import escape_room

def test_exists():
    assert escape_room

def test_example():
    word_list = ['APPLE', 'PLEAS', 'PLEASE']
    keypads = ['AELWXYZ', 'AELPXYZ', 'AELPSXY', 'SAELPRT', 'XAEBKSY']
    expected = [0, 1, 3, 2, 0]
    actual = escape_room(word_list, keypads)
    assert expected == actual