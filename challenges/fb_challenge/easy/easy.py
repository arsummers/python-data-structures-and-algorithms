
phrase = 'artisan martians'

def stickers_for(phrase):
    # take spaces out of strings
    # do another count to count comparison between the phrase and 'instagram'
    # if ANY of the letters in the phrase have a higher count than the gram letters, round up to the next nearest whole number, BUT don't let it bump up a sticker for each and every letter, otherwise you'll buy too many
    phrase_s = phrase.strip()
    insta = 'instagram'
    insta_dict = dict((i, insta.count(i)) for i in insta)
    phrase_dict = dict((i, phrase_s.count(i)) for i in phrase_s)

    stickers = 1

    letter_differences = {letter: phrase_dict[letter] - insta_dict.get(letter, 0) for letter in phrase_dict}

    print(letter_differences)

    for letter in letter_differences:
        if letter != 'a' and letter_differences[letter] > 0:
            stickers = letter_differences[letter]
        elif letter == 'a' and letter_differences[letter] > 0:
            divisor = letter_differences[letter] - 2
            stickers = divisor
        
    print(stickers+1)


stickers_for(phrase)