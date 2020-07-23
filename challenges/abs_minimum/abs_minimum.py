"""
Given an array of integers, find and print the minimum absolute difference between any two elements in the array. 

in: arr = [-2, 2, 4]
out: 2

algorithm:
get all possible pairs using itertools
from each pair 
have base minimum set to the value of the first pair's difference
iterate over each pair
update minimum if the new value is smaller than the current one

"""
from itertools import combinations

def abs_minimum(arr):
    # pairs = list(combinations(arr, 2))
    # starter = pairs[0]
    # minimum = abs(starter[0] - starter[1])

    # for i in pairs:
    #     current = abs(i[0] - i[1])
    #     if current < minimum:
    #         minimum = current

    # return minimum
    arr.sort()

    return min([abs(arr[i + 1] - arr[i]) for i in range(len(arr)-1)])

