# Implement an autocomplete system. That is, given a query string
# s and a set of all possible query strings, return all strings
# in the set that have s as a prefix.
# For example, given the query string de and the set of strings
# [dog, deer, deal], return [deer, deal].
# Hint: Try preprocessing the dictionary into a more efficient
# data structure to speed up queries.


# Note: Can be improved by constructing a Trie tree structure from the strings
def autocomplete(s, _set):
    output = []
    length = len(s)
    for item in _set:
        if item[0:length] == s:
            output.append(item)
    return output


# Driver code:
s = 'de'
_set = ['dog', 'deer', 'deal']
result = autocomplete(s, _set)
print(result)