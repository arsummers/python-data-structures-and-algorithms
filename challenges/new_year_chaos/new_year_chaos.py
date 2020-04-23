# numbers can only move up at most 2 spaces
# if difference between numbers is >=3, print too chaotic

def minimum_bribe(q):   
    min_bribes = 0
    loop_range = len(q)-1
    
    for i in range(loop_range):
        if q[i] - q[i+1] == 2:
            min_bribes += 2

        elif q[i] - q[i+1] == 1:
            min_bribes += 1

        elif q[i] - q[i+1] >= 3:
            return 'Too chaotic'
   
    return min_bribes
