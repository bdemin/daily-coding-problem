# A builder is looking to build a row of N houses that can be of K different colors.
# He has a goal of minimizing cost while ensuring that no two neighboring houses are
# of the same color.

# Given an N by K matrix where the nth row and kth column represents the cost to
# build the nth house with kth color, return the minimum cost which achieves this goal.


def minimum_cost(housePrices):
    minCost = [0] * len(housePrices[0])
    for house in housePrices:
        temp = [0] * len(house)

        for index in range(len(house)):
            temp[index] = house[index] + min(minCost[:index] + minCost[index+1:])

        minCost = temp
    return min(minCost)


# Driver code
housePrices = [[1,2,3], [4,2,1], [1,1,5]]
result = minimum_cost(housePrices)
print(result)

housePrices = [[1,2,15,3,20], [20,1,4,2,1], [8,6,1,1,5]]
result = minimum_cost(housePrices)
print(result)