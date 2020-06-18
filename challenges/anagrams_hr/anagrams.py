"""
Given two strings, a and b, that may or may not be of the same length, determine the minimum number of character deletions required to make a and b anagrams. Any characters can be deleted from either of the strings.

ex:
a = 'cde'
b = 'dcf'
output = 2, since c and f should be deleted

each time there is a discrepency between either the character itself, or the the number of times it appears, increment counter by the difference.

after a and b are sorted and Countered: # thinking these may not be necessary, may only need sorted

loop through a:
    if i not in b:
        remove i
        counter++

loop through b:
    if i not in a:
        remove i
        counter ++

counter += abs(length(a)-length(b))

"""

from collections import Counter



def make_anagram(a, b):
    changes = 0
    
    a = Counter(a)
    b = Counter(b)

    for key in a:
        if key not in b:
            changes += 1

        elif key in b and a[key] != b[key]:
            changes += abs(a[key] - b[key])

        
    for key in b:
        if key not in a:
            changes += 1

    changes += abs(len(a) - len(b))

    return changes

make_anagram('cde', 'abc')