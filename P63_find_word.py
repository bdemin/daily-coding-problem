# Given a 2D matrix of characters and a target word, write a function
# that returns whether the word can be found in the matrix by going
# left-to-right, or up-to-down.

# For example, given the following matrix:

# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]
# and the target word 'FOAM', you should return true, since it'sthe leftmost column.
# Similarly, given the target word 'MASS', you should return true, since it's the last row.


import numpy as np


def find_word(matrix, target):
    
    # Convert to Numpy for easier iteration
    matrix = np.array(matrix)
    m, n = matrix.shape

    # Run on over each character of the matrix
    for i in range(m):
        for j in range(n):
            # In case we found a similar character with the target:
            # Loop over columns while checking similarity with the target:
            target_index = 0
            # Check up-to-down
            while matrix[i + target_index, j] == target[target_index]:
                if target_index == len(target) - 1:
                    # All characters in target are passed - return True
                    return True
                elif i + target_index + 1 < m:
                    target_index += 1
                else:
                    break

            # Loop over rows while checking similarity with the target:
            target_index = 0
            # Check left-to-right
            while matrix[i, j + target_index] == target[target_index]:
                if target_index == len(target) - 1:
                    # All characters in target are passed - return True
                    return True
                elif j + target_index + 1 < n:
                    target_index += 1
                else:
                    break
    return False


# Driver code
matrix = [['F', 'A', 'C', 'I'],
        ['O', 'B', 'Q', 'P'],
        ['A', 'N', 'O', 'B'],
        ['M', 'A', 'S', 'S']]

target = 'FOAM'
print(find_word(matrix, target))

target = 'MASS'
print(find_word(matrix, target))

target = 'FOAN'
print(find_word(matrix, target))

target = 'QOS'
print(find_word(matrix, target))

target = 'ASS'
print(find_word(matrix, target))

target = 'FOAMS'
print(find_word(matrix, target))
