import sys
import time
start = time.time()
count = 0

def iteration_fibo(n):
    a = 0; b =1; result=0; global count
    for i in range(1, n):
        result = a + b
        a = b
        b = result
        count += 1    
    return result

sys.setrecursionlimit(10000)
print('35의 피보나치 수열의 값: ', iteration_fibo(35))
print('반복 횟수: ', count)
print('time: ', time.time() - start)

