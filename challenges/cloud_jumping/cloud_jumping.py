c = [0, 0, 0, 0, 1, 0, 1, 0]
# result should be 4

def cloud_jumping(c):
    jump_count = 0
    position = 0
    length = len(c)

    for _ in range(length):
        if position < length and c[position] == 0:
            print('hit first if')
            print('postion:', position)
            if position < length-2 and c[position+2] == 0:
                print('hit second if')           
                jump_count += 1
                position += 2
                print('postion:', position)
            elif position < length-2 and c[position+2] == 1:
                print('hit third if')
                jump_count += 1
                position += 1
                print('postion:', position)

    print("jumps:", jump_count)

cloud_jumping(c)