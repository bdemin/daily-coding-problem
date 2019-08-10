# We can determine how "out of order" an array A is by counting
# the number of inversions it has. Two elements A[i] and A[j]
# form an inversion if A[i] > A[j] but i < j. That is, a smaller
# element appears after a larger element.

# Given an array, count the number of inversions it has.
# Do this faster than O(N^2) time.

# You may assume each element in the array is distinct.

# For example, a sorted list has zero inversions.
# The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3).
# The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.


# The solution consists of Merge Sort algorithm with an additional list
# for counting swaps in the array. Each swap signifies an inversion.
# The inversions are stored as a list to count all the inversions
# from the call stack.
# Original implementation of Merge Sort taken from GeeksforGeeks.
def mergeSort(arr, inversions = []):
    if arr and len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
  
        mergeSort(L) # Sorting the left half
        mergeSort(R) # Sorting the right half
        
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i += 1
            else: 
                arr[k] = R[j] 
                j += 1
                inversions.append(None) # A swap was needed
            k += 1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i += 1
            k += 1
          
        while j < len(R): 
            arr[k] = R[j] 
            j += 1
            k += 1

    return arr, len(inversions) + 1


def count_inversions(arr):
    _, inversions = mergeSort(arr)
    return inversions


# Driver code
arr = [2, 4, 1, 3, 5]
assert count_inversions(arr) == 3

arr = [5, 4, 3, 2, 1]
assert count_inversions(arr) == 10