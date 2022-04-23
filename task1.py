import time


class TrafficLight:
    _color = ["red", "yellow", "green"]

    def running(self):
        while True:
            print(self._color[0])
            time.sleep(7)
            print(self._color[1])
            time.sleep(2)
            print(self._color[2])
            time.sleep(4)


mystreet = TrafficLight()
mystreet.running()
