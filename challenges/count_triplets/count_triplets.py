"""
You are given an array and you need to find number of tripets of indices (i, j, k) such that the elements at those indices are in geometric progression for a given common ratio r and i < j < k

a geometric sequence is a sequence of numbers where each term after the first is found by multiplying the previous one by a fixed, non-zero number called the common ratio

example:

arr = [1, 4, 16, 64]
r = 4

triplets = [1, 4, 16] and [4, 16, 24]

return the number of triplets

"""
from collections import Counter

def count_triplets(arr, r):
    arr_count = Counter(arr)
    holder = Counter()
    triplets_count = 0
    
    for i in arr:
        j = i // r
        k = i * r
        arr_count[i] -= 1
        if holder[j] and arr_count[k] and not i%r:
            triplets_count += holder[j]*arr_count[k]
        holder[i] += 1
    return triplets_count
