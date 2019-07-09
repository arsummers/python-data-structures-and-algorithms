from array_shift import insert_shift_array

def test_function_exists():
    assert insert_shift_array

def test_insert_into_middle_even_small():
    expected = [1, 7, 3]
    actual = insert_shift_array([1, 3], 7)
    assert expected == actual

def test_insert_into_middle_even_large():
    expected = [1, 2, 3, 7, 4, 5, 6]
    actual = insert_shift_array([1,2,3,4,5,6], 7)
    assert expected == actual

def test_insert_into_middle_odd():
    expected = [1, 2, 3, 7, 4, 5]
    actual = insert_shift_array([1, 2, 3, 4, 5], 7)
    assert expected == actual

def test_expected_failure_length_issue():
    expected = 'This array does not have a midpoint'
    actual = insert_shift_array([1], 7)
    assert expected == actual