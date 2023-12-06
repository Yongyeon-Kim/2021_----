def Ackermann(m,n):
    if m==0:
        return n+1
    elif m==1:
        return n+2
    elif m==2:
        return 2*n + 3
    elif m==3:
        return 2**(n+3) -3
    else:
        val = 2
        for i in range(0, n+3):
            val **= 2
        return val-3
print(Ackermann(4,1))

