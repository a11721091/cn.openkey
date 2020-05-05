import os
def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num-1, num * product)


L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = (x for x in L1 if isinstance(x,str))


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


