# Given two singly linked lists that intersect at some point,
# find the intersecting node. The lists are non-cyclical.

# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10,
# return the node with value 8.

# In this example, assume nodes with the same value are the exact same node objects.

# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

class Linked():
    def __init__(self, val = None, _next = None):
        self.val = val
        self.next = _next


def find_intersection(L1, L2):
    if not L1.next and L2.next:
        return 'Error! No intersection.'
    # elif L1.val != L2.val:
        
    elif L1.val == L2.val:
        return L1.val

    return find_intersection(L1.next, L2)
    return find_intersection(L1, L2.next)


# Driver code
A = Linked(3, Linked(7, Linked(8, Linked(10))))
B = Linked(99, Linked(1, Linked(8, Linked(10))))
result = find_intersection(A, B)
print(result)