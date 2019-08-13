# Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

# Given the root to such a tree, write a function to evaluate it.

# For example, given the following tree:

#     *
#    / \
#   +    +
#  / \  / \
# 3  2  4  5
# You should return 45, as it is (3 + 2) * (4 + 5).


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def evaluate(num1, num2, sign):
    # Perform operation on num1 and num2
    if sign == '+':
        return num1 + num2
    if sign == '-':
        return num1 - num2
    if sign == '*':
        return num1 * num2
    if sign == '/':
        return num1 / num2


def eval_tree(node):
    # Check if node is a number
    if not type(node.left.val) == str:
        return evaluate(node.left.val, node.right.val, node.val)
    
    # Node is an operation
    num1 = eval_tree(node.left)
    num2 = eval_tree(node.right)
    return evaluate(num1, num2, node.val)
    

# Driver code
root = Node('*', Node('+', Node(3), Node(2)), Node('+', Node(4), Node(5)))
result = eval_tree(root)
print(result)
