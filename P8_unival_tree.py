# A unival tree (which stands for "universal value") is a tree where all
# nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees:

#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_unival(node):
    if not node:
        return True
    elif node.left and node.left.val != node.val:
        return False
    elif node.right and node.right.val != node.val:
        return False
    elif is_unival(node.left) and is_unival(node.right):
        return True
    return False


def count_unival(node):
    if not node:
        return 0
    count = count_unival(node.left) + count_unival(node.right)
    if is_unival(node):
        count += 1
    return count


# Driver code:
node = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
result = count_unival(node)
print(result)