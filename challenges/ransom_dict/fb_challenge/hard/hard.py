# anagram!
# remove each string that is an anagram of an earlier string

text = ['code', 'doce', 'frame', 'edoc', 'framer']
# works with 'poke'!


def funWithAnagrams(text):
    # Write your code here
    # since python can iterate over strings, think of this as kind of a matrix
    i = 0
    j = 1

    # first goal = remove everything 'code'

    while j < len(text)-1:

        for letter in text[i]:
            if letter in text[j] and len(text[i]) == len(text[j]):
                text.remove(text[j])
                funWithAnagrams(text)
                return([text[i]])

        j += 1