# Given a string, find the palindrome that can be made by inserting the fewest number
# of characters as possible anywhere in the word. If there is more than one palindrome
# of minimum length that can be made, return the lexicographically earliest one
# (the first one alphabetically).

# For example, given the string "race", you should return "ecarace", since we can
# add three letters to it (which is the smallest amount to make a palindrome).
# There are seven other palindromes that can be made from "race" by adding three
# letters, but "ecarace" comes first alphabetically.

# As another example, given the string "google", you should return "elgoogle".


def palindrome(string, output = []):
    if len(string) <= 1:
        return len(string)
    if len(string) == 2:
        if (string[0] == string[-1]):
            return 0
        else:
            return 1

    elif string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return min(palindrome(string[:-1]), palindrome(string[1:])) + 1
    


# Driver code
string = 'race'
print(palindrome(string))

string = 'google'
print(palindrome(string))

string = 'ab'
print(palindrome(string))

string = ''
print(palindrome(string))

string = 'a'
print(palindrome(string))

string = 'aa'
print(palindrome(string))

string = 'abcda'
print(palindrome(string))