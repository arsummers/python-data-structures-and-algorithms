# anagram!
# remove each string that is an anagram of an earlier string, then return an ordered list of the remaining words
# example:
# input: ['code', 'doce', 'frame', 'edoc', 'framer']
# output: 'code', 'frame', 'framer'
# input = ['poke', 'ekop', 'kope', 'peok']
# output = ['poke']

# start with a brute force algorithm, then pare it down from there
from collections import Counter

text = ['code', 'doce', 'frame', 'edoc', 'framer', 'famer']


def anagram(text):
    # first step = check is the next item is an anagram, iterate through string in array
    # since an iterative solution is obviously being a pain, maybe you should try recursion.

    # def check_letters():
    #     pass

    i = 0
    j = 1

    while j < len(text)-1:

        for letter in text[i]:
            if letter in text[j] and len(text[i]) == len(text[j]):
                text.remove(text[j])
                print(f'text at j {text[j]}')
                anagram(text)
                print(text[i])
                i += 1
        
        j += 1
    
    print('***** CORRECT OUTPUT', text)
    return text #will be changed


anagram(text)