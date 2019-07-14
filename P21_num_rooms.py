# Given an array of time intervals (start, end) for classroom
# lectures (possibly overlapping), find the minimum number of
# rooms required.

# For example, given [(30, 75), (0, 50), (60, 150)], you
# should return 2.


# Brute force
def is_between(num, pair):
    if num >= pair[0] and num <= pair[1]:
        return True
    return False


def find_num_rooms(arr):
    numRooms = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if is_between(arr[i][0], arr[j]):
                numRooms += 1
            if is_between(arr[i][1], arr[j]):
                numRooms += 1
    return numRooms


# Driver code
arr = [(30, 75), (0, 50), (60, 150)]
result = find_num_rooms(arr)
print(result)
arr = [(0, 50), (40, 50), (30, 50), (60, 70)]
result = find_num_rooms(arr)
print(result)

