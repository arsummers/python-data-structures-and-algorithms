# anagram!
# remove each string that is an anagram of an earlier string, then return an ordered list of the remaining words
# example:
# input: ['code', 'doce', 'frame', 'edoc', 'framer']
# output: 'code', 'frame', 'framer'
# input = ['poke', 'ekop', 'kope', 'peok']
# output = ['poke']

# start with a brute force algorithm, then pare it down from there. Here's the text I was using as my main test case. Note that is has multiple items with anagrams, as well as a word that isn't an anagram but is similar to one of the anagrams
# text = ['code', 'doce', 'frame', 'edoc', 'framer', 'famer']


def anagram(text):

    sorted_words = dict()

    # reverses text list so that when it gets turned into a dictionary it will have the first instance of the anagram. Used list slice rather than the reverse method since reverse returns None.
    for word in text[::-1]:
        current = word #just another variable to keep the various instances of 'word' straight

        # takes each word from the text list, essentially 'unanagrams' it, then appends it to the dict of sorted words. The letters are the thing being sorted, not the word order.
        # removes duplicates from sorted words and returns it as a list
        sorted_words.update({''.join(sorted(current)) : current})


    return sorted(list(sorted_words.values()))

def anagram_oneliner(text):

    return sorted(list({''.join(sorted(word)) : word for word in text[::-1]}.values()))
