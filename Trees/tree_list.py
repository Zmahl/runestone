def make_branch(root):
    return [root, [], []]

def insert_left(root, new_child):
    old_child = root.pop(1)

    if len(old_child) > 1:
        #This will insert an empty branch in the tree along with a 
        root.insert(1, [new_child, old_child, []])
    
    else:
        root.insert(1, [new_child, [], []])
    
    return root

def insert_right(root, new_child):
    old_child = root.pop(2)

    if len(old_child) > 1:
        root.insert(2, [new_child, old_child, []])
    
    else:
        root.insert(2, [new_child, [], []])

