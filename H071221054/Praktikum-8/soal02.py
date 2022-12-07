lebar = float(input("Lebar : "))
tinggi = float(input("Tinggi : "))
panjang = float(input("Panjang : "))
massa = float(input("Massa : "))

class Kubus:
    def __init__(self, lebar, tinggi, panjang):
        self.lebar = lebar
        self.tinggi = tinggi
        self.panjang = panjang

    def setLebar(self, lebar):
        self.lebar = lebar
    def setTinggi(self, tinggi):
        self.tinggi = tinggi
    def setPanjang(self, panjang):
        self.panjang = panjang  
    def setMassa(self, massa):
        self.massa = massa
    def getMassaJenis(self):
        return (self.massa/(self.lebar * self.tinggi * self.panjang))

kubus = Kubus(lebar, tinggi, panjang)

kubus.setMassa(massa)
print("Massa Jenis =", kubus.getMassaJenis())
kubus.setMassa(massa * 2)
print("Massa Jenis =", kubus.getMassaJenis())


