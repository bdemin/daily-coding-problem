# Given an array of strictly the characters 'R', 'G', and 'B',
# segregate the values of the array so that all the Rs come left,
# the Gs come second, and the Bs come last. You can only swap
# elements of the array.

# Do this in linear time and in-place.

# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'],
# it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].


def swap(array, i, j):
    # Helper function that swaps between array[i] and array[j]
    array[i], array[j] = array[j], array[i]

def rgb(array):
    b_count = 0 # Calculate number of B's
    for i in range(len(array)):
        if array[i] == 'B':
            b_count += 1

    left = 0
    for i in range(len(array)):
        # All R's to the front
        if array[i] == 'R':
            swap(array, i, left)
            left += 1

    right = len(array) - 1
    for i in range(len(array)):
        # All B's to the end
        while array[left] != 'B' and left < right:  # Find first B
            left += 1

        while array[right] == 'B' and left < right:  # Find first non B on the right side
            right -= 1

        swap(array, left, right)

    return array


# Driver code
array = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
result = rgb(array)
print(result)

array = ['B', 'G', 'G', 'R', 'B', 'R', 'G']
result = rgb(array)
print(result)

array = ['R', 'G', 'B']
result = rgb(array)
print(result)

array = ['B', 'B', 'B', 'R', 'G', 'B']
result = rgb(array)
print(result)
