class Comply:
    def __init__(self, r, c):
        self.r = r
        self.c = c

    def __str__(self):
        if self.c < 0:
            return f"{self.r}{self.c}i"
        else:
            return f"{self.r}+{self.c}i"

    def __add__(self, other):
        return Comply(self.r + other.r, self.c + other.c)

    def __sub__(self, other):
        return Comply(self.r-other.r, self.c-other.c)

    def __mul__(self, other):
        res1 = (self.r*other.r)-(self.c*other.c)
        res2 = (self.r*other.c)-(self.c*other.r)
        return Comply(res1, res2)

    def __truediv__(self, other):
        res1 = ((self.r * other.r) - (self.c * other.c))/(other.r**2 + other.c**2)
        res2 = (self.r * other.c) - (self.c * other.r)/(other.r**2 + other.c**2)
        return Comply(res1, res2)


a = Comply(4, 2)
b = Comply(7, 8)
print(a)
print(a+b)
print(a/b)
print(a*b)
print(a-b)