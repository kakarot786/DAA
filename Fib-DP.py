def fibDP(n):
    a , b = 0 , 1
    if n < 0:
        return -1
    elif n  == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b


print(fibDP(10))