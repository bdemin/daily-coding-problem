# Given the root to a binary tree, implement serialize(root), which serializes the tree
# into a string, and deserialize(s), which deserializes the string back into the tree.


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def serialize(self, root, output = []):
        if root == None:
            output.append(None)
            return None

        output.append(root.val)
        self.serialize(root.left)
        self.serialize(root.right)
        return output


def deserialize(_input):
    if _input == None:
        return None
    node = Node(_input[0])
    _input.pop(0)
    node.left = deserialize(_input)
    node.right = deserialize(_input)


# Test driver:
node = Node('root', Node('left', Node('left.left')), Node('right'))
test = node.serialize(node)
deserialize(test)
# assert deserialize(serialize(node)).left.left.val == 'left.left'