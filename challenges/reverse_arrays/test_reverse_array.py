from reverse_array import reverse_in_place

def test_even():
    arr = [1, 2, 3, 4, 5, 6]
    expected = [6, 5, 4, 3, 2, 1]
    actual = reverse_in_place(arr)
    assert expected == actual

def test_odd():
    arr = [1, 2, 3, 4, 5]
    expected = [5, 4, 3, 2, 1]
    actual = reverse_in_place(arr)
    assert expected == actual

def test_two():
    arr = [1, 2]
    expected = [2, 1]
    actual = reverse_in_place(arr)
    assert expected == actual

def test_one():
    arr = [1]
    expected = [1]
    actual = reverse_in_place(arr)
    assert expected == actual

def test_empty():
    arr = []
    expected = []
    actual = reverse_in_place(arr)
    assert expected == actual