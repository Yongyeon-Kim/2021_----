class BinaryTree:
    class TreeNode:
        def __init__(self, data, left, right):
            self.data = data
            self.left = left
            self.right = right
            
    def __init__(self):
        self.count = 0

    def search(self, n):
        if n != None:
            if n.left:
                self.search(n.left)
                if n.left == None or n.right == None:
                    self.count += 1
            if n.right:
                self.search(n.right)
                if n.left == None or n.right == None:
                    self.count += 1
        return(self.count)

t = BinaryTree()
n8 = t.TreeNode(27, None, None)
n7 = t.TreeNode(9, None, None)
n6 = t.TreeNode(31, n8, None)
n5 = t.TreeNode(12, n7, None)
n4 = t.TreeNode(3, None, None)
n3 = t.TreeNode(26, None, n6)
n2 = t.TreeNode(7, n4, n5)
n1 = t.TreeNode(18, n2, n3)

root = n1
print("자식이 하나만 있는 노드의 개수: ",t.search(root))


