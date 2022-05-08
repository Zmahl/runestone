from msilib.schema import Binary


class BinaryTree:

    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None
    
    def insert_left(self, new_node):
    
        #If empty create a new binary tree and connect it to the root
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)

        #If there is an existing child, then push down the existing child make the new child
        #the closest child
        else:
            new_child = BinaryTree(new_node)
            new_child.left_child = self.left_child
            self.left_child = new_child
    
    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        
        else:
            new_child = BinaryTree(new_node)
            new_child.right_child = self.right_child
            self.right_child = new_child


root_a = BinaryTree("a")

root_a.insert_left("d")
root_a.insert_left("b")

root_a.insert