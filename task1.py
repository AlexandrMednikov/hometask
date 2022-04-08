mylist = [False, 1, 0, "text", [1, 2], {3, 8}, ("text", "againtext"), {"mykey": "myvalue"}]
for i in mylist:
    print(f"{i} принадлежит {type(i)}")
