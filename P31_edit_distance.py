# The edit distance between two strings refers to the minimum number of character
# insertions, deletions, and substitutions required to change one string to the other.
# For example, the edit distance between “kitten” and “sitting” is three: substitute
# the “k” for “s”, substitute the “e” for “i”, and append a “g”.

# Given two strings, compute the edit distance between them.


def find_edit_distance(string1, string2):
    m = len(string1)
    n = len(string2)
    matrix = [[None] * (n+1) for i in range(m+1)]

    for i in range(m+1):
        matrix[i][0] = i
    
    for i in range(n+1):
        matrix[0][i] = i

    for i in range(1, m+1):
        for j in range(1, n+1):
            if string1[i-1] == string2[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]) + 1

    return matrix[-1][-1]


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

string1 = 'kitten'
string2 = 'akitten'
result = find_edit_distance(string1, string2)
print(result)