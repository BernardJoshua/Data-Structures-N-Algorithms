class Node:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

class BinaryTree:
    def __init__(self):
        self.root = None 

    def insertNode(self, data):

        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return
        
        curr = self.root 

        while True:
            if data < curr.data:
                if curr.left is None:
                    curr.left = new_node
                    return 
                curr = curr.left 
            else:
                if curr.right is None:
                    curr.right = new_node 
                    return 
                curr = curr.right
