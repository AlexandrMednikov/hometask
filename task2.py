mylist = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([i for i in mylist if mylist.index(i) > 0 and i > mylist[mylist.index(i)-1]])
