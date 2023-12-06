import random

class CircularQ:
    def __init__(self, MAX_QSIZE = 10):
        self.MAX_QSIZE = MAX_QSIZE
        self.front = 0
        self.rear = 0
        self.queue = [None] * MAX_QSIZE
        
    def is_empty(self):
        return self.front == self.rear
    def is_full(self):
        return self.front == (self.rear + 1) % self.MAX_QSIZE  
        
    def enqueue(self, data):
        if self.is_full():
            raise FullError("포화상태")
        else:
            self.rear = (self.rear+1)%self.MAX_QSIZE
            self.queue[self.rear] = data
            
    def dequeue(self):
        if self.is_empty():
            raise EmptyError("공백상태")
        else:
            self.front = (self.front+1) % self.MAX_QSIZE
            return self.queue[self.front]

    def print_Queue(self):
        out = []
        if self.front < self.rear:
            out = self.queue[self.front+1:self.rear+1]
        else:
            out = self.queue[self.front+1:self.MAX_QSIZE] + self.queue[0:self.rear+1]
        print("[front=%d, rear=%d] ==>"%(self.front, self.rear), out)

    def buffer(self, data):
        if data % 5 == 0:
            self.enqueue(data)
            self.print_Queue()
            
        if data % 10 == 0:
            self.dequeue()
            self.print_Queue()

class EmptyError(Exception):
    pass
class FullError(Exception):
    pass
            
q = CircularQ()
for i in range(1, 101):
    n = random.randint(1,101)
    print("%d번째 난수의 값: %d"%(i, n))
    q.buffer(n)

