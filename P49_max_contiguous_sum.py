# Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

# Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

# Do this in O(N) time.


def find_max_contiguous_sum(arr):
    if not arr or max(arr) < 0:
        return 0

    current_max = arr[0]
    global_max = arr[0]

    for num in arr[1:]:
        current_max = max(num, current_max + num)
        global_max = max(current_max, global_max)

    return global_max


# Driver code
arr = [34, -50, 42, 14, -5, 86]
result = find_max_contiguous_sum(arr)
print(result)

arr = [-5, -1, -8, -9]
result = find_max_contiguous_sum(arr)
print(result)
