from unique_chars import unique_chars, unique_chars_return

def test_exists():
    st = 'string'
    assert unique_chars(st)

def test_false_simple():
    string = 'The quick brown fox jumps over the lazy dog'
    assert unique_chars(string) == False

def test_true():
    string = 'I love cats'
    assert unique_chars(string) == True

def test_false_cases():
    string = 'Donal the duck'
    assert unique_chars(string) == False

def test_false_chars():
    string = 'I am dog. Query.'
    assert unique_chars(string) == False

def test_empty():
    string = ''
    assert unique_chars(string) == True

# trying it another way for fun


def test_false_simple2():
    string = 'The quick brown fox jumps over the lazy dog'
    assert unique_chars_return(string) == False

def test_true2():
    string = 'I love cats'
    assert unique_chars_return(string) == True

def test_false_cases2():
    string = 'Donal the duck'
    assert unique_chars_return(string) == False

def test_false_chars2():
    string = 'I am dog. Query.'
    assert unique_chars_return(string) == False

def test_empty2():
    string = ''
    assert unique_chars_return(string) == True
