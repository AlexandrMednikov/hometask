youlist = list(input("Введите элементы вашего списка без пробелов,запятых и других знаков разграничения:"))
list1 = [i for i in youlist if (youlist.index(i)+1) % 2 != 0]
list2 = [i for i in youlist if (youlist.index(i)+1) % 2 == 0]
list3 = []
x = len(list2) if len(list2) > len(list1) else len(list1)

try:
    for i in range(x):
        list3.append(list2[i])
        list3.append(list1[i])
except IndexError:
    list3.append(youlist[-1])


print(list3)
