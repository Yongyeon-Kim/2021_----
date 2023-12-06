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

    def C_insert(self, data):
        if self.Cis_empty():
            self.Chead = self.Node(data, None)
        else:
            self.Chead = self.Node(data, self.Chead)
        self.Csize += 1

    def alternate(self):
        print("alternate함수 작동...")
        a = self.Ahead
        b = self.Bhead
        while a != None or b != None:
            if a != None:
                self.C_insert(a.data)
                a = a.link
            if b != None:
                self.C_insert(b.data)
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

    def print_Clist(self):
        print("C 연결리스트")
        c = self.Chead
        while c:
            if c.link != None:
                print(c.data, "->", end=" ")
            else:
                print(c.data)
            c = c.link

s = ListNode()
s.A_insert("a1")
s.A_insert("a2")
s.A_insert("a3")
s.A_insert("a4")
s.print_Alist()

s.B_insert("b1")
s.B_insert("b2")
s.B_insert("b3")
s.B_insert("b4")
s.print_Blist()

s.alternate()

s.print_Clist()
    



        