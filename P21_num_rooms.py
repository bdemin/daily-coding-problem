# Given an array of time intervals (start, end) for classroom
# lectures (possibly overlapping), find the minimum number of
# rooms required.

# For example, given [(30, 75), (0, 50), (60, 150)], you
# should return 2.


def better_find_num_rooms(arr):
    sortedStart = sorted([num[0] for num in arr])
    sortedEnd = sorted([num[1] for num in arr])
    
    numRooms = 0
    startedTime = 0
    endedTime = 0
    maxRooms = 0
    while startedTime < len(arr) and endedTime < len(arr):
        if sortedStart[startedTime] < sortedEnd[endedTime]:
            numRooms += 1
            startedTime += 1
        else:
            endedTime += 1
            numRooms -= 1
        maxRooms = max(numRooms, maxRooms)
    return maxRooms


# Driver code
arr = [(30, 75), (0, 50), (60, 150)]
result = better_find_num_rooms(arr)
print(result)
arr = [(0, 50), (40, 50), (30, 50), (60, 70)]
result = better_find_num_rooms(arr)
print(result)