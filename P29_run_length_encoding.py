# Run-length encoding is a fast and simple method of encoding strings.
# The basic idea is to represent repeated successive characters as a single
# count and character. For example, the string "AAAABBBCCDAA" would be
# encoded as "4A3B2C1D2A".

# Implement run-length encoding and decoding. You can assume the string
# to be encoded have no digits and consists solely of alphabetic characters.
# You can assume the string to be decoded is valid.


def encode(string):
    print(string)
    counter = 1
    lastChar = string[0]
    string = string[1:]
    returnString = ''

    for char in string:
        if char == lastChar:
            counter += 1
        else:
            returnString += str(counter)
            returnString += lastChar
            lastChar = char
            counter = 1

    returnString += str(counter)
    returnString += lastChar
    print(returnString)
    return returnString


# Driver code
string = "AAAABBBCCDAA"
assert encode(string) == "4A3B2C1D2A"
