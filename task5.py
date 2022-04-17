import random
dig = " ".join([str(random.randint(1, 100)) for i in range(20)])
with open("fortask5", "w", encoding="utf-8") as f:
    f.write(dig)
with open("fortask5", "r", encoding="utf-8") as f:
    print(sum([int(i) for i in f.read().split(" ")]))