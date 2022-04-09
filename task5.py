myask = []
mylist = []
while True:
    myask = input("Введите числа через пробел.Если решите остановить цикл введите '!' через пробел :").split(" ")
    if myask[-1] == "!":
        myask.pop()
        mylist += [int(i) for i in myask]
        print(f"Вы остановили цикл. Оставшаяся сумма = {sum(mylist)}")
        break
    mylist += [int(i) for i in myask]
    print(sum(mylist))
