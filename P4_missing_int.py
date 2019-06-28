# Given an array of integers, find the first missing positive integer in
# linear time and constant space. In other words, find the lowest positive
# integer that does not exist in the array. The array can contain duplicates
# and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.



# Note: Current solution doesn't meet the memory requirement
def missing_int(arr):
    # Find max value in the array
    arr_max = 0
    for num in arr:
        if num > arr_max:
            arr_max = num
    if arr_max == 0:
        return 1

    # Create a new array with length equal to arr_max
    # each value in new_arr satisfies arr[value] = value
    new_arr = [None] * (arr_max + 1)
    new_arr[0] = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            new_arr[arr[i]] = arr[i]

    # Loop over new_arr until reaching a missing value
    for i in range(len(new_arr)):
        if new_arr[i] == None:
            return i
    return len(new_arr)


# Driver code:
arr = [3, 4, -1, 1]
result = missing_int(arr)
print(result)

arr = [1, 2, 0]
result = missing_int(arr)
print(result)

arr = [2,1,5,6,4,3,8]
result = missing_int(arr)
print(result)