class Person:
    def __init__(self, name, age, isMale):
        self.name = name
        self.age = age
        self.isMale = isMale

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
            return ("Laki-laki")
        elif self.isMale == False:
            return ("Perempuan")

me = Person("Kefira", 18, False)
print(me.getName(), me.getAge(), me.getGender())