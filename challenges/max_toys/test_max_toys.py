import pytest
from max_toys import max_toys

def test_exists():
    assert max_toys

def test_simple_sorted():
    prices = [1, 2, 3, 4]
    k = 7
    expected = 3 #the number of toys he can buy
    actual = max_toys(prices, k)
    assert expected == actual

def test_simple_unsorted():
    prices = [2, 4, 3, 1]
    k = 7
    expected = 3
    actual = max_toys(prices, k)
    assert expected == actual

def test_bigger_unsorted():
    prices = [1, 12, 5, 111, 200, 1000, 10]
    k = 50
    expected = 4
    actual = max_toys(prices, k)
    assert expected == actual

def test_too_poor():
    prices = [12, 111, 200, 1000]
    k = 10
    expected = 0
    actual = max_toys(prices, k)
    assert expected == actual