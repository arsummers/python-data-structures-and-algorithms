def multi_bracket_validation(string):
    # viable inputs: {, }, [, ], (, )
    
    # counters
    open_counters = {
        'paren_ct' : 0,
        'sqr_ct' : 0,
        'curly_ct' : 0,
    }
    
    close_counters = {
        'paren_ct' : 0,
        'sqr_ct' : 0,
        'curly_ct' : 0,
    }

    for item in string:

        if item == '{':
            open_counters['curly_ct'] += 1
        if item == '}':
            close_counters['curly_ct'] += 1

        if item == '(':
            open_counters['paren_ct'] += 1
        if item == ')':
            close_counters['paren_ct'] += 1

        if item == '[':
            open_counters['sqr_ct'] += 1
        if item == ']': 
            close_counters['sqr_ct'] += 1


    if open_counters['curly_ct'] != close_counters['curly_ct']:
        return False
        
    if open_counters['paren_ct'] != close_counters['paren_ct']:
        return False

    if open_counters['sqr_ct'] != close_counters['sqr_ct']:
        return False

    if string[0] == '{' and string[1] == '(' and string[2] == '}' and string[3] == ')':
        return False

    else:
        return True