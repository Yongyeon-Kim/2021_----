class ListNode:
    class Node:
        def __init__(self, data, number, link):
            self.data = data
            self.number = number
            self.link = link
    
    def __init__(self):
        self.head = None
        self.Even_head = None
        self.Odd_head = None
        self.size = 0
        
    def size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def insert(self, data, number):
        if self.is_empty():
            self.head = self.Node(data, number, None)
        else:
            self.head = self.Node(data, number, self.head)
        self.size += 1
        
    def Eveninsert(self, data):
        if self.is_empty():
            self.Even_head = self.Node(data, None, None)
        else:
            self.Even_head = self.Node(data, None, self.Even_head)
        self.size += 1
            
    def Oddinsert(self, data):
        if self.is_empty():
            self.Odd_head = self.Node(data, None, None)
        else:
            self.Odd_head = self.Node(data, None, self.Odd_head)
        self.size +=1
        
    def Split(self):
        print("리스트 분리 중...")
        p = self.head
        while p:
            if p.number %2 == 0:
                self.Eveninsert(p.data)
            else:
                self.Oddinsert(p.data)
            p = p.link
        
    def print_list(self):
        p = self.head
        while True:
            if p.link != None:
                print(p.data, "->", end=" ")
            else:
                print(p.data)
                break
            p = p.link
            
    def print_Evenlist(self):
        e = self.Even_head
        print("짝수 노드: ", end=" ")
        while e:
            if e.link != None:
                print(e.data, "  ", end=" ")
            else:
                print(e.data)
            e = e.link
            
    def print_Oddlist(self):
        o = self.Odd_head
        print("홀수 노드: ", end=" ")
        while o:
            if o.link != None:
                print(o.data, "  ", end=" ")
            else:
                print(o.data)
            o = o.link

s = ListNode()
s.insert("용연", 1)
s.insert("대곤", 2)
s.insert("찬영", 3)
s.insert("성민", 4)
s.insert("희정", 5)
s.print_list()
s.Split()
s.print_Evenlist()
s.print_Oddlist()

