# The edit distance between two strings refers to the minimum number of character
# insertions, deletions, and substitutions required to change one string to the other.
# For example, the edit distance between “kitten” and “sitting” is three: substitute
# the “k” for “s”, substitute the “e” for “i”, and append a “g”.

# Given two strings, compute the edit distance between them.


def find_edit_distance(string1, string2):
    longest = max(len(string1), len(string2))
    distance = abs(len(string1) - len(string2))
    for i in range(longest):
        try:
            if string1[i] != string2[i]:
                distance += 1
        except:
            return distance
    return distance


# Driver code
string1 = 'kitten'
string2 = 'sitting'
result = find_edit_distance(string1, string2)
print(result)

string1 = 'kitten'
string2 = 'kitten'
result = find_edit_distance(string1, string2)
print(result)

string1 = ''
string2 = ''
result = find_edit_distance(string1, string2)
print(result)