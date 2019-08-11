# Given pre-order and in-order traversals of a binary tree,
# write a function to reconstruct the tree.

# For example, given the following preorder traversal:

# [a, b, d, e, c, f, g]

# And the following inorder traversal:

# [d, b, e, a, f, c, g]

# You should return the following tree:

#     a
#    / \
#   b   c
#  / \ / \
# d  e f  g

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def reconstruct_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_val = preorder[0]
    if len(preorder) == 1:
        return Node(root_val)

    root = Node(root_val)
    
    for i, val in enumerate(inorder):
        if val == root_val:
            root.left = reconstruct_tree(preorder[1:i+1], inorder[:i])
            root.right = reconstruct_tree(preorder[i+1:], inorder[i+1:])
    return root


# Driver code
preorder = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
inorder = ['d', 'b', 'e', 'a', 'f', 'c', 'g']
tree = reconstruct_tree(preorder, inorder)

assert tree.val == 'a'
assert tree.left.val == 'b'
assert tree.left.left.val == 'd'
assert tree.left.right.val == 'e'
assert tree.right.val == 'c'
assert tree.right.left.val == 'f'
assert tree.right.right.val == 'g'
