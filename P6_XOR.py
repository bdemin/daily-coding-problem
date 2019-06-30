# An XOR linked list is a more memory efficient doubly linked list.
# Instead of each node holding next and prev fields, it holds a field named both,
# which is an XOR of the next node and the previous node.
# Implement an XOR linked list; it has an add(element) which adds the
# element to the end, and a get(index) which returns the node at index.

# If using a language that has no pointers (such as Python),
# you can assume you have access to get_pointer and
# dereference_pointer functions that converts between nodes and memory addresses


# Note: not sure how to test the code since Python doesn't use
# pointers the same way as other languages.

class Node():
    def __init__(self, value = None, xor = None):
        self.value = value
        self.xor = xor


def get_pointer(node):
    pass


def dereference_pointer(node):
    pass


class XORlist():
    def __init__(self):
        self.head = Node()
        self.tail = Node()


    def add(self, element):
        new = Node()
        if self.head.value == None:
            self.head = self.tail = new.val
        else:
            new.xor = self.tail.xor ^ get_pointer(new)
            self.tail = new


    def get(self, index):
        temp_head = self.head
        temp_prev = 0
        if index >= 0:
            for i in range(index):
                temp_pnt = get_pointer(temp_head)
                temp_head = dereference_pointer(temp_head.both ^ temp_prev)
                temp_head = temp_pnt
                if temp_head == self.tail:
                    return None
            return temp_head