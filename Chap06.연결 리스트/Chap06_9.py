class ListNode:
    class Node:
        def __init__(self, coef, expon, link):
            self.coef = coef
            self.expon = expon
            self.link = link
    
    def __init__(self):
        self.Ahead = None; self.Asize = 0
        self.Bhead = None; self.Bsize = 0
        self.Chead = None; self.Csize = 0
    
    def Ais_empty(self):
        return self.Asize == 0
    def Bis_empty(self):
        return self.Bsize == 0
    def Cis_empty(self):
        return self.Csize == 0
    
    def A_insert(self, coef, expon):
        if self.Ais_empty():
            self.Ahead = self.Node(coef, expon, None)
        else:
            self.Ahead = self.Node(coef, expon, self.Ahead)
        self.Asize += 1
    
    def B_insert(self, coef, expon):
        if self.Bis_empty():
            self.Bhead = self.Node(coef, expon, None)
        else:
            self.Bhead = self.Node(coef, expon, self.Bhead)
        self.Bsize += 1
        
    def C_insert(self, coef, expon):
        if self.Cis_empty():
            self.Chead = self.Node(coef, expon, None)
        else:
            self.Chead = self.Node(coef, expon, self.Chead)
        self.Csize += 1
        
    def poly_add(self):
        print("다항식 계산중...")
        a = self.Ahead; b = self.Bhead; self.sum = 0
        while a != None or b != None:
            if a.expon == b.expon:
                self.sum = a.coef + b.coef
                self.C_insert(self.sum, a.expon)
                a = a.link; b = b.link
            elif a.expon > b.expon:
                self.C_insert(a.coef, a.expon)
                a = a.link
            elif a.expon < b.expon:
                self.C_insert(b.coef, b.expon)
                b = b.link
       

    def print_Clist(self):
        print("C 연결리스트")
        c = self.Chead
        while c:
            if c.link != None:
                print(c.coef,"^",c.expon,"+", end=" ")
            else:
                print(c.coef,"^",c.expon)
            c = c.link

s = ListNode()
s.A_insert(3,12)
s.A_insert(5,5)
s.A_insert(1,2)

s.B_insert(3,12)
s.B_insert(4,5)
s.B_insert(2,2)

s.poly_add()
s.print_Clist()


