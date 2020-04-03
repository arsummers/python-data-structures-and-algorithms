# given a list with multiple numbers that occur an even number of times and one number that occurs an odd number of times, return the number that shows up an odd number of times.
from collections import Counter

def odd_one_out(arr):
    # loops through dictionary containing counts of all items to check their values. It returns the key of the element with an odd value.
    
    counter = dict((i, arr.count(i)) for i in arr)
    return counter