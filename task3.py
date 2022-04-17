"""
Генератор фаила для задания. Вместо фамилий у сотрудников персональный код.
"""
# import random
# f = open("fortask3.txt", "w", encoding="utf-8")
# for i in range(20):
#     f.write(f"Код:{i+random.randint(1, 100)} "+str(random.randint(10000, 30000))+"\n")
# f.close()

with open("fortask3.txt", "r", encoding="utf-8") as f:
    rf = f.read().split("\n")
    data = [i.split(" ") for i in rf]
    if data[-1] == ['']:
        data.pop()
    under20 = [i for i in data if int(i[-1]) < 20000]
    print(f"Сотрудники с зарплатой меньше 20000:{', '.join([i[0] for i in under20])}")
    print(f"Средняя зарплата {sum([int(i[-1]) for i in data])/len(data)}")
