# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.


def decode_ways(message):
    if len(message) <= 1:
        return 1
    if int(message[0]) == 0:
        return 0
    if len(message) >= 2:
        if int(message[0:2]) <= 26:
            return decode_ways(message[1:]) + decode_ways(message[2:])
        else:
            return decode_ways(message[1:])


# Test driver:
message = '112345'
result = decode_ways(message)
print(result)