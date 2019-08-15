import pytest
from quick_sort import quick_sort

def test_exists():
    assert quick_sort

def test_sort_empty_list():
    lst = []
    left = []
    right = []
    assert quick_sort(lst, left, right) == []

def test_list_of_one():
    lst = [3]
    left = 3
    right = 3
    assert quick_sort(lst, left, right) == [3]


def test_presorted_list():
    lst = [1, 2, 3, 4, 5, 6, 7]
    n = len(lst)
    assert quick_sort(lst, 0, n-1) == [1, 2, 3, 4, 5, 6, 7]


def test_backwards_list():
    lst = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5]
    n = len(lst)
    assert quick_sort(lst, 0, n-1) == [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def test_repeating_list():
    lst = [1, 1, 1, 1, 1, 1]
    n = len(lst)
    assert quick_sort(lst, 0, n-1) == [1, 1, 1, 1, 1, 1]

def test_random_list():
    lst = [5, 1, 9, 3, 8, 4, 2, 6, 7, 10]
    n = len(lst)
    assert quick_sort(lst, 0, n-1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_duplicates():
    lst = [2, 1, 2, 4, 5, 5, 6, 7, 5, 1, 2]
    n = len(lst)
    assert quick_sort(lst, 0, n-1) == [1, 1, 2, 2, 2, 4, 5, 5, 5, 6, 7]
