class hoaDon:
    def __init__(self, id, ten, soLuong, donGia, chietKhau):
        self.id = id
        self.ten = ten
        self.soLuong = soLuong
        self.donGia = donGia
        self.chietKhau = chietKhau

    def tongTien(self):
        return self.donGia * self.soLuong - self.chietKhau

    def __str__(self):
        return f"{self.id} {self.ten} {self.soLuong} {self.donGia} {self.chietKhau} {self.tongTien()}"


if __name__ == "__main__":
    t = int(input())
    a = []
    for _ in range(t):
        a.append(hoaDon(input(), input(), int(input()), int(input()), int(input())))
    a.sort(key=lambda x: -x.tongTien())
    for x in a:
        print(x)
