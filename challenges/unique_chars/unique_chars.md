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

Input: `Donal the duck`
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
- Since Counter sorts by descending order of the number of occurrences, you can return True if the first value is less than or equal to 1, and False if the first value is greater than 1. The values will have to be converted into a list to access the first one, since dictionary values aren't indexable in python3


## Pseudocode
import Counter
join all characters in string with an empty ''
call lowercase on new string
Counter(the string)
list(Counter(string) values)
return False is list[0] > 1, else return True


## Code
```
from collections import Counter

def unique_chars(string):
    normalized = ''.join(string.lower())
    count_vals = list(Counter(normalized).values())

    if count_vals[0] > 1:
        return False

    else:
        return True

```

## What I needed to change to make the code run
- last two cases, both my edge cases, failed.
- First edge case shows up as True, when it should be False. Something is causing the periods to not register.
- had to change normalized_chars to `normalized = ''.join(string.lower().split())` to remove spaces.
- turning the values into a list gets rid of the sorting that Counter did for some reason. Instead of accessing the first index in the list, I had to find the max number in the list

- List index is out of range on empty string edge case
    - fixed by adding:
    ```if len(string) == 0:
            return True
    ```
    to top of function

## Big O stuff
I think it'd still be O(n), but not a nice O(n) for both time and space. Shouldn't be O(n)^2.

max() is O(n)
Counter() and list() will both be O(n) as well