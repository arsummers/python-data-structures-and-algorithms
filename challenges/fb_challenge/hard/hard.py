# anagram!
# remove each string that is an anagram of an earlier string, then return an ordered list of the remaining words
# example:
# input: ['code', 'doce', 'frame', 'edoc', 'framer']
# output: 'code', 'frame', 'framer'
# input = ['poke', 'ekop', 'kope', 'peok']
# output = 'poke'

text = ['code', 'doce', 'frame', 'edoc', 'framer']


def anagram(text):
    # first step = check is the next item is an anagram, iterate through string in array

    i = 0
    j = 1

    # first goal = remove everything 'code'

    while j < len(text)-1:

        for letter in text[i]:
            if letter in text[j] and len(text[i]) == len(text[j]):
                text.remove(text[j])
                anagram(text)
                print(text[i])


        
        j += 1

anagram(text)