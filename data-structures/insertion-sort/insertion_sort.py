def insertion_sort(lst):
    for i in range(len(lst)):
        j = (i - 1)
        temp = lst[i]

        while j >= 0 and temp < lst[j]:
            lst[j+1] = lst[j]
            j = j-1

        lst[j + 1] = temp
    return lst
    