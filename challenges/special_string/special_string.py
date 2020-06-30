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
    - if s is longer than 2:
        - if letter[i] == letter[i+1]
            - append, repeat for each time it repeats -> recursion?
        - if letter[i] == letter[i+2]
            - append substring
    - if s is 2 or shorter:
        - if letter[0] == letter[1]:
            - append the whole thing
    - if s is 1:
        - just append the letter
"""

def special_string(s):
    substrings = []

    current = s[0]

    if len(s) == 1:
        return len(s)
    if len(s) == 2:
        substrings.append(s[0])
        substrings.append(s[1])
        if s[0] == s[1]:
            substrings.append(s)
        return len(substrings)

    for letter in range(len(s)-2):
        substrings.append(letter)

    return num_strings