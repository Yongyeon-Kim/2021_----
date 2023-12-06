import random
import time

start = time.time()
key_size = 500
table_size = 1000

class Linear:
    def __init__(self):
        self.hash_table = [None] * table_size
        self.count = 0

    def hash_function(self, key):
        return key % table_size

    def add(self, key):
        x = self.hash_function(key)
        while self.hash_table[x] != None:
            x = (x+1)%table_size
            self.count += 1
        self.hash_table[x] = key

    def print_table(self):
        for i in range(table_size):
            print('bucket[{}] = {}'.format(i, self.hash_table[i]))
        print("총돌 횟수: ",self.count)
        print("실행시간: ", time.time() - start)
       
D = Linear()
key = [None] * key_size
for i in range(key_size):
    key[i] = random.randint(1, 9999)
for i in range(key_size):
    D.add(key[i])
D.print_table()


