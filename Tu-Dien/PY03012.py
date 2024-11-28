class SinhVien:
    def __init__(seft, hoTen, accepted, submit):
        seft.hoTen = hoTen
        seft.accepted = accepted
        seft.submit = submit

    def __str__(seft):
        return f"{seft.hoTen} {seft.accepted} {seft.submit}"


if __name__ == "__main__":
    t = int(input())
    sv = []
    while t > 0:
        t -= 1
        hoTen = input()
        a, s = map(int, input().split())
        sv.append(SinhVien(hoTen, a, s))
    sv.sort(key=lambda x: (-x.accepted, x.submit, x.hoTen))
    for x in sv:
        print(x)
