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

def test_search():
    node = tree.Node(100)
    tree.insert(root=node, key=302)
    assert tree.search_values(node, 100) == node

def test_find_min():
    node = tree.Node(50)
    tree.insert(node, 11)
    tree.insert(node, 30)
    tree.insert(node, 51)
    tree.insert(node, 4)
    tree.insert(node, 1)
    assert tree.find_min(node) == node.left.left.left

def test_find_max():
    node = tree.Node(50)
    tree.insert(node, 11)
    tree.insert(node, 30)
    tree.insert(node, 51)
    tree.insert(node, 4)
    tree.insert(node, 1)
    assert tree.find_max(node).val == 51

def test_leaf_delete():
    node = tree.Node(4)
    tree.insert(node, 5)
    tree.delete_node(node, 5)
    assert node.right == None

def test_one_child_delete():
    node = tree.Node(40)
    tree.insert(node, 50)
    tree.insert(node, 60)
    tree.delete_node(node, 50)
    assert node.right.val == 60

def test_two_children_delete():
    node = tree.Node(500)
    tree.insert(node, 501)
    tree.insert(node,499)
    tree.delete_node(node, 500)
    assert node.val == 501 and node.left.val == 499