class Myzeroerr(Exception):
    pass


try:
    print(1/int(input("Введите число: ")))
except ZeroDivisionError:
    print("На ноль делить нельзя!")
except Myzeroerr as err:
    print(err)


