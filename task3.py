class Worker:
    def __init__(self, name, surname, position, wage, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {"wage": wage, "bonus": bonus}


class Possition(Worker):
    def __init__(self, name, surname, position, wage, bonus=0):
        super().__init__(name, surname, position, wage, bonus)
        self.__income = {"wage": wage, "bonus": bonus}

    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_total_income(self):
        return self.__income["wage"]+self.__income["bonus"]


vladgorev = Possition("Владислав", "Горев", "Зам.Директора", 178000, 56400)

vladgorev.get_full_name()
print(f"Доход:{vladgorev.get_total_income()}")
