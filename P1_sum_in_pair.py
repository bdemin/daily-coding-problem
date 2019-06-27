def sum_in_pair(arr, k, step):
    #Find a pair of numbers in arr that sums up to the value k
    if len(arr) < 2:
        return False
    elif step >= len(arr):
        return sum_in_pair(arr[1:], k, 0)
    elif arr[0] + arr[step] == k:
        print(arr[0], ' + ', arr[step], ' = ', k, '\n')
    sum_in_pair(arr, k, step+1)


#test driver:
arr = [10, 15, 3, 7]
k = 17
sum_in_pair(arr, k, 0)


def better_sum_in_pair(arr, k):
    seen = {}
    for num in arr:
        target = k - num
        if target not in seen:
            seen[num] = num
        else:
            print(num, target, '\n')

#test driver:
better_sum_in_pair(arr, k)