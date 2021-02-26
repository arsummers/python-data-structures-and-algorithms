def addition(n):
    return n + n

def map_fun(arr):
    result = map(addition, arr)
    return list(result)

