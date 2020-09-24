## Problem Domain

Determine is a string is full of unique characters

- spaces don't count
- characters are not case sensitive ('a' and 'A' both count)
- no mention of special characters. For a challenge, let's assume non-alphanumeric characters can be in the string and can count.

## Test cases/edge cases
Input: `The quick brown fox jumps over the lazy dog`
Output: `False`

Input: `I love cats`
Output: `True`

Input: `Donald the duck`
Output: `False`

Input: `I am dog. Query.`
Output: `False`

Input: empty string
Output: `false`

That should cover edge cases for upper/lower case letters. 

## Algorithm/notes
A dictionary/hashmap help break each character down into unique keys. The count of each key should be the value in the dictionary.

I'm going to be working with special characters for fun, and because I'm not on a strict timer, but if I was only looking at alphanumeric characters, I'd be able to automatically return `False` if the length of the string was greater than `36` after spaces have been removed, since letters would have to repeat after that. 


#### Algorithm steps
- Normalize all input
    - convert all characters in string to lowercase, so that capital letters won't cause problems on purpose
- Remove all spaces
- Call Counter, from Python's collections library, on the resulting string. This will net me a dictionary that contains the number of times each letter shows up.
- Since Counter sorts by descending order of the number of occurrences, you can return True if the first value is less than or equal to 1, and False if the first value is greater than 1.


## Pseudocode

## Code