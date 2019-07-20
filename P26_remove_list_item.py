# Given a singly linked list and an integer k, remove the kth last element from
# the list. k is guaranteed to be smaller than the length of the list.

# The list is very long, so making more than one pass is prohibitively expensive.

# Do this in constant space and in one pass.


class Node(object):
    def __init__(self, data=None, next_n=None):
        self.data = data
        self.next = next_n

    def __str__(self):
        data = []
        while self:
            data.append(str(self.data))
            self = self.next
        return ' -> '.join(data)

    def add_node(self, node):
        self.next = node
        return node

    def remove_kth_last(self, k):
        slowP = fastP = self # initialize two "pointers" to linked list head
        for _ in range(k):
            fastP = fastP.next

        if hasattr(fastP, 'next'):
            while fastP.next:
                slowP = slowP.next
                fastP = fastP.next
            slowP.next = slowP.next.next
        else: # Remove head node
            self = self.next
        return self


# Driver code
linked = current = Node(0)
listLength = 5
for i in range(1, listLength):
    new_node = Node(i)
    current = current.add_node(new_node)

print(linked)
k = 4
linked = linked.remove_kth_last(k)
print(linked)

k = 1
linked = linked.remove_kth_last(k)
print(linked)

k = 2
linked = linked.remove_kth_last(k)
print(linked)

k = 2
linked = linked.remove_kth_last(k)
print(linked)
