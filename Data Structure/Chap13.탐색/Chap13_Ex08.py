import time

class BinaryTree:
    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
            
    def __init__(self):
        self.list = []
        self.root = None
        
    def new_node(self, data):
        self.root = self.insert_node(self.root, data)
            
    def insert_node(self, node, data):
        if node is None:
            node = self.TreeNode(data)
                
        if data < node.data:                
            if node.left != None:
                self.insert_node(node.left, data)
            else:
                node.left = self.TreeNode(data)
        elif data > node.data:
            if node.right != None:
                self.insert_node(node.right, data)
            else:
                node.right = self.TreeNode(data)
        return node
   
    def inorder(self, n):
        if n != None:
            if n.left != None:
                self.inorder(n.left)
            self.list.append(n.data)  
            if n.right != None:
                self.inorder(n.right)
        return self.list
    
    def insertion(self, array):
        for i in range(1, len(array)):
            for j in range(i, 0, -1):
                if array[j-1] > array[j]:
                    array[j-1], array[j] = array[j], array[j-1]
        return array

    def heapify(self, list, index, n):
        left = index * 2
        right = index * 2 + 1
        parent = index
        if(left <= n and list[parent] > list[left]):
            parent = left
        if(right <= n and list[parent] > list[right]):
            parent = right
        if parent != index:
            list[index], list[parent] = list[parent], list[index]
            return self.heapify(list, parent, n)

    def heap_sort(self, v):
        n = len(v)
        v = [0] + v

        for i in range(n, 0, -1):
            self.heapify(v, i, n)

        for i in range(n, 0, -1):
            print(v[1], end=', ')
            #print('[{}]'.format(v[1], end=''))
            v[i], v[1] = v[1], v[i]
            self.heapify(v, 1, i-1)

if __name__ == '__main__':
    array = [5,3,4,2,1]
    heap_array = [5,3,4,2,1]

    t = BinaryTree()
    for i in array:
        t.new_node(i)

    inorder_start = time.time()
    print(t.inorder(t.root))
    inorder_end = time.time()
    print("중위 순회 실행시간: ",(inorder_end - inorder_start))

    insertion_start = time.time()
    print(t.insertion(array))
    insertion_end = time.time()
    print("삽입 정렬 실행시간: ", (insertion_end - insertion_start))

    heapsort_start = time.time()
    t.heap_sort(heap_array)
    heapsort_end = time.time()
    print("힙 정렬 실행시간: ", (heapsort_end - heapsort_start))

