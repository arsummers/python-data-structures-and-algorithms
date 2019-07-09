def insert_shift_array(lst, val):
    midpoint = len(lst) // 2
    
    if len(lst) % 2 == 0:
        # I'm trying to get it to not change the midpoint here. Not sure if I would just be able to leave this if statement blank or not
        midpoint = midpoint
    # This section varies slightly from my whiteboarding solution because I while I was whiteboarding I didn't factor in for a list that was too short to have a midpoint.
    elif len(lst) % 2 != 0:
        midpoint += 1
    
    first_half = lst[:midpoint:]
    second_half = lst[midpoint::]

    first_half.append(val)
    return first_half + second_half