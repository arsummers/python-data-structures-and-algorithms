import pytest
from two_d_arr import hourglass_sum

def test_exists():
    assert hourglass_sum

def test_sample_simple():
    arr = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]

    expected = 7
    actual = hourglass_sum(arr)
    assert expected == actual

def test_sample_negatives():
    arr = [
        [-9, -9, -9, 1, 1, 1],
        [0, -9, 0, 4, 3, 2],
        [-9, -9, -9, 1, 2, 3],
        [0, 0, 8, 6, 6, 0],
        [0, 0, 0, -2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]

    expected = 28
    actual = hourglass_sum(arr)
    assert expected == actual

def test_sample_three():
    arr = [
        [1 1 1 0 0 0],
        [0 1 0 0 0 0],
        [1 1 1 0 0 0],
        [0 0 2 4 4 0],
        [0 0 0 2 0 0],
        [0 0 1 2 4 0]
    ]

    expected = 19
    actual = hourglass_sum(arr)
    assert expected == actual