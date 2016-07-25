class Tree():
    def __init__(self, cargo, left=None, right=None):
        self.cargo=cargo
        self.right=right
        self.left=left
        
    def __str__(self):
        return str(self.cargo)
        
def total(tree):
    if (tree)==None: return 0
        
    return total(tree.left)+total(tree.right)+tree.cargo
        
def print_tree(tree):
    if tree == None: return
    print tree.cargo,
    print_tree(tree.left)
    print_tree(tree.right)
    
def print_tree_postorder(tree):
    if tree == None: return
    print_tree_postorder(tree.left)
    print_tree_postorder(tree.right)
    print tree.cargo,
    
def print_tree_inorder(tree):
    if tree == None: return
    print_tree_inorder(tree.left)
    print tree.cargo,
    print_tree_inorder(tree.right)

    
def get_number(token_list):
    if get_token(token_list, '('):
        x = get_sum(token_list)         # get the subexpression
        get_token(token_list, ')')      # remove the closing parenthesis
        return x
    else:
        x = token_list[0]
        if type(x) != type(0): return None
        token_list[0:1] = []
        return Tree (x, None, None)
    
def get_token(token_list, expected):
    if token_list[0] == expected:
        del token_list[0]
        return True
    else:
        return False
        
def get_product(token_list):
    a = get_number(token_list)
    if get_token(token_list, '*'):
        b = get_product(token_list)       # this line changed
        return Tree ('*', a, b)
    else:
        return a
        
def get_sum(token_list):
    a = get_product(token_list)
    if get_token(token_list, '+'):
        b = get_sum(token_list)
        return Tree ('+', a, b)
    else:
        return a
        
def make_token_list(expr):
    import string
    expr=raw_input('Enter expression:   ')
    ll=[]
    for e in expr:
        ll.append(e)
    ll.append('end')
    return ll