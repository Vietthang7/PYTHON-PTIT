class giaoVien:
    def __init__(self, id, ten, maXT, tinHoc, chuyenMon):
        self.id = "GV" + format(id, "02d")
        self.ten = ten
        self.maXT = maXT
        self.tinHoc = tinHoc
        self.chuyenMon = chuyenMon

    def tongDiem(self):
        diem = self.tinHoc * 2 + self.chuyenMon
        x = self.maXT[1]
        if x == "1":
            return diem + 2.0
        elif x == "2":
            return diem + 1.5
        elif x == "3":
            return diem + 1.0
        else:
            return diem + 0.0

    def monHoc(self):
        x = self.maXT[0]
        if x == "A":
            return "TOAN"
        elif x == "B":
            return "LY"
        else:
            return "HOA"

    def ketQua(self):
        x = self.tongDiem()
        if x >= 18.0:
            return "TRUNG TUYEN"
        else:
            return "LOAI"

    def __str__(self):
        return f"{self.id} {self.ten} {self.monHoc()} {self.tongDiem()} {self.ketQua()}"


if __name__ == "__main__":
    t = int(input())
    a = []
    for i in range(t):
        a.append(giaoVien(i + 1, input(), input(), float(input()), float(input())))
    a.sort(key=lambda x: -x.tongDiem())
    for x in a:
        print(x)
