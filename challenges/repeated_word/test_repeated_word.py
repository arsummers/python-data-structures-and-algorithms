from repeated_word import repeated_word

def test_exists():
    assert repeated_word

def test_short_sentence():
    sentence = 'To be or not to be'
    assert repeated_word(sentence) == 'to'

def test_no_repeats():
    sentence = 'this has no repeating words'
    assert repeated_word(sentence) == None

def test_single_word():
    sentence = 'hello'
    assert repeated_word(sentence) == None

def test_only_repeating():
    sentence = 'hi hi hi hi'
    assert repeated_word(sentence) == 'hi'

def test_longer_sentence():
    sentence = 'Once upon a time, there was a brave princess who...'
    assert repeated_word(sentence) == 'a'

def test_empty_string():
    sentence = ''
    assert repeated_word(sentence) == None

def test_paragraph():
    sentence = 'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...'

    assert repeated_word(sentence) == 'it'