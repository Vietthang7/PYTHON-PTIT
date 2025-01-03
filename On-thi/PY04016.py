from datetime import *


class HoaDon:
    def __init__(self, id, hoTen, soPhong, ngayNhan, ngayTra, dichVu):
        self.id = "KH" + format(id, "02d")
        self.hoTen = hoTen
        self.soPhong = soPhong
        self.ngayNhan = ngayNhan
        self.ngayTra = ngayTra
        self.dichVu = dichVu
        date_format = "%d/%m/%y"
        begin = datetime.strptime(self.ngayNhan, date_format)
        end = datetime.strptime(self.ngayTra, date_format)
        time = end - begin
        self.soNgay = time.days + 1

    def tongTien(self):
        if self.soPhong[0] == "1":
            return 25 * self.soNgay + self.dichVu
        if self.soPhong[0] == "2":
            return 34 * self.soNgay + self.dichVu
        if self.soPhong[0] == "3":
            return 50 * self.soNgay + self.dichVu
        else:
            return 8 0 * self.soNgay + self.dichVu
