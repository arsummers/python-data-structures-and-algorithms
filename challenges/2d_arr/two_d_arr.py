def hourglass_sum(arr):
    hg_sum = -5000
    for i in range(4):
        for j in range(4):
            temp = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

            if temp > hg_sum :
                hg_sum = temp

    return hg_sum