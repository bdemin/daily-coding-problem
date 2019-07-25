# Given two singly linked lists that intersect at some point,
# find the intersecting node. The lists are non-cyclical.

# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10,
# return the node with value 8.

# In this example, assume nodes with the same value are the exact same node objects.

# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

class Node():
    def __init__(self, val = None, _next = None):
        self.val = val
        self.next = _next

    def __str__(self):
        return str(self.val)


def get_length(node):
    length = 0
    while node:
        length += 1
        node = node.next
    return length

def find_intersection(L1, L2):
    length1 = get_length(L1)
    length2 = get_length(L2)
    min_length = min(length1, length2)

    for i in range(length1 - min_length):
        L1 = L1.next
    for i in range(length2 - min_length):
        L2 = L2.next

    for i in range(min_length):
        if L1.val == L2.val:
            return L1
        L1 = L1.next
        L2 = L2.next

    return None


# Driver code
A = Node(3, Node(7, Node(8, Node(10))))
B = Node(99, Node(1, Node(8, Node(10))))
result = find_intersection(A, B)
print(result)
