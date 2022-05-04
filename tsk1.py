"""
В задании просили валидавать число месяц год я валидовал только число и месяц т.к понравилась идея с зодиаками,
но всеравно параметром функции checkzodiac оставил полную дату
"""


def eq(el):
    return int(el) if el[0] != 0 else int(el[1:])


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def elementdate(cls, date):
        return [eq(i) for i in date.split("-")]

    @staticmethod
    def checkzodiac(date):
        datint = [eq(i) for i in date.split("-")][:2]
        zodiac = {"Козерог": (22, 20), "Водолей": (21, 18), "Рыбы": (19, 20), "Овен": (21, 20), "Телец": (21, 20),
                  "Близнецы": (21, 21), "Рак": (22, 22), "Лев": (23, 22), "Дева": (23, 23), "Весы": (24, 23),
                  "Скропион": (24, 22), "Стрелец": (23, 21)}
        k, v = list(zodiac.keys()), list(zodiac.values())
        result = datint[1]-1 if datint[0] <= v[datint[1]-1][0] else datint[1]
        return k[result] if result != 0 else k[12]


item = Date("2-2-2001")
print(Date.checkzodiac("01-11-2001"))
print(Date.elementdate("01-11-2001"))
