def quick_sort(lst, left, right):
    if left < right:
        # sets position of pivot
        position = partition(lst, left, right)
        quick_sort(lst, left, position - 1)
        quick_sort(lst, position + 1, right)
    return lst

def partition(lst, left, right):
    pivot = lst[right]
    low = left - 1

    for i in range(left, right):
        if lst[i] <= pivot:
            low += 1
            lst[low], lst[i] = lst[i], lst[low]
    lst[low+1], lst[right] = lst[right], lst[low+1]

    return (low + 1)