from walks.inorder_walk import inorder_walk
from core_classes.node import node
from walks.postorder_walk import postorder_walk
from walks.preorder_walk import preorder_walk


def create_tree_demo():
    print("===> started creating tree demo")
    root = node()
    root.insert(value=30)
    root.insert(value=15)
    root.insert(value=60)
    root.insert(value=80)
    root.insert(value=0)
    print("===> finished creating tree demo\n")
    return root


if __name__ == '__main__':
    tree = create_tree_demo()

    print("--------------------------------")
    print("Traversing tree INORDER")  # traverse in sorted numeric order
    tree.walk(walk_type=inorder_walk().walk)

    print("--------------------------------")
    print("Traversing tree POSTORDER")  # traverse with left right then root
    tree.walk(walk_type=postorder_walk().walk)

    print("--------------------------------")
    print("Traversing tree preorder")  # traverse with root then left right
    tree.walk(walk_type=preorder_walk().walk)
