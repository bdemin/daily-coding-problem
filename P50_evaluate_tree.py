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
    if sign == '+':
        return num1 + num2
    if sign == '-':
        return num1 - num2
    if sign == '*':
        return num1 * num2
    if sign == '/':
        return num1 / num2

        
def eval_tree(root):
    pass

# Driver code
root = Node('*', Node('+', 3, 2), Node('+', 4, 5))