# Given an array of integers, return a new array such that each
# element at index i of the new array is the product of all the
# numbers in the original array except the one at i.


def arr_mul(arr, mul, skip_ind):
    # Help function that gets an array and multiplies each value by mul, except the value at skip_ind
    for i in range(len(arr)):
        if i != skip_ind:
            result = arr[i] * mul
            arr[i] = result
    return arr


def product(arr):
    output = [1] * len(arr)
    for i, num in enumerate(arr):
        output = arr_mul(output, num, i)
    print(output)


# Test driver:
arr = [1,2,3,4,5]
product(arr)

arr = [3,2,1]
product(arr)


