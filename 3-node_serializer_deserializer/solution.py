# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
# and deserialize(s), which deserializes the string back into the tree.
#
# For example, given the following Node class
#
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# The following test should pass:
#
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):

    if not node:
        return "x"                      # Place marker to represent end of path

    serial = "{}-".format(node.val)
    serial += serialize(node.left)      # Recursive call to serialize left to right
    serial += serialize(node.right)

    return serial

def deserialize(serial):
    print serial.split('-')

if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    # assert deserialize(serialize(node)).left.left.val == 'left.left'

    print "serialized node: {}".format(serialize(node))
