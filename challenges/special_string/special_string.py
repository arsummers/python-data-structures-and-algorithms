"""
A string is said to be a special string if either of two conditions is met:

All of the characters are the same, e.g. aaa.
All characters except the middle one are the same, e.g. aadaa.
A special substring is any substring of a string which meets one of those criteria. Given a string, determine how many special substrings can be formed from it.

ex:
s = 'mnonopoo'
special substrings = {m, n, o, n, o, p, o, o, non, ono, opo, oo}
12 substrings

1. append each character to subs list
2. for every letter in the s:
    - 

"""

def special_string(s):
    substrings = []
    num_strings = len(substrings)

    for letter in s:
        substrings.append(letter)

    return num_strings