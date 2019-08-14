# Implement an LRU (Least Recently Used) cache.
# It should be able to be initialized with a cache size n,
# and contain the following methods:

# set(key, value): sets key to value. If there are already
# n items in the cache and we are adding a new item,
# then it should also remove the least recently used item.

# get(key): gets the value at key. If no such key exists, return null.
# Each operation should run in O(1) time.


class Node:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRU(object):
    def __init__(self, n):
        self.data = dict()
        self.limit = n

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head


    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    
    def add_node(self, node):
        prev_node = self.tail.prev
        node.next = self.tail
        node.prev = prev_node
        prev_node.next = node
        self.tail.prev = node


    def _set(self, key, value):
        if key in self.data:
            used_node = self.data[key]
            self.remove_node(used_node)

        used_node = Node(key, value)
        self.add_node(used_node)
        self.data[key] = used_node

        if len(self.data) > self.limit:
            node_for_deletion = self.head.next
            self.remove_node(node_for_deletion)
            del self.data[node_for_deletion.key]


    def _get(self, key):
        if key in self.data:
            used_node = self.data[key]
            # Remove and add node so that it will appear first after being used
            self.remove_node(used_node)
            self.add_node(used_node)
            return self.data[key]

        return None

        
# Driver code
limit = 3
lru = LRU(limit)
lru._set('a', 1)
lru._set('b', 2)
lru._set('c', 3)
lru._set('d', 4)
lru._set('e', 5)
lru._set('c', 1)
lru._set('b', 10)
lru._get('a')
lru._get('c')
