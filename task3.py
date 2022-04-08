month = int(input("Введите число месяца:"))
yearlist = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль",
            "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
yeardict = {(i+1): yearlist[i] for i in range(len(yearlist))}

print(f"Решение с помощью списка: {yearlist[month-1]}")
print(f"Решение с помощью словаря: {yeardict[month]}")
