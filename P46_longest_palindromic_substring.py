# Given a string, find the longest palindromic contiguous substring.
# If there are more than one with the maximum length, return any one.

# For example, the longest palindromic substring of "aabcdcb" is "bcdcb".
# The longest palindromic substring of "bananas" is "anana".


def is_palindrome(string):
    return string == string[::-1]


def find_longest_palindrome(string):
    if len(string) == 0:
        return None
    elif is_palindrome(string):
        return string

    string1 = find_longest_palindrome(string[:-1])
    string2 = find_longest_palindrome(string[1:])

    if len(string1) > len(string2):
        return string1
    return string2
        

# Driver code
string = 'aabcdcb'
print(find_longest_palindrome(string))

string = 'bananas'
print(find_longest_palindrome(string))

string = ''
print(find_longest_palindrome(string))

string = 'a'
print(find_longest_palindrome(string))

string = 'aabccc'
print(find_longest_palindrome(string))
