# There is an N by M matrix of zeroes. Given N and M, write a function
# to count the number of ways of starting at the top-left corner and
# getting to the bottom-right corner. You can only move right or down.

# For example, given a 2 by 2 matrix, you should return 2, since there
# are two ways to get to the bottom-right:

# Right, then down
# Down, then right
# Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.


def find_num_ways(m,n):
    if m == 0 or n == 0:
        return 0
    elif m == 1 or n == 1:
        return 1
    else:
        return find_num_ways(m-1,n) + find_num_ways(m,n-1)
        

# driver code
m, n = 2,2
print(find_num_ways(m,n))

m, n = 5,5
print(find_num_ways(m,n))
