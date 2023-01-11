class rectangular_prism:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def getDensity(self):
        self.volume = self.length * self.width * self.height
        self.density = self.mass/self.volume
        return self.density

    def setMass(self, newMass):
        self.mass = newMass

length = float(input())
width = float(input())
height = float(input())
mass = float(input())

balok = rectangular_prism(length, width, height)

balok.setMass(mass)
print('Massa jenis:', balok.getDensity())

balok.setMass(mass*2)
print('Massa jenis:', balok.getDensity())