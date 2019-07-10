from array_binary_search import binary_search

def test_function_exists():
    assert binary_search

def test_even_array_key_exists():
    expected = 2
    actual = binary_search([4,8,15,16,23,42], 15)
    assert expected == actual

def test_even_array_key_not_exists():
    expected = -1
    actual = binary_search([11,22,33,44,55,66], 90)
    assert expected == actual

def test_odd_array_key_exists():
    expected = 4
    actual = binary_search([8,15,16,23,42], 23)
    assert expected == actual

def test_odd_array_key_not_exists():
    expected = -1
    actual = binary_search([11,22,33,44,55,66, 80], 90)
    assert expected == actual

def test_large_array():
    expected = 5
    actual = binary_search([5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99], 15)
    assert expected == actual

def test_small_array():
    expected = 1
    actual = binary_search([3, 13], 13)
    assert expected == actual

def test_array_of_minus_1():
    expected = 0
    actual = binary_search([-1], -1)
    assert expected == actual