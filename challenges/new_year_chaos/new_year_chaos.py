# numbers can only move up at most 2 spaces
# if difference between numbers is >=3, print too chaotic
# works by comparing indices to values

def minimum_bribe(q):   
    min_bribes = 0
    q = [j - 1 for j in q]

    for i, j in enumerate(q):
        if j-i > 2:
            return 'Too chaotic'

        for k in range(max(j-1, 0), i):
            if q[k] > j:
                min_bribes += 1

    return min_bribes
