class Road:
    def __init__(self, name, length, width):
        self.__length = length
        self.__width = width
        self.name = name

    def weigth_coverage(self, coverage=25, thickness=5):
        return self.__length*self.__width*coverage*thickness

myroad = Road("RoadtoRome", 100000, 12)
print(f"Покрытие {myroad.name} составит {myroad.weigth_coverage(30)} кг")
