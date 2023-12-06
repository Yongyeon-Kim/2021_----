class HeapTree:
    def __init__(self):
        self.heap = [None]

    def insert_max_heap(self, item):
        self.heap.append(item)
        print("삽입 연산: ",self.heap)
        
        index = len(self.heap) - 1
    
        while index != 1:
            Parent = index//2
            print("삽입 노드: ", self.heap[index], "인덱스 번호: ",index, end=" |#| ")
            print("부모 노드: ", self.heap[Parent], "인덱스 번호: ", Parent)

            if self.heap[Parent] < self.heap[index]:
                print("")
                self.heap[Parent], self.heap[index] = self.heap[index], self.heap[Parent]
                index = Parent
            else:
                break
            print("변환 후: ", self.heap)
        print("="*65)

    def delete_max_heap(self):
        if len(self.heap) < 1:
            print("공백 상태!")
        else:
            self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
            self.heap.pop(-1)
            self.maxHeap_sorted(1)
        print("삭제 연산 후: ", self.heap)

    def maxHeap_sorted(self, key):
        parent = key
        left = key * 2; right = key*2+1

        if left < len(self.heap) and self.heap[left] > self.heap[parent]:
            parent = left
        elif right < len(self.heap) and self.heap[right] > self.heap[parent]:
            parent = right

        if parent != key:
            self.heap[key], self.heap[parent] = self.heap[parent], self.heap[key]
            self.maxHeap_sorted(parent)

            



Heap = HeapTree()
Heap.insert_max_heap(9)
Heap.insert_max_heap(7)
Heap.insert_max_heap(6)
Heap.insert_max_heap(5)
Heap.insert_max_heap(2)
Heap.insert_max_heap(2)
Heap.insert_max_heap(4)
Heap.insert_max_heap(3)
Heap.insert_max_heap(1)
Heap.insert_max_heap(3)
Heap.delete_max_heap()