class TreeNode:
    def __init__(self, data = None):
        self.parent = None #Tree Node
        self.data = data
        self.childern = [] # Tree Node
        self.child_number = len(self.childern)
        self.child_iter = -1
    
    def add_child(self, child):
        child.parent = self
        self.childern.append(child)
        self.child_number = len(self.childern)
    
    
    def find_last_child(root):
        last_node = root
        while last_node.childern:
            for child in last_node.childern:
                







