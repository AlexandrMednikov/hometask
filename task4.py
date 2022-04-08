
words = input("Введите ваши слова через пробел:")
wordslisttest = words.split(" ")
wordslist = []
for i in wordslisttest:
    if len(i) <= 10:
        wordslist.append(i)
    else:
        wordslist.append(i[:10])

for i, val in enumerate(wordslist, start=1):
    print(f"{i} {val}")
