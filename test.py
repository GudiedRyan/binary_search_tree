import main as tree

def test_node():
    node = tree.Node(7)
    assert node.val == 7

def test_insert():
    node = tree.Node(7)
    tree.insert(root=node, key=8)
    assert node.val == 7 and node.right.val == 8

def test_insert_2():
    node = tree.insert(root=None,key=6)
    assert node.val == 6

def test_print():
    node = tree.Node(89)
    tree.insert(root=node, key=12)
    tree.insert(root=node, key=11)
    tree.insert(root=node, key=100)
    tree.insert(root=node, key=50)
    tree.print_values(root=node)
    assert node.right.val == 100