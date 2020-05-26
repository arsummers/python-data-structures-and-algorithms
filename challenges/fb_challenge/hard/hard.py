# anagram!
# remove each string that is an anagram of an earlier string, then return an ordered list of the remaining words
# example:
# input: ['code', 'doce', 'frame', 'edoc', 'framer']
# output: 'code', 'frame', 'framer'
# input = ['poke', 'ekop', 'kope', 'peok']
# output = ['poke']

# start with a brute force algorithm, then pare it down from there
text = ['code', 'doce', 'frame', 'edoc', 'framer', 'famer']


def anagram(text):
    # first step = check is the next item is an anagram, iterate through string in array
    # since an iterative solution is obviously being a pain, maybe you should try recursion.

    keepers = []
    sorted_words = []
    joiner = ''

    for word in text:
        i = 0

        sorted_words.append(joiner.join(sorted(word)))
        # sorted words isn't getting properly created
        # current = text[i]
        # sort_cur = sorted(current)

        # removes duplicates from sorted words and returns it as a list. this works well to remove stuff
        sorted_words = list(dict.fromkeys(sorted_words))

        # remove_stuff(sorted_words, sort_cur)

        # if sort_cur in sorted_words:
        #     print(sorted_words)

        #     keepers.append(current)
        #     # this is where I take out everything that matches
        #     remove_stuff(sorted_words, sort_cur)

            
        i += 1
    print(sorted_words)
        
        
        
        # if sorted(current) in sorted_words[i+1:len(text)]:
        #     text.remove(sorted(current))

        #     print(sorted(current))
        #     print(text)
        


    # i = 0
    # j = 1

    # while j < len(text)-1:

    #     for letter in text[i]:
    #         if letter in text[j] and len(text[i]) == len(text[j]):
    #             text.remove(text[j])
    #             print(f'text at j {text[j]}')
    #             anagram(text)
    #             print(text[i])
    #             i += 1
        
    #     j += 1
    
    print('***** CORRECT OUTPUT', keepers)
    return keepers #will be changed


anagram(text)