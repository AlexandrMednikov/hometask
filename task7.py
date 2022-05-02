from math import factorial


def f(n):
    for i in range(1, n+1):
        yield factorial(i)


for i in f(4):
    print(i)
