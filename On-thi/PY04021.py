class gameThu:
    def __init__(self, id, hoTen, gioVao, gioRa):
        self.id = id
        self.hoTen = hoTen
        self.gioVao = gioVao
        self.gioRa = gioRa

    def soPhut(self, gioVao, gioRa):
        x = int(gioVao[:2]) * 60 + int(gioVao[3:])
        y = int(gioRa[:2]) * 60 + int(gioRa[3:])
        return y - x

    def __str__(self):
        tong = self.soPhut()
        gio = tong // 60
        phut = tong - gio * 60
        return f"{self.id} {self.hoTen} {gio} gio {phut} phut"