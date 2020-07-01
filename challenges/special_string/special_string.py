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

Code to get all substrings from Geeks4Geeks: https://www.geeksforgeeks.org/python-get-all-substrings-of-given-string/

Breakdown of that list comprehension:
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            subs.append(s[i:j])
"""

def special_string(s):

    substrings = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]

    counter = 0

    if s == s[::-1]:
        substrings.append(s)
        counter += 1
        print(f'palindrome s: {s}')


    for elem in substrings:
        # captures first half of odd string, not inclusive of actual middle
        # odd_mid = elem[:len(elem)//2:]

        # if len(elem) == 1 or len(elem) % 2 == 0 and elem == elem[::-1]:
        #     print(elem)
        #     counter += 1
            
        # elif elem == elem[::-1]:
        #     for i in range(1, len(odd_mid)):
        #         if s[i] == s[0]:
        #             counter += 1

        if elem == elem[::-1] and elem != s:
            if len(elem) == 1 or len(elem) % 2 == 0 or len(elem) == 3:
                counter += 1
                print(f'evens: {elem}')
            elif len(elem) >= 5 or len(elem) % 2 != 0:
                for letter in range(1, len(elem[:len(elem)//2:])):
                    if elem[letter] == s[0]:
                        counter += 1
                        print(f'odds: {elem}')
                        print(f'odds letters: {elem[letter]}')




    # if len(s) == 2:
    #     if s[0] == s[1]:
    #         substrings.append(s)
    #     return len(substrings)


    # for i in range(len(s)-2):
    #     if s[i] == s[i+2]:
    #         sub_str = s[i] + s[i+1] + s[1+2]
    #         substrings.append(''.join(sub_str))
    #     if s[i] == s[i+1]:
    #         sub_str = s[i] + s[i+1]
    #         substrings.append(''.join(sub_str))


    print(substrings)
    return counter


"""
another idea for a code challenge:
determine how many characters you need to delete from two strings in order for them to match
at, cat = 2
thought, slough = 6 (unless it was sloughs)
"""
