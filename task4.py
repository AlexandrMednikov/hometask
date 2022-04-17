digeng = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
digru = ['Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть', 'Семь', 'Восемь', 'Девять', 'Десять']
f1 = open("fortask4", "r", encoding="utf-8")
f2 = open("fortask4.1", "w", encoding="utf-8")
rf1 = f1.read()
rf1 = rf1.split("\n")
rf1copy = []
base = 0
for i in rf1:
    for ii in i.split(" "):
        if ii in digeng:
            if base:
                rf1copy[-1]+=('\n')
                rf1copy.append(digru[digeng.index(ii)]+" ")
            else:
                rf1copy.append(digru[digeng.index(ii)]+" ")
                base += 1
        else:
            rf1copy.append(ii+" ")
rf2 = f2.write("".join(rf1copy))
f1.close()
f2.close()

