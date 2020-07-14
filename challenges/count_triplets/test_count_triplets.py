import pytest
from count_triplets import count_triplets

def test_exists():
    assert count_triplets

def test_two():
    arr = [1, 2, 2, 4]
    r = 2
    expected = 2
    actual = count_triplets(arr, r)
    assert expected == actual
    #2 triplets at [0, 1, 3], [0 2, 3]

def test_three():
    arr = [1, 3, 9, 9, 27, 81]
    r = 3
    expected = 6
    actual = count_triplets(arr, r)
    assert expected == actual

def test_five():
    arr = [1, 5, 5, 25, 125]
    r = 5
    expected = 4
    actual = count_triplets(arr, r)
    assert expected == actual