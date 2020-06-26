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
Call Counter on the string, giving the number of times each character exists

loop through string/Counter

a count variable: increment each time there's a difference between the number of characters. Start with the value of the first one, increment by the abs value of the first value minus the ones after

if the counter variable becomes > 1, return 'NO', else return 'YES'


"""

from collections import Counter

def sherlock(s):
    s_counts = Counter(s)

    base_setup = next(iter(s_counts.values()))
    base = base_setup

    tally = 0

    for key in s_counts:
        if s_counts[key] != base:
            tally += abs(s_counts[key] - base)
        
        if tally > 1:
            return 'NO'

    return 'YES'