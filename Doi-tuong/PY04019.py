from math import *


class NhanVien:
    def __init__(self, id, hoTen, lyThuyet, thucHanh):
        self.id = "TS0" + format(id, '01d')
        self.hoTen = hoTen
        self.lyThuyet = (lambda x: x if x <= 10 else x / 10.0)(lyThuyet)
        self.thucHanh = (lambda x: x if x <= 10 else x / 10.0)(thucHanh)

    def diemTB(self):
        return (self.lyThuyet + self.thucHanh) / 2

    def xepLoai(self):
        dtb = self.diemTB()
        if dtb >= 9.5:
            return "XUAT SAC"
        elif dtb >= 8.0:
            return "DAT"
        elif dtb >= 5:
            return "CAN NHAC"
        else:
            return "TRUOT"

    def __str__(self):
        return "{} {} {:.2f} {}".format(
            self.id, self.hoTen, self.diemTB(), self.xepLoai()
        )


if __name__ == "__main__":
    t = int(input())
    a = []
    for i in range(t):
        a.append(NhanVien(i + 1, input(), float(input()), float(input())))
    a.sort(key=lambda x: (-x.diemTB()))
    for x in a:
        print(x)
