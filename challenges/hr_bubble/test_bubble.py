import pytest
from bubble import count_swaps, bubble_sort
prob_dom = """

Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following three lines:

Array is sorted in numSwaps swaps., where numSwaps is the number of swaps that took place.
First Element: firstElement, where firstElement is the first element in the sorted array.
Last Element: lastElement, where lastElement is the last element in the sorted array.


Hint: To complete this challenge, you must add a variable that keeps a running tally of all swaps that occur during execution

"""

# honestly not sure how to test for multiple returns
def test_bubble_sort():
    arr = [5, 7, 3, 4, 6, 2, 8, 1, 9]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    actual = bubble_sort(arr)
    assert expected == actual

