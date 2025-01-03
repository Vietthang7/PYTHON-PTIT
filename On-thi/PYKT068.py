class MonHoc:
    def __init__(self, maMon, tenMon, hinhThucThi):
        self.maMon = maMon
        self.tenMon = tenMon
        self.hinhThucThi = hinhThucThi

    def __str__(self):
        return f"{self.maMon} {self.tenMon} {self.hinhThucThi}"


if __name__ == "__main__":
    t = int(input())
    mt = []
    while t > 0:
        t -= 1
        mt.append(MonHoc(input().strip(), input().strip(), input().strip()))
    mt.sort(key=lambda x: (x.maMon))
    for x in mt:
        print(x)
