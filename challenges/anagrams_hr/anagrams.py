"""
Given two strings, a and b, that may or may not be of the same length, determine the minimum number of character deletions required to make a and b anagrams. Any characters can be deleted from either of the strings.

ex:
a = 'cde'
b = 'dcf'
output = 2, since c and f should be deleted

each time there is a discrepency between either the character itself, or the the number of times it appears, increment counter by the difference.


solution ultimately adapted from hackerrank, as my approach, left commented out below, was close, but didn't pick up on everything.

"""

def make_anagram(a, b):
    changes = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for letter in alphabet:
        a_ = a.count(letter)
        b_ = b.count(letter)

        changes += abs(a_ - b_)

    return changes

make_anagram('accfgilmmnrsvwxxyyyz', 'bbdeeghhijjklmmmooppqrrstuvwwx')


# failed approach:
    # a = Counter(a)
    # b = Counter(b)

    # counter = 0
    
    # for key in a:

    #     if key not in b:
    #         changes += 1

    #     elif key in b:
    #         if a[key] != b[key]:
    #             print(f'key: {key}\n a key value: {a[key]}\n b key value:{b[key]}')
    #             changes += abs(a[key] - b[key])

        
    # for key in b:
    #     if key not in a:
    #         changes += 1