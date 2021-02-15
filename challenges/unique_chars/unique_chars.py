from collections import Counter

def unique_chars(string):

    if len(string) == 0:
        return True

    normalized = ''.join(string.lower().split())

    count_vals = list(Counter(normalized).values())

    if max(count_vals) > 1:
        return False

    else:
        return True


# trying again for fun. 
def unique_chars_return(string):
    normalized = ''.join(string.lower().split())
    the_set = set((normalized))

    if len(the_set) == len(normalized):
        return True

    return False