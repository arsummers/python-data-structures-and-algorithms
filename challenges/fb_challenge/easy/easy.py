
# problem domain:
# write a function that, given a string consisting of a word or words made up from lettters from the word 'instagram', outputs an integer with the number of stickers I will need to buy


from collections import Counter

def stickers_for(phrase):
    # do a count to count comparison between the phrase and 'instagram'
    # if ANY of the letters in the phrase have a higher count than the gram letters, round up to the next nearest whole number, BUT don't let it bump up a sticker for each and every letter, otherwise you'll buy too many
    # the correct sticker number will be the highest number in the letter differences dict (with special calculations for 'a') plus one

    insta = 'instagram'
    insta_dict = Counter(insta)
    phrase_dict = Counter(phrase)

    stickers = 1

    letter_differences = {letter: phrase_dict[letter] - insta_dict.get(letter, 0) for letter in phrase_dict}


    current = 0

    for letter in letter_differences:

        if letter != 'a':

            if current > letter_differences[letter]:
                current = current
                
            if letter_differences[letter] > current:
                current = letter_differences[letter]

        elif letter == 'a':
            
            if current > letter_differences[letter]:
                current = current

            if letter_differences[letter] > current:
                if letter_differences[letter] % 2 == 0:
                    current = letter_differences[letter] - 2
                
                elif letter_differences[letter] % 2 != 0:
                    current = letter_differences[letter] - 1

    stickers += current
    return stickers
