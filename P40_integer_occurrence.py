# Given an array of integers where every integer occurs three times
# except for one integer, which only occurs once, find and return
# the non-duplicated integer.

# For example, given [6, 1, 3, 3, 3, 6, 6], return 1.
# Given [13, 19, 13, 13], return 19.

# Do this in O(N) time and O(1) space.


def find_single_occurance(arr):
    arr_sum = sum(arr)
    arr_len = len(arr)
    # num_divisions = (arr_len - 1) / 3

    for i in range(arr_len):
        if (arr_sum - arr[i]) % 3 == 0:
            return arr[i]
    return False


# Driver code
arr = [6, 1, 3, 3, 3, 6, 6]
result = find_single_occurance(arr)
print(result)

arr = [13, 19, 13, 13]
result = find_single_occurance(arr)
print(result)
