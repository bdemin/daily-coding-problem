# Given a list of integers, write a function that returns the largest
# sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick
# 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?


# Similar to The House Robber Problem
def max_nonadj_sum(arr):
    temp = arr[0]
    next_sum = 0
    curr_sum = arr[0]
    for i in range(1, len(arr)):
        temp = curr_sum
        curr_sum = max(curr_sum, arr[i] + next_sum)
        next_sum = temp
    return max(curr_sum, next_sum)


# the max sum I can get till now including myself
# exclusive[i] = max(inclusive[i-1], exclusive[i-1]) ------------ max sum I can get excluding myself

# Driver code:
arr = [2, 4, 6, 2, 5]
assert max_nonadj_sum(arr) == 13

arr = [5, 1, 1, 5]
assert max_nonadj_sum(arr) == 10