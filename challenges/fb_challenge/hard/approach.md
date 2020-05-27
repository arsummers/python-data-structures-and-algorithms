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

# set up some type of current thing on the anagrams with Counter

1. silly feeling way to do it:
    a. generate a list of each word using Counter
       check where each match lives in the Counter array
       take the index of the first time something shows up
       match that index to the item in the given list
       remove everything else
       return

    b. have a current variable
        set current to Counter
        
1. The current working approach:
2. Take in list of words
3. Set up a variable as an empty list for the items to be returned
4. Set up a variable that is a dictionary, which will do the bulk of the heavy lifting here
5. Loop through the list of words in reverse
6. For each word in the list, sort the letters, and add it to the dictationary as a key-value pair. The key is the sorted version of the word. The value is the word as it appears before any other anagrams show up. Sample dictionary snippet: `{'cdeo':'code'}`. Using a dictionary automatically prevents duplicates. Looping through the original list in reverse means you'll always have the first instance of a word or its anagram, since the dictionary values will get updated multiple times.
7. Once you have a dictionary with every anagram removed, return a sorted list of the values from the dictionary. 