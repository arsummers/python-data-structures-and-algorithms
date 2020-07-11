"""
Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

Complete the function sherlockAndAnagrams in the editor below. It must return an integer that represents the number of anagrammatic pairs of substrings in s.

notes:
look for repeating characters
a single character without a match doesn't count as an anagram
pair anagrams together
 - 'cdcd' contains anagrams: [c, c], [d, d], [cd, dc], [cd, cd], [dc, cd]
 - [cdc] doesn't count as an anagram because it doesn't have a pair
there can be overlap in which substrings count as pairs:
    - 'bbbb' contains pairs [bbb, bbb] because that shows up twice as an anagram, even though they overlap at [[1], [2]]


basic level:
break string into all substrings
    - probably put this into an array to start
run Counter in each substring
    - add those to a "parent" Counter dict --> this will weed out non-anagrams, since anything that only shows up once won't get added to the final count

for every item in the counter dict, return the number // 2 --> that will only reveal the things with pairs, no floats.

get all substrings:
    - ref: https://www.geeksforgeeks.org/python-get-all-substrings-of-given-string/
            - used itertools version to avoid nesting for loops

"""
from collections import Counter
from itertools import combinations

def gramlock(s):
    substrings = [s[x:y] for x, y in combinations(range(len(s)+1), r=2)]
    sorted_substrings = [''.join(sorted(string)) for string in substrings]#returns a list of sorted versions of the strings, working from a generated matrix
    child = Counter(sorted_substrings)
    anagram_count = 0

    for i in child:
        if child[i] > 1:
            if child[i] // 2 >= 1:
                anagram_count += (child[i] // 2)


    # if all characters are the same, I'll need the sum of their instances
    # 
    
    return anagram_count