from itertools import cycle, count
for i in count(1):
    if i == 10:
        break
    print(i)
step = 0
for i in cycle(["Красный", "Оранджевый", "Зеленый", "Голубой", "Синий", "Фиолетовый"]):
    if step == 10:
        break
    print(i)
    step += 1
