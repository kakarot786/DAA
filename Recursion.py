def fact(n):
    if n == 0:
        return 1
    else:
        return fact(n-1) * n


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

