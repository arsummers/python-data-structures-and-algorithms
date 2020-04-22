def a_count(s, n):
    a_num = 0
    repeated_string = s*100
    new_string = repeated_string[:n]

    for letter in new_string:
        if letter == 'a':
            a_num += 1

    return a_num