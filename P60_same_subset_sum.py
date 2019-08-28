# Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

# For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

# Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add up to the same sum.


def find_subsets_with_same_sum(multiset):
    multiset = sorted(multiset) # Merge sort - O(nlogn)
    
    left_index = 1
    left_sum = multiset[0]
    right_index = len(multiset) - 2
    right_sum = multiset[-1]

    while left_index <= right_index:
        # Add values from both sides while keeping the sums balanced.
        # If the sums are equal we found the correct subsets.
        if left_sum > right_sum:
            right_sum += multiset[right_index]
            right_index -= 1
        else:
            left_sum += multiset[left_index]
            left_index += 1
        
    if left_sum == right_sum:
        return True
    return False
        

# Driver code
multiset = [15, 5, 20, 10, 35, 15, 10]
print(find_subsets_with_same_sum(multiset))

multiset = [15, 5, 20, 10, 35]
print(find_subsets_with_same_sum(multiset))
