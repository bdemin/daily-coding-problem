# Given an integer k and a string s, find the length of the
# longest substring that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest
# substring with k distinct characters is "bcb".


# Brute force
def longest_substring(k, s):
    memory = []
    maxMemory = []
    maxLength = 0
    maxLengthLast = 0
    temp_k = k
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[j] not in memory:
                memory.append(s[j])
                k -= 1
            if k < 0:
                break
            maxLength += 1
        if maxLength > maxLengthLast:
            maxLengthLast = maxLength
            maxMemory = s[i:j]
        maxLength = 0
        k = temp_k
        memory = []
    return maxMemory


# Driver code
s = 'abcba'
k = 2
result = longest_substring(k, s)
print(result)

s = 'aaabcdsf'
k = 4
result = longest_substring(k, s)
print(result)