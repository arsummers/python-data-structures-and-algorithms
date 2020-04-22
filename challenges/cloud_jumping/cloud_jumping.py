def cloud_jumping(c):
    jump_count = 0
    position = 0
    length = len(c)

    for _ in range(length):
        if length <= 3:
            jump_count = 1
        if position < length and c[position] == 0:

            if position < length-2 and c[position+2] == 0:           
                jump_count += 1
                position += 2

            elif position < length-2 and c[position+2] == 1:
                jump_count += 1
                position += 1
                print('postion:', position)

            elif position < length-1 and c[position+1] == 0:
                jump_count += 1
                position += 1

    return jump_count
