rating = [7, 5, 3, 2, 2, 1]
x = int(input("Введите число:"))

for i in rating:
    if x > i:
        rating.insert(rating.index(i), x)
        break
if x <= rating[-1]:
    rating.append(x)
print(rating)
