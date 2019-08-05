# Implement a stack that has the following methods:

# push(val), which pushes an element onto the stack
# pop(), which pops off and returns the topmost element of the stack.
# If there are no elements in the stack, then it should throw an error or return null.
# max(), which returns the maximum value in the stack currently.
# If there are no elements in the stack, then it should throw an error or return null.
# Each method should run in constant time.

class Node(object):
    def __init__(self, val, prev = None):
        self.val = val
        self.prev = prev


class Stack(object):
    def __init__(self, val = None):
        self.last = Node(val)
        self.max = float('-inf')
        self.last_max = float('-inf')

    def __repr__(self):
        return repr(self.last.val)

    def push(self, val):
        self.last = Node(val, self.last)
        if val > self.max:
            self.last_max = self.max
            self.max = val

    def pop(self):
        if self.last:
            temp = self.last.val
            if temp == self.max:
                self.max = self.last_max
            self.last = self.last.prev
            return temp

    def _max(self):
        return self.max


# Driver code
stack = Stack(5)
stack.push(6)
stack.push(7)

print(stack.pop())
print(stack.pop())

stack.push(8)
stack.push(9)
print(stack.pop())

print(stack._max())

stack.push(100)
stack.push(5)
print(stack._max())
