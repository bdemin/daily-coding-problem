# Given the root to a binary tree, implement serialize(root), which serializes the tree
# into a string, and deserialize(s), which deserializes the string back into the tree.


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root, output = []):
    if root == None:
        output.append(None)
        return None

    output.append(root.val)
    serialize(root.left)
    serialize(root.right)

    output = ' '.join(str(x) for x in output)

    return output


def deserialize(input_str):
    input_list = input_str.split(' ')
    return str2tree(input_list)


def str2tree(_input):
    if len(_input) != 0:
        val = _input.pop(0)
        if val != 'None':
            node = Node(val)
            node.left = str2tree(_input)
            node.right = str2tree(_input)
        else:
            node = Node(None)
    return node


# Test driver:
node = Node('root', Node('left', Node('left.left')), Node('right'))
test_string = serialize(node)
print(test_string)
test_tree = deserialize(test_string)
print(test_tree)
assert deserialize(serialize(node)).left.left.val == 'left.left'