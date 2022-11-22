lebar = float(input())
tinggi = float(input())
panjang = float(input())
massa = float(input())

class BangunRuang:
    def setTinggi(self, tinggi):
        self.tinggi = tinggi
    def setPanjang(self, panjang):
        self.panjang = panjang
    def setLebar(self, lebar):
        self.lebar = lebar  
    def setMassa(self, massa):
        self.massa = massa
    def getMassaJenis(self):
        return (self.massa/(self.lebar * self.tinggi * self.panjang))

kubus = BangunRuang()
kubus.setTinggi(tinggi)
kubus.setPanjang(panjang)
kubus.setLebar(lebar)
kubus.setMassa(massa)
print("Massa Jenis =", kubus.getMassaJenis())
kubus.setMassa(massa * 2)
print("Massa Jenis =", kubus.getMassaJenis())