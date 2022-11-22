class Person:
    def __init__(self, name, age, isMale, tinggi):
        self.name = name
        self.age = age
        self.isMale = isMale
        self.tinggi = tinggi
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setAge(self, age):
        self.age = age
    def getAge(self):
        return self.age
    def setGender(self, isMale):
        self.isMale = isMale
    def getGender(self):
        if self.isMale == True:
            return ("Male")
        elif self.isMale == False:
            return ("Female")
    def setTinggi(self, tinggi):
        self.tinggi = tinggi
    def getTinggi(self):
        return self.tinggi
orang1 = Person("Vicky", 19, True, 170)
orang2 = Person("Anya", 18, False, 159)

# print(Orang1.__dict__)
# print(Orang2.__dict__)
orang1.setName("Trisman")
orang1.setAge(17)
orang1.setGender(True)
orang1.setTinggi(165)
print(orang1.getName(),orang1.getAge(),orang1.getGender(),orang1.getTinggi())