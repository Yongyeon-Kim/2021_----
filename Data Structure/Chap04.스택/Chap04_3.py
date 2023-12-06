class Stack:
    def __init__(self,MAX_STACK_SIZE=100):
        self.stack = []
        self.MAX_STACK_SIZE = MAX_STACK_SIZE
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size >= self.MAX_STACK_SIZE

    def push(self, data):
        if self.is_full():
            raise FullError("스택 포화 에러")
        else:
            print("PUSH: 스택의 맨 위에 '%d' 를 삽입! " % data)
            self.stack.append(data)
            self.size += 1

    def pop(self):
        if self.is_empty():
            raise EmptyError("스택 공백 에러")
        else:
            print("POP: 스택의 맨 위에 data를 제거! ")
            self.stack.pop()
            self.size -= 1

    def peek(self):
        if self.is_empty():
            raise EmptyError("스택 공백 에러")
        else:
            print("PEEK: 스택의 맨 위에 data를 반환! ", end=" ")
            return self.stack[-1]

    def print_stack(self):
        print("현재 스택 상태: ",self.stack)

class FullError(Exception):
    pass
class EmptyError(Exception):
    pass

s1 = Stack()
#s1.pop()
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)
s1.pop()
s1.print_stack()
print(s1.peek())

