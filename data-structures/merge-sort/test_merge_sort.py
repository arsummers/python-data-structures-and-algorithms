import pytest
from merge_sort import merge_sort

def test_exists():
    assert merge_sort

def test_sort_empty_list():
    lst = []
    assert merge_sort(lst) == []

def test_list_of_one():
    lst = [3]
    assert merge_sort(lst) == [3]


def test_presorted_list():
    lst = [1, 2, 3, 4, 5, 6, 7]
    assert merge_sort(lst) == [1, 2, 3, 4, 5, 6, 7]

def test_backwards_list():
    lst = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5]
    assert merge_sort(lst) == [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def test_repeating_list():
    lst = [1, 1, 1, 1, 1, 1]
    assert merge_sort(lst) == [1, 1, 1, 1, 1, 1]

def test_random_list():
    lst = [5, 1, 9, 3, 8, 4, 2, 6, 7, 10]
    assert merge_sort(lst) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_duplicates():
    lst = [2, 1, 2, 4, 5, 5, 6, 7, 5, 1, 2]
    assert merge_sort(lst) == [1, 1, 2, 2, 2, 4, 5, 5, 5, 6, 7]
