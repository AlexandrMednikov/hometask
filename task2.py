with open("fortask2", "r", encoding="utf-8") as f:
    print("В фаиле "+str(len(f.readlines()))+" строк")
with open("fortask2", "r", encoding="utf-8") as f:
    for el in f.read().split("\n"):
        lenel = len(el.split(" "))
        print(f"В строке '{el}' колчество слов равно {lenel}")

