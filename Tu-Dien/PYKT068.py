class MonHoc:
    def __init__(seft, maMon, tenMon, hinhThucThi):
        seft.maMon = maMon
        seft.tenMon = tenMon
        seft.hinhThucThi = hinhThucThi

    def __str__(seft):
        return f"{seft.maMon} {seft.tenMon} {seft.hinhThucThi}"


if __name__ == "__main__":
    t = int(input())
    mt = []
    while t > 0:
        t -= 1
        mt.append(MonHoc(input().strip(), input().strip(), input().strip()))
    mt.sort(key=lambda x: x.maMon)
    for x in mt:
        print(x)
