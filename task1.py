def i_sum(a, b):
    sumarray = []
    for i in a:
        sumarray.append(i + b[a.index(i)])
    return sumarray


class Matrix:
    def __init__(self, array):
        self.array = array

    def __str__(self):
        myarray = []
        for i in self.array:
            myarray.extend(str(i)+" ")
            myarray.extend("\n")
        return "".join(myarray)

    def __add__(self, other):
        newarray = []
        for i in range(len(self.array)):
            newarray.append(i_sum(self.array[i], other.array[i]))
        return newarray


x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = [[3, 0, 1], [6, 5, 2], [2, 8, 4]]
x = Matrix(x)
y = Matrix(y)
xy = Matrix(x+y)

print(str(x))
print(str(xy))
