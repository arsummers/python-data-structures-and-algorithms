def reverse_in_place(arr):
    # no methods no gods no masters'
    # must be O(n) for time AND space and nothing more
    # will have to swap indices along a center axis
    # python will do a magic backend thing to make it inclusive and start at 0 index

    length = len(arr)

    if length <= 1:
        return arr

    for i in range(length//2):

        arr[i], arr[length - 1 -i ] = arr[length - 1 - i], arr[i]
     

    return arr

    #STEP THROUGH
    
# start: [1, 2, 3, 4, 5, 6]

# step 1:
#     i = 0
#     arr[i] = 1
#     #arr[6 - 1 - 0] which is arr[5]
#     arr[length - 1 - i] = 6
# steps 2 onward will continue swapping down to the middle. This will work with both even and odd sized lists.