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


def search_values(root:Node, key):
    if root is None or root.val == key:
        return root
    
    elif root.val < key:
        return search_values(root.right, key)
    
    else:
        return search_values(root.left, key)


def find_min(root:Node):
    while root.left != None:
        root = root.left
    return root

def find_max(root:Node):
    while root.right != None:
        root = root.right
    return root
    
def delete_node(root:Node, key):
    if root is None:
        return root
    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = find_min(root.right)
        root.val = temp.val
        root.right = delete_node(root.right, temp.val)
    return root