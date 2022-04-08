month = int(input("Введите число месяца:"))
yearlist = ["зима", "зима", "весна", "весна", "весна", "лето", "лето",
            "лето", "осень", "осень", "осень", "зима"]
yeardict = {(i+1): yearlist[i] for i in range(len(yearlist))}

print(f"Решение с помощью списка: {yearlist[month-1]}")
print(f"Решение с помощью словаря: {yeardict[month]}")
