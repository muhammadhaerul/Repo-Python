class Person:
    def __init__(self, name, age, isMale, tinggi, alamat):
        self.name = name
        self.age = age
        self.isMale = isMale
        self.tinggi = tinggi
        self.alamat = alamat

    def setAge(self, age):
        self.age = int(age)

    def getAge(self):
        return self.age

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
    
    def setGender(self, isMale):
        self.isMale = isMale
 
    def getGender(self):
        if isMale == True:
            self.isMale = 'male'
            return self.isMale
        elif isMale == False:
            self.isMale = 'female'
            return self.isMale
    
    def setTinggi(self, tinggi):
        self.tinggi = int(tinggi)

    def getTinggi(self):
        return self.tinggi

    def setAlamat(self, alamat):
        self.alamat = alamat

    def getAlamat(self):
        return self.alamat

name = input('Masukkan nama: ')
age = int(input('Masukkan umur: '))
isMale = input('is Male? True / False: ').upper()
if isMale == 'TRUE':
    isMale = bool(True)
elif isMale == 'FALSE':
    isMale = bool(False)
tinggi = int(input('Masukkan tinggi badan: '))
alamat = input('Tempat tinggal di: ')

person = Person(name, age, isMale, tinggi, alamat)
print('\nNama saya ' + person.getName())
print(f'Sekarang saya berumur {person.getAge()} tahun')
print(f'Saya berjenis kelamin {person.getGender()}')
print(f'tinggi saya {person.getTinggi()} cm')
print('saya tinggal di ' + person.getAlamat())

person.setName("Vicky")
person.setAge(18)
person.setTinggi(171)

print('\nNama saya ' + person.getName())
print(f'Sekarang saya berumur {person.getAge()} tahun')
print(f'Saya berjenis kelamin {person.getGender()}')
print(f'tinggi saya {person.getTinggi()} cm')
print('saya tinggal di ' + person.getAlamat())