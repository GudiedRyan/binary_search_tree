class Node:

    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val > key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def print_values(root):
    if root:
        print_values(root.left)
        print(root.val)
        print_values(root.right)