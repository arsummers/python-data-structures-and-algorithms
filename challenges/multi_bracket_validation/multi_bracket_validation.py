def multi_bracket_validation(string):
    # viable inputs: {, }, [, ], (, )
    bracket_list = string.split()
    
    # counters
    open_paren_ct = 0
    close_paren_ct = 0

    open_sqr_ct = 0
    close_sqr_ct = 0

    open_curly_ct = 0
    close_curly_ct = 0

    iterator = 0

    if len(bracket_list) % 2 != 0:
        return False
    else:
        return 'still testing'