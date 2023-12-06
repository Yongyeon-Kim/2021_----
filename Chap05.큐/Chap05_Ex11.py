class Deque:
    def __init__(self, MAX_QSIZE = 10):
        self.MAX_QSIZE = MAX_QSIZE
        self.front = 0
        self.rear = 0
        self.queue = [None] * MAX_QSIZE

    def is_empty(self):
        return self.front == self.rear
    def is_full(self):
        return self.front == (self.rear + 1) % self.MAX_QSIZE

    def add_rear(self, data):
        if self.is_full():
            raise FullError("포화 상태")
        else:
            self.rear = (self.rear+1)% self.MAX_QSIZE
            self.queue[self.rear] = data

    def add_front(self, data):
        if self.is_full():
            raise FullError("포화 상태")
        else:
            self.queue[self.front] = data
            self.front = self.front - 1

        if self.front < 0:
            self.front = self.MAX_QSIZE - 1

    def delete_rear(self):
        if self.is_empty():
            raise EmptyError("공백 상태")
        else:
            data = self.queue[self.rear]
            self.rear = self.rear - 1
        
        if self.rear < 0:
            self.rear = self.MAX_QSIZE - 1
        return data
    
    def delete_front(self):
        if self.is_empty():
            raise EmptyError("공백 상태")
        else:
            self.front = (self.front+1) % self.MAX_QSIZE
            return self.queue[self.front]

    def get_rear(self):
        if self.is_empty():
            raise EmptyError("공백 상태")
        return self.queue[self.rear]

    def get_front(self):
        if self.is_empty():
            raise EmptyError("공백 상태")
        return self.queue[(self.front+1)%self.MAX_QSIZE]

    def print_Queue(self):
        out = []
        if self.front < self.rear:
            out = self.queue[self.front+1:self.rear+1]
        else:
            out = self.queue[self.front+1:self.MAX_QSIZE] + self.queue[0:self.rear+1]
        print("덱 상태: [front=%d, rear=%d] ==>"%(self.front, self.rear), out)

    def palindrome(self):
        while self.front < self.rear:
            a = self.queue[(self.front+1)%self.MAX_QSIZE]
            b = self.queue[self.rear]
            print("비교 위치: [front=%d, rear=%d]" % (self.front+1, self.rear), end=" || ")
            print("해당 위치 문자: ", a ,"<=>", b)

            if a != b:
                raise NotPalindrome("회문이 아닙니다.")
            else:
                self.front += 1
                self.rear -= 1
        print("회문입니다.")
            
class EmptyError(Exception):
    pass
class FullError(Exception):
    pass
class NotPalindrome(Exception):
    pass

dq = Deque()    
dq.add_rear("c")
dq.add_rear("i")
dq.add_rear("c")
dq.add_rear("i")
dq.add_rear("c")
dq.print_Queue()
dq.palindrome()

