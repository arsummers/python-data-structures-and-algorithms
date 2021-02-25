from reverse_array import reverse_in_place, weird_fizzbuzz

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

def test_fizz():
    n = 3
    expected = "Fizz"
    actual = weird_fizzbuzz(n)
    assert expected == actual

def test_buzz():
    n = 5
    expected = "Buzz"
    actual = weird_fizzbuzz(n)
    assert expected == actual

def test_fizzbuzz():
    n = 15
    expected = "FizzBuzz"
    actual = weird_fizzbuzz(n)
    assert expected == actual