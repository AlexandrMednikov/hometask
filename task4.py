def pw(a, b):
    """

    :param a:число
    :param b:степень
    :return:Возвращает a в степени b.
    """
    if b == 0:
        return 1
    x = 0
    y = 1
    while x <= abs(b)-1:
        x += 1
        y = y*a
    return y if b>0 else 1/y

print(pw(5, -1))