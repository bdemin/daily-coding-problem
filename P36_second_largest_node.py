# Given the root to a binary search tree, find the second largest node in the tree.


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def go_right(node):
    parent = None
    while node.right:
        parent = node
        node = node.right
    return node, parent

def find_second_largest(root):
    # Second largest value in a BST is always the root of the largest element
    if root.left and not root.right:
         largest, = go_right(root.left)
    else:
        _, largest = go_right(root.right)

    return largest.val
    

node = Node(8, Node(3), Node(10, None, Node(14, None, Node(20))))
result = find_second_largest(node)
print(result)