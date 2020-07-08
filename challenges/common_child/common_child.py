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


def common_child(s1, s2):
    child = []
    i = 0
    temp_1 = s1[i:len(s1)]
    temp_2 = s2[i:len(s2)]

    def helper():        
        if s1[i] == s2[i]:
                child_str += s1[i]
                print(f'child str here{child_str}')
                i += 1
        if s1[i] != s2[i]:
                print(f'REASSIGNMENT {s1}, {s2}')
                s1, temp_1 = temp_1, s1
                s2, temp_2 = temp_2, s2
                i += 1
                helper()
    helper()
    temp_1 = [i for i in s1 if i in s2]
    temp_2 = [i for i in s2 if i in s1]

    if temp_1 == temp_2:
        child = temp_1
     
        

    print(f'temps: {temp_1}, {temp_2}')
    print(f'child str {child}')


    return len(child)
           




# problem domain: write a function that takes in a linked list and return the same linked list but with any duplicated values removed
# CHECK OUT elephantsql
