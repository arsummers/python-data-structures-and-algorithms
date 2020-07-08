"""
Given two strings, determine if they share a common substring. A substring may be as small as one character.

For example, the words "a", "and", "art" share the common substring . The words "be" and "cat" do not share a substring.
"""

def two_strings(s1, s2):
    for i in s1:
        if i in s2:
            return 'YES'
    return 'NO'