class Stationery:
    title = "eraser"

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    title = "Pen"

    def draw(self):
        print("Запуск отрисовки ручкой")


class Pencil(Stationery):
    title = "penicl"

    def draw(self):
        print("Запуск отрисовки карандашом")


class Handle(Stationery):
    title = "handle"

    def draw(self):
        print("Запуск отрисовки маркером")


A = Pen()
B = Pencil()
C = Handle()
A.draw()
B.draw()
C.draw()
