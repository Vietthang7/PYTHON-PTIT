from datetime import datetime
from math import *


class Cyclist:
    def __init__(self, name, place, time):
        self.name = name
        self.place = place
        self.id = "".join(i[0] for i in place.split() + name.split())
        h, m = map(int, time.split(":"))
        self.v = 120 / (h + m / 60 - 6)

    def __str__(self):
        return f"{self.id} {self.name} {self.place} {round(self.v)} Km/h"


if __name__ == "__main__":
    t = int(input())
    a = []
    while t > 0:
        t -= 1
        a.append(Cyclist(input(), input(), input()))
    a.sort(key=lambda x: (-x.v))
    for x in a:
        print(x)
