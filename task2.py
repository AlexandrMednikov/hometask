class Clothe:
    def __init__(self, v, h, inwork=False):
        self.v = v
        self.h = h
        self.__status = inwork

    def expenditure_cloth(self):
        pass

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, x):
        if not self.__status == False:
            self.__status = x
        else:
            raise Exception("The object is not being developed")
            self.__status = False

    @status.getter
    def status(self):
        return self.__status


class Coat(Clothe):
    def expenditure_cloth(self):
        return self.v / 6.5 + 0.5


class Suit(Clothe):
    def expenditure_cloth(self):
        return 2 * self.h + 0.3


lv = Suit(80, 190)
gucci = Coat(96, 186, "startwork")
print(lv.expenditure_cloth())
print(gucci.expenditure_cloth())
print(gucci.status)
gucci.status = "done"
print(gucci.status)
lv.status = "startwork"