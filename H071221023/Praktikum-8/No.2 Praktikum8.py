class Kubus:
    def __init__(self, lebar, tinggi, panjang, massa):
        self.lebar = lebar
        self.tinggi = tinggi
        self.panjang = panjang
        self.massa = massa 

    def setLebar(self, lebar):
        self.lebar = float(lebar)

    def setTinggi(self, tinggi):
        self.tinggi = float(tinggi)

    def setPanjang(self, panjang):
        self.panjang = float(panjang)
    
    def setMassa(self, massa):
        self.massa = float(massa)
    
    def getMassaJenis(self):
        MassaJenis = self.massa / (self.lebar*self.tinggi*self.panjang)
        self.MassaJenis = MassaJenis
        return self.MassaJenis

lebar = float(input())
tinggi = float(input())
panjang = float(input())
massa = float(input())

kubus = Kubus(lebar, tinggi, panjang, massa)
kubus.setMassa(massa)
print(kubus.panjang, kubus.lebar, kubus.tinggi)
print("Massa Jenis =", kubus.getMassaJenis())
kubus.setMassa(massa*2)
print("Massa Jenis =", kubus.getMassaJenis())

