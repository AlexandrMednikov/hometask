class Myerr(Exception):
    pass


myask = []
mylist = []
test = {}

while True:
    myask = input("Введите числа через пробел.Если решите остановить цикл введите '!' через пробел :").split(
    " ")
    if myask[-1] == "!":
        mylist += [i for i in myask if i.isdigit()]
        test = set(myask) - set(mylist)
        print(mylist)
        if test:
            raise Myerr("Вы ввели не только числа")
        break
    mylist += [i for i in myask if i.isdigit()]
    test = set(myask)-set(mylist)
    print(mylist)
    try:
        if test:
            raise Myerr("Вы ввeли не только числа")
    except Myerr:
        print("Вы ввeли не только числа")


