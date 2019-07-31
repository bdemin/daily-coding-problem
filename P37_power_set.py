# The power set of a set is the set of all its subsets.
# Write a function that, given a set, generates its power set.

# For example, given the set {1, 2, 3}, it should return
# {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

# You may also use a list or array to represent a set.


def dec2binary(n, num_len):
    # Helper function that takes a decimal number and converts it to binary
    binary_num = [0] * n
    i = 0
    while (n > 0):  
        binary_num[i] = n % 2
        n = int(n / 2)
        i += 1
  
    # Reverse and add zeros so len(num) = num_len 
    output_num = [0] * num_len
    for j in range(i - 1, -1, -1):
        output_num[j] = binary_num[j]
    return output_num

def find_power_set(arr):
    # Create all possible binary sets
    binary_sets = []
    for i in range(2**len(arr)):
        binary_sets.append(dec2binary(i, len(arr)))

    # Multiply every possible binary set with the input array
    power_set = []
    for binary_set in binary_sets:
        new_set = []
        for i in range(len(binary_set)):
            num = arr[i] * binary_set[i]
            if num:
                new_set.append(num)
        power_set.append(new_set)
    return power_set


# Driver code
arr = [1,2,3]
result = find_power_set(arr)
print(result)
