class ListNode:
    class Node:
        def __init__(self, data, link):
            self.data = data
            self.link = link
    
    def __init__(self):
        self.Ahead = None; self.Asize = 0
        self.Bhead = None; self.Bsize = 0
        self.Chead = None; self.Csize = 0

    def Asize(self):
        return self.Asize
    def Bsize(self):
        return self.Bsize
    def Csize(self):
        return self.Csize

    def Ais_empty(self):
        return self.Asize == 0
    def Bis_empty(self):
        return self.Bsize == 0
    def Cis_empty(self):
        return self.Csize == 0

    def A_insert(self, data):
        if self.Ais_empty():
            self.Ahead = self.Node(data, None)
        else:
            self.Ahead = self.Node(data, self.Ahead)
        self.Asize += 1

    def B_insert(self, data):
        if self.Bis_empty():
            self.Bhead = self.Node(data, None)
        else:
            self.Bhead = self.Node(data, self.Bhead)
        self.Bsize += 1

    def combine(self, data):
        if self.Cis_empty():
            self.Chead = self.Node(data, None)
        else:
            self.Chead = self.Node(data, self.Chead)
        self.Csize += 1

    def sorted(self):
        print("정렬 중...")
        a = self.Ahead; b = self.Bhead
        while a != None or b != None:
            if a.data > b.data:
                self.combine(a.data)
                a = a.link
            elif a.data < b.data:
                self.combine(b.data)
                b = b.link
            else:
                self.combine(a.data)
                self.combine(b.data)
                a = a.link
                b = b.link

    def print_Alist(self):
        print("A 연결리스트")
        a = self.Ahead
        while a:
            if a.link != None:
                print(a.data, "->", end=" ")
            else:
                print(a.data)
            a = a.link

    def print_Blist(self):
        print("B 연결리스트")
        b = self.Bhead
        while b:
            if b.link != None:
                print(b.data, "->", end=" ")
            else:
                print(b.data)
            b = b.link

    def print_merge(self):
        print("정렬되어 합병된 연결리스트")
        c = self.Chead
        while c:
            if c.link != None:
                print(c.data, "->", end=" ")
            else:
                print(c.data)
            c = c.link


s = ListNode()
s.A_insert(1)
s.A_insert(6)
s.A_insert(8)
s.print_Alist()

s.B_insert(1)
s.B_insert(7)
s.B_insert(9)
s.print_Blist()

s.sorted()
s.print_merge()

