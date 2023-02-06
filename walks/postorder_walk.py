from walks.walk_interface import walk_interface
from core_classes.node import node


class postorder_walk(walk_interface):
    def __init__(self):
        pass

    def walk(self, root: node):  # walk function for inorder given a binary tree root
        if root is None:
            return
        else:
            self.walk(root.left)
            self.walk(root.right)
            print(f'visited node with value: {root.node_val}')

