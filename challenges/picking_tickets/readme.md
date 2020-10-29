An array of n ticket prices, 'tickets'
    - tickets = [1, 2, 4, 7, 3] (n=5)

number m is defined as the size of some subsequence('s'), where each element covers and unbroken range of integers.

example: if you sort 's',  the absolute difference between elements 'j' and 'j+1' would be either 0 or 1.

it's really just a maximum subsequence problem

Determine the max length of a subsequence chosen from the tickets array.

input: [8,6,4,8,4]
valid subseqs are: [4,4,5], [8,8]
subseqs have m values (the length of the subseq) of 3 and 2.
output: 3

In simpler terms: Return the length of the longest possible subsequence.

basic steps:
- sort tickets array
- get subsequences
return length


- have a max length variable
- iterate over sorted arr.
- if number at i == number at i+1, or number at i == number at i+1 minus 1, add number at i to temp list
- reassign length of temp_max and max_len to the length of the temp array.

- once I get to a new subseq:
    - empty out temp array
    - rebuild from new subsequence
    - reassign temp length
    - compare temp length to max length
    - reassign max length as needed

