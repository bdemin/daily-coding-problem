# Given a dictionary of words and a string made up of those words (no spaces),
# return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string
# "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string
# "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].


def string_in_dict(dictionary, string):
    wordLocation = 0
    returnList = []

    for word in dictionary:
        if word in string:
            string = string.replace(word, str(wordLocation))
        wordLocation += 1
        
    for index in string:
        if index.isdigit(): 
            returnList.append(dictionary[int(index)])
        else:
            return None
    return returnList


# Driver code
dictionary = ['quick', 'brown', 'the', 'fox']
string = "thequickbrownfox"
result = string_in_dict(dictionary, string)
print(result)

dictionary = ['bed', 'bath', 'bedbath', 'and', 'beyond']
string = "bedbathandbeyond"
result = string_in_dict(dictionary, string)
print(result)

dictionary = ['bed', 'bath']
string = "bedbeyondbath"
result = string_in_dict(dictionary, string)
print(result)