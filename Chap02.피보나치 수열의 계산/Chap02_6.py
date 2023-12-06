import sys
import time
start = time.time()
count = 0

def recursion_fibo(n):
    global count
    count +=1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursion_fibo(n-1) + recursion_fibo(n-2)


sys.setrecursionlimit(10000)
print('35의 피보나치 수열의 값: ', recursion_fibo(4))
print('재귀호출 횟수: ', count)
print('time: ', time.time() - start)

