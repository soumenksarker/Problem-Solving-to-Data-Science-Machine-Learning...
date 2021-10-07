class Binary_Tree:
    def __init__(self,root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left_child(self,Node):
        if self.left_child == None:
            self.left_child = Node
        else:
            t = Binary_Tree(Node)
            t.left_child = self.left_child
            self.left_child = t
    def insert_right_child(self,Node):
        if self.right_child == None:
            self.right_child = Node
        else:
            t = Binary_Tree(Node)
            t.right_child = self.left_child
            self.right_child = t
            
    def get_right_child(self):
        return self.right_child
    
    def get_left_child(self):
        return self.left_child
    
    def set_root_value(self,obj):
        self.key = obj

    def get_root_value(self):
        return self.key
    
