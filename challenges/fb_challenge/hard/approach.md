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
        

Here is some python that didn't work, but I thinkw as close:

```
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
```

here is more code I've decided to discard:
```
 counts_ = []

    for word in text:
        counts = Counter(word)
        counts_.append(counts)
    print(counts_)
    print(len(counts_[0]))
    i = 0
    j = 1
    while i < len(counts_) and j < len(counts_):
        # for something
        # now that I have the counts, I need to check the first one against every one that comes after it. Things to check: that all the letters in one are in the one that comes after, and that they have the same count per letter.
        
        if 'a' in counts_[i]:
            print('a is here')

        if 'a' not in counts_[i]:
            print['a is not here']

        i += 1
        j += 1
```
