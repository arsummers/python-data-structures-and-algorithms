# given a list with multiple numbers that occur an even number of times and one number that occurs an odd number of times, return the number that shows up an odd number of times.
from collections import Counter

def odd_one_out(arr):
    counter = Counter()
    # loops through dictionary containing counts of all items to check their values. It returns the key of the element with an odd value.
    for num in arr:
        counter[num] += 1
        if counter[num] % 2 != 0:
            return counter[num]
        