def repeated_word(sentence):
    sentence = sentence.lower().split()
    word_list = []

    for word in sentence:
        if word not in word_list:
            word_list.append(word)
        elif word in word_list:
            return word
        