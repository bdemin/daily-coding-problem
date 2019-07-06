# There exists a staircase with N steps, and you can climb up
# either 1 or 2 steps at a time. Given N, write a function that
# returns the number of unique ways you can climb the staircase.
# The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:

# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time,
# you could climb any number from a set of positive integers X?
# For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.


def staircase(N):
    if N <= 2:
        return N
    else:
        return staircase(N-2) + staircase(N-1)
    

# Driver code:
for num_stairs in range(5):
    print(f'For {num_stairs} stairs, there are {staircase(num_stairs)} ways')


# Solve for a set of possible steps:
def staircase_x(N, X):
    if N < 0:
        return 0
    elif N == 0:
        return 1
    else:
        result = 0
        for x in X:
            result += staircase_x(N-x, X)
        return result


# Driver code:
num_stairs = 5
X = [1, 3, 5]
print(staircase_x(num_stairs, X))