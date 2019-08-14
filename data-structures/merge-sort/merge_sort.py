def merge_sort(lst):
    length = len(lst)
    if length > 1:

        middle = length // 2     
        left = lst[:middle]
        right = lst[middle:]

        merge_sort(left)
        merge_sort(right)
        merge(left, right, lst)
    return lst

def merge(left, right, lst):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            lst[k] = left[i]
            i += 1

        else:
            lst[k] = right[j]
            j += 1

        k += 1

# sets remaining entries in list to remaining values in right
    while i < len(left):
        lst[k] = left[i]
        i += 1
        k += 1

# sets remaining entries in list to remaining values in left
    while j < len(right):
        lst[k] = right[j]
        j += 1
        k += 1

