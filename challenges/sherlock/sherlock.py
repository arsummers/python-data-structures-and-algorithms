"""Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just 1 char at 1 index in the string, and the remaining characters will occur the same number of times. Given a string s, determine if it is valid. If so, return YES, otherwise return NO.

example:

input: 'abc'
output: 'YES'

input: 'abcc'
output: 'YES'

input: 'abccc'
output: 'NO'

input: 'aabbcd'
output: 'NO'

Algo:
Call Counter on the string, giving the number of times each character exists. Counter values get turned into a list for easier access.

loop through string/Counter

a count variable: increment each time there's a difference between the number of characters. Start with the value of the first one, increment by the abs value of the first value minus the ones after

if the counter variable becomes > 1, return 'NO', else return 'YES'


"""

from collections import Counter

def sherlock(s):
    s_counts = list(Counter(s).values())

    base = s_counts[0]

    tally = 0

    last_index = len(s_counts) - 1

    for num in s_counts:
        if num != base:
            tally += abs(base - num)
        
        if s_counts[last_index] == 1 and s_counts[last_index-1] > 2:
            return 'YES'

        if tally > 1:
            return 'NO'

    return 'YES'

"""
ok, in edge case it fails because only one letter is causing trouble, although the rest of them appear much more often. Since Counter orders things by how often they occur, I really only need an extra check on the last thing.
"""