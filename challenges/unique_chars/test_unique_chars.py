from unique_chars import unique_chars

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