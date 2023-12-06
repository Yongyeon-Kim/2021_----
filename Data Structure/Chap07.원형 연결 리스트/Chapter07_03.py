class CircularList:
    class Node:
        def __init__(self, data, link):
            self.data = data
            self.lnk = link
            
    def __init__(self):
        self.head = None
        self.size = 0
    
    def Is_empty(self):
        return self.size == 0
    
    def Insert(self, data):
        print("원형 연결 리스트 앞에 '%d' 삽입" % data)
        p = self.Node(data, None)
        if self.Is_empty():
            self.head = p
            p.link = self.head
        else:
            p.link = self.head.link
            self.head.link = p
        self.size += 1
        
    def Search(self, data):
        print("탐색할 data는 '%d' 입니다." % data)
        count = 1
        if self.Is_empty():
            raise EmptyError("탐색할 원형 연결 리스트 없음!")
        else:
            first = self.head.link
            x = self.Node(data, None)
            y = first
            while y.link != first:
                if x.data == y.data:
                    print("탐색한 데이터 '%d'는 '%d' 번째" % (data, count))
                    break
                else:
                    y = y.link
                    count += 1
                    
    def Print_list(self):
        print("현재 원형 리스트 상태:", end=" ")
        if self.Is_empty():
            print("공백상태")
        else:
            first = self.head.link
            p = first
            while p.link != first:
                print(p.data, "->", end=" ")
                p = p.link
            print(p.data)
                        
class EmptyError(Exception):
    pass

c = CircularList()
c.Insert(10)
c.Insert(20)
c.Insert(30)
c.Insert(40)
c.Print_list()

c.Search(30)


