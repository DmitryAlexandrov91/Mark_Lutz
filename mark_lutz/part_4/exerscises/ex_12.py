from functools import reduce
from math import factorial


def recursion_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursion_factorial(n - 1)


def reduce_factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


def cycle_factorial(n):
    if n == 0:
        return 0
    res = 1
    for x in range(1, n + 1):
        res *= x
    return res


def math_factorial(n):
    return factorial(n)
