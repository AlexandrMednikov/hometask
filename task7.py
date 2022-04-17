import re
import json
f = open("fortask7.txt", "r", encoding="utf-8")
f2 = open("fortask7.1", "w", encoding="utf-8")
fr = f.read()
fr = fr.split("\n")
mydict = {}
income = []
for i in fr:
    word = "".join((re.findall(r"[А-Я][а-я]+-?[А-Я]?[а-я]+", i)))
    value = [int(i) for i in (re.findall(r"\d+", i))]
    value = value[0]-value[1]
    income.append(value)
    mydict[word] = value
result = [mydict, dict(average_profit=(sum(income)/len(income)))]
json.dump(result, f2)
f.close()
f2.close()
