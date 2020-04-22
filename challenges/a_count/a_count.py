def a_count(s, n):
    all_a_num = 0
   
    for letter in s:
        if letter == 'a':
            all_a_num += 1
    
    shortened_n = n//len(s)

    real_a_count = all_a_num * shortened_n
    
    for letter in s[:n%len(s)]:
        if letter == 'a':
            real_a_count += 1

    return real_a_count