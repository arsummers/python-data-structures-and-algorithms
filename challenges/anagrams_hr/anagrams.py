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
    
    a = list(a)
    b = list(b)

    for i in a:
        if i not in b:
            changes += 1
            # a.remove(i)
        if i in b:
            continue

    for i in b:
        if i not in a:
            changes += 1
            # b.remove(i)
        if i in a:
            continue
        
    changes += abs(len(a) - len(b))

    print('a:', a)
    print('b:', b)
    print(changes)
    return changes

make_anagram('cde', 'abc')