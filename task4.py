"""
 Плохо понял задумку автора задания. Мы пишем програму связаную с производством машин или видерегистратором
а может даже ПО для Автомобилей. От этого бы зависило использование __init__.
 Также я унаследовал для WorkCar show_speed чтобы код не повторялся. Мне кажется правельнее было писать это
методом класса Car и вносить куча булевых условий и прочего, но я решил для дз ограничится таким вот
не красивым приёом. Т.к на даный момент вынужден экономить свое время.
 Не смотря на то что Пичарм ругается что надо делать методы статичными, я подумал что лучше всетаки оставлю так.
"""


class Car:
    def __init__(self, name):
        self.name = name
    speed = 100
    color = "White"
    is_police = False

    def go(self):
        print("Машина остановилась")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула на {direction}")

    def show_spedd(self):
        print(self.speed)


class TownCar(Car):
    color = "Grey"
    speed = 90

    def show_spedd(self, constant=60):
        if self.speed > constant:
            print("Вы превысили значение скорости")
        else:
            print(self.speed)


class SportCar(Car):
    color = "Red"
    speed = 200


class WorkCar(Car, TownCar):
    speed = 50
    color = "Grey"

    def show_speed(self):
        return super(TownCar).show_spedd(40)


class Policecar(Car):
    color = "Blue"
    speed = 189
    is_police = True
