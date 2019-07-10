from array_binary_search import binary_search

def test_function_exists():
    assert binary_search

def test_even_array_key_exists():
    expected = 2
    actual = binary_search([4,8,15,16,23,42], 15)
    assert expected == actual