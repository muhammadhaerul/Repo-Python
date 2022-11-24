class Person:
    def __init__(self, name, age, isMale):
        self.name = name
        self.age = age
        self.isMale = isMale
    
    def setName(self, newName):
        self.name = newName

    def getName(self):
        return self.name

    def setAge(self, newAge):
        self.age = newAge

    def getAge(self):
        return self.age
    
    def setGender(self, isMale):
        self.isMale = isMale

    def getGender(self):
        if self.isMale == True:
            return 'Male'
        elif self.isMale == False:
            return 'Female'

person1 = Person('Putra', 20, True)
print(person1.__dict__)
print(person1.getName(), person1.getAge(), person1.getGender())

person1.setName('Putri')
person1.setAge(18)
person1.setGender(False)
print(person1.__dict__)
print(person1.getName(), person1.getAge(), person1.getGender())