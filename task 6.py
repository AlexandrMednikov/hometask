import re
with open('fortask6.txt', 'r', encoding='utf-8') as f:
    fr = f.read()
    fr = fr.split("\n")
    mydict = {}
    for i in fr:
        word = "".join(re.findall(r"[А-Я].+:", i))
        value = (sum([int(i) for i in (re.findall(r"\d+", i))]))
        mydict[word]=value
    print(mydict)