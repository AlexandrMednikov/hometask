f = open("fortask1.txt", "w", encoding="utf-8")
while True:
    put = input("Введите текст который хотите записать в фаил:")
    if put == "":
        break
    f.writelines([ww for ww in [w+"\n" for w in put.split(" ")] if ww != "\n"])
f.close()
