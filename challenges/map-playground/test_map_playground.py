from map_playground import map_fun

def test_one_list():
    arr = [1, 2, 3, 4, 5]
    expected = [2, 4, 6, 8, 10]
    actual = map_fun(arr)
    assert expected == actual

