def print_tree_inorder_par(tree):
    if tree == None: return
    print '(',
    print_tree_inorder_par(tree.left)
    #print ')',
    print tree.cargo,
    print_tree_inorder_par(tree.right)
    print ')',