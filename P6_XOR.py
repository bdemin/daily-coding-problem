# An XOR linked list is a more memory efficient doubly linked list.
# Instead of each node holding next and prev fields, it holds a field named both,
# which is an XOR of the next node and the previous node.
# Implement an XOR linked list; it has an add(element) which adds the
# element to the end, and a get(index) which returns the node at index.

# If using a language that has no pointers (such as Python),
# you can assume you have access to get_pointer and
# dereference_pointer functions that converts between nodes and memory addresses


class Node():
    def __init__(self, value = None, both = None):
        self.value = value
        self.both = both


class XORlist():
    def __init__(self):
        head = Node()
        tail = Node()


    def add(self, element):
        pass


    def get(self, index):
        pass


# def xor(a,b):
#     if bool(a) != bool(b):
#         return True
    # return False