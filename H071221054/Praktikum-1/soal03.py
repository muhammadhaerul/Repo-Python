print('Menghitung Volume dan Luas Permukaan Kerucut')
print('--------------------------------------------')
import math 

r = float(input('Masukkan jari-jari: '))
t = float(input('Masukkan tinggi: '))

phi = math.pi
s = (r*r + t*t)**0.5
volume = (phi*r*r*t)/3
luas = phi*r*r + phi*r*s

print('> Volume : ', round(volume,2))
print('> Luas Permukaan : ', round(luas,2))