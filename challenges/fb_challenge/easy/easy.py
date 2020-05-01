
# problem domain:
# write a function that, given a string consisting of a word or words made up from lettters from the word 'instagram', outputs an integer with the number of stickers I will need to buy
# artisan martians needs 2 stickers
# taming giant gnats needs 3
# tiara needs 1
# aaaa needs 2

# phrase = 'artisan martians'
phrase = 'tiara'
# phrase = 'taming giant gnats'
# phrase = 'aaaaa'

from collections import Counter

def stickers_for(phrase):
    # take spaces out of strings
    # do another count to count comparison between the phrase and 'instagram'
    # if ANY of the letters in the phrase have a higher count than the gram letters, round up to the next nearest whole number, BUT don't let it bump up a sticker for each and every letter, otherwise you'll buy too many

    def remove(phrase):
        return phrase.replace(' ', '')
    phrase_s = remove(phrase)
    insta = 'instagram'
    insta_dict = Counter(insta)
    phrase_dict = Counter(phrase_s)

    stickers = 1
    print('insta dict:', insta_dict)
    print('phrase dict:', phrase_dict)

    letter_differences = {letter: phrase_dict[letter] - insta_dict.get(letter, 0) for letter in phrase_dict}

    print('letter difs:', letter_differences)

    current = 0

    for letter in letter_differences:
        print(letter, letter_differences[letter])

        if letter != 'a':

            if current > letter_differences[letter]:
                current = current
                print('current is bigger than the letter count')
                
            if letter_differences[letter] > current:
                current = letter_differences[letter]

        elif letter == 'a':
            
            if current > letter_differences[letter]:
                current = current
                print('a block where current is biggest')

            if letter_differences[letter] > current:
                current = letter_differences[letter] - 1 
                print('the other if inside the a block')

    print('current:', current)
    stickers += current
 
stickers_for(phrase)