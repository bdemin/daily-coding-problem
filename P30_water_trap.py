# You are given an array of non-negative integers that represents a two-dimensional
# elevation map where each element is unit-width wall and the integer is the height.
# Suppose it will rain and all spots between two walls get filled up.

# Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

# For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

# Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in
# the second, and 3 in the fourth index (we cannot hold 5 since it would run off to
# the left), so we can trap 8 units of water.



# This method satisfies O(N) time and O(1) space but there is an additional
# list which uses O(n) space. This list is not needed to compute the
# solution and is used to get a better representation of the output.
def water_trap(elevationMap):
    print(elevationMap)
    returnList = [0] * len(elevationMap) # Stores how much water can be added in each cell
    frontIndex = len(elevationMap) - 2
    backIndex = 1
    
    backMax = elevationMap[0]
    frontMax = elevationMap[-1]
    maxFillVolume = min(backMax, frontMax) # Max volume of water between front and back bounds

    forwardFlag = True # Direction switch flag
    while frontIndex >= backIndex:
        if forwardFlag:
            # Going forward
            if maxFillVolume >= elevationMap[backIndex]:
                # Can be filled!
                fill = maxFillVolume - elevationMap[backIndex]
                returnList[backIndex] = fill
            else:
                # Set new bound and switch direction
                backMax = elevationMap[backIndex]
                returnList[backIndex] = 0
                maxFillVolume = min(backMax, frontMax)
                forwardFlag = not forwardFlag # Switch direction
            backIndex += 1

        else:
            # Going backwards
            if maxFillVolume > elevationMap[frontIndex]:
                # Can be filled!
                fill = maxFillVolume - elevationMap[frontIndex]
                returnList[frontIndex] = fill
            else:
                # Set new bound and switch direction!
                frontMax = elevationMap[frontIndex]
                returnList[frontIndex] = 0
                maxFillVolume = min(backMax, frontMax)
                forwardFlag = not forwardFlag # Switch direction
            frontIndex -= 1
    print(returnList,'\n')


# Driver code
elevationMap = [2, 1, 2]
water_trap(elevationMap)

elevationMap = [3, 0, 1, 3, 0, 5]
water_trap(elevationMap)

elevationMap = [3,7,2,6,2,3]
water_trap(elevationMap)

elevationMap = [9,4,3,2,4,7,5,7,1,9]
water_trap(elevationMap)

elevationMap = [3,1,9,1,3]
water_trap(elevationMap)
