# Implement regular expression matching with the following special characters:

# . (period) which matches any single character
# * (asterisk) which matches zero or more of the preceding element
# That is, implement a function that takes in a string and a valid regular
# expression and returns whether or not the string matches the regular expression.

# For example, given the regular expression "ra." and the string "ray",
# your function should return true. The same regular expression on the
# string "raymond" should return false.

# Given the regular expression ".*at" and the string "chat", your function
# should return true. The same regular expression on the string "chats"
# should return false.


def check_regex(re, string):
    boolMat = [[False]*(len(re)+1) for i in range(len(string)+1)]
    boolMat[0][0] = True
    
    for i in range(0, len(string) + 1):
        for j in range(1, len(re) + 1):
            if re[j-1] == '*':
                boolMat[i][j] = boolMat[i][j-2] or (i > 0 and j > 1 and (re[j-2] == '.' or 
                            string[i-1] == re[j-2]) and boolMat[i-1][j])
            elif i > 0 and (re[j-1] == '.' or re[j-1] == string[i-1]):
                boolMat[i][j] = boolMat[i-1][j-1]
    return boolMat[-1][-1]


# Driver code
re = 'ra.'
string = "ray"
assert check_regex(re, string) == True

string = "raymond"
assert check_regex(re, string) == False

re = ".*at" 
string = "chat"
assert check_regex(re, string) == True

string = "chats"
assert check_regex(re, string) == False

re = "c*a*b" 
string = "aab"
assert check_regex(re, string) == True

re = "mis*is*p*"
string = "mississippi"
assert check_regex(re, string) == False

re = ".*" 
string = "ab"
assert check_regex(re, string) == True