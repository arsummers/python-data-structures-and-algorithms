# text = ['code', 'code', 'frame', 'code', 'framer', 'frame']
# sorty = []
# joiner = ''

# this is a decent way to get a list with no duplicates:
# sorted_words = list(dict.fromkeys(sorted_words))


# # this makes a list of lists which isn't useful for what I'm trying to accomplish
# for word in text:
#     sorty.append(joiner.join(sorted(word)))

# if sorty.count('cdeo') >= 1:
#     print('yes')

# print(sorty)

text = ['code', 'doce', 'frame', 'edoc', 'framer', 'famer']

def anagram(text):
    text = text[::-1]

    # first step = check is the next item is an anagram, iterate through string in array
    # since an iterative solution is obviously being a pain, maybe you should try recursion.

    # IDEA: I could instead make a dictionary where the 'sorted' version of a word is the key, and the one I need to return is the value. Loop through list in reverse, so the last thing modified will be the first instance
    sorted_words = dict()
    joiner = ''

    for word in text:
        # takes each word from the text list, essentially 'unanagrams' it, then appends it to the list of sorted words. The letters are the thing being sorted, not the word order.
        current = word #just another variable to keep the various instances of 'word' straight

        sorted_words.update({joiner.join(sorted(current)) : current})

        sort_cur = joiner.join(sorted(current))
        # removes duplicates from sorted words and returns it as a list


        # if sort_cur in sorted_words:
        #     print(sorted_words)

        #     keepers.append(current)
        #     # this is where I take out everything that matches
        #     remove_stuff(sorted_words, sort_cur)

            
    print(sorted_words)

anagram(text)
