"""
Добавил возможность прибавлять число к клеткам, не дорабатывал с __radd__ и.т.п.
Оператор для целочисленного деления используется - '/'
"""


class Cell:
    def __init__(self, q):
        self.quantity = q

    def __add__(self, other):
        if isinstance(other, int):
            return self.quantity + other
        return self.quantity + other.quantity

    def __sub__(self, other):
        if isinstance(other, int):
            if self.quantity - other == 0:
                raise ValueError("Разница клеток равна нулю")
            else:
                return self.quantity - other
        if self.quantity - other.quantity == 0:
            raise ValueError("Разница клеток равна нулю")
        else:
            return self.quantity - other.quantity

    def __mul__(self, other):
        if isinstance(other, int):
            return self.quantity * other
        return self.quantity * other.quantity

    def __truediv__(self, other):
        if isinstance(other, int):
            return self.quantity // other
        return self.quantity // other.quantity

    def make_order(self, x):
        diapason = self.quantity
        result = []
        while diapason:
            result.append(f"{chr(9633)} " * x + "\n")
            if diapason <= x:
                result.append(f"{chr(9633)} " * diapason)
                return result
            diapason -= x


a = Cell(45)
b = Cell(32)
print(a+b)
print(a*3)
print(b/1)
#print(a-46)
print(a.make_order(5))
for i in b.make_order(4):
    print(i)
