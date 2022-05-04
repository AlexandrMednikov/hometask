class WareHouse:
    """
    clear_both - сокращает поставки в одну данную
    Очень хотелось бы получить обратную связь по поводу результата строчки 103 и 109.
    Почемуто пишет что свободная площадь разная однако данные по полощади должны были совпадать.
    Cтрочка 106 107 и 114 подтверждают что новый созданый обьект занимает столько же места сколько в сумме
    те два из которых он был создан.
    """
    defolt_lenght = 8700
    defolt_width = 7800
    defolt_height = 500
    defolt_area = defolt_width * defolt_height * defolt_lenght
    free_area = defolt_area
    adress = "Abrakadabra.st"
    owner = "OOO'Kum'"
    _listofgoods = []

    @staticmethod
    def content(lst=_listofgoods):
        print("\nСклад Содержит")
        for i in lst:
            print(f"Оборудование '{i.mark}' в количестве {i.quantity} штук")
        print(f"Свободная площадь - {warehouse.free_area} см.кв\n")

    def accept(self, lst=_listofgoods):
        if self in lst:
            print("Товар уже добавлен.")
        elif WareHouse.free_area>0:
            WareHouse.free_area -= self.area
            lst.append(self)
        else:
            print("Не получится добавить товар.\nСклад заполнен!")

    def issue(self, lst=_listofgoods):
        if self in lst:
            WareHouse.free_area -= self.area
            lst.remove(self)
        else:
            print("Товар на складе не обнаружен")


    def clear_both(lst=_listofgoods):
        search = set([i for i in [i.mark for i in lst] if [i.mark for i in lst].count(i)>1])
        needquantity = 0
        for i in search:
            for it in lst:
                if it.mark == i:
                    needquantity += it.quantity
                    tp = type(it)
                    warehouse.issue(it)
            warehouse.accept(tp(i, needquantity))
            needquantity = 0


class OfficeEq:
    storage_location = "warehouse"
    owner = "OOO'Kum'"

    def __init__(self, mark, quantity, lenght, width, height):
        self.mark = mark
        self.quantity = quantity
        self.lenght = lenght
        self.width = width
        self.height = height
        self.sum_lenght = lenght * quantity
        self.sum_width = width * quantity
        self.sum_height = height * quantity
        self.area = self.width * self.height * self.lenght * self.quantity

    def content(self):
        print(f"Марка:{self.mark}\nКоличество:{self.quantity}\nДлина:{self.lenght}\nШирина:{self.width}")
        print(f"Высота:{self.height}\nЗанимаемый рзмер:{self.area}")


class Printer(OfficeEq):
    def __init__(self, mark, quantity, lenght=48, width=28, height=50):
        super().__init__(mark, quantity, lenght, width, height)

class Xerox(OfficeEq):
    def __init__(self, mark, quantity, lenght, width, height=110):
        super().__init__(mark, quantity, lenght, width, height)

class CoolerBottles(OfficeEq):
    def __init__(self, mark, quantity, lenght=25, width=25, height=48, volume=19):
        super().__init__(mark, quantity, lenght, width, height)
        self.volume = volume


Colma_batch_1 = Printer("Colma", 30)
Zerr_batch_1 = Xerox("Zerr", 30, 100, 50, 150)
Vodica_batch_1 = CoolerBottles("Vodica", 100)
Rodnichok_batch_1 = CoolerBottles("Rodnichok", 50)
Vodica_batch_2 = CoolerBottles("Vodica", 200)
warehouse = WareHouse

warehouse.accept(Vodica_batch_1)
warehouse.accept(Zerr_batch_1)
warehouse.accept(Colma_batch_1)
warehouse.accept(Vodica_batch_2)
warehouse.content()
print(warehouse.free_area)
print(warehouse._listofgoods)
print(warehouse._listofgoods[0].mark)
warehouse.accept(Colma_batch_1)
warehouse.issue(Colma_batch_1)
print(warehouse._listofgoods)
warehouse.content()
Vodica_batch_1.content()
Vodica_batch_2.content()
warehouse.clear_both()
# Теперь только однин обект является атрибутом соответсвуещего класса и имеет общее количество обектов
# и занимеммой площади
warehouse.content()
print(warehouse._listofgoods)
(warehouse._listofgoods)[1].content()