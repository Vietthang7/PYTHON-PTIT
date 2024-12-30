class SinhVien:
    def __init__(self, msv, ten, lop):
        self.msv = msv.strip()
        self.ten = ten.strip()
        self.lop = lop.strip()
        self.data = ""
        self.chuyenCan = 10
        self.status = ""

    def __str__(self):
        return f"{self.msv} {self.ten} {self.lop} {self.chuyenCan} {self.status}"


if __name__ == "__main__":
    mp = dict()
    n = int(input())
    a = []
    for _ in range(n):
        a.append(SinhVien(input(), input(), input()))
    for _ in range(n):
        tmp = input().split()
        mp[tmp[0]] = tmp[1]
    for x in a:
        x.data = mp[x.msv]
    for x in a:
        for y in x.data:
            if y == "v":
                x.chuyenCan -= 2
            if y == "m":
                x.chuyenCan -= 1
        if x.chuyenCan <= 0:
            x.chuyenCan = 0
            x.status = "KDDK"
    for x in a:
        print(x)
