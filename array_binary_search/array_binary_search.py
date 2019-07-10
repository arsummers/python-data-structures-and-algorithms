def binary_search(lst, search_key):
    
    left_end = 0
    right_end = len(lst) - 1

    for item in lst:
        if left_end <= right_end:

            mid = (left_end + right_end)// 2

            if lst[mid] < search_key:
                left_end = mid + 1

            elif lst[mid] > search_key:
                right_end = mid - 1

            else:
                return mid
        else:
             return -1