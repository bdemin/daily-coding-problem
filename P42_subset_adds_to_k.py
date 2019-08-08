# Given a list of integers S and a target number k, write a function that returns
# a subset of S that adds up to k. If such a subset cannot be made, then return null.

# Integers can appear more than once in the list. You may aske all numbers in the list are positive.

# For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it ks up to 24.


def recfunc(S, index, k, subset, subsets):

    # Sum k is zero, append the found subset
    if (k == 0):
        subsets.append(subset)
        return

    # No remaining elements, subset not found
    if (index == 0):
        return

    # Case 1: do not include last element in current subset
    recfunc(S, index - 1, k, subset, subsets)

    # Case 2: include last element in current subset
    new_subset = [] + subset
    new_subset.append(S[index - 1])
    recfunc(S, index - 1, k - S[index - 1], new_subset, subsets)
    if subsets:
        return subsets[0]


def find_subsets(S, k):
    index = len(S)
    subset = []
    return recfunc(S, index, k, subset, subsets = [])


# Driver code
S = [1,5,6]
k = 4
result = find_subsets(S, k)
print(result)

S = [12, 1, 61, 5, 9, 2]
k = 24
result = find_subsets(S, k)
print(result)
