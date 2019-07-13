# Given an array of integers and a number k, where
# 1 <= k <= length of the array, compute the maximum
# values of each subarray of length k.

# For example, given array = [10, 5, 2, 7, 8, 7] and
# k = 3, we should get: [10, 7, 8, 8], since:

# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)
# Do this in O(n) time and O(k) space. You can modify
# the input array in-place and you do not need to store
# the results. You can simply print them out as you compute them.


# Brute force
def max_subarrays(arr, k):
    kMax = [0] * (len(arr)-k+1)
    # kCount = 0
    for i in range(len(arr)-k+1):
        for j in range(k):
            if arr[i+j] > kMax[i]:
                kMax[i] = arr[i+j]
    print(kMax)


# Driver code
arr = [10, 5, 2, 7, 8, 7]
k = 3
max_subarrays(arr, k)


# Better solution
def max_subarrays_2(arr, k):
    pass


# Driver code
arr = [10, 5, 2, 7, 8, 7]
k = 3
max_subarrays_2(arr, k)