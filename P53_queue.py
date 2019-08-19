# Implement a queue using two stacks.
# Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods:
# enqueue, which inserts an element into the queue, and dequeue, which removes it.


class Queue(object):
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []


    def enqueue(self, new_item):
        if len(self.stack_1) == 0:
            self.stack_1.append(new_item)
        else:
            # Empty the first stack and fill up the second
            while len(self.stack_1) > 0:
                self.stack_2.append(self.stack_1.pop())

            # Add the new item
            self.stack_1.append(new_item)

            # Empty the second stack and fill up the first
            while len(self.stack_2) > 0:
                self.stack_1.append(self.stack_2.pop())
            
            
    def dequeue(self):
        if self.stack_1:
            return self.stack_1.pop()
        return None


# Driver code
queue = Queue()
for i in range(10):
    queue.enqueue(i)
for i in range(10):
    print(queue.dequeue())
