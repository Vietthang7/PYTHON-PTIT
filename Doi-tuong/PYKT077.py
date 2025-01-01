from datetime import datetime


class MonHoc:
    def __init__(self, maMon, tenMon):
        self.maMon = maMon
        self.tenMon = tenMon

    def __str__(self):
        return f"{self.maMon} {self.tenMon}"


stt = 1


class LichThi:
    def __init__(self, ngay, gio, nhom, monHoc):
        self.thoiGian = " ".join([ngay, gio])
        self.nhom = nhom
        self.monHoc = monHoc
        global stt
        self.ma = "T" + format(stt, "03d")
        stt += 1
    
