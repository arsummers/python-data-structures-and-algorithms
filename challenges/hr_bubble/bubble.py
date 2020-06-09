def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

arr = [6,4,1]
def count_swaps(arr):
    swaps = 0 #number of swaps that took place
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swaps += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    first_elem = arr[0]
    last_elem = arr[len(arr)-1]

    print(f'Array is sorted in {swaps} swaps.')
    print(f'First Element: {first_elem}')
    print(f'Last Element: {last_elem}')

    return swaps, first_elem, last_elem

count_swaps(arr)