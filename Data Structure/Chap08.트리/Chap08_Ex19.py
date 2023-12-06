class BinaryTree:
    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
    
    def __init__(self):
        self.root = None

    def new_node(self, data):
        self.root = self.insert_node(self.root, data)

    def insert_node(self, node, data):
        if node is None:
            node = self.TreeNode(data)

        if data < node.data:
            node.left = self.insert_node(node.left, data)
        elif data > node.data:
            node.right = self.insert_node(node.right, data)
        return node
                
    def reverse_inorder(self, n):
        if n != None:
            if n.right != None:
                self.reverse_inorder(n.right)
            print(n.data," ",end="")
            if n.left != None:
                self.reverse_inorder(n.left)
    
array = [11, 3, 4, 1, 56, 5, 6, 2, 98, 32, 23]

t = BinaryTree()
for i in array:
    t.new_node(i)

t.reverse_inorder(t.root)



