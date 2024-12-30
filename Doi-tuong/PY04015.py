from math import *


class HoaDon:
    def __init__(self, id, hoTen, dau, cuoi):
        self.id = "KH" + format(id, "02d")
        self.hoTen = hoTen
        self.dau = dau
        self.cuoi = cuoi

    def tongTien(self):
        x = self.cuoi - self.dau
        if x <= 50:
            return round(x * 100 * 102.0 / 100)
        elif 51 <= x <= 100:
            tmp = 50 * 100 + (x - 50) * 150
            return round(tmp * 103.0 / 100)
        elif x > 100:
            tmp = 50 * 100 + 50 * 150 + (x - 100) * 200
            return round(tmp * 105.0 / 100)

    def __str__(self):
        return "{} {} {}".format(self.id, self.hoTen, self.tongTien())


if __name__ == "__main__":
    t = int(input())
    a = []
    for i in range(t):
        hoTen = input()
        dau = int(input())
        cuoi = int(input())
        res = HoaDon(i + 1, hoTen, dau, cuoi)
        a.append(res)
    a.sort(key=lambda x: (-x.tongTien()))
    for x in a:
        print(x)
