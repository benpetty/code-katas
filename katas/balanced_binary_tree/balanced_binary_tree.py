"""

https://www.interviewcake.com/question/python3/balanced-binary-tree

Write a function to see if a binary tree is "superbalanced" (a new tree
property we just made up).

A tree is "superbalanced" if the difference between the depths of any two leaf
nodes is no greater than one.

Here's a sample binary tree node class:

  class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right
"""


def is_balanced(tree_root):
    """

    Complexity:
        O(n) time and O(n) space.

    """

    # A tree with no nodes is superbalanced, since there are no leaves!
    if tree_root is None:
        return True

    # We short-circuit as soon as we find more than 2
    depths = []

    # We'll treat this list as a stack that will store tuples of (node, depth)
    nodes_stack = []
    nodes_stack.append((tree_root, 0))

    while len(nodes_stack):

        # Pop a node and its depth from the top of our stack
        node, depth = nodes_stack.pop()

        # Case: we found a leaf
        if (not node.left) and (not node.right):

            # We only care if it's a new depth
            if depth not in depths:
                depths.append(depth)

                # Two ways we might now have an unbalanced tree:
                #   1) more than 2 different leaf depths
                #   2) 2 leaf depths that are more than 1 apart
                if (len(depths) > 2) or (
                    len(depths) == 2 and abs(depths[0] - depths[1]) > 1
                ):
                    return False

        # Case: this isn't a leaf - keep stepping down
        else:
            if node.left:
                nodes_stack.append((node.left, depth + 1))
            if node.right:
                nodes_stack.append((node.right, depth + 1))

    return True
