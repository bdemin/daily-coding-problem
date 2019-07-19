# Implement locking in a binary tree. A binary tree node can be locked or unlocked
# only if all of its descendants or ancestors are not locked.

# Design a binary tree node class with the following methods:

# is_locked, which returns whether the node is locked
# lock, which attempts to lock the node. If it cannot be locked, then it should
# return false. Otherwise, it should lock it and return true.
# unlock, which unlocks the node. If it cannot be unlocked, then it should
# return false. Otherwise, it should unlock it and return true.
# You may augment the node to add parent pointers or any other property you
# would like. You may assume the class is used in a single-threaded program,
# so there is no need for actual locks or mutexes. Each method should run
# in O(h), where h is the height of the tree


def check_children(children):
    # Helper function to check lock status of all the node's children
    if len(children) == 0:
        return True
    elif len(children) == 1:
        if not children[0].locked:
            check_children(children[0].children)
    elif len(children) == 2:
        if not children[0].locked:
            check_children(children[0].children)
        if not children[1].locked:
            check_children(children[1].children)
    return True
    
def check_parents(node):
    # Helper function to check lock status of all the parents
    if not node.parent: # no parents
        return True
    elif not node.parent.locked: # parent is not locked
            return check_parents(node.parent)
    return False

class Node(object):
    def __init__(self, val = None, parent = None):
        self.val = val
        self.parent = parent
        self.locked = False

        self.children = []
        if self.parent:
            # If node is created with a parent, add it as a child of the parent
            self.add_child()

    def add_child(self):
        self.parent.children.append(self)

    def is_locked(self):
        return self.locked
    
    def lock(self):
        if check_children(self.children):
            if check_parents(self):
                self.locked = True
                return True
        return False

    def unlock(self):
        if check_children(self.children):
            if check_parents(self):
                self.locked = False
                return True
        return False


# Driver code
a = Node("a", None)
b = Node("b", a)
c = Node("c", a)
d = Node("d", b)
e = Node("e", b)
f = Node("f", c)
g = Node("g", c)

assert b.lock()
assert b.is_locked()
assert c.lock()
assert b.unlock()
assert not b.is_locked()
assert d.lock()

assert not g.lock()
assert c.unlock()
assert g.lock()

assert f.lock()
assert e.lock()