# anagram!
# remove each string that is an anagram of an earlier string, then return an ordered list of the remaining words
# example:
# input: ['code', 'doce', 'frame', 'edoc', 'framer']
# output: 'code', 'frame', 'framer'
# input = ['poke', 'ekop', 'kope', 'peok']
# output = ['poke']
This will still need some work before it's ready to code out.

1. check for anagrams
    a. if all the letters in one word exist in equal amounts in other words, those words are anagrams
    b. work through the anagrams first

2. if it is an anagram, hang on to only the first time it appears
    a. the first instances of anagram could be stored in another structure, then the rest could be set aside since we don't need to use them anymore
    b. or the list could become altered.
    
    if the list is altered:
        check each item against the "current" item
        delete items that are anagrams
        move up "current" item
        repeat check

3. When there are no more anagrams, return the remaining words as an ordered list
