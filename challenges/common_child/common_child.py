"""
A string is said to be a child of a another string if it can be formed by deleting 0 or more characters from the other string. Given two strings of equal length, what's the longest string that can be constructed such that it is a child of both?

For example, ABCD and ABDC have two children with maximum length 3, ABC and ABD. They can be formed by eliminating either the D or C from both strings. Note that we will not consider ABCD as a common child because we can't rearrange characters and ABCD != ABDC.

in:HARRY, SALLY
out: 2

The longest string that can be formed by deleting zero or more characters from HARRY  and SALLY is AY, whose length is 2.


notes:
strings are immutable objects, going to have to work with that

vars:
might not need the temps
temp_1 --> will contain the letters of s1 as it gets "shortened" for index comparison
temp_2 --> same as temp_1, but with s2
child_str --> the valid child string. length will be returned

loop through s1 --> in a range:
    maybe this should be a helper function?
    check if the first letter matches s1 and s2 at the same index
        if it does:
            add that letter to the child string
            reassign s1 and s2 as below
        if it doesn't:
            reassign s1 and s2 to the string slice that is the [current index to the end of the string]
            restart loop through this part of the string

"""


def commonChild(s1, s2):
    s1_len = len(s1)
    s2_len = len(s2)
    temp_arr = [[None]*(s2_len+1) for i in range(s1_len + 1)]

    for i in range(s1_len + 1):
        for j in range(s2_len + 1):
            if i == 0 or j == 0:
                temp_arr[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                temp_arr[i][j] = temp_arr[i-1][j-1]+1
            else:
                temp_arr[i][j] = max(temp_arr[i-1][j], temp_arr[i][j-1])
    return temp_arr[s1_len][s2_len]

    
    



    # m = len(X) 
    # n = len(Y) 
  
    # # declaring the array for storing the dp values 
    # L = [[None]*(n + 1) for i in range(m + 1)] 
  
    # """Following steps build L[m + 1][n + 1] in bottom up fashion 
    # Note: L[i][j] contains length of LCS of X[0..i-1] 
    # and Y[0..j-1]"""
    # for i in range(m + 1): 
    #     for j in range(n + 1): 
    #         if i == 0 or j == 0 : 
    #             L[i][j] = 0
    #         elif X[i-1] == Y[j-1]: 
    #             L[i][j] = L[i-1][j-1]+1
    #         else: 
    #             L[i][j] = max(L[i-1][j], L[i][j-1]) 
  
    # # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
    # return L[m][n] 
           




# problem domain: write a function that takes in a linked list and return the same linked list but with any duplicated values removed
# CHECK OUT elephantsql
