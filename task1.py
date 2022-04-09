def div(a, b):
    """
    :param a:делимое
    :param b:делитель
    :return: возвращает a/b
    """

    try:
        if a % b == 0:
            return a//b
        else:
            return a/b
    except ZeroDivisionError:
        print("На ноль делить нельзя")


x = int(input("Введите что делить: "))
y = int(input("Введите на что делить: "))
print(div(x, y))
