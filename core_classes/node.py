from typing import Callable


class node:
    def __init__(self,
                 node_val: int = None):  # node_val can be many types but consistence (all node's node_val from same type)
        self.node_val = node_val
        self.left = None
        self.right = None

    def insert(self, value) -> None:
        if self.node_val is None:
            print(f"Created a new root node with the value of {value}")
            self.node_val = value
        else:
            if self.node_val > value:
                if self.left is None:
                    self.left = node(value)
                    print(f'added value: {value} to left of {self.node_val}')
                else:
                    self.left.insert(value)
            elif self.node_val < value:
                if self.right is None:
                    self.right = node(value)
                    print(f'added value: {value} to right of {self.node_val}')

                else:
                    self.right.insert(value)
            elif self.node_val == value:
                raise ValueError("Value already inserted!")

    def walk(self, walk_type: Callable = None) -> None:
        walk_type(self)
