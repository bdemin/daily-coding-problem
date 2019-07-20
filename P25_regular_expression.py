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
    iString = 0
    iRe = 0
    while iRe < len(re):
        if re[iRe] == string[iString]:
            iString += 1
            iRe += 1
            continue
        elif iRe < len(re)-1 and re[iRe+1] == '*':
            letter = re[iRe]
            repeats = 0
            while letter == string[iRe+repeats]:
                repeats += 1
                iString += 1
            iRe += 2
            iString += repeats
            continue
        if re[iRe] == '.':
            if iRe < len(string)-1:
                return False
            else:
                iString += 1
                iRe += 1
                continue
        if re[iRe] == '*':
            if re[iRe-1] == '.':

                return True
            letter = re[iRe-1]
            repeats = 0
            while letter == string[iRe+repeats]:
                repeats += 1
            iRe += 2
            iString += repeats
            continue
        return False
    return True



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