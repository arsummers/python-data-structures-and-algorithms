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