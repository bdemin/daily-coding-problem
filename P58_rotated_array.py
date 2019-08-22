# An sorted array of integers was rotated an unknown number of times.

# Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

# For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

# You can assume all the integers in the array are unique.


def rec(arr, start, end, key):
    # Modified Binary Search
    if start > end:
        return None
      
    mid = (start + end) // 2
    if arr[mid] == key:
        return mid
  
    elif arr[start] <= arr[mid]:
        if key >= arr[start] and key <= arr[mid]:
            return rec(arr, start, mid-1, key)
        return rec(arr, mid+1, end, key)

    elif key >= arr[mid] and key <= arr[end]:
        return rec(arr, mid+1, end, key)
    return rec(arr, start, mid-1, key)


def find_element(arr, element):
    # Driving function
    index = rec(arr, 0, len(arr) - 1, element)
    return index


# Driver code
arr = [13, 18, 25, 2, 8, 10]
element = 8
result = find_element(arr, element)
print(result)
