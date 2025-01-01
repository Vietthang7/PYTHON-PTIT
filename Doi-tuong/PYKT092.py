class thiSinh:
    def __init__(self, id, hoTen, diem, danToc, khuVuc):
        self.id = "TS" + format(id, "02d")
        self.hoTen = self.chuanHoa(hoTen)
        self.diem = diem + self.uuTienDT(danToc) + self.uuTienKV(khuVuc)
        self.trangThai = "Do" if self.diem >= 20.5 else "Truot"

    def chuanHoa(self, hoTen):
        return " ".join(i.capitalize() for i in hoTen.strip().split())

    def uuTienDT(self, danToc):
        if danToc == "Kinh":
            return 0
        else:
            return 1.5

    def uuTienKV(self, khuVuc):
        if khuVuc == "1":
            return 1.5
        elif khuVuc == "2":
            return 1
        else:
            return 0

    def __str__(self):
        return f"{self.id} {self.hoTen} {self.diem:.1f} {self.trangThai}"


if __name__ == "__main__":
    t = int(input())
    a = []
    for i in range(t):
        a.append(thiSinh(i + 1, input(), float(input()), input(), input()))
    a.sort(key=lambda x: (-x.diem, x.id))
    for x in a:
        print(x)
