class BinaryTree:
    class TreeNode:
        def __init__(self, data, left, right):
            self.data = data
            self.left = left
            self.right = right

    def __init__(self):
        self.size = 0
        
    def calc_dir_size(self, n):
        if n != None:
            if n.left:
                self.calc_dir_size(n.left)
            if n.right:
                self.calc_dir_size(n.right)
            self.size += n.data
            print("디렉토리 용량:",n.data,"이며, ",end="총 용량: ")
            print(self.size)

t = BinaryTree()
n4 = t.TreeNode(500, None, None)
n5 = t.TreeNode(200, None, None)
n3 = t.TreeNode(100, n4, n5)
n2 = t.TreeNode(50, None, None)
n1 = t.TreeNode(0, n2, n3)

root = n1
t.calc_dir_size(root)


