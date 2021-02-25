from collections import Counter
def escape_room(word_list, keypads):
    # goal is to see how many of each word in the word list can be made from the letters in the keypad
    # The word will not have any letters not in the keypad
    # the first letter of the keypad WILL be in the valid word
    # if keypad word letter at index 0 isn't in the word in the word list, it will auto-0
    # how can I do this without a bunch of loops?

    # input: word_list = ['APPLE', 'PLEAS', 'PLEASE']
    #        keypads = ['AELWXYZ', 'AELPXYZ', 'AELPSXY', 'SAELPRT', 'XAEBKSY']
    # output: expected = [0, 1, 3, 2, 0]

    # for each word, check if the letters for it exist in the keypad. if all the letters are in the keypad, bump the counter up one, then move onto next letter. if any letters are missing, don't increment. if the first letter in the keypad isn't in in the word, pass over it.


    # num_words = [0] * len(keypads)
    num_words = []

    # removes duplicate letters, so I won't every have to loop through something larger than 26 letters in the word_list
    word_set = [''.join(set((word))) for word in word_list]
    # word_collection = [Counter(word) for word in word_set]

    # keypad_collection = [Counter(keypad) for keypad in keypads]

    # for keypad in keypads: dictionary = {'A': 0, 'B': 0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0} 

    # maybe I could do make a Counter dictionary for each thing, then do something with a left join, and if all the elements of the word list word can overlap with the keypad, the counter can increment

    # for i in range(len(keypads)):
    #     for word in remove_dupes:
    #         for letter in word:
    #             if letter not in keypads[i]:
    #                 break              

    # left join should return all elements from left table, and their matched records from right table.
    # left table should be the word list, right table should be the keypads. right side should return none if it doesn't have a match on the left side.
    #  will need to join each item in the right table on each item on the left table.
    # 

    joined_table = []

    def pseudo_left_join(word, keypad):
        """
        will return a list of 1s and 0s depending on if the letter in the word exists in the keypad
        """
        helper_table = []

        for letter in word:
            if letter not in keypad:
                helper_table.append(0)
            helper_table.append(1)

        joined_table.append(helper_table)
        return joined_table

    # pseudo_left_join('APLE', 'AELSXYZ')
    result = map(pseudo_left_join, joined_table)

    def count_possibilities(joined_table):
  
        for item in joined_table:
            if 0 in item:
                num_words.append(0)
            if 0 not in item:
                num_words.append(1)
    
    count_possibilities(joined_table)



    # pseudo_left_join([word for word in word_set], [keypad for keypad in keypads]) 
    # need to check the pseudojoin on each word onto a single keypad element




    # for keypad in keypads:
    #     pseudo_left_join(word, keypad)




    # count_possibilities(joined_table)
    # return pseudo_left_join('APLE', 'AELSXYZ')

        
    # return num_words
    # return joined_table
    return list(result)
    # return word_set