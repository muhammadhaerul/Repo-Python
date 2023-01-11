from abc import ABC, abstractmethod

class MakhlukHidup(ABC):
    @abstractmethod
    def makan(self):
        pass

class Human(MakhlukHidup):
    def __init__ (self, name, umur):
        self.name = name
        self.__umur = umur
    def setUmur(self, umur):
        self.__umur = umur
    def getUmur(self):
        print(self.__umur)
    def makan(self):
        print("Ayo Mari Makan!")

class Kucing:
    def __init__(self, jenis):
        self._jenis = jenis
    def jalan(self):
        print("Kucing sedang memakan rumput")

class Ular(Kucing):
    def __init__(self, jenis):
        super().__init__(jenis)
    def jalan(self):
        print("Ular sedang berdiri")

def jalan(kucing):
        kucing.jalan()

name = print("Nama : Natas")
umur = print("Umur : 15")

data = Human(name, umur)

cat = Kucing("gila")
hide = Ular("Raksasa")

jalan(cat)
jalan(hide)