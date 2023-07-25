def fib2(n):
    x = []
    a, b = 0, 1
    while a < n:
        x.append(a)
        a = b
        b = a + b
    return x


fib2(100)
