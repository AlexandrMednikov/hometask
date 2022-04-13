from functools import reduce
print(reduce(lambda x, y: x * y, list(range(100, 1001, 2))))
