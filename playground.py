import main as tree



# node = tree.Node(89)
# tree.insert(root=node, key=12)
# tree.insert(root=node, key=11)
# tree.insert(root=node, key=100)
# tree.insert(root=node, key=50)
# tree.print_values(root=node)

node = tree.Node(89)
tree.insert(root=node, key=12)
tree.insert(root=node, key=11)
tree.insert(root=node, key=100)
tree.insert(root=node, key=50)
tree.search_tree(node, 50)